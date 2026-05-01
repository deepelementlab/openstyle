# Design System: wait 54 material

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a mid gray with white canvas, using Dark Vivid Teal as the primary accent for interactive elements. The typography is anchored by `Raleway`, creating a consistent reading experience. The type scale spans 11px to 30px across 8 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Row-based section composition present.
- Sectioned page architecture with repeated blocks.
- Primary typeface: `Raleway`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **White** (`#fff`): Primary surface color
### Accent
- **Dark Vivid Teal** (`#009688`): CTAs, links, and interactive highlights
- **Blue** (`#337ab7`): CTAs, links, and interactive highlights
- **Green** (`#4caf50`): CTAs, links, and interactive highlights
- **Vivid Cyan** (`#03a9f4`): CTAs, links, and interactive highlights
- **Vivid Red** (`#ff5722`): CTAs, links, and interactive highlights
- **Soft Vivid Red** (`#f44336`): CTAs, links, and interactive highlights
### Neutral
- **White 2** (`#fff`): Structural background
- **White 3** (`rgba(255,255,255, 0.84)`): Structural background
- **Light Gray** (`#D2D2D2`): Border and divider color
- **White 4** (`rgba(255,255,255,.15)`): Structural background
- **Light Gray 2** (`#ddd`): Structural background
- **Mid Gray** (`#777`): Border and divider color
- **Black** (`rgba(0, 0, 0, 0.12)`): Structural background
- **Charcoal** (`#333`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"Raleway", sans-serif` (Primary)
- `"Open Sans", sans-serif`
- `"Helvetica Neue", Helvetica, Arial, sans-serif`
- `inherit`
- `"Material Icons"`
- `sans-serif`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Raleway, sans-serif | 16px | 400 | 1.428571 | normal |
| Heading | Open Sans, sans-serif | 14px | 700 | 1.5 | 0 |
| Sub-heading | Helvetica Neue, Helvetica, Arial, sans-serif | 12px | 300 | 1.333333 | 1px |
| Body | inherit | 18px | 600 | 1 | -1px |
| Caption | Material Icons | 11px | normal | 20px | -1px |
| Button | sans-serif | 24px | 500 | 30px | -1px |
| Mono | sans-serif | 13px | 500 | 30px | -1px |
| Label | sans-serif | 30px | 500 | 30px | -1px |

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
0–60px (12 steps)

### Border Radius Scale
0–100px (10 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `none` |
| 2 | `inset 0 1px 1px rgba(0, 0, 0, 0.075)` |
| 3 | `0 1px 6px 0 rgba(0, 0, 0, 0.12), 0 1px 6px 0 rgba(0, 0, 0, 0.12)` |
| 4 | `inset 0 3px 5px rgba(0, 0, 0, 0.125)` |
| 5 | `0 8px 17px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)` |
| 6 | `0 2px 2px 0 rgba(0, 0, 0, 0.14), 0 3px 1px -2px rgba(0, 0, 0, 0.2), 0 1px 5px 0 rgba(0, 0, 0, 0.12)` |
| 7 | `inset 0 -1px 0 rgba(0, 0, 0, 0.25)` |
| 8 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 8px rgba(102, 175, 233, 0.6)` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#009688` as the primary accent for CTAs and interactive elements.
- Use `Raleway` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media (min-width:768px)`
- `@media (max-width:767px)`
- `@media (max-width: 767px)`
- `@media (min-width:1200px)`
- `@media print`
- `@media (min-width:768px) and (max-width:991px)`
- `@media (min-width:992px) and (max-width:1199px)`
- `@media (min-width: 768px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `wait 54 material` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** White (`#fff`)
- **CTA / Accent:** Dark Vivid Teal (`#009688`)
- **Border:** White 2 (`#fff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.