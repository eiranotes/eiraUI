#!/usr/bin/env python3
"""Capture public App Store screenshots for evidence-only UI analysis.

The script uses Apple's public Search/Lookup API first and falls back to parsing the
public App Store product page. It writes downloaded images and an integrity manifest to
an output directory. The output is intended for a short-lived CI artifact; do not commit
third-party screenshots to the repository unless the storage policy permits it.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import sys
from dataclasses import asdict, dataclass
from io import BytesIO
from pathlib import Path
from typing import Iterable
from urllib.parse import urlparse

import requests
from PIL import Image

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151 Safari/537.36"
)


@dataclass(frozen=True)
class CaptureRecord:
    index: int
    source_url: str
    saved_path: str
    width: int
    height: int
    mode: str
    format: str
    sha256: str
    byte_length: int


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--app-id", required=True)
    parser.add_argument("--country", default="us")
    parser.add_argument("--app-url", required=True)
    parser.add_argument("--output", type=Path, default=Path("capture-output"))
    return parser.parse_args()


def normalise_url(value: str) -> str:
    value = html.unescape(value)
    value = value.replace("\\u002F", "/").replace("\\/", "/")
    return value.strip('"\' ,')


def unique_ordered(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        value = normalise_url(value)
        if value and value not in seen:
            seen.add(value)
            result.append(value)
    return result


def lookup_urls(session: requests.Session, app_id: str, country: str) -> tuple[dict, list[str]]:
    response = session.get(
        "https://itunes.apple.com/lookup",
        params={"id": app_id, "country": country},
        timeout=30,
    )
    response.raise_for_status()
    payload = response.json()
    results = payload.get("results") or []
    if len(results) != 1:
        raise RuntimeError(f"Lookup returned {len(results)} results for app id {app_id}")
    record = results[0]
    urls: list[str] = []
    for key in ("screenshotUrls", "ipadScreenshotUrls", "appletvScreenshotUrls"):
        candidates = record.get(key) or []
        if key == "screenshotUrls":
            urls.extend(str(item) for item in candidates)
    return record, unique_ordered(urls)


def page_urls(session: requests.Session, app_url: str) -> tuple[str, list[str]]:
    response = session.get(app_url, timeout=30)
    response.raise_for_status()
    body = response.text

    candidates: list[str] = []
    patterns = (
        r'https://is\d+-ssl\.mzstatic\.com/image/thumb/[^"\'<>\\\s]+',
        r'https:\\/\\/is\d+-ssl\.mzstatic\.com\\/image\\/thumb\\/[^"<>\s]+',
    )
    for pattern in patterns:
        candidates.extend(re.findall(pattern, body))

    # App Store screenshot assets normally contain PurpleSource and a rendered-size suffix.
    candidates = [
        item
        for item in unique_ordered(candidates)
        if "PurpleSource" in item and re.search(r"\.(?:png|jpg|jpeg|webp)(?:\?|$)", item)
    ]
    return body, candidates


def render_full_size_url(url: str) -> str:
    """Prefer Apple's full screenshot form when a sized derivative is supplied."""
    parsed = urlparse(url)
    path = parsed.path
    # Keep 0x0ss.* untouched. Convert common WxHbb.* / WxH.* derivatives to 0x0ss.*.
    path = re.sub(
        r"/\d+x\d+(?:bb|sr|sc|cw|ac|ss)?\.(png|jpg|jpeg|webp)$",
        r"/0x0ss.\1",
        path,
        flags=re.IGNORECASE,
    )
    return parsed._replace(path=path).geturl()


def download_image(session: requests.Session, url: str, destination: Path, index: int) -> CaptureRecord:
    attempted = [render_full_size_url(url), url]
    last_error: Exception | None = None
    for candidate in unique_ordered(attempted):
        try:
            response = session.get(candidate, timeout=60)
            response.raise_for_status()
            payload = response.content
            image = Image.open(BytesIO(payload))
            image.load()
            if image.width < 200 or image.height < 200:
                raise RuntimeError(f"Image is unexpectedly small: {image.size}")

            # Normalise to PNG to make local inspection deterministic.
            if image.mode not in ("RGB", "RGBA"):
                image = image.convert("RGBA" if "A" in image.getbands() else "RGB")
            saved_path = destination / f"screenshot-{index:02d}.png"
            image.save(saved_path, format="PNG", optimize=True)
            saved_bytes = saved_path.read_bytes()
            return CaptureRecord(
                index=index,
                source_url=candidate,
                saved_path=str(saved_path),
                width=image.width,
                height=image.height,
                mode=image.mode,
                format="PNG",
                sha256=hashlib.sha256(saved_bytes).hexdigest(),
                byte_length=len(saved_bytes),
            )
        except Exception as exc:  # try the original URL before failing
            last_error = exc
    raise RuntimeError(f"Unable to download screenshot {index} from {url}: {last_error}")


def build_contact_sheet(records: list[CaptureRecord], output: Path) -> None:
    images = [Image.open(output / Path(record.saved_path).name).convert("RGB") for record in records]
    thumb_width = 320
    resized: list[Image.Image] = []
    for image in images:
        height = round(image.height * thumb_width / image.width)
        resized.append(image.resize((thumb_width, height), Image.Resampling.LANCZOS))

    columns = 3
    rows = (len(resized) + columns - 1) // columns
    cell_height = max(image.height for image in resized) + 72
    sheet = Image.new("RGB", (columns * thumb_width, rows * cell_height), "white")
    from PIL import ImageDraw, ImageFont

    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default()
    for i, image in enumerate(resized):
        x = (i % columns) * thumb_width
        y = (i // columns) * cell_height
        sheet.paste(image, (x, y))
        draw.text((x + 10, y + image.height + 12), f"REF-{i + 1:02d}", fill="black", font=font)
    sheet.save(output / "contact-sheet.jpg", quality=90, optimize=True)


def main() -> int:
    args = parse_args()
    args.output.mkdir(parents=True, exist_ok=True)

    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT, "Accept-Language": "en-US,en;q=0.9"})

    lookup_record: dict = {}
    lookup_error: str | None = None
    lookup_screenshots: list[str] = []
    try:
        lookup_record, lookup_screenshots = lookup_urls(session, args.app_id, args.country)
    except Exception as exc:
        lookup_error = repr(exc)

    page_body = ""
    page_error: str | None = None
    page_screenshots: list[str] = []
    try:
        page_body, page_screenshots = page_urls(session, args.app_url)
        (args.output / "app-store-page.html").write_text(page_body, encoding="utf-8")
    except Exception as exc:
        page_error = repr(exc)

    urls = lookup_screenshots or page_screenshots
    if not urls:
        print(json.dumps({"lookup_error": lookup_error, "page_error": page_error}, indent=2))
        raise RuntimeError("No iPhone screenshots were resolved")

    records: list[CaptureRecord] = []
    seen_sha: set[str] = set()
    for source_index, url in enumerate(urls, start=1):
        record = download_image(session, url, args.output, source_index)
        if record.sha256 in seen_sha:
            Path(record.saved_path).unlink(missing_ok=True)
            continue
        seen_sha.add(record.sha256)
        records.append(record)

    # Keep exact public order but renumber saved files if duplicate removal created gaps.
    if [record.index for record in records] != list(range(1, len(records) + 1)):
        rewritten: list[CaptureRecord] = []
        for new_index, record in enumerate(records, start=1):
            old_path = Path(record.saved_path)
            new_path = args.output / f"screenshot-{new_index:02d}.png"
            old_path.replace(new_path)
            rewritten.append(
                CaptureRecord(
                    index=new_index,
                    source_url=record.source_url,
                    saved_path=str(new_path),
                    width=record.width,
                    height=record.height,
                    mode=record.mode,
                    format=record.format,
                    sha256=hashlib.sha256(new_path.read_bytes()).hexdigest(),
                    byte_length=new_path.stat().st_size,
                )
            )
        records = rewritten

    build_contact_sheet(records, args.output)

    metadata = {
        "appId": args.app_id,
        "country": args.country,
        "appUrl": args.app_url,
        "lookupError": lookup_error,
        "pageError": page_error,
        "lookup": {
            key: lookup_record.get(key)
            for key in (
                "trackName",
                "artistName",
                "bundleId",
                "version",
                "currentVersionReleaseDate",
                "releaseNotes",
                "description",
                "minimumOsVersion",
                "fileSizeBytes",
                "primaryGenreName",
                "averageUserRating",
                "userRatingCount",
                "formattedPrice",
                "trackViewUrl",
            )
            if key in lookup_record
        },
        "lookupScreenshotCount": len(lookup_screenshots),
        "pageScreenshotCandidateCount": len(page_screenshots),
        "capturedScreenshotCount": len(records),
        "screenshots": [asdict(record) for record in records],
    }
    (args.output / "metadata.json").write_text(
        json.dumps(metadata, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(json.dumps(metadata, indent=2, ensure_ascii=False))

    if len(records) != 6:
        raise RuntimeError(f"Expected 6 public iPhone screenshots, captured {len(records)}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"capture failed: {exc}", file=sys.stderr)
        raise
