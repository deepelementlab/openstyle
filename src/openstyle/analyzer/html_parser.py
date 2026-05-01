from __future__ import annotations

from pathlib import Path

from bs4 import BeautifulSoup

from openstyle.models import ComponentSpec


class HTMLParser:
    def parse_file(self, html_file: Path) -> dict:
        soup = BeautifulSoup(html_file.read_text(encoding="utf-8", errors="ignore"), "html.parser")
        title = soup.title.get_text(strip=True) if soup.title else html_file.parent.name
        components = self._detect_components(soup)
        layout_notes = self._infer_layout_notes(soup)
        return {
            "title": title,
            "components": components,
            "layout_notes": layout_notes,
        }

    def _detect_components(self, soup: BeautifulSoup) -> list[ComponentSpec]:
        specs: list[ComponentSpec] = []
        if soup.select("nav, .navbar, header"):
            specs.append(ComponentSpec(name="Navigation", selectors=["nav", ".navbar", "header"], traits=["top navigation", "brand + links"]))
        if soup.select("button, .btn, a.button"):
            specs.append(ComponentSpec(name="Buttons", selectors=["button", ".btn", "a.button"], traits=["primary actions", "hover states"]))
        if soup.select(".card, .panel, .thumbnail, .product, .service"):
            specs.append(ComponentSpec(name="Cards", selectors=[".card", ".panel", ".thumbnail", ".product"], traits=["content containers"]))
        if soup.select("form, input, textarea, select"):
            specs.append(ComponentSpec(name="Forms", selectors=["form", "input", "textarea", "select"], traits=["data input", "interactive controls"]))
        if soup.select(".hero, #hero, .banner, .slider, #home"):
            specs.append(ComponentSpec(name="Hero", selectors=[".hero", "#hero", ".banner", ".slider", "#home"], traits=["intro section", "headline + call-to-action"]))
        return specs

    @staticmethod
    def _infer_layout_notes(soup: BeautifulSoup) -> list[str]:
        notes: list[str] = []
        if soup.select(".container, .container-fluid"):
            notes.append("Uses container-based layout wrappers.")
        if soup.select("[class*='col-'], [class*='span']"):
            notes.append("Grid system detected via column classes.")
        if soup.select(".row, .row-fluid"):
            notes.append("Row-based section composition present.")
        if soup.select("section, .section"):
            notes.append("Sectioned page architecture with repeated blocks.")
        if not notes:
            notes.append("Custom layout structure without explicit framework classes.")
        return notes
