# Design System: dance 66 persona

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a black with white canvas, using Vivid Cyan as the primary accent for interactive elements. The typography is anchored by `Ubuntu`, creating a consistent reading experience. The type scale spans 16px to 16px across 8 levels.

**Key Characteristics:**
- Custom layout structure without explicit framework classes.
- Primary typeface: `Ubuntu`
- Accent palette driven by 3 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **White** (`#fff`): Primary surface color
### Accent
- **Vivid Cyan** (`#06e8fc`): CTAs, links, and interactive highlights
- **Blue** (`#527ed2`): CTAs, links, and interactive highlights
- **Soft Vivid Orange** (`#fd926d`): CTAs, links, and interactive highlights
### Neutral
- **White 2** (`#fff`): Structural background
- **Black** (`rgba(0, 0, 0, 0.35)`): Structural background
- **White 3** (`#ffffff`): Structural background
- **Dark Gray** (`#6f7575`): Border and divider color
- **Light Gray** (`#eee`): Structural background
- **Mid Gray** (`rgba(129, 134, 134, 0.35)`): Border and divider color
- **Pale Vivid Red** (`#fffdfd`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"Ubuntu", sans-serif` (Primary)
- `"Open Sans", sans-serif`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Ubuntu, sans-serif | 16px | bold | 0.75em | normal |
| Heading | Open Sans, sans-serif | 16px | 400 | 2em | normal |
| Sub-heading | Open Sans, sans-serif | 16px | 400 | inherit | normal |
| Body | Open Sans, sans-serif | 16px | 400 | 1.8em | normal |
| Caption | Open Sans, sans-serif | 16px | 400 | 23px | normal |
| Button | Open Sans, sans-serif | 16px | 400 | 23px | normal |
| Mono | Open Sans, sans-serif | 16px | 400 | 23px | normal |
| Label | Open Sans, sans-serif | 16px | 400 | 23px | normal |

## 4. Component Stylings

### Buttons
- **Selectors:** `button`, `.btn`, `a.button`
- **Traits:** primary actions; hover states
### Forms
- **Selectors:** `form`, `input`, `textarea`, `select`
- **Traits:** data input; interactive controls

## 5. Layout Principles

### Spacing Scale
0–28px (11 steps)

### Border Radius Scale
0–50px (4 steps)

## 6. Depth & Elevation

- No significant shadow system detected.

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#06e8fc` as the primary accent for CTAs and interactive elements.
- Use `Ubuntu` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media (max-width:1680px)`
- `@media (max-width:1600px)`
- `@media (max-width:1440px)`
- `@media (max-width: 1366px)`
- `@media (max-width: 1280px)`
- `@media (max-width: 1080px)`
- `@media (max-width: 1024px)`
- `@media (max-width: 991px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `dance 66 persona` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** White (`#fff`)
- **CTA / Accent:** Vivid Cyan (`#06e8fc`)
- **Border:** White 2 (`#fff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.