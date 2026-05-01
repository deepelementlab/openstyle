# Design System: wait 108 cleanme

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a black with white canvas, using Dark Vivid Blue as the primary accent for interactive elements. The typography is anchored by `font Awesome 5 Free`, creating a consistent reading experience. The type scale spans 13px to 60px across 7 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Row-based section composition present.
- Primary typeface: `font Awesome 5 Free`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **White** (`#ffffff`): Primary surface color
### Accent
- **Dark Vivid Blue** (`#00539C`): CTAs, links, and interactive highlights
- **Soft Vivid Amber** (`#FFD662`): CTAs, links, and interactive highlights
- **Dark Vivid Blue 2** (`rgba(0, 83, 156, 1)`): CTAs, links, and interactive highlights
- **Soft Vivid Blue** (`#4ae`): CTAs, links, and interactive highlights
- **Dark Vivid Blue 3** (`rgba(0, 83, 156, .9)`): CTAs, links, and interactive highlights
- **Vivid Cyan** (`#00acee`): CTAs, links, and interactive highlights
### Neutral
- **White 2** (`#ffffff`): Structural background
- **Black** (`#000000`): Structural background
- **Light Gray** (`#eeeeee`): Structural background
- **Light Gray 2** (`#dddddd`): Structural background
- **Dark Gray** (`#666666`): Structural background
- **White 3** (`rgba(255, 255, 255, .1)`): Structural background
- **Black 2** (`rgba(0, 0, 0, .1)`): Structural background
- **Black 3** (`#000`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"font Awesome 5 Free"` (Primary)
- `"Montserrat", sans-serif`
- `"Font Awesome 5 Free"`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | font Awesome 5 Free | 16px | 400 | 0 | 2px |
| Heading | Montserrat, sans-serif | 14px | 300 | 1 | 1px |
| Sub-heading | Font Awesome 5 Free | 18px | 100 | 1.1em | 1px |
| Body | Font Awesome 5 Free | 20px | 900 | 1em | 1px |
| Caption | Font Awesome 5 Free | 22px | 700 | 16px | 1px |
| Button | Font Awesome 5 Free | 60px | 700 | 40px | 1px |
| Mono | Font Awesome 5 Free | 0.0 | 700 | 40px | 1px |
| Label | Font Awesome 5 Free | 13px | 700 | 40px | 1px |

## 4. Component Stylings

### Navigation
- **Selectors:** `nav`, `.navbar`, `header`
- **Traits:** top navigation; brand + links
### Buttons
- **Selectors:** `button`, `.btn`, `a.button`
- **Traits:** primary actions; hover states
### Cards
- **Selectors:** `.card`, `.panel`, `.thumbnail`, `.product`
- **Traits:** content containers
### Forms
- **Selectors:** `form`, `input`, `textarea`, `select`
- **Traits:** data input; interactive controls
### Hero
- **Selectors:** `.hero`, `#hero`, `.banner`, `.slider`, `#home`
- **Traits:** intro section; headline + call-to-action

## 5. Layout Principles

### Spacing Scale
0–60px (12 steps)

### Border Radius Scale
0–100px (10 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `0 0 30px rgba(0, 0, 0, 0.1)` |
| 2 | `none` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#00539C` as the primary accent for CTAs and interactive elements.
- Use `font Awesome 5 Free` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 5 media query breakpoint(s):
- `@media (max-width: 767.98px)`
- `@media (max-width: 768px)`
- `@media (min-width: 992px)`
- `@media (max-width: 992px)`
- `@media(max-width: 767.98px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `wait 108 cleanme` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** White (`#ffffff`)
- **CTA / Accent:** Dark Vivid Blue (`#00539C`)
- **Border:** White 2 (`#ffffff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.