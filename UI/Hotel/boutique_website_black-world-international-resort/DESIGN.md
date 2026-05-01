# Design System: tops 87 Luxury

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a mid gray with pale vivid yellow canvas, using Blue as the primary accent for interactive elements. The typography is anchored by `GillSans`, creating a consistent reading experience. The type scale spans 12px to 18px across 7 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Sectioned page architecture with repeated blocks.
- Primary typeface: `GillSans`
- Accent palette driven by 5 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **Pale Vivid Yellow** (`#fcf8e3`): Primary surface color
- **Pale Green** (`#dff0d8`): Primary surface color
- **Pale Red** (`#f2dede`): Primary surface color
### Accent
- **Blue** (`#428bca`): CTAs, links, and interactive highlights
- **Muted Green** (`#3c763d`): CTAs, links, and interactive highlights
- **Amber** (`#8a6d3b`): CTAs, links, and interactive highlights
- **Red** (`#a94442`): CTAs, links, and interactive highlights
- **Cyan** (`#31708f`): CTAs, links, and interactive highlights
### Neutral
- **White** (`#fff`): Structural background
- **White 2** (`rgba(255, 255, 255, .15)`): Structural background
- **Light Gray** (`#ddd`): Structural background
- **Mid Gray** (`#777`): Border and divider color
- **Mid Gray 2** (`#8a8a8a`): Border and divider color
- **Charcoal** (`#333`): Structural background
- **Charcoal 2** (`#424446`): Structural background
- **Light Gray 2** (`#eee`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"GillSans", Arial, sans-serif` (Primary)
- `"picto-foundry-general"`
- `"picto-foundry-household"`
- `"dubielitalic", Arial, sans-serif`
- `"picto-foundry-emotions"`
- `"picto-foundry-shopping-finance"`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | GillSans, Arial, sans-serif | 12px | normal | 1 | normal |
| Heading | picto-foundry-general | 14px | bold | 1.428571 | normal |
| Sub-heading | picto-foundry-household | 18px | 700 | 1.5em | normal |
| Body | dubielitalic, Arial, sans-serif | 16px | 300 | 1.2em | normal |
| Caption | picto-foundry-emotions | 16px | 200 | 30px | normal |
| Button | picto-foundry-shopping-finance | 16px | 200 | 46px | normal |
| Mono | picto-foundry-shopping-finance | 16px | 200 | 46px | normal |
| Label | picto-foundry-shopping-finance | 0.0 | 200 | 46px | normal |

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
0–40px (12 steps)

### Border Radius Scale
0–140px (10 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `none` |
| 2 | `inset 0 1px 1px rgba(0, 0, 0, 0.075)` |
| 3 | `0 0 0 1px #b2b2b2` |
| 4 | `0 1px 4px rgba(0, 0, 0, 0.1)` |
| 5 | `inset 0 3px 5px rgba(0, 0, 0, 0.125)` |
| 6 | `0 0 0 1px rgba(178, 178, 178, 0)` |
| 7 | `inset 0 -1px 0 rgba(0, 0, 0, 0.25)` |
| 8 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 8px rgba(102, 175, 233, 0.6)` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#428bca` as the primary accent for CTAs and interactive elements.
- Use `GillSans` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media (min-width: 768px)`
- `@media screen and (min-width: 750px)`
- `@media screen and (min-width: 1200px)`
- `@media (max-width: 767px)`
- `@media screen and (min-width: 1400px)`
- `@media (min-width: 1200px)`
- `@media screen and (min-width: 1000px)`
- `@media print`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `tops 87 Luxury` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** Pale Vivid Yellow (`#fcf8e3`)
- **CTA / Accent:** Blue (`#428bca`)
- **Border:** White (`#fff`)
- **Surface:** Pale Green (`#dff0d8`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.