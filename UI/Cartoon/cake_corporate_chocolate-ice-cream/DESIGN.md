# Design System: cpts 1476 cgw

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a mid gray with white canvas, using Blue as the primary accent for interactive elements. The typography is anchored by `montserratbold`, creating a consistent reading experience. The type scale spans 12px to 40px across 7 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Row-based section composition present.
- Sectioned page architecture with repeated blocks.
- Primary typeface: `montserratbold`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **White** (`#fff`): Primary surface color
### Accent
- **Blue** (`#337ab7`): CTAs, links, and interactive highlights
- **Light Vivid Red** (`#fba1a1`): CTAs, links, and interactive highlights
- **Soft Vivid Cyan** (`#59d4f0`): CTAs, links, and interactive highlights
- **Muted Green** (`#3c763d`): CTAs, links, and interactive highlights
- **Amber** (`#8a6d3b`): CTAs, links, and interactive highlights
- **Red** (`#a94442`): CTAs, links, and interactive highlights
### Neutral
- **White 2** (`#fff`): Structural background
- **White 3** (`rgba(255, 255, 255, .15)`): Structural background
- **White 4** (`#ffffff`): Structural background
- **Light Gray** (`#ddd`): Structural background
- **Mid Gray** (`#777`): Border and divider color
- **Mid Gray 2** (`#a1a2a6`): Border and divider color
- **Charcoal** (`#333`): Structural background
- **Black** (`#000`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"montserratbold"` (Primary)
- `"latoregular"`
- `"Helvetica Neue", Helvetica, Arial, sans-serif`
- `inherit`
- `"custom-font"`
- `"slick"`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | montserratbold | 18px | normal | 1.428571 | 2px |
| Heading | latoregular | 12px | bold | 1 | 1px |
| Sub-heading | Helvetica Neue, Helvetica, Arial, sans-serif | 14px | 500 | 1.5 | 0 |
| Body | inherit | 20px | 300 | 0 | 7px |
| Caption | custom-font | 30px | 200 | 1.333333 | 3px |
| Button | slick | 40px | 200 | 30px | 3px |
| Mono | slick | 16px | 200 | 30px | 3px |
| Label | slick | 0.0 | 200 | 30px | 3px |

## 4. Component Stylings

### Navigation
- **Selectors:** `nav`, `.navbar`, `header`
- **Traits:** top navigation; brand + links
### Buttons
- **Selectors:** `button`, `.btn`, `a.button`
- **Traits:** primary actions; hover states

## 5. Layout Principles

### Spacing Scale
0–40px (12 steps)

### Border Radius Scale
0–50px (10 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `none` |
| 2 | `inset 0 1px 1px rgba(0, 0, 0, 0.075)` |
| 3 | `inset 0 1px 1px rgba(0, 0, 0, 0)` |
| 4 | `inset 0 3px 5px rgba(0, 0, 0, 0.125)` |
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
- Use `montserratbold` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media (min-width: 768px)`
- `@media (min-width: 992px)`
- `@media (min-width: 992px) and (max-width: 1199px)`
- `@media (max-width: 768px)`
- `@media (max-width: 767px)`
- `@media (min-width: 1200px)`
- `@media print`
- `@media (min-width: 768px) and (max-width: 991px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `cpts 1476 cgw` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** White (`#fff`)
- **CTA / Accent:** Blue (`#337ab7`)
- **Border:** White 2 (`#fff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.