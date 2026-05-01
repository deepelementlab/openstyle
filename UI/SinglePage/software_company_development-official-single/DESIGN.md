# Design System: moban2365

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a deep deep vivid blue with white canvas, using Vivid Red as the primary accent for interactive elements. The typography is anchored by `roboto-regular`, creating a consistent reading experience. The type scale spans 19px to 38px across 8 levels.

**Key Characteristics:**
- Grid system detected via column classes.
- Row-based section composition present.
- Sectioned page architecture with repeated blocks.
- Primary typeface: `roboto-regular`
- Accent palette driven by 5 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **Deep Vivid Blue** (`#001835`): Primary text color
### Accent
- **Vivid Red** (`#ed254d`): CTAs, links, and interactive highlights
- **Soft Vivid Amber** (`#f9da4f`): CTAs, links, and interactive highlights
- **Muted Blue** (`#555c6f`): CTAs, links, and interactive highlights
- **Dark Vivid Blue** (`#002f68`): CTAs, links, and interactive highlights
- **Dark Muted Blue** (`rgba(63, 80, 96, 0.15)`): CTAs, links, and interactive highlights
### Neutral
- **White** (`#FFFFFF`): Structural background
- **Dark Muted Blue 2** (`#3f4452`): Structural background
- **White 2** (`rgba(255, 255, 255, 0.5)`): Structural background
- **Black** (`#000000`): Structural background
- **Black 2** (`rgba(0, 0, 0, 0.5)`): Structural background
- **White 3** (`rgba(255, 255, 255, 0.6)`): Structural background
- **Black 3** (`rgba(0, 0, 0, 0.8)`): Structural background
- **White 4** (`rgba(255, 255, 255, 0.05)`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"roboto-regular", sans-serif` (Primary)
- `"roboto-black", sans-serif`
- `"domine-bold", serif`
- `"roboto-bold", serif`
- `"roboto-bold", sans-serif`
- `"roboto-medium", sans-serif`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | roboto-regular, sans-serif | 26px | bold | inherit | 0.15rem |
| Heading | roboto-black, sans-serif | 22px | normal | 0 | 0.3rem |
| Sub-heading | domine-bold, serif | 38px | normal | 3rem | -0.1rem |
| Body | roboto-bold, serif | 24px | normal | 1 | 0.05rem |
| Caption | roboto-bold, sans-serif | 32px | normal | 1.25 | 0.4rem |
| Button | roboto-medium, sans-serif | 29px | normal | 1.5 | 0.5rem |
| Mono | roboto-medium, sans-serif | 21px | normal | 1.5 | 0.5rem |
| Label | roboto-medium, sans-serif | 19px | normal | 1.5 | 0.5rem |

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
0–20px (12 steps)

### Border Radius Scale
3–50px (2 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `0 -1px 5px rgba(0, 0, 0, 0.3)` |
| 2 | `0 1px 2px rgba(0, 0, 0, 0.1)` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#ed254d` as the primary accent for CTAs and interactive elements.
- Use `roboto-regular` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media only screen and (max-width:768px)`
- `@media only screen and (max-width:600px)`
- `@media only screen and (max-width:400px)`
- `@media only screen and (max-width:1024px)`
- `@media screen and (max-width:1024px)`
- `@media screen and (max-width:768px)`
- `@media screen and (max-width:600px)`
- `@media screen and (max-width:400px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `moban2365` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** Deep Vivid Blue (`#001835`)
- **CTA / Accent:** Vivid Red (`#ed254d`)
- **Border:** White (`#FFFFFF`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.