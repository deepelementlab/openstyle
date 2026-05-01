# Design System: tbmx 1 personal

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a black with white canvas, using Soft Vivid Blue as the primary accent for interactive elements. The typography is anchored by `Merriweather`, creating a consistent reading experience. The type scale spans 12px to 60px across 7 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Row-based section composition present.
- Sectioned page architecture with repeated blocks.
- Primary typeface: `Merriweather`
- Accent palette driven by 1 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **White** (`#ffffff`): Primary surface color
### Accent
- **Soft Vivid Blue** (`#2d8eff`): CTAs, links, and interactive highlights
### Neutral
- **White 2** (`#ffffff`): Structural background
- **Black** (`#000000`): Structural background
- **White 3** (`rgba(255,255,255,0.5)`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"Merriweather", serif` (Primary)
- `"Roboto", sans-serif`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Merriweather, serif | 20px | 300 | 1.8 | 0.02em |
| Heading | Roboto, sans-serif | 35px | 500 | 1.6 | 0.1em |
| Sub-heading | Roboto, sans-serif | 0.0 | 500 | 0 | 0.25em |
| Body | Roboto, sans-serif | 60px | 500 | 0 | 0.25em |
| Caption | Roboto, sans-serif | 36px | 500 | 0 | 0.25em |
| Button | Roboto, sans-serif | 12px | 500 | 0 | 0.25em |
| Mono | Roboto, sans-serif | 24px | 500 | 0 | 0.25em |
| Label | Roboto, sans-serif | 26px | 500 | 0 | 0.25em |

## 4. Component Stylings

### Navigation
- **Selectors:** `nav`, `.navbar`, `header`
- **Traits:** top navigation; brand + links
### Buttons
- **Selectors:** `button`, `.btn`, `a.button`
- **Traits:** primary actions; hover states
### Hero
- **Selectors:** `.hero`, `#hero`, `.banner`, `.slider`, `#home`
- **Traits:** intro section; headline + call-to-action

## 5. Layout Principles

### Spacing Scale
0–100px (9 steps)

### Border Radius Scale
- `5px`

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `none` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#2d8eff` as the primary accent for CTAs and interactive elements.
- Use `Merriweather` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 4 media query breakpoint(s):
- `@media (max-width: 575.98px)`
- `@media (max-width: 768px)`
- `@media (max-width: 991.98px)`
- `@media (max-width: 1199.98px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `tbmx 1 personal` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** White (`#ffffff`)
- **CTA / Accent:** Soft Vivid Blue (`#2d8eff`)
- **Border:** White 2 (`#ffffff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.