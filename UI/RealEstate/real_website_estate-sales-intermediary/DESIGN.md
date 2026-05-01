# Design System: moban4513

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a charcoal with white canvas, using Lime as the primary accent for interactive elements. The typography is anchored by `Helvetica Neue`, creating a consistent reading experience. The type scale spans 12px to 24px across 8 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Row-based section composition present.
- Sectioned page architecture with repeated blocks.
- Primary typeface: `Helvetica Neue`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **White** (`#fff`): Primary surface color
### Accent
- **Lime** (`#a8cf45`): CTAs, links, and interactive highlights
- **Blue** (`#337ab7`): CTAs, links, and interactive highlights
- **Muted Green** (`#3c763d`): CTAs, links, and interactive highlights
- **Amber** (`#8a6d3b`): CTAs, links, and interactive highlights
- **Red** (`#a94442`): CTAs, links, and interactive highlights
- **Vivid Blue** (`#2750ff`): CTAs, links, and interactive highlights
### Neutral
- **White 2** (`#fff`): Structural background
- **White 3** (`rgba(255,255,255,.15)`): Structural background
- **White 4** (`#ffffff`): Structural background
- **Light Gray** (`#ddd`): Structural background
- **Mid Gray** (`#999`): Border and divider color
- **Charcoal** (`#333`): Structural background
- **Mid Gray 2** (`#777`): Border and divider color
- **Charcoal 2** (`#1f1f1f`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"Helvetica Neue", Helvetica, Arial, sans-serif` (Primary)
- `inherit`
- `sans-serif`
- `monospace, monospace`
- `"Glyphicons Halflings"`
- `Menlo, Monaco, Consolas, "Courier New", monospace`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Helvetica Neue, Helvetica, Arial, sans-serif | 18px | 400 | 1.428571 | normal |
| Heading | inherit | 14px | 300 | 1 | 0 |
| Sub-heading | sans-serif | 15px | 700 | 30px | 0.5px |
| Body | monospace, monospace | 12px | 600 | 1.5 | 1px |
| Caption | Glyphicons Halflings | 16px | normal | 1.333333 | 1px |
| Button | Menlo, Monaco, Consolas, Courier New, monospace | 21px | 500 | 46px | 1px |
| Mono | Menlo, Monaco, Consolas, Courier New, monospace | 13px | 500 | 46px | 1px |
| Label | Menlo, Monaco, Consolas, Courier New, monospace | 24px | 500 | 46px | 1px |

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
0–100px (10 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `none` |
| 2 | `inset 0 1px 1px rgba(0, 0, 0, 0.075)` |
| 3 | `0 5px 14px rgba(0, 0, 0, 0.1)` |
| 4 | `inset 0 3px 5px rgba(0, 0, 0, 0.125)` |
| 5 | `inset 0 1px 1px rgba(0, 0, 0, 0.05)` |
| 6 | `inset 0 -1px 0 rgba(0, 0, 0, 0.25)` |
| 7 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 8px rgba(102, 175, 233, 0.6)` |
| 8 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#a8cf45` as the primary accent for CTAs and interactive elements.
- Use `Helvetica Neue` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media (min-width:768px)`
- `@media (max-width:767px)`
- `@media (min-width:1200px)`
- `@media print`
- `@media (min-width:768px) and (max-width:991px)`
- `@media (min-width:992px) and (max-width:1199px)`
- `@media (min-width:992px)`
- `@media screen and (min-width:768px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `moban4513` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** White (`#fff`)
- **CTA / Accent:** Lime (`#a8cf45`)
- **Border:** White 2 (`#fff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.