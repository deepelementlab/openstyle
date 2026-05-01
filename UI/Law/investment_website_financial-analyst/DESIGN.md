# Design System: cpts 1777 cvw

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a black with white canvas, using Blue as the primary accent for interactive elements. The typography is anchored by `Questrial`, creating a consistent reading experience. The type scale spans 12px to 18px across 8 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Sectioned page architecture with repeated blocks.
- Primary typeface: `Questrial`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **White** (`#fff`): Primary surface color
### Accent
- **Blue** (`#337ab7`): CTAs, links, and interactive highlights
- **Vivid Red** (`#ec082b`): CTAs, links, and interactive highlights
- **Muted Green** (`#3c763d`): CTAs, links, and interactive highlights
- **Amber** (`#8a6d3b`): CTAs, links, and interactive highlights
- **Red** (`#a94442`): CTAs, links, and interactive highlights
- **Blue 2** (`#3b5998`): CTAs, links, and interactive highlights
### Neutral
- **White 2** (`#fff`): Structural background
- **White 3** (`rgba(255, 255, 255, .15)`): Structural background
- **Black** (`#000`): Structural background
- **Light Gray** (`#ddd`): Structural background
- **Mid Gray** (`#777`): Border and divider color
- **Light Gray 2** (`#eee`): Structural background
- **Charcoal** (`#333`): Structural background
- **Silver** (`#ccc`): Border and divider color
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"Questrial", sans-serif` (Primary)
- `FontAwesome`
- `"Helvetica Neue", Helvetica, Arial, sans-serif`
- `"Open Sans Condensed", sans-serif`
- `inherit`
- `"Jacques Francois Shadow", cursive`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Questrial, sans-serif | 12px | 600 | 1.428571 | 1px |
| Heading | FontAwesome | 16px | bold | 1 | 2px |
| Sub-heading | Helvetica Neue, Helvetica, Arial, sans-serif | 16px | normal | 1.5 | 3px |
| Body | Open Sans Condensed, sans-serif | 14px | 400 | 1.333333 | 4px |
| Caption | inherit | 18px | 700 | 30px | 0.5px |
| Button | Jacques Francois Shadow, cursive | 16px | 500 | 46px | 0.5px |
| Mono | Jacques Francois Shadow, cursive | 16px | 500 | 46px | 0.5px |
| Label | Jacques Francois Shadow, cursive | 16px | 500 | 46px | 0.5px |

## 4. Component Stylings

### Navigation
- **Selectors:** `nav`, `.navbar`, `header`
- **Traits:** top navigation; brand + links
### Buttons
- **Selectors:** `button`, `.btn`, `a.button`
- **Traits:** primary actions; hover states
### Cards
- **Selectors:** `.card`, `.panel`, `.thumbnail`, `.product`
- **Traits:** content containers
### Forms
- **Selectors:** `form`, `input`, `textarea`, `select`
- **Traits:** data input; interactive controls

## 5. Layout Principles

### Spacing Scale
0–20px (12 steps)

### Border Radius Scale
0–100px (10 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `none` |
| 2 | `inset 0 1px 1px rgba(0, 0, 0, 0.075)` |
| 3 | `inset 0 3px 5px rgba(0, 0, 0, 0.125)` |
| 4 | `inset 0 0 0 2px #fff` |
| 5 | `inset 0 -1px 0 rgba(0, 0, 0, 0.25)` |
| 6 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 8px rgba(102, 175, 233, 0.6)` |
| 7 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168` |
| 8 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#337ab7` as the primary accent for CTAs and interactive elements.
- Use `Questrial` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media (min-width: 768px)`
- `@media (max-width: 767px)`
- `@media (min-width: 1200px)`
- `@media print`
- `@media (min-width: 768px) and (max-width: 991px)`
- `@media (min-width: 992px) and (max-width: 1199px)`
- `@media (min-width: 992px)`
- `@media screen and (max-width: 767px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `cpts 1777 cvw` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** White (`#fff`)
- **CTA / Accent:** Blue (`#337ab7`)
- **Border:** White 2 (`#fff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.