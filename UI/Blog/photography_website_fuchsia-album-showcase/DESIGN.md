# Design System: tpmo 496 pipeline

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a black with white canvas, using Vivid Blue as the primary accent for interactive elements. The typography is anchored by `Helvetica Neue`, creating a consistent reading experience. The type scale spans 14px to 24px across 7 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Sectioned page architecture with repeated blocks.
- Primary typeface: `Helvetica Neue`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **White** (`#fff`): Primary surface color
### Accent
- **Vivid Blue** (`#0275d8`): CTAs, links, and interactive highlights
- **Green** (`#5cb85c`): CTAs, links, and interactive highlights
- **Soft Vivid Amber** (`#f0ad4e`): CTAs, links, and interactive highlights
- **Soft Red** (`#d9534f`): CTAs, links, and interactive highlights
- **Soft Cyan** (`#5bc0de`): CTAs, links, and interactive highlights
- **Pink** (`#993366`): CTAs, links, and interactive highlights
### Neutral
- **White 2** (`#fff`): Structural background
- **Light Gray** (`#eceeef`): Structural background
- **Mid Gray** (`#818a91`): Border and divider color
- **White 3** (`rgba(255,255,255,.15)`): Structural background
- **Black** (`#000`): Structural background
- **Light Gray 2** (`#ddd`): Structural background
- **Silver** (`#ccc`): Border and divider color
- **Charcoal** (`#373a3c`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"Helvetica Neue", Helvetica, Arial, sans-serif` (Primary)
- `sans-serif`
- `monospace, monospace`
- `inherit`
- `Menlo, Monaco, Consolas, "Courier New", monospace`
- `serif`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Helvetica Neue, Helvetica, Arial, sans-serif | 20px | 400 | 1.5 | normal |
| Heading | sans-serif | 16px | 700 | 1 | 2px |
| Sub-heading | monospace, monospace | 14px | 300 | 0 | 1px |
| Body | inherit | 16px | 500 | inherit | 1px |
| Caption | Menlo, Monaco, Consolas, Courier New, monospace | 24px | 800 | 1.333333 | 1px |
| Button | serif | 16px | 800 | 18px | 1px |
| Mono | serif | 16px | 800 | 18px | 1px |
| Label | serif | 0.0 | 800 | 18px | 1px |

## 4. Component Stylings

### Navigation
- **Selectors:** `nav`, `.navbar`, `header`
- **Traits:** top navigation; brand + links
### Buttons
- **Selectors:** `button`, `.btn`, `a.button`
- **Traits:** primary actions; hover states
### Forms
- **Selectors:** `form`, `input`, `textarea`, `select`
- **Traits:** data input; interactive controls

## 5. Layout Principles

### Spacing Scale
0–40px (12 steps)

### Border Radius Scale
0–50px (10 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `0 0 8px rgba(0, 0, 0, 0.6)` |
| 2 | `0 0 0 0.075rem #fff, 0 0 0 0.2rem #0074d9` |
| 3 | `none` |
| 4 | `inset 0 1px 1px rgba(153, 51, 102, 0.075), 0 0 8px rgba(153, 51, 102, 0.45)` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#0275d8` as the primary accent for CTAs and interactive elements.
- Use `Helvetica Neue` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media (min-width:544px)`
- `@media (min-width:768px)`
- `@media screen and (min-width:0\0)`
- `@media (min-width:992px)`
- `@media print`
- `@media (min-width:1200px)`
- `@media screen and (-webkit-min-device-pixel-ratio:0)`
- `@media all and (transform-3d),(-webkit-transform-3d)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `tpmo 496 pipeline` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** White (`#fff`)
- **CTA / Accent:** Vivid Blue (`#0275d8`)
- **Border:** White 2 (`#fff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.