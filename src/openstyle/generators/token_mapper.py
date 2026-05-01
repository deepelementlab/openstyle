from __future__ import annotations

import re


def _hex_to_rgb(color: str) -> tuple[int, int, int] | None:
    c = color.strip().lower()
    if not c.startswith("#"):
        return None
    value = c[1:]
    if len(value) == 3:
        value = "".join(v * 2 for v in value)
    if len(value) != 6:
        return None
    return int(value[0:2], 16), int(value[2:4], 16), int(value[4:6], 16)


def _parse_rgb_functional(color: str) -> tuple[int, int, int] | None:
    m = re.match(r"rgba?\(\s*([^)]+)\)", color.strip())
    if not m:
        return None
    parts = [p.strip() for p in m.group(1).split(",")]
    if len(parts) < 3:
        return None
    try:
        return int(float(parts[0])), int(float(parts[1])), int(float(parts[2]))
    except ValueError:
        return None


def _any_to_rgb(color: str) -> tuple[int, int, int] | None:
    rgb = _hex_to_rgb(color)
    if rgb:
        return rgb
    return _parse_rgb_functional(color)


def _rgb_to_hex(rgb: tuple[int, int, int]) -> str:
    return "#{:02x}{:02x}{:02x}".format(*rgb)


def _rgb_to_hsl(r: int, g: int, b: int) -> tuple[float, float, float]:
    r_f, g_f, b_f = r / 255.0, g / 255.0, b / 255.0
    max_c = max(r_f, g_f, b_f)
    min_c = min(r_f, g_f, b_f)
    l = (max_c + min_c) / 2
    if max_c == min_c:
        return 0.0, 0.0, l * 100
    d = max_c - min_c
    s = d / (2 - max_c - min_c) if l > 0.5 else d / (max_c + min_c)
    if max_c == r_f:
        h = ((g_f - b_f) / d + (6 if g_f < b_f else 0)) / 6
    elif max_c == g_f:
        h = ((b_f - r_f) / d + 2) / 6
    else:
        h = ((r_f - g_f) / d + 4) / 6
    return h * 360, s * 100, l * 100


def _hue_name(h_deg: float) -> str:
    if h_deg < 15:
        return "Red"
    if h_deg < 35:
        return "Orange"
    if h_deg < 50:
        return "Amber"
    if h_deg < 70:
        return "Yellow"
    if h_deg < 90:
        return "Lime"
    if h_deg < 150:
        return "Green"
    if h_deg < 175:
        return "Teal"
    if h_deg < 200:
        return "Cyan"
    if h_deg < 250:
        return "Blue"
    if h_deg < 280:
        return "Indigo"
    if h_deg < 310:
        return "Purple"
    if h_deg < 340:
        return "Pink"
    return "Red"


def name_color(value: str) -> str:
    rgb = _any_to_rgb(value)
    if rgb is None:
        return value
    h, s, l = _rgb_to_hsl(*rgb)
    if s < 10:
        if l >= 95:
            return "White"
        if l >= 82:
            return "Light Gray"
        if l >= 65:
            return "Silver"
        if l >= 45:
            return "Mid Gray"
        if l >= 28:
            return "Dark Gray"
        if l >= 12:
            return "Charcoal"
        return "Black"
    hue = _hue_name(h)
    parts: list[str] = []
    if l < 18:
        parts.append("Deep")
    elif l < 32:
        parts.append("Dark")
    elif l > 88:
        parts.append("Pale")
    elif l > 72:
        parts.append("Light")
    elif l > 58:
        parts.append("Soft")
    if s < 35:
        parts.append("Muted")
    elif s > 80:
        parts.append("Vivid")
    parts.append(hue)
    return " ".join(parts)


def name_color_unique(colors: list[dict]) -> list[dict]:
    named: list[dict] = []
    used_names: dict[str, int] = {}
    for item in colors:
        base = name_color(item["value"])
        count = used_names.get(base, 0)
        used_names[base] = count + 1
        if count > 0:
            name = f"{base} {count + 1}"
        else:
            name = base
        named.append({**item, "semantic_name": name})
    return named


def color_role_description(role: str, value: str) -> str:
    rgb = _any_to_rgb(value)
    lum = 0.5
    if rgb:
        _, _, l = _rgb_to_hsl(*rgb)
        lum = l / 100.0
    descs = {
        "primary": [
            ("Primary text color" if lum < 0.4 else "Primary surface color"),
            ("Main identity color" if lum < 0.3 else "Primary background"),
        ],
        "accent": [
            "CTAs, links, and interactive highlights",
            "Brand accent for buttons and emphasis",
        ],
        "neutral": [
            ("Border and divider color" if 0.4 < lum < 0.85 else "Structural background"),
            ("Muted text and secondary elements" if lum < 0.5 else "Subtle surface tint"),
        ],
        "semantic": [
            "Status and feedback color",
            "Semantic indicator",
        ],
    }
    candidates = descs.get(role, ["Design token"])
    return candidates[0]


def _invert_hex(color: str) -> str:
    rgb = _hex_to_rgb(color)
    if not rgb:
        return color
    return _rgb_to_hex(tuple(255 - c for c in rgb))


def build_dark_palette(light_palette: dict[str, str]) -> dict[str, str]:
    mapped = dict(light_palette)
    bg = light_palette.get("--bg", light_palette.get("--white", "#ffffff"))
    fg = light_palette.get("--fg", light_palette.get("--black", "#171717"))
    mapped["--bg"] = _smart_darken(bg)
    mapped["--fg"] = _smart_lighten(fg)
    if "--surface" in mapped:
        mapped["--surface"] = _smart_darken(mapped["--surface"])
    if "--border" in mapped:
        mapped["--border"] = _dark_border(mapped.get("--border", "#e0e0e0"))
    if "--weak" in mapped:
        mapped["--weak"] = _dark_weak(mapped["--weak"])
    if "--shadow-ring" in mapped:
        mapped["--shadow-ring"] = "rgba(255,255,255,0.10) 0px 0px 0px 1px"
    if "--shadow-ring-light" in mapped:
        mapped["--shadow-ring-light"] = "rgba(255,255,255,0.08) 0px 0px 0px 1px"
    mapped["--source-bg"] = bg
    mapped["--source-fg"] = fg
    return mapped


def _smart_darken(color: str) -> str:
    rgb = _hex_to_rgb(color)
    if not rgb:
        return "#0a0a0a"
    _, _, l = _rgb_to_hsl(*rgb)
    if l > 50:
        return "#0f1117"
    return _rgb_to_hex(tuple(max(0, c - 60) for c in rgb))


def _smart_lighten(color: str) -> str:
    rgb = _hex_to_rgb(color)
    if not rgb:
        return "#ededed"
    _, _, l = _rgb_to_hsl(*rgb)
    if l < 50:
        return "#eef0f5"
    return _rgb_to_hex(tuple(min(255, c + 80) for c in rgb))


def _dark_border(border: str) -> str:
    rgb = _any_to_rgb(border)
    if rgb:
        return _rgb_to_hex(tuple(max(0, c - 130) for c in rgb))
    return "#2a2e38"


def _dark_weak(weak: str) -> str:
    rgba_match = re.match(r"rgba?\(\s*([^)]+)\)", weak)
    if rgba_match:
        parts = [p.strip() for p in rgba_match.group(1).split(",")]
        if len(parts) >= 3:
            try:
                r = int(float(parts[0]))
                g = int(float(parts[1]))
                b = int(float(parts[2]))
                a = float(parts[3]) if len(parts) > 3 else 0.6
                r = min(255, r + 180)
                g = min(255, g + 180)
                b = min(255, b + 180)
                return f"rgba({r},{g},{b},{a})"
            except ValueError:
                pass
    return "rgba(230,230,240,0.6)"


def map_shadow_to_dark(shadow: str) -> str:
    return re.sub(r"rgba?\(\s*0\s*,\s*0\s*,\s*0\s*,\s*([0-9.]+)\)", r"rgba(255,255,255,\1)", shadow)


def suggest_inverse(color: str) -> str:
    return _invert_hex(color)
