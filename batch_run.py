from __future__ import annotations

import hashlib
import json
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from openstyle.pipeline import OpenStylePipeline
from openstyle.naming import strip_mobancss_bundle_suffix, slugify_ascii
from pypinyin import Style, lazy_pinyin

OPENSTYLE_ROOT = Path(r"e:\OpenStyle")
OUTPUT_DIR = Path(r"e:\OpenStyle\UI")
CACHE_PATH = OPENSTYLE_ROOT / ".openstyle-en-cache.json"

SKIP_ROOT = {"ui", "openstyle", ".git", ".cursor", "node_modules", ".venv", "__pycache__"}
SKIP_INNER = {
    "vendor", "node_modules", "demo", "docs", "source", "vendors",
    "bower_components", "documentation", "examples", "example", "demos",
    "tests", "test", "coverage", ".git",
}

NOISE_WORDS = frozenset({
    "template", "templates", "website", "web", "site", "page", "pages",
    "html", "html5", "css", "css3", "bootstrap", "responsive", "static",
    "www", "com", "net", "org", "mobancss",
    "the", "a", "an", "and", "or", "of", "for", "with", "in", "on",
    "整站", "模板", "网站", "素材", "专题", "活动", "上线", "倒计时",
    "幻灯", "轮播", "背景", "大图", "单页", "多页",
})

SITE_TYPE_KEYWORDS = {
    "website": "website", "site": "website", "portal": "portal",
    "landing": "landing", "app": "app", "blog": "blog",
    "shop": "shop", "store": "store", "company": "company",
    "corporate": "corporate", "agency": "agency", "market": "market",
    "mall": "mall", "platform": "platform", "foundation": "foundation",
}

CATEGORY_KEYWORDS = {
    "digital": "digital", "electronics": "electronics", "3c": "3c",
    "product": "product", "design": "design", "fashion": "fashion",
    "food": "food", "travel": "travel", "real-estate": "real-estate",
    "charity": "charity", "legal": "legal", "law": "legal",
    "finance": "finance", "banking": "banking",
    "education": "education", "training": "training", "logistics": "logistics",
    "shipping": "logistics", "transport": "logistics", "machinery": "industrial",
    "industrial": "industrial", "mechanical": "industrial",
    "photography": "photography", "photo": "photography",
    "christmas": "christmas", "spring-festival": "spring-festival",
    "beauty": "beauty", "hair": "beauty", "salon": "beauty",
    "game": "game", "gaming": "game", "floral": "floral",
    "flower": "floral", "plant": "floral", "gardening": "floral",
    "cleaning": "cleaning", "villa": "villa", "luxury": "luxury",
    "marketing": "marketing", "ecommerce": "ecommerce",
    "commerce": "ecommerce", "shopping": "ecommerce",
    "news": "news", "media": "media", "social": "social",
    "personal": "personal", "resume": "resume", "consulting": "consulting",
    "3d": "3d", "it": "it", "cosplay": "cosplay", "festival": "festival",
    "holiday": "holiday", "medical": "medical", "health": "health",
    "restaurant": "restaurant", "cafe": "restaurant", "coffee": "restaurant",
    "hotel": "hotel", "wedding": "wedding", "music": "music",
    "sport": "sport", "fitness": "fitness", "gym": "fitness",
    "automotive": "automotive", "car": "automotive", "auto": "automotive",
    "pet": "pet", "animal": "pet", "construction": "construction",
    "building": "construction", "architecture": "architecture",
    "interior": "interior", "furniture": "furniture",
    "insurance": "insurance", "security": "security",
    "energy": "energy", "solar": "energy",
    "environment": "environment", "green": "environment",
    "art": "art", "painting": "art", "gallery": "art",
    "movie": "movie", "film": "movie", "cinema": "movie",
    "book": "book", "library": "library", "school": "education",
    "university": "education", "baby": "baby", "kids": "kids",
    "children": "kids", "toy": "toy",
}


def load_cache() -> dict:
    if CACHE_PATH.exists():
        try:
            return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return {}
    return {}


def save_cache(cache: dict) -> None:
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    CACHE_PATH.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")


def translate_to_english(text: str) -> str | None:
    translators = []
    try:
        from deep_translator import MyMemoryTranslator
        translators.append(lambda: MyMemoryTranslator(source="chinese simplified", target="english"))
    except Exception:
        pass
    try:
        from deep_translator import GoogleTranslator
        translators.append(lambda: GoogleTranslator(source="auto", target="en"))
    except Exception:
        pass
    for make_t in translators:
        try:
            result = make_t().translate(text[:500])
            if result and any(c.isalpha() and ord(c) < 128 for c in result):
                return result.strip()
        except Exception:
            continue
    return None


def pinyin_fallback(text: str) -> str:
    parts: list[str] = []
    for ch in text:
        if "\u4e00" <= ch <= "\u9fff":
            parts.extend(lazy_pinyin(ch, style=Style.NORMAL))
        elif ch.isascii() and (ch.isalnum() or ch in "._- "):
            parts.append(ch.lower())
        else:
            parts.append(" ")
    return " ".join(p for p in "".join(parts).split() if p)


def clean_display_name(raw: str) -> str:
    s = raw.strip()
    idx = s.find("_")
    if idx > 0:
        prefix = s[:idx]
        suffix = s[idx + 1:]
        has_chinese_suffix = any("\u4e00" <= c <= "\u9fff" for c in suffix)
        has_english_suffix = any(c.isalpha() and ord(c) < 128 for c in suffix)
        if has_chinese_suffix or has_english_suffix:
            main_part = prefix
        else:
            main_part = s
    else:
        main_part = s
    main_part = re.sub(r"模板$", "", main_part).strip(" _-")
    return main_part


def make_output_slug(english_title: str, seed: str = "") -> str:
    if not english_title:
        return "template"

    words = re.split(r"[\s\-_,;：；、]+", english_title.lower())
    words = [w.strip(".,;:!?()[]{}""''") for w in words]
    words = [w for w in words if w and w not in NOISE_WORDS and len(w) > 1]

    site_type = ""
    category = ""
    kw_parts: list[str] = []

    for w in words:
        if w in SITE_TYPE_KEYWORDS and not site_type:
            site_type = SITE_TYPE_KEYWORDS[w]
        elif w in CATEGORY_KEYWORDS and not category:
            category = CATEGORY_KEYWORDS[w]
        else:
            if w not in NOISE_WORDS and w not in SITE_TYPE_KEYWORDS and w not in CATEGORY_KEYWORDS:
                kw_parts.append(w)

    if not site_type:
        site_type = "website"
    if not category:
        if kw_parts:
            category = slugify_ascii(kw_parts.pop(0)) or "web"
        else:
            category = "web"

    seen_kw: set[str] = set()
    unique_kw: list[str] = []
    for k in kw_parts:
        s = slugify_ascii(k)
        if s and s not in seen_kw:
            seen_kw.add(s)
            unique_kw.append(s)

    unique_kw = unique_kw[:5]
    kw_slug = "-".join(unique_kw)

    if kw_slug:
        raw = f"{category}_{site_type}_{kw_slug}"
    else:
        raw = f"{category}_{site_type}"

    raw = re.sub(r"[^a-z0-9_\-]", "", raw)
    raw = re.sub(r"-{2,}", "-", raw).strip("-_")
    raw = re.sub(r"_{2,}", "_", raw).strip("_")

    if len(raw) > 120:
        digest = hashlib.sha1(seed.encode("utf-8")).hexdigest()[:8]
        keep = max(30, 110 - len(digest))
        head = raw[:keep].rstrip("-_") or "tpl"
        raw = f"{head}-{digest}"

    return raw


def unique_slug(base: str, used: set[str]) -> str:
    def clash(c: str) -> bool:
        return any(u.casefold() == c.casefold() for u in used)

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


def find_index_files(bundle: Path) -> list[Path]:
    results: list[Path] = []
    for pattern in ("index.html", "index.htm", "Index.html", "INDEX.HTML"):
        results.extend(bundle.rglob(pattern))

    seen: set[Path] = set()
    unique: list[Path] = []
    for p in sorted(results):
        if p.name.casefold() not in ("index.html", "index.htm"):
            continue
        r = p.resolve()
        if r in seen:
            continue
        try:
            rel = r.relative_to(bundle.resolve())
        except ValueError:
            continue
        if len(rel.parts) > 6:
            continue
        dir_parts = {part.casefold() for part in rel.parts[:-1]}
        if dir_parts & {s.casefold() for s in SKIP_INNER}:
            continue
        seen.add(r)
        unique.append(p)
    return unique


def write_clean_readme(target: Path, slug: str, english_title: str, tokens) -> None:
    title = english_title.strip() if english_title and any(c.isalpha() and ord(c) < 128 for c in english_title) else slug.replace("-", " ").replace("_", " ").title()
    if not title:
        title = slug.replace("-", " ").replace("_", " ").title()
    color_groups = sorted(tokens.colors.keys())
    components = [c.name for c in tokens.components]
    primary_font = ""
    if tokens.typography:
        primary_font = tokens.typography[0].family.split(",")[0].strip().strip('"').strip("'")

    lines = [
        f"# {title}",
        "",
        "A design system extracted from an HTML website template by **OpenStyle**. "
        "This document summarizes the visual design tokens — colors, typography, spacing, and component patterns — derived from the template's CSS.",
        "",
        "## Files",
        "",
        "| File | Description |",
        "|------|-------------|",
        "| `DESIGN.md` | Complete design system specification (9 sections) |",
        "| `preview.html` | Interactive design token catalog (light mode) |",
        "| `preview-dark.html` | Interactive design token catalog (dark mode) |",
        "",
        "## Extracted Summary",
        "",
        f"- **Design system name:** {tokens.template_name}",
        f"- **Color groups:** {', '.join(color_groups) or '—'}",
        f"- **Detected components:** {', '.join(components) or '—'}",
        f"- **Typography levels:** {len(tokens.typography)}",
        f"- **Spacing tokens:** {len(tokens.spacing_scale)}",
        f"- **Shadow tokens:** {len(tokens.shadows)}",
    ]

    if primary_font and primary_font not in ("system-ui", "inherit"):
        lines.extend(["", f"- **Primary font:** `{primary_font}`"])

    lines.extend([
        "",
        "## Usage",
        "",
        "Use `DESIGN.md` as a reference for AI agents (Claude, Cursor, Stitch) to generate UI that follows this design language. "
        "Open `preview.html` or `preview-dark.html` in a browser to see the actual design tokens rendered visually.",
        "",
    ])

    (target / "README.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    pipeline = OpenStylePipeline()
    cache = load_cache()
    output_dir = OUTPUT_DIR
    output_dir.mkdir(parents=True, exist_ok=True)

    used_slugs: set[str] = {p.name for p in output_dir.iterdir() if p.is_dir()}

    bundles = sorted(
        [p for p in OPENSTYLE_ROOT.iterdir() if p.is_dir()],
        key=lambda p: p.name.casefold(),
    )

    generated = 0
    skipped = 0
    errors = 0

    for bundle in bundles:
        if bundle.name.casefold() in {s.casefold() for s in SKIP_ROOT}:
            continue

        index_files = find_index_files(bundle)
        if not index_files:
            print(f"[SKIP] No index.html in {bundle.name!r}")
            skipped += 1
            continue

        raw_display = strip_mobancss_bundle_suffix(bundle.name)
        display_zh = clean_display_name(raw_display)

        if display_zh in cache and isinstance(cache[display_zh], dict) and "en_title" in cache[display_zh]:
            english_title = cache[display_zh]["en_title"]
        else:
            english_title = translate_to_english(display_zh)
            time.sleep(0.15)
            if not english_title or not any(c.isalpha() and ord(c) < 128 for c in english_title):
                english_title = pinyin_fallback(display_zh)
            cache[display_zh] = {"en_title": english_title}
            save_cache(cache)

        slug = make_output_slug(english_title, seed=bundle.name)
        slug = unique_slug(slug, used_slugs)

        for idx, index_file in enumerate(index_files):
            template_dir = index_file.parent.resolve()

            if len(index_files) == 1:
                target = output_dir / slug
            else:
                target = output_dir / f"{slug}-v{idx + 1}"

            if target.exists() and (target / "DESIGN.md").exists():
                print(f"[SKIP exists] {target.name}")
                continue

            target.mkdir(parents=True, exist_ok=True)

            try:
                tokens = pipeline.analyze_template(template_dir)

                design_text = pipeline.doc_gen.render(tokens)
                (target / "DESIGN.md").write_text(design_text, encoding="utf-8")

                light_ctx, dark_ctx = pipeline._build_preview_context(tokens)
                (target / "preview.html").write_text(pipeline.preview_gen.render(light_ctx), encoding="utf-8")
                (target / "preview-dark.html").write_text(pipeline.preview_gen.render(dark_ctx), encoding="utf-8")

                write_clean_readme(target, slug, english_title, tokens)

                print(f"[OK] {bundle.name} -> {target.name}")
                generated += 1

            except Exception as exc:
                print(f"[ERROR] {bundle.name} ({index_file.parent.name}): {exc}")
                errors += 1

    save_cache(cache)
    print(f"\nCompleted. Generated: {generated}, Skipped: {skipped}, Errors: {errors}")


if __name__ == "__main__":
    main()
