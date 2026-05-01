# Design System: baby 6 skytouch onepage

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a charcoal with light green canvas, using Blue as the primary accent for interactive elements. The type scale spans 12px to 21px across 8 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Row-based section composition present.
- Sectioned page architecture with repeated blocks.
- Primary typeface: `inherit`
- Accent palette driven by 5 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **Light Green** (`#d6e9c6`): Primary surface color
- **Pale Red** (`#eed3d7`): Primary surface color
- **Pale Vivid Amber** (`#fbeed5`): Primary surface color
### Accent
- **Blue** (`#428bca`): CTAs, links, and interactive highlights
- **Vivid Blue** (`#1371AF`): CTAs, links, and interactive highlights
- **Amber** (`#c09853`): CTAs, links, and interactive highlights
- **Red** (`#b94a48`): CTAs, links, and interactive highlights
- **Muted Green** (`#468847`): CTAs, links, and interactive highlights
### Neutral
- **White** (`#fff`): Structural background
- **White 2** (`rgba(255,255,255,0.15)`): Structural background
- **Mid Gray** (`#999`): Border and divider color
- **Light Gray** (`#ddd`): Structural background
- **Charcoal** (`#333`): Structural background
- **Black** (`#000`): Structural background
- **Black 2** (`rgba(0,0,0,0.075)`): Structural background
- **Light Gray 2** (`#eee`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `inherit` (Primary)
- `"Helvetica Neue", Helvetica, Arial, sans-serif`
- `sans-serif`
- `monospace, serif`
- `Monaco, Menlo, Consolas, "Courier New", monospace`
- `"Glyphicons Halflings"`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | inherit | 12px | normal | 1.428571 | normal |
| Heading | Helvetica Neue, Helvetica, Arial, sans-serif | 18px | bold | 1 | normal |
| Sub-heading | sans-serif | 14px | 200 | 1.5 | normal |
| Body | monospace, serif | 16px | 400 | 1.33 | normal |
| Caption | Monaco, Menlo, Consolas, Courier New, monospace | 16px | 500 | inherit | normal |
| Button | Glyphicons Halflings | 16px | 300 | 1.4 | normal |
| Mono | Glyphicons Halflings | 21px | 300 | 1.4 | normal |
| Label | Glyphicons Halflings | 16px | 300 | 1.4 | normal |

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
0–20px (12 steps)

### Border Radius Scale
0–50px (10 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `inset 0 1px 1px rgba(0, 0, 0, 0.075)` |
| 2 | `none` |
| 3 | `inset 0 3px 5px rgba(0, 0, 0, 0.125)` |
| 4 | `1px 1px 1px rgba(0, 0, 0, 0.1) inset, 1px 1px 1px rgba(255, 255, 255, 0.1)` |
| 5 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 8px rgba(102, 175, 233, 0.6)` |
| 6 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #dbc59e` |
| 7 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #d59392` |
| 8 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #7aba7b` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#428bca` as the primary accent for CTAs and interactive elements.
- Use `inherit` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media(min-width:768px)`
- `@media(max-width:767px)`
- `@media(min-width:1200px)`
- `@media(min-width:768px) and (max-width:991px)`
- `@media(min-width:992px) and (max-width:1199px)`
- `@media screen and (min-width:768px)`
- `@media print`
- `@media (min-width: 768px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `baby 6 skytouch onepage` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** Light Green (`#d6e9c6`)
- **CTA / Accent:** Blue (`#428bca`)
- **Border:** White (`#fff`)
- **Surface:** Pale Red (`#eed3d7`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.