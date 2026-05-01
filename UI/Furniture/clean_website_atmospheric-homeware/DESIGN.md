# Design System: moban2984

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a charcoal with white canvas, using Red as the primary accent for interactive elements. The typography is anchored by `Poppins`, creating a consistent reading experience. The type scale spans 12px to 24px across 8 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Row-based section composition present.
- Sectioned page architecture with repeated blocks.
- Primary typeface: `Poppins`
- Accent palette driven by 5 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **White** (`#fff`): Primary surface color
### Accent
- **Red** (`#c43b68`): CTAs, links, and interactive highlights
- **Blue** (`#337ab7`): CTAs, links, and interactive highlights
- **Muted Green** (`#3c763d`): CTAs, links, and interactive highlights
- **Amber** (`#8a6d3b`): CTAs, links, and interactive highlights
- **Red 2** (`#a94442`): CTAs, links, and interactive highlights
### Neutral
- **White 2** (`#fff`): Structural background
- **Charcoal** (`#333`): Structural background
- **Light Gray** (`#ddd`): Structural background
- **Black** (`#000`): Structural background
- **Mid Gray** (`#777`): Border and divider color
- **Charcoal 2** (`#212121`): Structural background
- **White 3** (`#f5f5f5`): Structural background
- **Charcoal 3** (`#3f3f3f`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"Poppins", sans-serif` (Primary)
- `"Poppins"`
- `"Old Standard TT", serif`
- `Old Standard TT`
- `Poppins`
- `"Helvetica Neue", Helvetica, Arial, sans-serif`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Poppins, sans-serif | 16px | 600 | 1.428571 | 1px |
| Heading | Poppins | 14px | 500 | 1 | normal |
| Sub-heading | Old Standard TT, serif | 18px | 700 | 1.5 | 2px |
| Body | Old Standard TT | 12px | bold | 30px | 7px |
| Caption | Poppins | 15px | normal | 26px | 7px |
| Button | Helvetica Neue, Helvetica, Arial, sans-serif | 24px | 400 | 40px | 7px |
| Mono | Helvetica Neue, Helvetica, Arial, sans-serif | 13px | 400 | 40px | 7px |
| Label | Helvetica Neue, Helvetica, Arial, sans-serif | 20px | 400 | 40px | 7px |

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
0–60px (12 steps)

### Border Radius Scale
0–100px (10 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `none` |
| 2 | `inset 0 1px 1px rgba(0, 0, 0, 0.075)` |
| 3 | `inset 0 3px 5px rgba(0, 0, 0, 0.125)` |
| 4 | `inset 0 -1px 0 rgba(0, 0, 0, 0.25)` |
| 5 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 8px rgba(102, 175, 233, 0.6)` |
| 6 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168` |
| 7 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b` |
| 8 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#c43b68` as the primary accent for CTAs and interactive elements.
- Use `Poppins` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media (min-width:768px)`
- `@media (max-width:767px)`
- `@media (min-width:1200px)`
- `@media print`
- `@media (min-width:768px) and (max-width:991px)`
- `@media (min-width:992px) and (max-width:1199px)`
- `@media (min-width:992px)`
- `@media screen and (min-width:768px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `moban2984` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** White (`#fff`)
- **CTA / Accent:** Red (`#c43b68`)
- **Border:** White 2 (`#fff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.