from __future__ import annotations

import hashlib
import json
import re
import time
from pathlib import Path

from pypinyin import Style, lazy_pinyin

_MOBCSS_PATTERNS = (
    re.compile(r"模板_www\.mobancss\.com$", re.IGNORECASE),
    re.compile(r"_www\.mobancss\.com$", re.IGNORECASE),
)


def strip_mobancss_bundle_suffix(name: str) -> str:
    """Strip `模板_www.mobancss.com` / `_www.mobancss.com` and trailing `模板`."""
    s = name.strip()
    for pat in _MOBCSS_PATTERNS:
        s = pat.sub("", s)
    s = re.sub(r"模板$", "", s)
    return s.strip(" _-")


def slugify_ascii(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return re.sub(r"-{2,}", "-", text).strip("-") or "template"


# Windows: avoid huge single path components (WinError 123 / MAX_PATH). Only trim when obnoxiously long.
DEFAULT_SLUG_MAX_LEN = 140


def shorten_filesystem_slug(slug: str, *, seed: str, max_len: int = DEFAULT_SLUG_MAX_LEN) -> str:
    """Shorten an ASCII slug when it exceeds *max_len* (pinyin of long folder names can exceed OS limits)."""
    slug = slugify_ascii(slug)
    if not slug:
        slug = "template"
    if len(slug) <= max_len:
        return slug
    digest = hashlib.sha1(seed.encode("utf-8")).hexdigest()[:8]
    keep = max(24, max_len - len(digest) - 1)
    head = slug[:keep].rstrip("-") or "tpl"
    out = f"{head}-{digest}"
    return out if len(out) <= max_len else out[:max_len]


def _pinyin_slug(text: str) -> str:
    parts: list[str] = []
    buf: list[str] = []
    for ch in text:
        if "\u4e00" <= ch <= "\u9fff":
            if buf:
                parts.append("".join(buf))
                buf = []
            parts.extend(lazy_pinyin(ch, style=Style.NORMAL))
        elif ch.isascii() and (ch.isalnum() or ch in "._-"):
            buf.append(ch.lower())
        else:
            if buf:
                parts.append("".join(buf))
                buf = []
    if buf:
        parts.append("".join(buf))
    joined = "-".join(p for p in parts if p)
    return slugify_ascii(joined)


def _translate_to_english(text: str) -> str | None:
    try:
        from deep_translator import GoogleTranslator

        t = GoogleTranslator(source="auto", target="en")
        # Avoid over-long API payloads
        snippet = text[:800]
        return t.translate(snippet)
    except Exception:  # noqa: BLE001
        return None


def bundle_english_labels(
    display_name_zh: str,
    *,
    cache_path: Path | None = None,
    use_translation: bool = True,
    sleep_s: float = 0.35,
) -> tuple[str, str]:
    """Return (english_title, ascii_slug) for a cleaned Chinese bundle label."""
    key = display_name_zh.strip()
    cache: dict[str, dict[str, str]] = {}
    if cache_path and cache_path.exists():
        try:
            cache = json.loads(cache_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            cache = {}
    if key in cache:
        entry = cache[key]
        if isinstance(entry, str):
            slug = entry
            title = slug.replace("-", " ").strip().title() or "Website Template"
            slug = shorten_filesystem_slug(slug, seed=key)
            return title, slug
        if isinstance(entry, dict) and "title" in entry and "slug" in entry:
            slug = shorten_filesystem_slug(entry["slug"], seed=key)
            return entry["title"], slug

    english = _translate_to_english(key) if use_translation else None
    if sleep_s > 0:
        time.sleep(sleep_s)
    if english:
        title = english.strip()
        slug = slugify_ascii(english)
    else:
        slug = _pinyin_slug(key)
        title = slug.replace("-", " ").strip().title() or "Website Template"

    if not slug:
        slug = "template"

    slug = shorten_filesystem_slug(slug, seed=key)

    if cache_path:
        cache[key] = {"title": title, "slug": slug}
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        cache_path.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")

    return title, slug


def english_output_slug(
    display_name_zh: str,
    *,
    cache_path: Path | None = None,
    use_translation: bool = True,
    sleep_s: float = 0.35,
) -> str:
    """Backward-compatible: slug only."""
    _, slug = bundle_english_labels(
        display_name_zh,
        cache_path=cache_path,
        use_translation=use_translation,
        sleep_s=sleep_s,
    )
    return slug


def unique_slug(base: str, used: set[str]) -> str:
    def clash(candidate: str) -> bool:
        cf = candidate.casefold()
        return any(u.casefold() == cf for u in used)

    if not clash(base):
        used.add(base)
        return base
    digest = hashlib.sha1(base.encode("utf-8")).hexdigest()[:6]
    candidate = f"{base}-{digest}"
    n = 2
    while clash(candidate):
        candidate = f"{base}-{digest}-{n}"
        n += 1
    used.add(candidate)
    return candidate
