# Design System: dance 31 sjdi

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a deep deep blue with white canvas, using Vivid Pink as the primary accent for interactive elements. The typography is anchored by `Open Sans`, creating a consistent reading experience. The type scale spans 10px to 42px across 6 levels.

**Key Characteristics:**
- Custom layout structure without explicit framework classes.
- Primary typeface: `Open Sans`
- Accent palette driven by 1 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **Deep Blue** (`#081148`): Primary text color
### Accent
- **Vivid Pink** (`#e91e63`): CTAs, links, and interactive highlights
### Neutral
- **White** (`rgb(255, 255, 255)`): Structural background
- **White 2** (`#fff`): Structural background
- **White 3** (`#FFFFFF`): Structural background
- **White 4** (`rgba(255, 255, 255, 0.15)`): Structural background
- **Pale Vivid Blue** (`#F0F8FF`): Structural background
- **Light Gray** (`#EEE`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"Open Sans", sans-serif` (Primary)
- `"Lato", sans-serif`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Open Sans, sans-serif | 14px | 400 | 25px | 5px |
| Heading | Lato, sans-serif | 16px | 400 | 25px | 5px |
| Sub-heading | Lato, sans-serif | 42px | 400 | 25px | 5px |
| Body | Lato, sans-serif | 30px | 400 | 25px | 5px |
| Caption | Lato, sans-serif | 10px | 400 | 25px | 5px |
| Button | Lato, sans-serif | 16px | 400 | 25px | 5px |

## 4. Component Stylings

### Forms
- **Selectors:** `form`, `input`, `textarea`, `select`
- **Traits:** data input; interactive controls

## 5. Layout Principles

### Spacing Scale
0–45px (11 steps)

### Border Radius Scale

## 6. Depth & Elevation

- No significant shadow system detected.

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#e91e63` as the primary accent for CTAs and interactive elements.
- Use `Open Sans` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media(max-width:1440px)`
- `@media(max-width:1366px)`
- `@media(max-width:1280px)`
- `@media(max-width:1080px)`
- `@media(max-width:1024px)`
- `@media(max-width:991px)`
- `@media(max-width:966px)`
- `@media(max-width:900px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `dance 31 sjdi` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** Deep Blue (`#081148`)
- **CTA / Accent:** Vivid Pink (`#e91e63`)
- **Border:** White (`rgb(255, 255, 255)`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.