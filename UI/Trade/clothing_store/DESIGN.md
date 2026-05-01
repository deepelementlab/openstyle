# Design System: cpts 1262 ced

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a deep deep muted blue with pale green canvas, using Red as the primary accent for interactive elements. The typography is anchored by `Oswald`, creating a consistent reading experience. The type scale spans 12px to 18px across 8 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Primary typeface: `Oswald`
- Accent palette driven by 5 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **Deep Muted Blue** (`#1B242F`): Primary text color
- **Pale Green** (`#dff0d8`): Primary surface color
- **Pale Vivid Yellow** (`#fcf8e3`): Primary surface color
- **Pale Red** (`#f2dede`): Primary surface color
### Accent
- **Red** (`#bc3726`): CTAs, links, and interactive highlights
- **Muted Green** (`#3c763d`): CTAs, links, and interactive highlights
- **Amber** (`#8a6d3b`): CTAs, links, and interactive highlights
- **Red 2** (`#a94442`): CTAs, links, and interactive highlights
- **Cyan** (`#31708f`): CTAs, links, and interactive highlights
### Neutral
- **White** (`#fff`): Structural background
- **Black** (`#000`): Structural background
- **Light Gray** (`#ddd`): Structural background
- **White 2** (`rgba(255, 255, 255, .15)`): Structural background
- **Mid Gray** (`#999`): Border and divider color
- **Charcoal** (`#333`): Structural background
- **Black 2** (`rgba(0, 0, 0, .075)`): Structural background
- **Dark Gray** (`#555`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"Oswald", sans-serif` (Primary)
- `"Libre Baskerville", serif`
- `inherit`
- `sans-serif`
- `monospace, monospace`
- `"Helvetica Neue", Helvetica, Arial, sans-serif`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Oswald, sans-serif | 16px | 600 | 1.428571 | normal |
| Heading | Libre Baskerville, serif | 12px | normal | 1 | normal |
| Sub-heading | inherit | 16px | bold | 1.5 | normal |
| Body | sans-serif | 14px | 700 | 0 | normal |
| Caption | monospace, monospace | 16px | 400 | 1.33 | normal |
| Button | Helvetica Neue, Helvetica, Arial, sans-serif | 16px | 500 | 20px | normal |
| Mono | Helvetica Neue, Helvetica, Arial, sans-serif | 16px | 500 | 20px | normal |
| Label | Helvetica Neue, Helvetica, Arial, sans-serif | 18px | 500 | 20px | normal |

## 4. Component Stylings

### Forms
- **Selectors:** `form`, `input`, `textarea`, `select`
- **Traits:** data input; interactive controls
### Hero
- **Selectors:** `.hero`, `#hero`, `.banner`, `.slider`, `#home`
- **Traits:** intro section; headline + call-to-action

## 5. Layout Principles

### Spacing Scale
0–20px (12 steps)

### Border Radius Scale
0–100px (10 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `inset 0 1px 1px rgba(0, 0, 0, 0.075)` |
| 2 | `none` |
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
- Use `#bc3726` as the primary accent for CTAs and interactive elements.
- Use `Oswald` as the base font family to preserve the template's typographic identity.

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
- `@media (min-width: 992px)`
- `@media screen and (min-width: 768px)`
- `@media (min-width: 768px) and (max-width: 991px)`
- `@media (min-width: 992px) and (max-width: 1199px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `cpts 1262 ced` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** Deep Muted Blue (`#1B242F`)
- **CTA / Accent:** Red (`#bc3726`)
- **Border:** White (`#fff`)
- **Surface:** Pale Green (`#dff0d8`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.