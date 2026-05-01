# Design System: cpts 1126 bsq

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a black with white canvas, using Vivid Cyan as the primary accent for interactive elements. The typography is anchored by `Open Sans`, creating a consistent reading experience. The type scale spans 12px to 60px across 7 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Row-based section composition present.
- Primary typeface: `Open Sans`
- Accent palette driven by 5 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **White** (`#fff`): Primary surface color
### Accent
- **Vivid Cyan** (`#00b0bb`): CTAs, links, and interactive highlights
- **Dark Vivid Cyan** (`#00969f`): CTAs, links, and interactive highlights
- **Vivid Blue** (`#08c`): CTAs, links, and interactive highlights
- **Dark Muted Blue** (`#3c4451`): CTAs, links, and interactive highlights
- **Vivid Amber** (`#f89406`): CTAs, links, and interactive highlights
### Neutral
- **White 2** (`#fff`): Structural background
- **White 3** (`rgba(255,255,255,0.15)`): Structural background
- **Mid Gray** (`#999`): Border and divider color
- **Black** (`rgba(0,0,0,0.1)`): Structural background
- **Black 2** (`rgba(0,0,0,0.075)`): Structural background
- **Light Gray** (`#ddd`): Structural background
- **Black 3** (`rgba(0,0,0,0.25)`): Structural background
- **Silver** (`#ccc`): Border and divider color
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"Open Sans", Arial, sans-serif` (Primary)
- `"Helvetica Neue", Helvetica, Arial, sans-serif`
- `inherit`
- `Monaco, Menlo, Consolas, "Courier New", monospace`
- `"Titillium Web", Arial, sans-serif`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Open Sans, Arial, sans-serif | 14px | bold | 20px | -1px |
| Heading | Helvetica Neue, Helvetica, Arial, sans-serif | 20px | normal | 0 | -1px |
| Sub-heading | inherit | 18px | 700 | 30px | -1px |
| Body | Monaco, Menlo, Consolas, Courier New, monospace | 18px | 400 | 1 | -1px |
| Caption | Titillium Web, Arial, sans-serif | 12px | 200 | 40px | -1px |
| Button | Titillium Web, Arial, sans-serif | 12px | 300 | 14px | -1px |
| Mono | Titillium Web, Arial, sans-serif | 0.0 | 300 | 14px | -1px |
| Label | Titillium Web, Arial, sans-serif | 60px | 300 | 14px | -1px |

## 4. Component Stylings

### Navigation
- **Selectors:** `nav`, `.navbar`, `header`
- **Traits:** top navigation; brand + links
### Forms
- **Selectors:** `form`, `input`, `textarea`, `select`
- **Traits:** data input; interactive controls

## 5. Layout Principles

### Spacing Scale
0–40px (12 steps)

### Border Radius Scale
0–15px (10 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `inset 0 1px 1px rgba(0, 0, 0, 0.075)` |
| 2 | `0 1px 5px 0 rgba(0, 0, 0, 0.3)` |
| 3 | `none` |
| 4 | `0 2px 8px 0 rgba(0, 0, 0, 0.6)` |
| 5 | `0 5px 10px rgba(0, 0, 0, 0.2)` |
| 6 | `inset 0 2px 4px rgba(0, 0, 0, 0.15), 0 1px 2px rgba(0, 0, 0, 0.05)` |
| 7 | `0 1px 3px rgba(0, 0, 0, 0.1)` |
| 8 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 8px rgba(82, 168, 236, 0.6)` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#00b0bb` as the primary accent for CTAs and interactive elements.
- Use `Open Sans` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media print`
- `@media(min-width:768px) and (max-width:979px)`
- `@media(max-width:767px)`
- `@media(min-width:1200px)`
- `@media(max-width:480px)`
- `@media(max-width:979px)`
- `@media(min-width:980px)`
- `@media only screen and (min-width: 1200px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `cpts 1126 bsq` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** White (`#fff`)
- **CTA / Accent:** Vivid Cyan (`#00b0bb`)
- **Border:** White 2 (`#fff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.