# Design System: moban2603

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a black with white canvas, using Vivid Amber as the primary accent for interactive elements. The typography is anchored by `Helvetica Neue`, creating a consistent reading experience. The type scale spans 10px to 20px across 7 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Row-based section composition present.
- Sectioned page architecture with repeated blocks.
- Primary typeface: `Helvetica Neue`
- Accent palette driven by 4 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **White** (`#ffffff`): Primary surface color
### Accent
- **Vivid Amber** (`#FECE1A`): CTAs, links, and interactive highlights
- **Vivid Blue** (`#0088cc`): CTAs, links, and interactive highlights
- **Vivid Amber 2** (`#f89406`): CTAs, links, and interactive highlights
- **Soft Vivid Red** (`#ee5f5b`): CTAs, links, and interactive highlights
### Neutral
- **White 2** (`#ffffff`): Structural background
- **White 3** (`rgba(255, 255, 255, 0.15)`): Structural background
- **Black** (`#181A1C`): Structural background
- **Black 2** (`rgba(0, 0, 0, 0.1)`): Structural background
- **Black 3** (`rgba(0, 0, 0, 0.075)`): Structural background
- **Mid Gray** (`#999999`): Border and divider color
- **Black 4** (`rgba(0, 0, 0, 0.25)`): Structural background
- **White 4** (`#fff`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"Helvetica Neue", Helvetica, Arial, sans-serif` (Primary)
- `"Porta"`
- `"porta"`
- `Arial`
- `inherit`
- `Monaco, Menlo, Consolas, "Courier New", monospace`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Helvetica Neue, Helvetica, Arial, sans-serif | 14px | normal | 20px | -1px |
| Heading | Porta | 20px | bold | 0 | -1px |
| Sub-heading | porta | 18px | 200 | 30px | -1px |
| Body | Arial | 12px | 100 | 1 | -1px |
| Caption | inherit | 0.0 | lighter | 40px | -1px |
| Button | Monaco, Menlo, Consolas, Courier New, monospace | 12px | 300 | normal | -1px |
| Mono | Monaco, Menlo, Consolas, Courier New, monospace | 15px | 300 | normal | -1px |
| Label | Monaco, Menlo, Consolas, Courier New, monospace | 10px | 300 | normal | -1px |

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
### Hero
- **Selectors:** `.hero`, `#hero`, `.banner`, `.slider`, `#home`
- **Traits:** intro section; headline + call-to-action

## 5. Layout Principles

### Spacing Scale
0–20px (12 steps)

### Border Radius Scale
0–500px (10 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `inset 0 1px 1px rgba(0, 0, 0, 0.075)` |
| 2 | `none` |
| 3 | `0 5px 10px rgba(0, 0, 0, 0.2)` |
| 4 | `inset 0 2px 4px rgba(0, 0, 0, 0.15), 0 1px 2px rgba(0, 0, 0, 0.05)` |
| 5 | `0 1px 3px rgba(0, 0, 0, 0.1)` |
| 6 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 8px rgba(82, 168, 236, 0.6)` |
| 7 | `inset 0 1px 2px rgba(0, 0, 0, 0.025)` |
| 8 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #dbc59e` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#FECE1A` as the primary accent for CTAs and interactive elements.
- Use `Helvetica Neue` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media (max-width: 767px)`
- `@media (max-width: 979px)`
- `@media print`
- `@media (min-width: 768px) and (max-width: 979px)`
- `@media (min-width: 1200px)`
- `@media (max-width: 480px)`
- `@media (min-width: 980px)`
- `@media screen and (-webkit-min-device-pixel-ratio:0)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `moban2603` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** White (`#ffffff`)
- **CTA / Accent:** Vivid Amber (`#FECE1A`)
- **Border:** White 2 (`#ffffff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.