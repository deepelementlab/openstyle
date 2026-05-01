from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class ColorToken:
    value: str
    usage: str
    frequency: int = 0


@dataclass
class TypographyToken:
    family: str
    size_px: float
    weight: str
    line_height: str
    letter_spacing: str
    usage: str


@dataclass
class ComponentSpec:
    name: str
    selectors: list[str] = field(default_factory=list)
    traits: list[str] = field(default_factory=list)


@dataclass
class DesignTokens:
    template_name: str
    source_dir: Path
    colors: dict[str, list[ColorToken]] = field(default_factory=dict)
    typography: list[TypographyToken] = field(default_factory=list)
    spacing_scale: list[str] = field(default_factory=list)
    radius_scale: list[str] = field(default_factory=list)
    shadows: list[str] = field(default_factory=list)
    breakpoints: list[str] = field(default_factory=list)
    components: list[ComponentSpec] = field(default_factory=list)
    layout_notes: list[str] = field(default_factory=list)

