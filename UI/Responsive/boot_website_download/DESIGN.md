# Design System: btzero 4 onassis

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a charcoal with light green canvas, using Blue as the primary accent for interactive elements. The type scale spans 12px to 21px across 8 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Row-based section composition present.
- Sectioned page architecture with repeated blocks.
- Primary typeface: `inherit`
- Accent palette driven by 4 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **Light Green** (`#d6e9c6`): Primary surface color
- **Pale Red** (`#eed3d7`): Primary surface color
- **Pale Vivid Amber** (`#fbeed5`): Primary surface color
### Accent
- **Blue** (`#428bca`): CTAs, links, and interactive highlights
- **Amber** (`#c09853`): CTAs, links, and interactive highlights
- **Red** (`#b94a48`): CTAs, links, and interactive highlights
- **Muted Green** (`#468847`): CTAs, links, and interactive highlights
### Neutral
- **White** (`#ffffff`): Structural background
- **White 2** (`rgba(255, 255, 255, 0.15)`): Structural background
- **Mid Gray** (`#999999`): Border and divider color
- **Light Gray** (`#dddddd`): Structural background
- **Charcoal** (`#333333`): Structural background
- **Black** (`rgba(0, 0, 0, 0.075)`): Structural background
- **Light Gray 2** (`#eeeeee`): Structural background
- **Black 2** (`#000000`): Structural background
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
| Display | inherit | 12px | normal | 1.428571 | 3px |
| Heading | Helvetica Neue, Helvetica, Arial, sans-serif | 14px | bold | 1 | 2px |
| Sub-heading | sans-serif | 18px | 700 | inherit | 1px |
| Body | monospace, serif | 16px | 300 | 1.5 | 0.15em |
| Caption | Monaco, Menlo, Consolas, Courier New, monospace | 16px | 200 | 40px | 0.1em |
| Button | Glyphicons Halflings | 21px | 100 | 1.33 | 0.1em |
| Mono | Glyphicons Halflings | 16px | 100 | 1.33 | 0.1em |
| Label | Glyphicons Halflings | 16px | 100 | 1.33 | 0.1em |

## 4. Component Stylings

### Navigation
- **Selectors:** `nav`, `.navbar`, `header`
- **Traits:** top navigation; brand + links
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
| 2 | `inset 0 3px 5px rgba(0, 0, 0, 0.125)` |
| 3 | `none` |
| 4 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 8px rgba(102, 175, 233, 0.6)` |
| 5 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #dbc59e` |
| 6 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #d59392` |
| 7 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #7aba7b` |
| 8 | `0 6px 12px rgba(0, 0, 0, 0.175)` |

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
> "Based on the `btzero 4 onassis` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** Light Green (`#d6e9c6`)
- **CTA / Accent:** Blue (`#428bca`)
- **Border:** White (`#ffffff`)
- **Surface:** Pale Red (`#eed3d7`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.