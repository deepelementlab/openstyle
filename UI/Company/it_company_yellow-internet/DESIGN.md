# Design System: moban2479

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a charcoal with white canvas, using Vivid Amber as the primary accent for interactive elements. The typography is anchored by `Open Sans`, creating a consistent reading experience. The type scale spans 12px to 21px across 8 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Row-based section composition present.
- Primary typeface: `Open Sans`
- Accent palette driven by 5 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **White** (`#ffffff`): Primary surface color
### Accent
- **Vivid Amber** (`#ffc400`): CTAs, links, and interactive highlights
- **Blue** (`#428bca`): CTAs, links, and interactive highlights
- **Amber** (`#c09853`): CTAs, links, and interactive highlights
- **Red** (`#b94a48`): CTAs, links, and interactive highlights
- **Muted Green** (`#468847`): CTAs, links, and interactive highlights
### Neutral
- **White 2** (`#ffffff`): Structural background
- **White 3** (`#fff`): Structural background
- **White 4** (`rgba(255, 255, 255, 0.15)`): Structural background
- **Mid Gray** (`#999999`): Border and divider color
- **Light Gray** (`#dddddd`): Structural background
- **Charcoal** (`#333333`): Structural background
- **Black** (`rgba(0, 0, 0, 0.075)`): Structural background
- **Black 2** (`#000000`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"Open Sans", sans-serif` (Primary)
- `inherit`
- `"Helvetica Neue", Helvetica, Arial, sans-serif`
- `"Glyphicons Halflings"`
- `Arial`
- `sans-serif`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Open Sans, sans-serif | 12px | bold | 1.428571 | -0.3px |
| Heading | inherit | 14px | normal | 1 | -0.31em |
| Sub-heading | Helvetica Neue, Helvetica, Arial, sans-serif | 18px | 200 | 1.5 | -0.31em |
| Body | Glyphicons Halflings | 16px | 300 | 30px | -0.31em |
| Caption | Arial | 13px | 500 | 20px | -0.31em |
| Button | sans-serif | 16px | 500 | 0 | -0.31em |
| Mono | sans-serif | 21px | 500 | 0 | -0.31em |
| Label | sans-serif | 16px | 500 | 0 | -0.31em |

## 4. Component Stylings

### Navigation
- **Selectors:** `nav`, `.navbar`, `header`
- **Traits:** top navigation; brand + links
### Buttons
- **Selectors:** `button`, `.btn`, `a.button`
- **Traits:** primary actions; hover states
### Hero
- **Selectors:** `.hero`, `#hero`, `.banner`, `.slider`, `#home`
- **Traits:** intro section; headline + call-to-action

## 5. Layout Principles

### Spacing Scale
0–30px (12 steps)

### Border Radius Scale
0–50px (10 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `inset 0 1px 1px rgba(0, 0, 0, 0.075)` |
| 2 | `inset 0 3px 5px rgba(0, 0, 0, 0.125)` |
| 3 | `none` |
| 4 | `0 1px 1px rgba(0, 0, 0, 0.1)` |
| 5 | `inset 0 1px 3px rgba(0, 0, 0, 0.1), 0 0 8px #ccc` |
| 6 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 8px rgba(102, 175, 233, 0.6)` |
| 7 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #dbc59e` |
| 8 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #d59392` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#ffc400` as the primary accent for CTAs and interactive elements.
- Use `Open Sans` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media (min-width: 768px)`
- `@media (max-width: 767px)`
- `@media (min-width: 1200px)`
- `@media (min-width: 768px) and (max-width: 991px)`
- `@media (min-width: 992px) and (max-width: 1199px)`
- `@media screen and (min-width: 768px)`
- `@media print`
- `@media (min-width: 992px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `moban2479` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** White (`#ffffff`)
- **CTA / Accent:** Vivid Amber (`#ffc400`)
- **Border:** White 2 (`#ffffff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.