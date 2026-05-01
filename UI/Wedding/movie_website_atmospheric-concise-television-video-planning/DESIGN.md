# Design System: twts 25 thomsoon

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a black with silver canvas. The typography is anchored by `Raleway`, creating a consistent reading experience. The type scale spans 13px to 35px across 7 levels.

**Key Characteristics:**
- Custom layout structure without explicit framework classes.
- Primary typeface: `Raleway`
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **Black** (`#000000`): Primary text color
### Accent
- No distinct color tokens detected in this category.
### Neutral
- **Black 2** (`#000000`): Structural background
- **Silver** (`#c3c3c3`): Border and divider color
- **White** (`#f4f4f4`): Structural background
- **Dark Gray** (`#686868`): Border and divider color
- **White 2** (`#f8f7f7`): Structural background
- **Black 3** (`#000`): Structural background
- **White 3** (`#fff`): Structural background
- **Light Gray** (`#f1f1f1`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"Raleway", sans-serif` (Primary)
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Raleway, sans-serif | 13px | 400 | 50px | 1px |
| Heading | Raleway, sans-serif | 14px | 500 | 40px | 1px |
| Sub-heading | Raleway, sans-serif | 15px | 900 | 70px | 1px |
| Body | Raleway, sans-serif | 23px | 800 | 80px | 1px |
| Caption | Raleway, sans-serif | 16px | 700 | 1 | 1px |
| Button | Raleway, sans-serif | 0.0 | 700 | 0 | 1px |
| Mono | Raleway, sans-serif | 35px | 700 | 0 | 1px |
| Label | Raleway, sans-serif | 18px | 700 | 0 | 1px |

## 4. Component Stylings

### Navigation
- **Selectors:** `nav`, `.navbar`, `header`
- **Traits:** top navigation; brand + links
### Hero
- **Selectors:** `.hero`, `#hero`, `.banner`, `.slider`, `#home`
- **Traits:** intro section; headline + call-to-action

## 5. Layout Principles

### Spacing Scale
0–150px (7 steps)

### Border Radius Scale
- `100%`

## 6. Depth & Elevation

- No significant shadow system detected.

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `Raleway` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 5 media query breakpoint(s):
- `@media all and (max-width: 1330px) and (min-width: 1180px)`
- `@media all and (max-width: 1179px) and (min-width: 1024px)`
- `@media all and (max-width: 1023px) and (min-width: 769px)`
- `@media all and (max-width: 768px) and (min-width: 481px)`
- `@media all and (max-width: 480px) and (min-width: 320px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `twts 25 thomsoon` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** Black (`#000000`)
- **Border:** Black 2 (`#000000`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.