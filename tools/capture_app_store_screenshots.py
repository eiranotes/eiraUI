#!/usr/bin/env python3
"""Capture all public iPhone App Store screenshots for one exact app ID."""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import asdict, dataclass
from io import BytesIO
from pathlib import Path

import requests
from PIL import Image, ImageDraw, ImageFont


@dataclass(frozen=True)
class ScreenshotRecord:
    index: int
    source_url: str
    file: str
    width: int
    height: int
    sha256: str
    byte_length: int


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--app-id", required=True)
    parser.add_argument("--country", required=True)
    parser.add_argument("--expected", required=True, type=int)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    args.output.mkdir(parents=True, exist_ok=True)
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 AppleWebKit/537.36 Chrome/151 Safari/537.36",
        "Accept-Language": "ko-KR,ko;q=0.9,en;q=0.8",
    })

    response = session.get(
        "https://itunes.apple.com/lookup",
        params={"id": args.app_id, "country": args.country},
        timeout=30,
    )
    response.raise_for_status()
    payload = response.json()
    results = payload.get("results") or []
    if len(results) != 1:
        raise RuntimeError(f"Expected one lookup result, got {len(results)}")
    app = results[0]
    urls = app.get("screenshotUrls") or []
    if len(urls) != args.expected:
        raise RuntimeError(f"Expected {args.expected} iPhone screenshots, got {len(urls)}")

    records: list[ScreenshotRecord] = []
    seen: set[str] = set()
    for index, url in enumerate(urls, start=1):
        image_response = session.get(url, timeout=60)
        image_response.raise_for_status()
        image = Image.open(BytesIO(image_response.content))
        image.load()
        if image.mode not in ("RGB", "RGBA"):
            image = image.convert("RGB")
        path = args.output / f"screenshot-{index:02d}.png"
        image.save(path, format="PNG", optimize=True)
        data = path.read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        if digest in seen:
            raise RuntimeError(f"Duplicate screenshot content at published index {index}")
        seen.add(digest)
        records.append(ScreenshotRecord(
            index=index,
            source_url=url,
            file=path.name,
            width=image.width,
            height=image.height,
            sha256=digest,
            byte_length=len(data),
        ))

    thumb_width = 280
    thumbs: list[Image.Image] = []
    for record in records:
        image = Image.open(args.output / record.file).convert("RGB")
        height = round(image.height * thumb_width / image.width)
        thumbs.append(image.resize((thumb_width, height), Image.Resampling.LANCZOS))
    columns = 3
    rows = (len(thumbs) + columns - 1) // columns
    label_height = 44
    cell_height = max(item.height for item in thumbs) + label_height
    sheet = Image.new("RGB", (columns * thumb_width, rows * cell_height), "white")
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default()
    for offset, thumb in enumerate(thumbs):
        x = (offset % columns) * thumb_width
        y = (offset // columns) * cell_height
        sheet.paste(thumb, (x, y))
        draw.text((x + 10, y + thumb.height + 12), f"REF-{offset + 1:02d}", fill="black", font=font)
    sheet.save(args.output / "contact-sheet.jpg", quality=92, optimize=True)

    metadata = {
        "lookup": {
            key: app.get(key)
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
                "supportedDevices",
            )
            if key in app
        },
        "publishedScreenshotCount": len(urls),
        "capturedScreenshotCount": len(records),
        "screenshots": [asdict(record) for record in records],
    }
    (args.output / "metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(metadata, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
