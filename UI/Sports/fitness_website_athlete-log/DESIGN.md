# Design System: moban4054

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a charcoal with white canvas, using Vivid Yellow as the primary accent for interactive elements. The typography is anchored by `Oswald`, creating a consistent reading experience. The type scale spans 12px to 24px across 7 levels.

**Key Characteristics:**
- Grid system detected via column classes.
- Row-based section composition present.
- Sectioned page architecture with repeated blocks.
- Primary typeface: `Oswald`
- Accent palette driven by 2 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **White** (`#fff`): Primary surface color
### Accent
- **Vivid Yellow** (`#9BB70D`): CTAs, links, and interactive highlights
- **Muted Teal** (`#628d7c`): CTAs, links, and interactive highlights
### Neutral
- **White 2** (`#fff`): Structural background
- **White 3** (`#ffffff`): Structural background
- **Charcoal** (`#333`): Structural background
- **Light Gray** (`#eee`): Structural background
- **Charcoal 2** (`#222`): Structural background
- **Black** (`#111`): Structural background
- **Silver** (`#bbb`): Border and divider color
- **Black 2** (`#000`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"Oswald", sans-serif` (Primary)
- `"Crimson Text", serif`
- `"Dancing Script", cursive`
- `"Archivo Narrow", sans-serif`
- `"Cabin", Helvetica, sans-serif`
- `"Merriweather", Georgia, serif`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Oswald, sans-serif | 16px | bold | 30px | 1px |
| Heading | Crimson Text, serif | 14px | 700 | 0 | 2px |
| Sub-heading | Dancing Script, cursive | 12px | 500 | 1.2 | 0.9px |
| Body | Archivo Narrow, sans-serif | 15px | 400 | 20px | 0.25px |
| Caption | Cabin, Helvetica, sans-serif | 20px | 600 | 16px | 0 |
| Button | Merriweather, Georgia, serif | 0.0 | 600 | 1.38 | 0 |
| Mono | Merriweather, Georgia, serif | 24px | 600 | 1.38 | 0 |
| Label | Merriweather, Georgia, serif | 18px | 600 | 1.38 | 0 |

## 4. Component Stylings

### Navigation
- **Selectors:** `nav`, `.navbar`, `header`
- **Traits:** top navigation; brand + links
### Buttons
- **Selectors:** `button`, `.btn`, `a.button`
- **Traits:** primary actions; hover states

## 5. Layout Principles

### Spacing Scale
0–50px (12 steps)

### Border Radius Scale
0–13px (6 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `0 25px 18px -26px rgba(0, 0, 0, 0.75)` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#9BB70D` as the primary accent for CTAs and interactive elements.
- Use `Oswald` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 7 media query breakpoint(s):
- `@media only screen and (max-width: 767px)`
- `@media only screen and (min-width: 960px) and (max-width: 1199px)`
- `@media only screen and (min-width: 768px) and (max-width: 959px)`
- `@media(max-width:767px)`
- `@media only screen and (max-width: 480px)`
- `@media all and (max-width: 768px)`
- `@media all and (max-width: 800px), only screen and (-webkit-min-device-pixel-ratio: 2) and (max-width: 1024px), only screen and (min--moz-device-pixel-ratio: 2) and (max-width: 1024px), only screen and (-o-min-device-pixel-ratio: 2/1) and (max-width: 1024px), only screen and (min-device-pixel-ratio: 2) and (max-width: 1024px), only screen and (min-resolution: 192dpi) and (max-width: 1024px), only screen and (min-resolution: 2dppx) and (max-width: 1024px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `moban4054` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** White (`#fff`)
- **CTA / Accent:** Vivid Yellow (`#9BB70D`)
- **Border:** White 2 (`#fff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.