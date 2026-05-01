# Design System: sbtp 35 bdh

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a vivid yellow with pale vivid green canvas, using Dark Muted Blue as the primary accent for interactive elements. The typography is anchored by `Open Sans`, creating a consistent reading experience. The type scale spans 12px to 24px across 8 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Row-based section composition present.
- Sectioned page architecture with repeated blocks.
- Primary typeface: `Open Sans`
- Accent palette driven by 4 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **Vivid Yellow** (`#ff0`): Primary surface color
- **Pale Vivid Green** (`#dbffd1`): Primary surface color
### Accent
- **Dark Muted Blue** (`#2c3e50`): CTAs, links, and interactive highlights
- **Green** (`#27AE60`): CTAs, links, and interactive highlights
- **Dark Muted Blue 2** (`#34495E`): CTAs, links, and interactive highlights
- **Green 2** (`rgba(39,174,96,0.93)`): CTAs, links, and interactive highlights
### Neutral
- **Silver** (`#bdc3c7`): Border and divider color
- **White** (`#FFF`): Structural background
- **Black** (`rgba(0,0,0,0)`): Structural background
- **Mid Gray** (`#999`): Border and divider color
- **Silver 2** (`#ccc`): Border and divider color
- **Black 2** (`rgba(0, 0, 0, 0.6)`): Structural background
- **White 2** (`#fff`): Structural background
- **Pale Muted Cyan** (`#ECF0F1`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"Open Sans", sans-serif` (Primary)
- `"fontello"`
- `sans-serif`
- `monospace, serif`
- `inherit`
- `"webflow-icons"`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Open Sans, sans-serif | 16px | 600 | 0 | 0.075em |
| Heading | fontello | 16px | 700 | 1.5 | 0.1em |
| Sub-heading | sans-serif | 16px | normal | 18px | 0.1em |
| Body | monospace, serif | 24px | 300 | 1 | 0.1em |
| Caption | inherit | 12px | bold | inherit | 0.1em |
| Button | webflow-icons | 16px | 100 | 24px | 0.1em |
| Mono | webflow-icons | 16px | 100 | 24px | 0.1em |
| Label | webflow-icons | 16px | 100 | 24px | 0.1em |

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
### Hero
- **Selectors:** `.hero`, `#hero`, `.banner`, `.slider`, `#home`
- **Traits:** intro section; headline + call-to-action

## 5. Layout Principles

### Spacing Scale
0–40px (12 steps)

### Border Radius Scale
50–100px (2 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `none` |
| 2 | `0 0 8px rgba(0, 0, 0, 0.6)` |
| 3 | `inset 0 1px 1px rgba(0, 0, 0, 0.075)` |
| 4 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 8px rgba(82, 168, 236, 0.6)` |
| 5 | `0 0 3px rgba(51, 51, 51, 0.4)` |
| 6 | `0 1px 2px rgba(0, 0, 0, 0.25)` |
| 7 | `inset 0 -3px 6px rgba(0, 0, 0, 0.1)` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#2c3e50` as the primary accent for CTAs and interactive elements.
- Use `Open Sans` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media screen and (max-width:991px)`
- `@media screen and (max-width:767px)`
- `@media screen and (max-width:479px)`
- `@media (max-width: 991px)`
- `@media (max-width: 767px)`
- `@media (max-width: 479px)`
- `@media (min-width: 320px) and (max-width: 480px)`
- `@media screen and max-width 306em`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `sbtp 35 bdh` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** Vivid Yellow (`#ff0`)
- **CTA / Accent:** Dark Muted Blue (`#2c3e50`)
- **Border:** Silver (`#bdc3c7`)
- **Surface:** Pale Vivid Green (`#dbffd1`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.