# Design System: btst 48 ace

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a black with white canvas, using Blue as the primary accent for interactive elements. The typography is anchored by `FontAwesome`, creating a consistent reading experience. The type scale spans 11px to 24px across 8 levels.

**Key Characteristics:**
- Grid system detected via column classes.
- Row-based section composition present.
- Primary typeface: `FontAwesome`
- Accent palette driven by 5 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **White** (`#FFF`): Primary surface color
### Accent
- **Blue** (`#428bca`): CTAs, links, and interactive highlights
- **Red** (`#d15b47`): CTAs, links, and interactive highlights
- **Soft Muted Blue** (`#abbac3`): CTAs, links, and interactive highlights
- **Light Muted Blue** (`#c5d0dc`): CTAs, links, and interactive highlights
- **Soft Blue** (`#6fb3e0`): CTAs, links, and interactive highlights
### Neutral
- **White 2** (`#FFF`): Structural background
- **White 3** (`rgba(255,255,255,0.15)`): Structural background
- **White 4** (`#fff`): Structural background
- **Black** (`rgba(0,0,0,0.2)`): Structural background
- **Mid Gray** (`#999`): Border and divider color
- **Charcoal** (`#333`): Structural background
- **Dark Gray** (`#555`): Structural background
- **Light Gray** (`#DDD`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `FontAwesome` (Primary)
- `"Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif`
- `inherit`
- `"Open Sans"`
- `Arial, Helvetica, sans-serif`
- `"Helvetica Neue", Helvetica, Arial, sans-serif`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | FontAwesome | 13px | normal | 20px | normal |
| Heading | Open Sans, Helvetica Neue, Helvetica, Arial, sans-serif | 14px | bold | 24px | normal |
| Sub-heading | inherit | 12px | lighter | 1.428571 | normal |
| Body | Open Sans | 18px | bolder | 1 | normal |
| Caption | Arial, Helvetica, sans-serif | 16px | 200 | 18px | normal |
| Button | Helvetica Neue, Helvetica, Arial, sans-serif | 11px | 500 | 15px | normal |
| Mono | Helvetica Neue, Helvetica, Arial, sans-serif | 15px | 500 | 15px | normal |
| Label | Helvetica Neue, Helvetica, Arial, sans-serif | 24px | 500 | 15px | normal |

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
0–16px (12 steps)

### Border Radius Scale
0–100px (10 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `none` |
| 2 | `0 2px 4px rgba(0, 0, 0, 0.2)` |
| 3 | `inset 0 1px 1px rgba(0, 0, 0, 0.075)` |
| 4 | `2px 1px 2px 0 rgba(0, 0, 0, 0.2)` |
| 5 | `-2px 1px 2px 0 rgba(0, 0, 0, 0.2)` |
| 6 | `inset 0 3px 5px rgba(0, 0, 0, 0.125)` |
| 7 | `0 1px 2px rgba(0, 0, 0, 0.05)` |
| 8 | `0 -2px 3px 0 rgba(0, 0, 0, 0.15)` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#428bca` as the primary accent for CTAs and interactive elements.
- Use `FontAwesome` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media(min-width:768px)`
- `@media only screen and (max-width:480px)`
- `@media only screen and (max-width:767px)`
- `@media(min-width:1200px)`
- `@media(max-width:767px)`
- `@media only screen and (max-width:991px)`
- `@media(min-width:768px) and (max-width:991px)`
- `@media(min-width:992px) and (max-width:1199px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `btst 48 ace` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** White (`#FFF`)
- **CTA / Accent:** Blue (`#428bca`)
- **Border:** White 2 (`#FFF`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.