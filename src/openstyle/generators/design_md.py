from __future__ import annotations

import re
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

from openstyle.generators.token_mapper import (
    _any_to_rgb,
    _rgb_to_hsl,
    color_role_description,
    name_color,
)
from openstyle.models import DesignTokens


def _clean_font_name(family: str) -> str:
    return family.split(",")[0].strip().strip('"').strip("'")


def _summarize_scale(values: list[str]) -> str:
    if not values:
        return ""
    nums = []
    for v in values:
        m = re.match(r"([\d.]+)", v)
        if m:
            nums.append(float(m.group(1)))
    if len(nums) < 2:
        return ""
    return f"{min(nums):.0f}–{max(nums):.0f}px ({len(nums)} steps)"


class DesignDocGenerator:
    def __init__(self, template_dir: Path) -> None:
        self.env = Environment(
            loader=FileSystemLoader(str(template_dir)),
            autoescape=select_autoescape(enabled_extensions=()),
            trim_blocks=True,
            lstrip_blocks=True,
        )
        self.template = self.env.get_template("design_template.md")

    def render(self, tokens: DesignTokens) -> str:
        used_names: dict[str, int] = {}
        color_sections: dict[str, list[dict]] = {}
        for key, values in tokens.colors.items():
            items = []
            for item in values:
                base = name_color(item.value)
                count = used_names.get(base, 0)
                used_names[base] = count + 1
                semantic_name = f"{base} {count + 1}" if count > 0 else base
                desc = color_role_description(item.usage, item.value)
                items.append({
                    "semantic_name": semantic_name,
                    "value": item.value,
                    "usage": item.usage,
                    "frequency": item.frequency,
                    "description": desc,
                })
            color_sections[key] = items

        accent_colors = []
        for item in tokens.colors.get("accent", []):
            base = name_color(item.value)
            accent_colors.append({"value": item.value, "semantic_name": base})

        typography_rows = [
            {
                "family": t.family,
                "size": t.size_px,
                "weight": t.weight,
                "line_height": t.line_height,
                "letter_spacing": t.letter_spacing,
                "usage": t.usage,
            }
            for t in tokens.typography
        ]

        primary_font = ""
        if tokens.typography:
            primary_font = _clean_font_name(tokens.typography[0].family)

        visual_desc = self._build_visual_description(tokens, primary_font, accent_colors)

        return self.template.render(
            brand_name=tokens.template_name,
            visual_theme_description=visual_desc,
            color_sections=color_sections,
            typography_rows=typography_rows,
            components=tokens.components,
            spacing_scale=tokens.spacing_scale,
            spacing_scale_clean=_summarize_scale(tokens.spacing_scale),
            radius_scale=tokens.radius_scale,
            radius_scale_clean=_summarize_scale(tokens.radius_scale),
            shadows=tokens.shadows,
            breakpoints=tokens.breakpoints,
            layout_notes=tokens.layout_notes,
            primary_font=primary_font,
            accent_colors=accent_colors,
        )

    @staticmethod
    def _build_visual_description(tokens: DesignTokens, primary_font: str, accent_colors: list[dict]) -> str:
        fg_color = ""
        bg_color = ""
        for section in ("primary", "neutral"):
            for c in tokens.colors.get(section, []):
                rgb = _any_to_rgb(c.value)
                if rgb is None:
                    continue
                _, _, l = _rgb_to_hsl(*rgb)
                if l > 50 and not bg_color:
                    bg_color = c.value
                elif l <= 50 and not fg_color:
                    fg_color = c.value

        parts: list[str] = []
        if fg_color:
            fg_name = name_color(fg_color)
            parts.append(f"deep {fg_name.lower()}" if "dark" in fg_name.lower() or "deep" in fg_name.lower() else fg_name.lower())
        if bg_color:
            bg_name = name_color(bg_color)
            parts.append(f"{bg_name.lower()} canvas" if bg_name.lower() != "white" else "white canvas")

        accent_name = ""
        if accent_colors:
            accent_name = accent_colors[0].get("semantic_name", "")

        if accent_name:
            parts.append(f"{accent_name} as the primary accent for interactive elements")

        base = "This template presents a structured, modular web design"
        if parts:
            base += f" built on a {' with '.join(parts[:2])}"
            if len(parts) > 2:
                base += f", using {parts[2]}"
        base += "."

        if primary_font and primary_font not in ("system-ui", "inherit"):
            base += f" The typography is anchored by `{primary_font}`, creating a consistent reading experience."

        if tokens.typography and len(tokens.typography) > 2:
            sizes = [t.size_px for t in tokens.typography if t.size_px > 0]
            if sizes:
                base += f" The type scale spans {min(sizes):.0f}px to {max(sizes):.0f}px across {len(sizes)} levels."

        return base
