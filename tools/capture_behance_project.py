#!/usr/bin/env python3
"""Capture a complete public Behance project evidence set.

The script drives a real browser, scrolls the project to completion, records every
project-module media URL in document order, downloads the highest-resolution public
asset available, extracts animated frames, and creates contact sheets for inspection.

Third-party media is evidence-only. Keep it in a short-lived CI artifact; do not commit
it to a public repository unless the project storage policy explicitly allows that.
"""

from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import math
import re
import shutil
import sys
import time
from dataclasses import asdict, dataclass
from io import BytesIO
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import urlsplit, urlunsplit

import requests
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageSequence
from playwright.async_api import Browser, Page, async_playwright

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151 Safari/537.36"
)
MEDIA_RE = re.compile(
    r"https://mir-s\d+-cdn-cf\.behance\.net/(?:project_modules|project_modules_max|projects)/[^\"'<>\\\s)]+",
    re.IGNORECASE,
)
IMAGE_EXT_RE = re.compile(r"\.(?:png|jpe?g|gif|webp|avif)(?:\?|$)", re.IGNORECASE)


@dataclass(frozen=True)
class MediaRecord:
    index: int
    kind: str
    source_url: str
    downloaded_url: str
    file: str
    width: int
    height: int
    format: str
    mode: str
    animated: bool
    frame_count: int
    duration_ms: int
    sha256: str
    byte_length: int


@dataclass(frozen=True)
class FrameRecord:
    media_index: int
    frame_index: int
    timestamp_ms: int
    file: str
    width: int
    height: int
    sha256: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    parser.add_argument("--project-id", required=True)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--max-animation-frames", type=int, default=24)
    return parser.parse_args()


def unique_ordered(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if not value:
            continue
        value = value.replace("\\u002F", "/").replace("\\/", "/")
        value = value.strip('"\' ,')
        if value and value not in seen:
            seen.add(value)
            result.append(value)
    return result


def canonical_media_key(url: str) -> str:
    parts = urlsplit(url)
    path = re.sub(
        r"/(?:disp|max_1200|max_3840|1400|2800|original)/",
        "/SIZE/",
        parts.path,
        flags=re.IGNORECASE,
    )
    path = re.sub(
        r"/\d+x\d+(?:bb|sr|sc|cw|ac|ss)?\.(png|jpg|jpeg|gif|webp|avif)$",
        r"/SIZE.\1",
        path,
        flags=re.IGNORECASE,
    )
    return f"{parts.netloc}{path}"


def highest_resolution_candidates(url: str) -> list[str]:
    parts = urlsplit(url)
    path = parts.path
    candidates: list[str] = []

    # Behance project modules commonly expose multiple path-size variants.
    for replacement in ("project_modules_max", "project_modules/2800", "project_modules/1400"):
        candidate_path = re.sub(
            r"project_modules(?:_max)?/(?:disp|max_1200|max_3840|1400|2800|original)",
            replacement,
            path,
            flags=re.IGNORECASE,
        )
        candidates.append(urlunsplit((parts.scheme, parts.netloc, candidate_path, parts.query, parts.fragment)))

    # Keep original as a guaranteed fallback.
    candidates.append(url)
    return unique_ordered(candidates)


async def dismiss_overlays(page: Page) -> None:
    labels = [
        "Accept all",
        "Accept All",
        "Allow all",
        "동의",
        "모두 허용",
        "Close",
        "닫기",
        "Not now",
        "나중에",
    ]
    for label in labels:
        try:
            button = page.get_by_role("button", name=re.compile(f"^{re.escape(label)}$", re.I))
            if await button.count():
                await button.first.click(timeout=1200)
        except Exception:
            pass


async def auto_scroll(page: Page) -> dict[str, int]:
    last_height = 0
    stable_rounds = 0
    iterations = 0
    while iterations < 160 and stable_rounds < 5:
        iterations += 1
        metrics = await page.evaluate(
            """
            () => ({
              height: Math.max(document.body.scrollHeight, document.documentElement.scrollHeight),
              y: window.scrollY,
              viewport: window.innerHeight
            })
            """
        )
        height = int(metrics["height"])
        if height <= last_height + 4:
            stable_rounds += 1
        else:
            stable_rounds = 0
            last_height = height
        await page.evaluate("window.scrollBy(0, Math.max(640, window.innerHeight * 0.8))")
        await page.wait_for_timeout(650)
        await dismiss_overlays(page)
    await page.evaluate("window.scrollTo(0, 0)")
    await page.wait_for_timeout(700)
    return {"height": last_height, "iterations": iterations, "stableRounds": stable_rounds}


async def collect_media(page: Page, project_id: str) -> tuple[list[dict[str, Any]], list[str]]:
    dom_records = await page.evaluate(
        """
        () => {
          const out = [];
          let order = 0;
          for (const el of document.querySelectorAll('img, video, source, picture, [style*="background-image"]')) {
            const urls = [];
            const push = value => { if (value && typeof value === 'string') urls.push(value); };
            push(el.currentSrc);
            push(el.src);
            push(el.poster);
            push(el.getAttribute && el.getAttribute('data-src'));
            push(el.getAttribute && el.getAttribute('data-original'));
            push(el.getAttribute && el.getAttribute('data-srcset'));
            push(el.getAttribute && el.getAttribute('srcset'));
            const style = el.getAttribute && el.getAttribute('style');
            if (style) {
              for (const match of style.matchAll(/url\(["']?([^"')]+)["']?\)/g)) push(match[1]);
            }
            out.push({
              order: order++,
              tag: el.tagName,
              alt: el.getAttribute && (el.getAttribute('alt') || ''),
              urls
            });
          }
          return out;
        }
        """
    )
    resources = await page.evaluate(
        "performance.getEntriesByType('resource').map(entry => entry.name)"
    )
    html = await page.content()
    html_urls = MEDIA_RE.findall(html)

    normalized: list[dict[str, Any]] = []
    seen: set[str] = set()
    for record in dom_records:
        candidates: list[str] = []
        for raw in record.get("urls", []):
            if not raw:
                continue
            # srcset/data-srcset can contain comma-delimited width candidates.
            for part in str(raw).split(","):
                candidates.extend(MEDIA_RE.findall(part))
                token = part.strip().split(" ")[0]
                if "behance.net" in token:
                    candidates.append(token)
        for url in unique_ordered(candidates):
            if project_id not in url or not IMAGE_EXT_RE.search(url):
                continue
            key = canonical_media_key(url)
            if key in seen:
                continue
            seen.add(key)
            normalized.append(
                {
                    "order": int(record["order"]),
                    "tag": record.get("tag", ""),
                    "alt": record.get("alt", ""),
                    "url": url,
                    "source": "dom",
                }
            )

    fallback_urls = unique_ordered([*resources, *html_urls])
    next_order = max([item["order"] for item in normalized], default=-1) + 1
    for url in fallback_urls:
        if project_id not in url or not IMAGE_EXT_RE.search(url):
            continue
        key = canonical_media_key(url)
        if key in seen:
            continue
        seen.add(key)
        normalized.append(
            {
                "order": next_order,
                "tag": "RESOURCE",
                "alt": "",
                "url": url,
                "source": "resource",
            }
        )
        next_order += 1

    normalized.sort(key=lambda item: item["order"])
    return normalized, unique_ordered([*resources, *html_urls])


def download_asset(
    session: requests.Session,
    source_url: str,
    destination: Path,
    index: int,
) -> tuple[MediaRecord, Image.Image]:
    errors: list[str] = []
    for candidate in highest_resolution_candidates(source_url):
        try:
            response = session.get(candidate, timeout=90)
            response.raise_for_status()
            payload = response.content
            if len(payload) < 2048:
                raise RuntimeError(f"asset too small: {len(payload)} bytes")
            image = Image.open(BytesIO(payload))
            image.seek(0)
            image.load()
            if image.width < 180 or image.height < 180:
                raise RuntimeError(f"image dimensions too small: {image.size}")

            fmt = (image.format or Path(urlsplit(candidate).path).suffix.lstrip(".") or "BIN").upper()
            animated = bool(getattr(image, "is_animated", False))
            frame_count = int(getattr(image, "n_frames", 1))
            duration_ms = 0
            if animated:
                try:
                    duration_ms = sum(int(frame.info.get("duration", 0)) for frame in ImageSequence.Iterator(image))
                except Exception:
                    duration_ms = int(image.info.get("duration", 0)) * frame_count
                image.seek(0)

            suffix = ".gif" if animated and fmt == "GIF" else ".png"
            path = destination / f"module-{index:03d}{suffix}"
            if suffix == ".gif":
                path.write_bytes(payload)
            else:
                still = ImageOps.exif_transpose(image.convert("RGBA" if "A" in image.getbands() else "RGB"))
                still.save(path, format="PNG", optimize=True)
            saved = path.read_bytes()
            record = MediaRecord(
                index=index,
                kind="animated" if animated else "image",
                source_url=source_url,
                downloaded_url=candidate,
                file=path.name,
                width=image.width,
                height=image.height,
                format=fmt,
                mode=image.mode,
                animated=animated,
                frame_count=frame_count,
                duration_ms=duration_ms,
                sha256=hashlib.sha256(saved).hexdigest(),
                byte_length=len(saved),
            )
            return record, image
        except Exception as exc:
            errors.append(f"{candidate}: {exc!r}")
    raise RuntimeError("unable to download asset\n" + "\n".join(errors))


def sample_frame_indices(frame_count: int, maximum: int) -> list[int]:
    if frame_count <= maximum:
        return list(range(frame_count))
    # Evenly sample, always preserving first and last frames.
    return sorted({round(i * (frame_count - 1) / (maximum - 1)) for i in range(maximum)})


def extract_animation_frames(
    record: MediaRecord,
    image: Image.Image,
    output: Path,
    maximum: int,
) -> list[FrameRecord]:
    if not record.animated:
        return []
    frame_dir = output / "frames" / f"module-{record.index:03d}"
    frame_dir.mkdir(parents=True, exist_ok=True)
    selected = set(sample_frame_indices(record.frame_count, maximum))
    result: list[FrameRecord] = []
    elapsed = 0
    previous_digest: str | None = None
    for frame_index, frame in enumerate(ImageSequence.Iterator(image)):
        duration = int(frame.info.get("duration", image.info.get("duration", 0)) or 0)
        if frame_index not in selected:
            elapsed += duration
            continue
        rgba = frame.convert("RGBA")
        path = frame_dir / f"frame-{frame_index:04d}.png"
        rgba.save(path, format="PNG", optimize=True)
        data = path.read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        if digest == previous_digest:
            path.unlink(missing_ok=True)
        else:
            result.append(
                FrameRecord(
                    media_index=record.index,
                    frame_index=frame_index,
                    timestamp_ms=elapsed,
                    file=str(path.relative_to(output)),
                    width=rgba.width,
                    height=rgba.height,
                    sha256=digest,
                )
            )
            previous_digest = digest
        elapsed += duration
    return result


def contain_thumbnail(image: Image.Image, width: int, height: int) -> Image.Image:
    canvas = Image.new("RGB", (width, height), "white")
    rgb = ImageOps.exif_transpose(image.convert("RGB"))
    rgb.thumbnail((width - 20, height - 20), Image.Resampling.LANCZOS)
    x = (width - rgb.width) // 2
    y = (height - rgb.height) // 2
    canvas.paste(rgb, (x, y))
    return canvas


def build_contact_sheet(
    entries: list[tuple[str, Image.Image]],
    output_path: Path,
    columns: int = 3,
    cell_width: int = 420,
    cell_height: int = 520,
) -> None:
    if not entries:
        return
    label_height = 52
    rows = math.ceil(len(entries) / columns)
    sheet = Image.new("RGB", (columns * cell_width, rows * (cell_height + label_height)), "white")
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default()
    for offset, (label, image) in enumerate(entries):
        x = (offset % columns) * cell_width
        y = (offset // columns) * (cell_height + label_height)
        thumb = contain_thumbnail(image, cell_width, cell_height)
        sheet.paste(thumb, (x, y))
        draw.rectangle((x, y, x + cell_width - 1, y + cell_height - 1), outline=(210, 210, 210))
        draw.text((x + 12, y + cell_height + 16), label, fill="black", font=font)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output_path, quality=92, optimize=True)


async def capture_page(url: str, project_id: str, output: Path) -> dict[str, Any]:
    async with async_playwright() as playwright:
        browser: Browser = await playwright.chromium.launch(
            headless=True,
            args=["--disable-blink-features=AutomationControlled"],
        )
        context = await browser.new_context(
            viewport={"width": 1440, "height": 1000},
            device_scale_factor=1,
            user_agent=USER_AGENT,
            locale="en-US",
        )
        page = await context.new_page()
        response = await page.goto(url, wait_until="domcontentloaded", timeout=120_000)
        await page.wait_for_timeout(5_000)
        await dismiss_overlays(page)
        scroll = await auto_scroll(page)
        await page.wait_for_timeout(2_000)
        title = await page.title()
        final_url = page.url
        media, resource_urls = await collect_media(page, project_id)
        html = await page.content()
        (output / "page.html").write_text(html, encoding="utf-8")
        await page.screenshot(path=str(output / "page-top.png"), full_page=False)
        # A full-page screenshot can exceed Chromium's image limits on long Behance pages.
        # Capture viewport tiles instead.
        total_height = int(await page.evaluate("Math.max(document.body.scrollHeight, document.documentElement.scrollHeight)"))
        tile_dir = output / "page-tiles"
        tile_dir.mkdir(exist_ok=True)
        tile_height = 900
        tile_count = min(math.ceil(total_height / tile_height), 120)
        for index in range(tile_count):
            await page.evaluate(f"window.scrollTo(0, {index * tile_height})")
            await page.wait_for_timeout(180)
            await page.screenshot(path=str(tile_dir / f"tile-{index:03d}.png"), full_page=False)
        await browser.close()
    return {
        "title": title,
        "finalUrl": final_url,
        "httpStatus": response.status if response else None,
        "scroll": scroll,
        "pageHeight": total_height,
        "tileCount": tile_count,
        "mediaCandidates": media,
        "resourceUrlCount": len(resource_urls),
    }


async def async_main() -> int:
    args = parse_args()
    output = args.output
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)

    page_metadata = await capture_page(args.url, args.project_id, output)
    candidates = page_metadata["mediaCandidates"]
    if not candidates:
        raise RuntimeError("No Behance project-module media candidates were found")

    session = requests.Session()
    session.headers.update({
        "User-Agent": USER_AGENT,
        "Referer": args.url,
        "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    })

    media_dir = output / "media"
    media_dir.mkdir()
    records: list[MediaRecord] = []
    frame_records: list[FrameRecord] = []
    module_sheet_entries: list[tuple[str, Image.Image]] = []
    animation_sheet_entries: list[tuple[str, Image.Image]] = []
    failures: list[dict[str, Any]] = []

    for index, candidate in enumerate(candidates, start=1):
        try:
            record, image = download_asset(session, candidate["url"], media_dir, index)
            records.append(record)
            first = image.convert("RGBA" if "A" in image.getbands() else "RGB")
            module_sheet_entries.append((f"MODULE-{index:03d} · {record.width}×{record.height} · {record.format}", first.copy()))
            frames = extract_animation_frames(record, image, output, args.max_animation_frames)
            frame_records.extend(frames)
            for frame_record in frames:
                frame_image = Image.open(output / frame_record.file)
                animation_sheet_entries.append(
                    (
                        f"M{frame_record.media_index:03d} F{frame_record.frame_index:04d} @ {frame_record.timestamp_ms}ms",
                        frame_image.copy(),
                    )
                )
        except Exception as exc:
            failures.append({"index": index, "candidate": candidate, "error": repr(exc)})

    if not records:
        raise RuntimeError(f"All {len(candidates)} media downloads failed: {failures}")

    build_contact_sheet(module_sheet_entries, output / "contact-sheet-modules.jpg")
    build_contact_sheet(animation_sheet_entries, output / "contact-sheet-animation-frames.jpg")

    metadata = {
        "projectId": args.project_id,
        "requestedUrl": args.url,
        **{key: value for key, value in page_metadata.items() if key != "mediaCandidates"},
        "candidateCount": len(candidates),
        "capturedMediaCount": len(records),
        "animatedMediaCount": sum(1 for record in records if record.animated),
        "sampledAnimationFrameCount": len(frame_records),
        "failedMediaCount": len(failures),
        "media": [asdict(record) for record in records],
        "animationFrames": [asdict(record) for record in frame_records],
        "failures": failures,
    }
    (output / "metadata.json").write_text(
        json.dumps(metadata, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(json.dumps(metadata, indent=2, ensure_ascii=False))

    # Fail closed if the browser saw project modules but most could not be captured.
    if len(records) < max(1, math.ceil(len(candidates) * 0.8)):
        raise RuntimeError(
            f"Captured only {len(records)} of {len(candidates)} project media candidates"
        )
    return 0


def main() -> int:
    return asyncio.run(async_main())


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"capture failed: {exc}", file=sys.stderr)
        raise
