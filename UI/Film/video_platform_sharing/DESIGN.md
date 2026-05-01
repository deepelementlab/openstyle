# Design System: moban4358

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a deep deep blue with white canvas, using Muted Blue as the primary accent for interactive elements. The typography is anchored by `Feather-Icons`, creating a consistent reading experience. The type scale spans 13px to 24px across 8 levels.

**Key Characteristics:**
- Custom layout structure without explicit framework classes.
- Primary typeface: `Feather-Icons`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **Deep Blue** (`#05172a`): Primary text color
### Accent
- **Muted Blue** (`#3e416d`): CTAs, links, and interactive highlights
- **Vivid Cyan** (`#00dffc`): CTAs, links, and interactive highlights
- **Soft Vivid Blue** (`#377dff`): CTAs, links, and interactive highlights
- **Soft Vivid Red** (`#ff3b30`): CTAs, links, and interactive highlights
- **Mid Gray** (`#77838f`): CTAs, links, and interactive highlights
- **Vivid Blue** (`#1e87f0`): CTAs, links, and interactive highlights
### Neutral
- **White** (`#fff`): Structural background
- **Dark Gray** (`#666`): Structural background
- **White 2** (`rgba(255, 255, 255, 0.7)`): Structural background
- **Mid Gray 2** (`#999`): Border and divider color
- **Light Gray** (`#e5e5e5`): Structural background
- **White 3** (`rgba(255, 255, 255, 0.5)`): Structural background
- **Charcoal** (`#333`): Structural background
- **Black** (`#000`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"Feather-Icons"` (Primary)
- `Consolas, monaco, monospace`
- `"Open Sans", "HelveticaNeue", "Helvetica Neue", Helvetica, Arial, sans-serif`
- `"Brand-Icons"`
- `"Material-Icons"`
- `"Line-Awesome"`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Feather-Icons | 14px | 600 | 1 | 0.003125in |
| Heading | Consolas, monaco, monospace | 13px | 500 | 1.5 | 0.1875pt |
| Sub-heading | Open Sans, HelveticaNeue, Helvetica Neue, Helvetica, Arial, sans-serif | 24px | normal | 1.4 | 0.046875pc |
| Body | Brand-Icons | 16px | 700 | 0 | normal |
| Caption | Material-Icons | 14px | bold | 1.3 | normal |
| Button | Line-Awesome | 15px | 400 | 1.2 | normal |
| Mono | Line-Awesome | 16px | 400 | 1.2 | normal |
| Label | Line-Awesome | 16px | 400 | 1.2 | normal |

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
0–70px (12 steps)

### Border Radius Scale
0–500px (9 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `none` |
| 2 | `0 14px 25px rgba(0, 0, 0, 0.16)` |
| 3 | `0 5px 15px rgba(0, 0, 0, 0.08)` |
| 4 | `inset 0 0 2px rgba(0, 0, 0, 0.07)` |
| 5 | `0 5px 12px rgba(0, 0, 0, 0.15)` |
| 6 | `0 2px 8px rgba(0, 0, 0, 0.08)` |
| 7 | `0 28px 50px rgba(0, 0, 0, 0.16)` |
| 8 | `0 1.5pt 0.4375pc -0.1875pc #000` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#3e416d` as the primary accent for CTAs and interactive elements.
- Use `Feather-Icons` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media (min-width: 960px)`
- `@media (min-width: 1200px)`
- `@media (min-width: 640px)`
- `@media (min-width: 1600px)`
- `@media (max-width: 768px)`
- `@media (max-width:960px)`
- `@media (max-width: 960px)`
- `@media (max-width: 959px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `moban4358` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** Deep Blue (`#05172a`)
- **CTA / Accent:** Muted Blue (`#3e416d`)
- **Border:** White (`#fff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.