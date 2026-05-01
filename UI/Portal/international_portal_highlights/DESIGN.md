# Design System: moban3142

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a black with white canvas, using Vivid Red as the primary accent for interactive elements. The typography is anchored by `Roboto`, creating a consistent reading experience. The type scale spans 12px to 48px across 7 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Row-based section composition present.
- Sectioned page architecture with repeated blocks.
- Primary typeface: `Roboto`
- Accent palette driven by 3 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **White** (`#fff`): Primary surface color
### Accent
- **Vivid Red** (`#ff0303`): CTAs, links, and interactive highlights
- **Vivid Red 2** (`#ff084e`): CTAs, links, and interactive highlights
- **Vivid Green** (`#30ca00`): CTAs, links, and interactive highlights
### Neutral
- **White 2** (`#fff`): Structural background
- **Black** (`#000`): Structural background
- **Black 2** (`rgba(0, 0, 0, 0.5)`): Structural background
- **Black 3** (`rgba(0, 0, 0, 0.05)`): Structural background
- **Black 4** (`#1d1d1d`): Structural background
- **White 3** (`rgba(255, 255, 255, 0.5)`): Structural background
- **Light Gray** (`#e0e0e0`): Structural background
- **Charcoal** (`#3a3a3a`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"Roboto", sans-serif` (Primary)
- `"PT Serif", serif`
- `"Pe-icon-7-stroke"`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Roboto, sans-serif | 14px | 400 | 1.5 | 1px |
| Heading | PT Serif, serif | 18px | 300 | 1 | 2px |
| Sub-heading | Pe-icon-7-stroke | 12px | 500 | 1.8 | 2px |
| Body | Pe-icon-7-stroke | 48px | 700 | 1.2 | 2px |
| Caption | Pe-icon-7-stroke | 30px | 700 | 1.9 | 2px |
| Button | Pe-icon-7-stroke | 20px | 700 | 0 | 2px |
| Mono | Pe-icon-7-stroke | 16px | 700 | 0 | 2px |
| Label | Pe-icon-7-stroke | 0.0 | 700 | 0 | 2px |

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
| 1 | `0 2px 6px 0 rgba(0, 0, 0, 0.3)` |
| 2 | `2px 5px 30px rgba(0, 0, 0, 0.15)` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#ff0303` as the primary accent for CTAs and interactive elements.
- Use `Roboto` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 5 media query breakpoint(s):
- `@media only screen and (min-width: 992px) and (max-width: 1199px)`
- `@media only screen and (min-width: 768px) and (max-width: 991px)`
- `@media only screen and (min-width: 320px) and (max-width: 767px)`
- `@media only screen and (min-width: 480px) and (max-width: 767px)`
- `@media only screen and (min-width: 576px) and (max-width: 767px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `moban3142` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** White (`#fff`)
- **CTA / Accent:** Vivid Red (`#ff0303`)
- **Border:** White 2 (`#fff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.