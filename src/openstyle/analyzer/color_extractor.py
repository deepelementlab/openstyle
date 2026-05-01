from __future__ import annotations

import re
from collections import Counter

from colormath.color_objects import sRGBColor


HEX_PATTERN = re.compile(r"^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$")


def _to_rgb(color: str) -> tuple[int, int, int] | None:
    color = color.strip().lower()
    if HEX_PATTERN.match(color):
        hex_value = color.lstrip("#")
        if len(hex_value) == 3:
            hex_value = "".join(ch * 2 for ch in hex_value)
        return tuple(int(hex_value[i : i + 2], 16) for i in (0, 2, 4))
    rgb_match = re.match(r"rgba?\(([^)]+)\)", color)
    if rgb_match:
        parts = [p.strip() for p in rgb_match.group(1).split(",")]
        if len(parts) >= 3:
            try:
                return int(float(parts[0])), int(float(parts[1])), int(float(parts[2]))
            except ValueError:
                return None
    return None


class ColorExtractor:
    def categorize(self, color_counts: Counter[str]) -> dict[str, list[dict]]:
        ranked = color_counts.most_common(24)
        if not ranked:
            return {"primary": [], "accent": [], "neutral": [], "semantic": []}

        colored: list[tuple[str, int, tuple[int, int, int], float, float]] = []
        for color, count in ranked:
            rgb = _to_rgb(color)
            if not rgb:
                continue
            srgb = sRGBColor(rgb[0] / 255.0, rgb[1] / 255.0, rgb[2] / 255.0)
            sat = max(rgb) - min(rgb)
            lum = (0.2126 * srgb.rgb_r + 0.7152 * srgb.rgb_g + 0.0722 * srgb.rgb_b)
            colored.append((color, count, rgb, sat, lum))

        colored.sort(key=lambda x: x[1], reverse=True)
        primary = []
        accent = []
        neutral = []
        semantic = []

        for color, count, _rgb, sat, lum in colored:
            item = {"value": color, "frequency": count}
            if sat < 20:
                neutral.append(item)
            elif lum > 0.85 or lum < 0.15:
                primary.append(item)
            elif "red" in color or "green" in color:
                semantic.append(item)
            else:
                accent.append(item)

        if not primary and colored:
            primary.append({"value": colored[0][0], "frequency": colored[0][1]})

        return {
            "primary": primary[:4],
            "accent": accent[:6],
            "neutral": neutral[:8],
            "semantic": semantic[:4],
        }
