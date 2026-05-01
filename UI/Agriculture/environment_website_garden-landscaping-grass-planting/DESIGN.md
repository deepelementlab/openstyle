# Design System: dntp 4 czl

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a charcoal with white canvas, using Vivid Orange as the primary accent for interactive elements. The type scale spans 1px to 21px across 7 levels.

**Key Characteristics:**
- Grid system detected via column classes.
- Row-based section composition present.
- Sectioned page architecture with repeated blocks.
- Primary typeface: `system-ui`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **White** (`#fff`): Primary surface color
### Accent
- **Vivid Orange** (`#f26522`): CTAs, links, and interactive highlights
- **Soft Vivid Blue** (`#41b4fb`): CTAs, links, and interactive highlights
- **Soft Vivid Amber** (`#ffcf3d`): CTAs, links, and interactive highlights
- **Vivid Red** (`#cf2b01`): CTAs, links, and interactive highlights
- **Vivid Lime** (`#7da500`): CTAs, links, and interactive highlights
- **Vivid Yellow** (`#b7ca0d`): CTAs, links, and interactive highlights
### Neutral
- **White 2** (`#fff`): Structural background
- **Charcoal** (`#444`): Structural background
- **Light Gray** (`#ddd`): Structural background
- **Light Gray 2** (`#eee`): Structural background
- **Light Gray 3** (`#dddddd`): Structural background
- **Mid Gray** (`#888`): Border and divider color
- **Silver** (`#ccc`): Border and divider color
- **Mid Gray 2** (`#858585`): Border and divider color
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `system-ui` (Primary)
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | system-ui | 12px | normal | 1.42857 | normal |
| Heading | system-ui | 1.0 | 400 | 40px | normal |
| Sub-heading | system-ui | 0.0 | 400 | 40px | normal |
| Body | system-ui | 8.0 | 400 | 40px | normal |
| Caption | system-ui | 15px | 400 | 40px | normal |
| Button | system-ui | 16px | 400 | 40px | normal |
| Mono | system-ui | 14px | 400 | 40px | normal |
| Label | system-ui | 21px | 400 | 40px | normal |

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
0–3px (3 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `none` |
| 2 | `0 1px 0 rgba(255, 255, 255, 0.3) inset, 0 0 2px rgba(255, 255, 255, 0.3) inset, 0 1px 2px rgba(0, 0, 0, 0.29)` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#f26522` as the primary accent for CTAs and interactive elements.
- Use `system-ui` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 2 media query breakpoint(s):
- `@media (max-width: 959px)`
- `@media only screen and (max-width: 768px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `dntp 4 czl` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** White (`#fff`)
- **CTA / Accent:** Vivid Orange (`#f26522`)
- **Border:** White 2 (`#fff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.