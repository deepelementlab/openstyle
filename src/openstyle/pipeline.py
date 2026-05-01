from __future__ import annotations

import re
from pathlib import Path

from openstyle.analyzer.color_extractor import ColorExtractor
from openstyle.analyzer.css_parser import CSSParser
from openstyle.analyzer.html_parser import HTMLParser
from openstyle.generators.design_md import DesignDocGenerator
from openstyle.generators.preview_html import PreviewGenerator
from openstyle.generators.token_mapper import (
    build_dark_palette,
    color_role_description,
    name_color,
    name_color_unique,
)
from openstyle.models import ColorToken, DesignTokens, TypographyToken
from openstyle.readme_en import write_readme_en


class OpenStylePipeline:
    def __init__(self, base_dir: Path | None = None) -> None:
        self.base_dir = base_dir or Path(__file__).resolve().parent
        self.css_parser = CSSParser()
        self.html_parser = HTMLParser()
        self.color_extractor = ColorExtractor()
        templates_dir = self.base_dir / "templates"
        self.doc_gen = DesignDocGenerator(templates_dir)
        self.preview_gen = PreviewGenerator(templates_dir)

    def analyze_template(self, template_dir: Path) -> DesignTokens:
        html_files = sorted(template_dir.glob("*.html"))
        if not html_files:
            raise FileNotFoundError(f"No html files found in {template_dir}")
        index_file = template_dir / "index.html"
        main_html = index_file if index_file.exists() else html_files[0]

        css_files = self._find_css_files(template_dir, main_html)
        css_data = self.css_parser.parse_files(css_files)
        html_data = self.html_parser.parse_file(main_html)

        categorized = self.color_extractor.categorize(css_data["colors"])
        colors = {
            section: [
                ColorToken(value=item["value"], usage=section, frequency=item["frequency"]) for item in items
            ]
            for section, items in categorized.items()
        }

        typography = self._build_typography(css_data)
        tokens = DesignTokens(
            template_name=self._clean_name(template_dir.name),
            source_dir=template_dir,
            colors=colors,
            typography=typography,
            spacing_scale=[v for v, _ in css_data["spacings"].most_common(12)],
            radius_scale=[v for v, _ in css_data["radii"].most_common(10)],
            shadows=[v for v, _ in css_data["shadows"].most_common(8)],
            breakpoints=[v for v, _ in css_data["breakpoints"].most_common(8)],
            components=html_data["components"],
            layout_notes=html_data["layout_notes"],
        )
        return tokens

    def generate_all(
        self,
        template_dir: Path,
        output_dir: Path,
        *,
        output_folder_name: str | None = None,
        readme_bundle: dict | None = None,
    ) -> Path:
        tokens = self.analyze_template(template_dir)
        folder_name = output_folder_name if output_folder_name is not None else self._slugify(tokens.template_name)
        target = output_dir / folder_name
        target.mkdir(parents=True, exist_ok=True)

        design_text = self.doc_gen.render(tokens)
        (target / "DESIGN.md").write_text(design_text, encoding="utf-8")

        light_context, dark_context = self._build_preview_context(tokens)
        (target / "preview.html").write_text(self.preview_gen.render(light_context), encoding="utf-8")
        (target / "preview-dark.html").write_text(self.preview_gen.render(dark_context), encoding="utf-8")

        if readme_bundle:
            write_readme_en(
                target,
                bundle_folder_name=readme_bundle["bundle_folder_name"],
                bundle_title_zh=readme_bundle["bundle_title_zh"],
                bundle_title_en=readme_bundle["bundle_title_en"],
                bundle_slug=readme_bundle["bundle_slug"],
                template_variant=template_dir.name,
                source_template_dir=template_dir.resolve(),
                tokens=tokens,
            )
        return target

    def generate_preview_from_design(self, design_md: Path, output_dir: Path) -> Path:
        name = design_md.parent.name
        target = output_dir
        target.mkdir(parents=True, exist_ok=True)
        base_palette = {
            "--bg": "#ffffff",
            "--fg": "#171717",
            "--surface": "#f8fafc",
            "--border": "#e0e0e0",
            "--accent": "#0072f5",
            "--weak": "rgba(23,23,23,0.55)",
        }
        light = self._build_base_preview(name, base_palette, dark=False)
        dark = self._build_base_preview(name, build_dark_palette(base_palette), dark=True)
        (target / "preview.html").write_text(self.preview_gen.render(light), encoding="utf-8")
        (target / "preview-dark.html").write_text(self.preview_gen.render(dark), encoding="utf-8")
        return target

    def _find_css_files(self, template_dir: Path, html_file: Path) -> list[Path]:
        html_text = html_file.read_text(encoding="utf-8", errors="ignore")
        hrefs = re.findall(r'href=["\']([^"\']+\.css)["\']', html_text, flags=re.IGNORECASE)
        files: list[Path] = []
        for href in hrefs:
            css_path = (template_dir / href).resolve()
            if css_path.exists():
                files.append(css_path)
        if files:
            return files
        fallback = list(template_dir.glob("css/*.css")) + list(template_dir.glob("*.css"))
        if not fallback:
            raise FileNotFoundError("No css files found for template")
        return fallback

    @staticmethod
    def _build_typography(css_data: dict) -> list[TypographyToken]:
        families = [v for v, _ in css_data["font_families"].most_common(6)] or ["system-ui"]
        sizes = [v for v, _ in css_data["font_sizes"].most_common(8)] or ["16px"]
        weights = [v for v, _ in css_data["font_weights"].most_common(6)] or ["400"]
        lines = [v for v, _ in css_data["line_heights"].most_common(6)] or ["1.5"]
        letters = [v for v, _ in css_data["letter_spacings"].most_common(6)] or ["normal"]
        usage = ["Display", "Heading", "Sub-heading", "Body", "Caption", "Button", "Mono", "Label"]

        tokens: list[TypographyToken] = []
        for idx, size in enumerate(sizes):
            tokens.append(
                TypographyToken(
                    family=families[min(idx, len(families) - 1)],
                    size_px=_to_px(size),
                    weight=weights[min(idx, len(weights) - 1)],
                    line_height=lines[min(idx, len(lines) - 1)],
                    letter_spacing=letters[min(idx, len(letters) - 1)],
                    usage=usage[min(idx, len(usage) - 1)],
                )
            )
        return tokens

    def _build_preview_context(self, tokens: DesignTokens) -> tuple[dict, dict]:
        def first(section: str, default: str) -> str:
            items = tokens.colors.get(section, [])
            return items[0].value if items else default

        def classify_fg_bg() -> tuple[str, str]:
            candidates = [c.value for c in tokens.colors.get("neutral", []) + tokens.colors.get("primary", [])]
            best_bg = "#ffffff"
            best_fg = "#171717"
            bg_score = -1.0
            fg_score = 2.0
            for c in candidates:
                lum = _luminance(c)
                if lum is None:
                    continue
                if lum > bg_score:
                    bg_score = lum
                    best_bg = c
                if lum < fg_score:
                    fg_score = lum
                    best_fg = c
            if best_bg.lower() == best_fg.lower():
                best_bg = "#ffffff"
                best_fg = "#171717"
            return best_fg, best_bg

        fg, bg = classify_fg_bg()

        accent_color = first("accent", "#0072f5")
        border_color = self._pick_border_color(tokens)
        weak_color = self._build_weak_color(fg)
        surface_color = self._pick_surface_color(tokens)

        base_palette = {
            "--bg": bg,
            "--fg": fg,
            "--accent": accent_color,
            "--border": border_color,
            "--weak": weak_color,
            "--surface": surface_color,
        }
        return (
            self._build_base_preview(tokens.template_name, base_palette, dark=False, tokens=tokens),
            self._build_base_preview(tokens.template_name, build_dark_palette(base_palette), dark=True, tokens=tokens),
        )

    def _build_base_preview(self, template_name: str, palette: dict[str, str], dark: bool, tokens: DesignTokens | None = None) -> dict:
        color_groups: dict[str, list[dict]] = {}
        if tokens:
            for section in ("primary", "accent", "neutral", "semantic"):
                items = tokens.colors.get(section, [])
                raw = [{"value": item.value, "role": item.usage} for item in items[:6]]
                named = name_color_unique(raw)
                for n in named:
                    n["description"] = color_role_description(n["role"], n["value"])
                color_groups[section] = named
        all_colors: list[dict] = []
        for group_items in color_groups.values():
            all_colors.extend(group_items)
        all_colors = all_colors[:24]
        primary_font = "system-ui"
        if tokens and tokens.typography:
            primary_font = tokens.typography[0].family.split(",")[0].strip().strip('"').strip("'")
        return {
            "template_name": template_name,
            "mode": "Dark" if dark else "Light",
            "palette": palette,
            "color_groups": color_groups,
            "sample_colors": all_colors,
            "typography": tokens.typography[:8] if tokens else [],
            "primary_font": primary_font,
            "spacing_scale": tokens.spacing_scale[:10] if tokens else ["4px", "8px", "12px", "16px", "24px", "32px"],
            "radius_scale": tokens.radius_scale[:8] if tokens else ["2px", "4px", "6px", "8px", "12px", "9999px"],
            "shadows": tokens.shadows[:6] if tokens else [palette.get("--shadow-ring", "none")],
            "components": [{"name": c.name, "traits": c.traits} for c in (tokens.components if tokens else [])],
        }

    @staticmethod
    def _pick_border_color(tokens: DesignTokens) -> str:
        for section in ("neutral", "primary"):
            for c in tokens.colors.get(section, []):
                lum = _luminance(c.value)
                if lum is not None and 0.6 < lum < 0.95:
                    return c.value
        return "#e0e0e0"

    @staticmethod
    def _pick_surface_color(tokens: DesignTokens) -> str:
        for section in ("neutral", "primary"):
            for c in tokens.colors.get(section, []):
                lum = _luminance(c.value)
                if lum is not None and 0.9 < lum < 0.99 and not c.value.lower().startswith("rgba"):
                    return c.value
        return "#f8fafc"

    @staticmethod
    def _build_weak_color(fg: str) -> str:
        lum = _luminance(fg)
        if lum is None or lum < 0.5:
            return "rgba(23,23,23,0.55)"
        return "rgba(255,255,255,0.55)"

    @staticmethod
    def _clean_name(name: str) -> str:
        return re.sub(r"[_-]+", " ", name).strip()

    @staticmethod
    def _slugify(name: str) -> str:
        slug = re.sub(r"[^0-9a-zA-Z\u4e00-\u9fff]+", "-", name).strip("-").lower()
        return slug or "template"


def _to_px(value: str) -> float:
    value = value.strip().lower()
    if value.endswith("px"):
        try:
            return float(value[:-2])
        except ValueError:
            return 16.0
    if value.endswith("rem"):
        try:
            return float(value[:-3]) * 16.0
        except ValueError:
            return 16.0
    try:
        return float(value)
    except ValueError:
        return 16.0


def _luminance(color: str) -> float | None:
    color = color.strip().lower()
    if color.startswith("#"):
        value = color[1:]
        if len(value) == 3:
            value = "".join(ch * 2 for ch in value)
        if len(value) != 6:
            return None
        try:
            r = int(value[0:2], 16) / 255.0
            g = int(value[2:4], 16) / 255.0
            b = int(value[4:6], 16) / 255.0
            return 0.2126 * r + 0.7152 * g + 0.0722 * b
        except ValueError:
            return None
    return None
