# Design System: cpts 635 bsv

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a mid gray with pale vivid yellow canvas, using Muted Amber as the primary accent for interactive elements. The typography is anchored by `Inconsolata-Regular`, creating a consistent reading experience. The type scale spans 12px to 40px across 8 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Primary typeface: `Inconsolata-Regular`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **Pale Vivid Yellow** (`#fcf8e3`): Primary surface color
- **Pale Green** (`#dff0d8`): Primary surface color
- **Pale Red** (`#f2dede`): Primary surface color
### Accent
- **Muted Amber** (`#958e71`): CTAs, links, and interactive highlights
- **Blue** (`#337ab7`): CTAs, links, and interactive highlights
- **Muted Green** (`#3c763d`): CTAs, links, and interactive highlights
- **Amber** (`#8a6d3b`): CTAs, links, and interactive highlights
- **Red** (`#a94442`): CTAs, links, and interactive highlights
- **Cyan** (`#31708f`): CTAs, links, and interactive highlights
### Neutral
- **White** (`#fff`): Structural background
- **White 2** (`rgba(255, 255, 255, .15)`): Structural background
- **Light Gray** (`#ddd`): Structural background
- **Mid Gray** (`#777`): Border and divider color
- **Charcoal** (`#333`): Structural background
- **Dark Gray** (`#535353`): Structural background
- **Black** (`#000`): Structural background
- **Light Gray 2** (`#eee`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"Inconsolata-Regular"` (Primary)
- `"Open Sans", sans-serif`
- `"Helvetica Neue", Helvetica, Arial, sans-serif`
- `inherit`
- `sans-serif`
- `monospace, monospace`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Inconsolata-Regular | 14px | normal | 1.428571 | normal |
| Heading | Open Sans, sans-serif | 16px | bold | 1.8em | 3px |
| Sub-heading | Helvetica Neue, Helvetica, Arial, sans-serif | 12px | 300 | 1 | 1px |
| Body | inherit | 18px | 400 | 1.5 | 0 |
| Caption | sans-serif | 16px | 600 | 1.333333 | 0 |
| Button | monospace, monospace | 16px | 500 | 2em | 0 |
| Mono | monospace, monospace | 16px | 500 | 2em | 0 |
| Label | monospace, monospace | 40px | 500 | 2em | 0 |

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
0–15px (12 steps)

### Border Radius Scale
0–50px (10 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `none` |
| 2 | `inset 0 1px 1px rgba(0, 0, 0, 0.075)` |
| 3 | `inset 0 3px 5px rgba(0, 0, 0, 0.125)` |
| 4 | `0 0 1px rgba(0, 0, 0, 0)` |
| 5 | `0 0 0 0 #2c3f52` |
| 6 | `0 0 0 10px #2c3f52` |
| 7 | `inset 0 -1px 0 rgba(0, 0, 0, 0.25)` |
| 8 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 8px rgba(102, 175, 233, 0.6)` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#958e71` as the primary accent for CTAs and interactive elements.
- Use `Inconsolata-Regular` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media (min-width: 768px)`
- `@media (max-width: 767px)`
- `@media (min-width: 1200px)`
- `@media print`
- `@media (min-width: 768px) and (max-width: 991px)`
- `@media (min-width: 992px) and (max-width: 1199px)`
- `@media (min-width: 992px)`
- `@media(max-width:1080px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `cpts 635 bsv` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** Pale Vivid Yellow (`#fcf8e3`)
- **CTA / Accent:** Muted Amber (`#958e71`)
- **Border:** White (`#fff`)
- **Surface:** Pale Green (`#dff0d8`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.