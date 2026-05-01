from __future__ import annotations

import logging
import re
from collections import Counter
from pathlib import Path

import cssutils

cssutils.log.setLevel(logging.CRITICAL)


COLOR_PATTERN = re.compile(
    r"(#[0-9a-fA-F]{3,8}\b|rgba?\([^)]+\)|hsla?\([^)]+\)|oklab\([^)]+\))"
)


class CSSAnalysisResult(dict):
    pass


class CSSParser:
    def parse_files(self, css_files: list[Path]) -> CSSAnalysisResult:
        colors: Counter[str] = Counter()
        font_families: Counter[str] = Counter()
        font_sizes: Counter[str] = Counter()
        font_weights: Counter[str] = Counter()
        line_heights: Counter[str] = Counter()
        letter_spacings: Counter[str] = Counter()
        spacings: Counter[str] = Counter()
        radii: Counter[str] = Counter()
        shadows: Counter[str] = Counter()
        breakpoints: Counter[str] = Counter()
        selector_props: dict[str, dict[str, str]] = {}

        for css_path in css_files:
            raw = css_path.read_text(encoding="utf-8", errors="ignore")
            for color in COLOR_PATTERN.findall(raw):
                colors[color.strip()] += 1

            sheet = cssutils.parseString(raw)
            self._collect_media_queries(raw, breakpoints)
            self._collect_spacing_tokens(raw, spacings)

            for rule in sheet:
                if rule.type == rule.STYLE_RULE:
                    selector_text = rule.selectorText
                    props: dict[str, str] = {}
                    for prop in rule.style:
                        key = prop.name.strip().lower()
                        value = prop.value.strip()
                        props[key] = value
                        if key == "font-family":
                            font_families[value] += 1
                        elif key == "font-size":
                            font_sizes[value] += 1
                        elif key == "font-weight":
                            font_weights[value] += 1
                        elif key == "line-height":
                            line_heights[value] += 1
                        elif key == "letter-spacing":
                            letter_spacings[value] += 1
                        elif key == "border-radius":
                            radii[value] += 1
                        elif key == "box-shadow":
                            shadows[value] += 1
                    selector_props[selector_text] = props

        return CSSAnalysisResult(
            colors=colors,
            font_families=font_families,
            font_sizes=font_sizes,
            font_weights=font_weights,
            line_heights=line_heights,
            letter_spacings=letter_spacings,
            spacings=spacings,
            radii=radii,
            shadows=shadows,
            breakpoints=breakpoints,
            selector_props=selector_props,
        )

    @staticmethod
    def _collect_media_queries(raw_css: str, breakpoints: Counter[str]) -> None:
        for match in re.findall(r"@media[^{]+", raw_css, flags=re.IGNORECASE):
            breakpoint = " ".join(match.split())
            breakpoints[breakpoint] += 1

    @staticmethod
    def _collect_spacing_tokens(raw_css: str, spacings: Counter[str]) -> None:
        pattern = re.compile(
            r"(?:margin|padding|gap|row-gap|column-gap)\s*:\s*([^;}{]+);",
            flags=re.IGNORECASE,
        )
        for value in pattern.findall(raw_css):
            for token in re.split(r"\s+", value.strip()):
                if token and re.search(r"\d", token):
                    spacings[token] += 1
