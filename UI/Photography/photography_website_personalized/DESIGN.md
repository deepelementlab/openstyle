# Design System: cpts 1218 dob

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a charcoal with white canvas, using Vivid Cyan as the primary accent for interactive elements. The typography is anchored by `Droid Sans`, creating a consistent reading experience. The type scale spans 13px to 19px across 8 levels.

**Key Characteristics:**
- Grid system detected via column classes.
- Primary typeface: `Droid Sans`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **White** (`#fff`): Primary surface color
### Accent
- **Vivid Cyan** (`#15A1E2`): CTAs, links, and interactive highlights
- **Vivid Red** (`#ec0606`): CTAs, links, and interactive highlights
- **Muted Blue** (`#5d6f7b`): CTAs, links, and interactive highlights
- **Dark Blue** (`#233c4c`): CTAs, links, and interactive highlights
- **Dark Muted Blue** (`#2C3E50`): CTAs, links, and interactive highlights
- **Muted Teal** (`#4B857A`): CTAs, links, and interactive highlights
### Neutral
- **White 2** (`#fff`): Structural background
- **Charcoal** (`#292B2D`): Structural background
- **Black** (`#000`): Structural background
- **Charcoal 2** (`#313131`): Structural background
- **Charcoal 3** (`#414141`): Structural background
- **Mid Gray** (`#777`): Border and divider color
- **Charcoal 4** (`#3A3B3B`): Structural background
- **White 3** (`#f9f9f9`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"Droid Sans", sans-serif` (Primary)
- `"Roboto", sans-serif`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Droid Sans, sans-serif | 16px | 700 | 1.7em | 2px |
| Heading | Roboto, sans-serif | 14px | 900 | 1.6em | 5px |
| Sub-heading | Roboto, sans-serif | 19px | 400 | 2em | 5px |
| Body | Roboto, sans-serif | 16px | 300 | 0 | 5px |
| Caption | Roboto, sans-serif | 15px | 500 | 36px | 5px |
| Button | Roboto, sans-serif | 13px | 500 | 36px | 5px |
| Mono | Roboto, sans-serif | 18px | 500 | 36px | 5px |
| Label | Roboto, sans-serif | 16px | 500 | 36px | 5px |

## 4. Component Stylings

### Forms
- **Selectors:** `form`, `input`, `textarea`, `select`
- **Traits:** data input; interactive controls

## 5. Layout Principles

### Spacing Scale
0–14px (12 steps)

### Border Radius Scale
0–500px (4 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `0 0 0 16px rgba(255, 255, 255, 0.65) inset, 0 1px 2px rgba(0, 0, 0, 0.1)` |
| 2 | `inset 0 0 0 1px rgba(255, 255, 255, 0.1), 0 1px 2px rgba(0, 0, 0, 0.1)` |
| 3 | `none` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#15A1E2` as the primary accent for CTAs and interactive elements.
- Use `Droid Sans` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media screen and (max-width:1366px)`
- `@media screen and (max-width:1280px)`
- `@media screen and (max-width:1024px)`
- `@media screen and (max-width:800px)`
- `@media screen and (max-width:768px)`
- `@media screen and (max-width:640px)`
- `@media screen and (max-width:480px)`
- `@media screen and (max-width:320px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `cpts 1218 dob` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** White (`#fff`)
- **CTA / Accent:** Vivid Cyan (`#15A1E2`)
- **Border:** White 2 (`#fff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.