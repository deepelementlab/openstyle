# Design System: zero 47 zVintauge

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a charcoal with white canvas, using Muted Teal as the primary accent for interactive elements. The typography is anchored by `Crimson Text`, creating a consistent reading experience. The type scale spans 12px to 24px across 7 levels.

**Key Characteristics:**
- Grid system detected via column classes.
- Row-based section composition present.
- Sectioned page architecture with repeated blocks.
- Primary typeface: `Crimson Text`
- Accent palette driven by 3 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **White** (`#fff`): Primary surface color
### Accent
- **Muted Teal** (`#628d7c`): CTAs, links, and interactive highlights
- **Cyan** (`#1c7791`): CTAs, links, and interactive highlights
- **Mid Gray** (`#92907C`): CTAs, links, and interactive highlights
### Neutral
- **White 2** (`#fff`): Structural background
- **White 3** (`#ffffff`): Structural background
- **Charcoal** (`#333`): Structural background
- **Black** (`#000`): Structural background
- **Mid Gray 2** (`#999`): Border and divider color
- **White 4** (`#f7f7f7`): Structural background
- **Black 2** (`#161616`): Structural background
- **Black 3** (`#000000`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"Crimson Text", serif` (Primary)
- `"Montserrat", sans-serif`
- `"Dancing Script", cursive`
- `"Cabin", Helvetica, sans-serif`
- `"Merriweather", Georgia, serif`
- `"Cabin", sans-serif`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Crimson Text, serif | 16px | bold | 0 | 1px |
| Heading | Montserrat, sans-serif | 14px | 500 | 30px | 2px |
| Sub-heading | Dancing Script, cursive | 0.0 | 400 | 1.2 | 0.9px |
| Body | Cabin, Helvetica, sans-serif | 20px | 600 | 1 | 0 |
| Caption | Merriweather, Georgia, serif | 22px | 600 | 20px | 2.5px |
| Button | Cabin, sans-serif | 12px | 600 | 16px | 2.5px |
| Mono | Cabin, sans-serif | 24px | 600 | 16px | 2.5px |
| Label | Cabin, sans-serif | 15px | 600 | 16px | 2.5px |

## 4. Component Stylings

### Navigation
- **Selectors:** `nav`, `.navbar`, `header`
- **Traits:** top navigation; brand + links
### Buttons
- **Selectors:** `button`, `.btn`, `a.button`
- **Traits:** primary actions; hover states

## 5. Layout Principles

### Spacing Scale
0–100px (12 steps)

### Border Radius Scale
0–13px (4 steps)

## 6. Depth & Elevation

- No significant shadow system detected.

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#628d7c` as the primary accent for CTAs and interactive elements.
- Use `Crimson Text` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media(max-width:767px)`
- `@media only screen and (min-width: 960px) and (max-width: 1199px)`
- `@media only screen and (min-width: 768px) and (max-width: 959px)`
- `@media only screen and (max-width: 767px)`
- `@media only screen and (max-width: 1100px)`
- `@media only screen and (max-width: 960px)`
- `@media only screen and (max-width: 690px)`
- `@media(max-width:480px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `zero 47 zVintauge` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** White (`#fff`)
- **CTA / Accent:** Muted Teal (`#628d7c`)
- **Border:** White 2 (`#fff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.