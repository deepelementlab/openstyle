# Design System: moban4047

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a black with white canvas, using Vivid Red as the primary accent for interactive elements. The typography is anchored by `Montserrat`, creating a consistent reading experience. The type scale spans 12px to 25px across 7 levels.

**Key Characteristics:**
- Grid system detected via column classes.
- Row-based section composition present.
- Sectioned page architecture with repeated blocks.
- Primary typeface: `Montserrat`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **White** (`#fff`): Primary surface color
### Accent
- **Vivid Red** (`#F3542D`): CTAs, links, and interactive highlights
- **Vivid Orange** (`#ff970b`): CTAs, links, and interactive highlights
- **Vivid Orange 2** (`#f26324`): CTAs, links, and interactive highlights
- **Green** (`#56AE33`): CTAs, links, and interactive highlights
- **Vivid Orange 3** (`#FE9B13`): CTAs, links, and interactive highlights
- **Cyan** (`#1c7791`): CTAs, links, and interactive highlights
### Neutral
- **White 2** (`#fff`): Structural background
- **White 3** (`#ffffff`): Structural background
- **Light Gray** (`#dddddd`): Structural background
- **Black** (`#000`): Structural background
- **Charcoal** (`#333`): Structural background
- **Mid Gray** (`#777`): Border and divider color
- **Charcoal 2** (`#3F3F3F`): Structural background
- **Light Gray 2** (`#ddd`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `Montserrat, sans-serif` (Primary)
- `"Noto Serif", serif`
- `Arial, Helvetica, sans-serif`
- `"Racing Sans One", cursive`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Montserrat, sans-serif | 16px | bold | 0 | 1px |
| Heading | Noto Serif, serif | 25px | 500 | 25px | 2px |
| Sub-heading | Arial, Helvetica, sans-serif | 0.0 | normal | 20px | 2px |
| Body | Racing Sans One, cursive | 15px | 400 | 16px | 2px |
| Caption | Racing Sans One, cursive | 12px | 400 | 42px | 2px |
| Button | Racing Sans One, cursive | 13px | 400 | 1.2 | 2px |
| Mono | Racing Sans One, cursive | 16px | 400 | 1.2 | 2px |
| Label | Racing Sans One, cursive | 16px | 400 | 1.2 | 2px |

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
0–60px (12 steps)

### Border Radius Scale
0–4px (3 steps)

## 6. Depth & Elevation

- No significant shadow system detected.

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#F3542D` as the primary accent for CTAs and interactive elements.
- Use `Montserrat` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 7 media query breakpoint(s):
- `@media all and (max-width: 768px), only screen and (-webkit-min-device-pixel-ratio: 2) and (max-width: 1024px), only screen and (min--moz-device-pixel-ratio: 2) and (max-width: 1024px), only screen and (-o-min-device-pixel-ratio: 2/1) and (max-width: 1024px), only screen and (min-device-pixel-ratio: 2) and (max-width: 1024px), only screen and (min-resolution: 192dpi) and (max-width: 1024px), only screen and (min-resolution: 2dppx) and (max-width: 1024px)`
- `@media only screen and (min-width: 960px) and (max-width: 1199px)`
- `@media only screen and (min-width: 768px) and (max-width: 959px)`
- `@media only screen and (max-width: 767px)`
- `@media all and (max-width: 768px)`
- `@media(max-width: 768px)`
- `@media(max-width: 468px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `moban4047` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** White (`#fff`)
- **CTA / Accent:** Vivid Red (`#F3542D`)
- **Border:** White 2 (`#fff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.