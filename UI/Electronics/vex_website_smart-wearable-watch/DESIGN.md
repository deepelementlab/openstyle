# Design System: twts 250 VEX Bootstrap4

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a charcoal with white canvas, using Vivid Blue as the primary accent for interactive elements. The typography is anchored by `-apple-system`, creating a consistent reading experience. The type scale spans 14px to 20px across 8 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Row-based section composition present.
- Sectioned page architecture with repeated blocks.
- Primary typeface: `-apple-system`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **White** (`#fff`): Primary surface color
### Accent
- **Vivid Blue** (`#0275d8`): CTAs, links, and interactive highlights
- **Green** (`#5cb85c`): CTAs, links, and interactive highlights
- **Soft Vivid Amber** (`#f0ad4e`): CTAs, links, and interactive highlights
- **Soft Red** (`#d9534f`): CTAs, links, and interactive highlights
- **Soft Cyan** (`#5bc0de`): CTAs, links, and interactive highlights
- **Soft Vivid Orange** (`#f9a743`): CTAs, links, and interactive highlights
### Neutral
- **White 2** (`#fff`): Structural background
- **Light Gray** (`#eceeef`): Structural background
- **White 3** (`rgba(255,255,255,.15)`): Structural background
- **Mid Gray** (`#818a91`): Border and divider color
- **Light Gray 2** (`#ddd`): Structural background
- **Charcoal** (`#373a3c`): Structural background
- **Black** (`#000`): Structural background
- **Silver** (`#ccc`): Border and divider color
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif` (Primary)
- `"themefisher-font"`
- `sans-serif`
- `monospace, monospace`
- `inherit`
- `Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif | 20px | 700 | 1 | normal |
| Heading | themefisher-font | 16px | 300 | 0 | 3px |
| Sub-heading | sans-serif | 14px | 400 | 1.5 | 3px |
| Body | monospace, monospace | 16px | bold | inherit | 3px |
| Caption | inherit | 20px | 500 | 1.25 | 3px |
| Button | Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace | 14px | inherit | 25px | 3px |
| Mono | Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace | 16px | inherit | 25px | 3px |
| Label | Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace | 16px | inherit | 25px | 3px |

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
0–40px (12 steps)

### Border Radius Scale
0–50px (8 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `none` |
| 2 | `0 0 8px rgba(0, 0, 0, 0.6)` |
| 3 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #a3d7a3` |
| 4 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #f8d9ac` |
| 5 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #eba5a3` |
| 6 | `0 0 0 0.075rem #fff, 0 0 0 0.2rem #0074d9` |
| 7 | `0 15px 40px rgba(249, 167, 68, 0.5)` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#0275d8` as the primary accent for CTAs and interactive elements.
- Use `-apple-system` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media (min-width:576px)`
- `@media (min-width:992px)`
- `@media (min-width:768px)`
- `@media (min-width:1200px)`
- `@media screen and (min-width:0\0)`
- `@media print`
- `@media (max-width:575px)`
- `@media (max-width:767px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `twts 250 VEX Bootstrap4` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** White (`#fff`)
- **CTA / Accent:** Vivid Blue (`#0275d8`)
- **Border:** White 2 (`#fff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.