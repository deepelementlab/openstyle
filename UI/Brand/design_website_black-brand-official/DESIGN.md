# Design System: moban3752

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a black with white canvas, using Muted Blue as the primary accent for interactive elements. The typography is anchored by `Roboto`, creating a consistent reading experience. The type scale spans 14px to 60px across 8 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Row-based section composition present.
- Primary typeface: `Roboto`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **White** (`#fff`): Primary surface color
### Accent
- **Muted Blue** (`#646d93`): CTAs, links, and interactive highlights
- **Soft Muted Blue** (`#7c87ad`): CTAs, links, and interactive highlights
- **Vivid Red** (`#E82C0C`): CTAs, links, and interactive highlights
- **Soft Vivid Red** (`#FF6E5B`): CTAs, links, and interactive highlights
- **Vivid Red 2** (`#AA1600`): CTAs, links, and interactive highlights
- **Soft Red** (`#e87352`): CTAs, links, and interactive highlights
### Neutral
- **White 2** (`#fff`): Structural background
- **Black** (`#000`): Structural background
- **Silver** (`#aaa`): Border and divider color
- **Dark Gray** (`#666`): Structural background
- **White 3** (`#ffffff`): Structural background
- **Light Gray** (`#eaeaea`): Structural background
- **Light Gray 2** (`#eee`): Structural background
- **Charcoal** (`#333`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"Roboto", sans-serif` (Primary)
- `"BebasNeueRegular", "Arial Narrow", Arial, sans-serif`
- `"Quattrocento", serif`
- `"icomoon"`
- `FontAwesome`
- `Georgia`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Roboto, sans-serif | 14px | 100 | 1 | normal |
| Heading | BebasNeueRegular, Arial Narrow, Arial, sans-serif | 16px | bold | 200px | normal |
| Sub-heading | Quattrocento, serif | 18px | 300 | 0 | normal |
| Body | icomoon | 24px | 400 | 62px | normal |
| Caption | FontAwesome | 15px | 600 | 40px | normal |
| Button | Georgia | 25px | 700 | 45px | normal |
| Mono | Georgia | 20px | 700 | 45px | normal |
| Label | Georgia | 60px | 700 | 45px | normal |

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
0–50px (12 steps)

### Border Radius Scale
0–50px (9 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `none` |
| 2 | `inset 0 1px 0 #FF6E5B` |
| 3 | `3px 3px 1px rgba(136, 136, 136, 0.1)` |
| 4 | `0 0 0 1px #aaa, 1px 0 0 0 rgba(255, 255, 255, 0.9) inset, 0 1px 2px rgba(0, 0, 0, 0.2)` |
| 5 | `0 0 0 1px #40496e, 0 1px 2px rgba(0, 0, 0, 0.1) inset` |
| 6 | `0 10px 0 #fff, 0 20px 0 #fff` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#646d93` as the primary accent for CTAs and interactive elements.
- Use `Roboto` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media (max-width: 991px)`
- `@media screen and (max-width: 1140px)`
- `@media screen and (max-width: 600px)`
- `@media (max-width: 1280px)`
- `@media (max-width: 767px)`
- `@media only screen and (max-width:980px)`
- `@media only screen and (max-width:730px)`
- `@media only screen and (max-width:480px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `moban3752` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** White (`#fff`)
- **CTA / Accent:** Muted Blue (`#646d93`)
- **Border:** White 2 (`#fff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.