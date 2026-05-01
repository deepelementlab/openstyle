# Design System: moban4743

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a deep deep blue with pale vivid blue canvas, using Vivid Blue as the primary accent for interactive elements. The typography is anchored by `Roboto`, creating a consistent reading experience. The type scale spans 12px to 44px across 8 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Row-based section composition present.
- Sectioned page architecture with repeated blocks.
- Primary typeface: `Roboto`
- Accent palette driven by 5 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **Deep Blue** (`#081f3e`): Primary text color
- **Pale Vivid Blue** (`rgba(230, 241, 255, 0.5)`): Primary surface color
- **Deep Vivid Blue** (`#020f20`): Primary text color
- **Pale Vivid Blue 2** (`rgba(230, 241, 255, 0.75)`): Primary surface color
### Accent
- **Vivid Blue** (`#006cff`): CTAs, links, and interactive highlights
- **Muted Blue** (`#536174`): CTAs, links, and interactive highlights
- **Vivid Red** (`#ff0000`): CTAs, links, and interactive highlights
- **Vivid Blue 2** (`rgba(0, 108, 255, 0.5)`): CTAs, links, and interactive highlights
- **Vivid Blue 3** (`rgba(0, 108, 255, 0.75)`): CTAs, links, and interactive highlights
### Neutral
- **White** (`#ffffff`): Structural background
- **Pale Muted Blue** (`#f5f7f9`): Structural background
- **Dark Gray** (`#57595c`): Structural background
- **Black** (`rgba(0, 0, 0, 0.15)`): Structural background
- **Silver** (`#cacaca`): Border and divider color
- **White 2** (`rgba(255, 255, 255, 0.35)`): Structural background
- **Black 2** (`rgba(0, 0, 0, 0.5)`): Structural background
- **White 3** (`rgba(255, 255, 255, 0.5)`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"Roboto", sans-serif` (Primary)
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Roboto, sans-serif | 14px | 500 | 2 | normal |
| Heading | Roboto, sans-serif | 44px | 700 | 0 | normal |
| Sub-heading | Roboto, sans-serif | 12px | 400 | 66px | normal |
| Body | Roboto, sans-serif | 22px | 300 | 42px | normal |
| Caption | Roboto, sans-serif | 16px | 600 | 50px | normal |
| Button | Roboto, sans-serif | 18px | 600 | 70px | normal |
| Mono | Roboto, sans-serif | 15px | 600 | 70px | normal |
| Label | Roboto, sans-serif | 13px | 600 | 70px | normal |

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
0–100px (12 steps)

### Border Radius Scale
0–50px (4 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `none` |
| 2 | `0 2px 6px 0 rgba(0, 0, 0, 0.3)` |
| 3 | `0 2px 5px rgba(0, 0, 0, 0.1)` |
| 4 | `0 5px 20px rgba(0, 0, 0, 0.15)` |
| 5 | `0 10px 10px 0 rgba(0, 0, 0, 0.2)` |
| 6 | `0 5px 40px rgba(0, 0, 0, 0.15)` |
| 7 | `0 3px 5px rgba(0, 0, 0, 0.15)` |
| 8 | `0 0 0 transparent` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#006cff` as the primary accent for CTAs and interactive elements.
- Use `Roboto` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 3 media query breakpoint(s):
- `@media only screen and (max-width: 767px)`
- `@media only screen and (min-width: 768px) and (max-width: 991px)`
- `@media only screen and (min-width: 992px) and (max-width: 1199px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `moban4743` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** Deep Blue (`#081f3e`)
- **CTA / Accent:** Vivid Blue (`#006cff`)
- **Border:** White (`#ffffff`)
- **Surface:** Pale Vivid Blue (`rgba(230, 241, 255, 0.5)`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.