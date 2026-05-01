# Design System: monster lite

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a deep dark muted blue with white canvas, using Vivid Blue as the primary accent for interactive elements. The typography is anchored by `Rubik`, creating a consistent reading experience. The type scale spans 12px to 20px across 8 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Row-based section composition present.
- Primary typeface: `Rubik`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **White** (`#ffffff`): Primary surface color
### Accent
- **Vivid Blue** (`#009efb`): CTAs, links, and interactive highlights
- **Vivid Red** (`#f62d51`): CTAs, links, and interactive highlights
- **Soft Vivid Blue** (`#7460ee`): CTAs, links, and interactive highlights
- **Green** (`#55ce63`): CTAs, links, and interactive highlights
- **Mid Gray** (`rgba(120, 130, 140, 0.13)`): CTAs, links, and interactive highlights
- **Soft Vivid Amber** (`#ffbc34`): CTAs, links, and interactive highlights
### Neutral
- **White 2** (`#ffffff`): Structural background
- **White 3** (`#fff`): Structural background
- **Dark Muted Blue** (`#263238`): Structural background
- **Pale Muted Cyan** (`#f2f7f8`): Structural background
- **Light Gray** (`#eceeef`): Structural background
- **Dark Gray** (`#636c72`): Border and divider color
- **Charcoal** (`#292b2c`): Structural background
- **Light Gray 2** (`#ddd`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"Rubik", sans-serif` (Primary)
- `-apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif`
- `fontawesome`
- `sans-serif`
- `monospace, monospace`
- `inherit`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Rubik, sans-serif | 14px | 400 | 30px | normal |
| Heading | -apple-system, system-ui, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif | 20px | 500 | 1.5 | normal |
| Sub-heading | fontawesome | 18px | 300 | 1.25 | normal |
| Body | sans-serif | 12px | 700 | 1.1 | normal |
| Caption | monospace, monospace | 16px | bold | 1 | normal |
| Button | inherit | 14px | inherit | inherit | normal |
| Mono | inherit | 16px | inherit | inherit | normal |
| Label | inherit | 16px | inherit | inherit | normal |

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
| 2 | `0 0 0 2px rgba(2, 117, 216, 0.5)` |
| 3 | `0 0 0 2px rgba(204, 204, 204, 0.5)` |
| 4 | `0 0 0 2px rgba(91, 192, 222, 0.5)` |
| 5 | `0 0 0 2px rgba(92, 184, 92, 0.5)` |
| 6 | `0 0 0 2px rgba(240, 173, 78, 0.5)` |
| 7 | `0 0 0 2px rgba(217, 83, 79, 0.5)` |
| 8 | `0 0 0 2px rgba(2, 117, 216, 0.25)` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#009efb` as the primary accent for CTAs and interactive elements.
- Use `Rubik` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media (min-width:576px)`
- `@media (min-width:768px)`
- `@media (min-width:992px)`
- `@media (min-width:1200px)`
- `@media print`
- `@media (max-width:767px)`
- `@media (max-width:575px)`
- `@media (max-width:991px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `monster lite` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** White (`#ffffff`)
- **CTA / Accent:** Vivid Blue (`#009efb`)
- **Border:** White 2 (`#ffffff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.