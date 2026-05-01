# Design System: dgmg 34 cappuccino

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a deep deep muted blue with pale green canvas, using Dark Muted Red as the primary accent for interactive elements. The type scale spans 12px to 18px across 8 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Sectioned page architecture with repeated blocks.
- Primary typeface: `inherit`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **Deep Muted Blue** (`#1B242F`): Primary text color
- **Pale Green** (`#dff0d8`): Primary surface color
- **Pale Vivid Yellow** (`#fcf8e3`): Primary surface color
- **Pale Red** (`#f2dede`): Primary surface color
### Accent
- **Dark Muted Red** (`#673840`): CTAs, links, and interactive highlights
- **Red** (`#bf6459`): CTAs, links, and interactive highlights
- **Muted Green** (`#3c763d`): CTAs, links, and interactive highlights
- **Amber** (`#8a6d3b`): CTAs, links, and interactive highlights
- **Red 2** (`#a94442`): CTAs, links, and interactive highlights
- **Mid Gray** (`#8d7979`): CTAs, links, and interactive highlights
### Neutral
- **White** (`#fff`): Structural background
- **Light Gray** (`#ddd`): Structural background
- **White 2** (`rgba(255, 255, 255, .15)`): Structural background
- **Mid Gray 2** (`#999`): Border and divider color
- **Black** (`#000`): Structural background
- **Charcoal** (`#333`): Structural background
- **Black 2** (`rgba(0, 0, 0, .075)`): Structural background
- **White 3** (`#f5f5f5`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `inherit` (Primary)
- `sans-serif`
- `monospace, monospace`
- `"Helvetica Neue", Helvetica, Arial, sans-serif`
- `Menlo, Monaco, Consolas, "Courier New", monospace`
- `"Glyphicons Halflings"`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | inherit | 16px | normal | 1.428571 | 1px |
| Heading | sans-serif | 12px | 700 | 1.8em | 1px |
| Sub-heading | monospace, monospace | 14px | bold | 1 | 1px |
| Body | Helvetica Neue, Helvetica, Arial, sans-serif | 18px | 400 | 1.5 | 1px |
| Caption | Menlo, Monaco, Consolas, Courier New, monospace | 16px | 300 | 1.33 | 1px |
| Button | Glyphicons Halflings | 16px | 500 | 20px | 1px |
| Mono | Glyphicons Halflings | 16px | 500 | 20px | 1px |
| Label | Glyphicons Halflings | 16px | 500 | 20px | 1px |

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
0–50px (10 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `inset 0 1px 1px rgba(0, 0, 0, 0.075)` |
| 2 | `none` |
| 3 | `inset 0 3px 5px rgba(0, 0, 0, 0.125)` |
| 4 | `0 1px 1px rgba(0, 0, 0, 0.4)` |
| 5 | `inset 0 -1px 0 rgba(0, 0, 0, 0.25)` |
| 6 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 8px rgba(102, 175, 233, 0.6)` |
| 7 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168` |
| 8 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#673840` as the primary accent for CTAs and interactive elements.
- Use `inherit` as the base font family to preserve the template's typographic identity.

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
> "Based on the `dgmg 34 cappuccino` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** Deep Muted Blue (`#1B242F`)
- **CTA / Accent:** Dark Muted Red (`#673840`)
- **Border:** White (`#fff`)
- **Surface:** Pale Green (`#dff0d8`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.