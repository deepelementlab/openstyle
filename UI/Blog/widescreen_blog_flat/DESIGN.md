# Design System: moban3133

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a deep dark gray with white canvas, using Red as the primary accent for interactive elements. The typography is anchored by `Open Sans`, creating a consistent reading experience. The type scale spans 10px to 30px across 8 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Row-based section composition present.
- Primary typeface: `Open Sans`
- Accent palette driven by 1 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **White** (`#fff`): Primary surface color
### Accent
- **Red** (`#d0344e`): CTAs, links, and interactive highlights
### Neutral
- **White 2** (`#fff`): Structural background
- **White 3** (`#f7f7f7`): Structural background
- **Light Gray** (`#efefef`): Structural background
- **Dark Gray** (`#5e5e5e`): Structural background
- **Charcoal** (`#333`): Structural background
- **Black** (`rgba(0,0,0,0.15)`): Structural background
- **Mid Gray** (`#808080`): Border and divider color
- **Mid Gray 2** (`#737373`): Border and divider color
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"Open Sans", sans-serif` (Primary)
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Open Sans, sans-serif | 12px | 600 | 24px | 1px |
| Heading | Open Sans, sans-serif | 13px | 700 | 35px | 1.5px |
| Sub-heading | Open Sans, sans-serif | 15px | normal | 25px | 0.8px |
| Body | Open Sans, sans-serif | 20px | 300 | 38px | 1.2px |
| Caption | Open Sans, sans-serif | 10px | 300 | 30px | 1.1px |
| Button | Open Sans, sans-serif | 18px | 300 | 22px | 0.4px |
| Mono | Open Sans, sans-serif | 14px | 300 | 22px | 0.4px |
| Label | Open Sans, sans-serif | 30px | 300 | 22px | 0.4px |

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
0–50px (11 steps)

### Border Radius Scale
0–50px (6 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `none` |
| 2 | `0 11px 9px 0 rgba(0, 0, 0, 0.02)` |
| 3 | `0 13px 35px -12px rgba(35, 35, 35, 0.15)` |
| 4 | `0 10px 40px 0 rgba(0, 0, 0, 0.03)` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#d0344e` as the primary accent for CTAs and interactive elements.
- Use `Open Sans` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media (min-width: 1200px)`
- `@media (max-width: 1199px)`
- `@media (min-width: 992px) and (max-width: 1199px)`
- `@media (max-width: 991px)`
- `@media (min-width: 768px) and (max-width: 991px)`
- `@media (max-width: 767px)`
- `@media (min-width: 576px) and (max-width: 991px)`
- `@media (min-width: 576px) and (max-width: 767px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `moban3133` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** White (`#fff`)
- **CTA / Accent:** Red (`#d0344e`)
- **Border:** White 2 (`#fff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.