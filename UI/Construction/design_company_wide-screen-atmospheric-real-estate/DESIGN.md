# Design System: cpts 1372 cdh

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a charcoal with pale vivid yellow canvas, using Blue as the primary accent for interactive elements. The typography is anchored by `Helvetica Neue`, creating a consistent reading experience. The type scale spans 12px to 18px across 8 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Row-based section composition present.
- Sectioned page architecture with repeated blocks.
- Primary typeface: `Helvetica Neue`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **Pale Vivid Yellow** (`#fcf8e3`): Primary surface color
- **Pale Green** (`#dff0d8`): Primary surface color
- **Pale Red** (`#f2dede`): Primary surface color
### Accent
- **Blue** (`#2a80b9`): CTAs, links, and interactive highlights
- **Blue 2** (`#337ab7`): CTAs, links, and interactive highlights
- **Muted Green** (`#3c763d`): CTAs, links, and interactive highlights
- **Amber** (`#8a6d3b`): CTAs, links, and interactive highlights
- **Red** (`#a94442`): CTAs, links, and interactive highlights
- **Cyan** (`#31708f`): CTAs, links, and interactive highlights
### Neutral
- **White** (`#fff`): Structural background
- **White 2** (`rgba(255,255,255,.15)`): Structural background
- **Charcoal** (`#333`): Structural background
- **Light Gray** (`#ddd`): Structural background
- **Black** (`#000`): Structural background
- **Mid Gray** (`#777`): Border and divider color
- **Light Gray 2** (`#eee`): Structural background
- **Black 2** (`rgba(0,0,0,.075)`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"Helvetica Neue", Helvetica, Arial, sans-serif` (Primary)
- `"Dosis", sans-serif`
- `inherit`
- `sans-serif`
- `monospace, monospace`
- `"Glyphicons Halflings"`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Helvetica Neue, Helvetica, Arial, sans-serif | 12px | 400 | 1.428571 | 2px |
| Heading | Dosis, sans-serif | 18px | 600 | 1 | 1px |
| Sub-heading | inherit | 14px | 700 | 1.5 | normal |
| Body | sans-serif | 16px | 500 | 1.333333 | 0 |
| Caption | monospace, monospace | 16px | 300 | 30px | 4px |
| Button | Glyphicons Halflings | 16px | 200 | 46px | 4px |
| Mono | Glyphicons Halflings | 16px | 200 | 46px | 4px |
| Label | Glyphicons Halflings | 16px | 200 | 46px | 4px |

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
0–30px (12 steps)

### Border Radius Scale
0–50px (10 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `none` |
| 2 | `inset 0 1px 1px rgba(0, 0, 0, 0.075)` |
| 3 | `inset 0 3px 5px rgba(0, 0, 0, 0.125)` |
| 4 | `0 0 3px rgba(0, 0, 0, 0.1)` |
| 5 | `inset 0 -1px 0 rgba(0, 0, 0, 0.25)` |
| 6 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 8px rgba(102, 175, 233, 0.6)` |
| 7 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168` |
| 8 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#2a80b9` as the primary accent for CTAs and interactive elements.
- Use `Helvetica Neue` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media (min-width:768px)`
- `@media only screen and (max-width:768px)`
- `@media only screen and (max-width:480px)`
- `@media (max-width:767px)`
- `@media (min-width:1200px)`
- `@media print`
- `@media (min-width:768px) and (max-width:991px)`
- `@media (min-width:992px) and (max-width:1199px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `cpts 1372 cdh` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** Pale Vivid Yellow (`#fcf8e3`)
- **CTA / Accent:** Blue (`#2a80b9`)
- **Border:** White (`#fff`)
- **Surface:** Pale Green (`#dff0d8`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.