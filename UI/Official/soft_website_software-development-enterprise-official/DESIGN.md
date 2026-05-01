# Design System: cpts 1072 bpf

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a black with white canvas, using Vivid Blue as the primary accent for interactive elements. The typography is anchored by `Source Sans Pro`, creating a consistent reading experience. The type scale spans 10px to 21px across 7 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Row-based section composition present.
- Primary typeface: `Source Sans Pro`
- Accent palette driven by 4 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **White** (`#ffffff`): Primary surface color
### Accent
- **Vivid Blue** (`#0088cc`): CTAs, links, and interactive highlights
- **Vivid Amber** (`#f89406`): CTAs, links, and interactive highlights
- **Soft Vivid Red** (`#ee5f5b`): CTAs, links, and interactive highlights
- **Soft Vivid Amber** (`#fbb450`): CTAs, links, and interactive highlights
### Neutral
- **White 2** (`#ffffff`): Structural background
- **White 3** (`rgba(255, 255, 255, 0.15)`): Structural background
- **Mid Gray** (`#999999`): Border and divider color
- **Black** (`rgba(0, 0, 0, 0.25)`): Structural background
- **Black 2** (`rgba(0, 0, 0, 0.075)`): Structural background
- **Black 3** (`rgba(0, 0, 0, 0.1)`): Structural background
- **White 4** (`#fff`): Structural background
- **Light Gray** (`#ddd`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"Source Sans Pro", "Helvetica Neue", Helvetica, Arial, sans-serif` (Primary)
- `"Helvetica Neue", Helvetica, Arial, sans-serif`
- `inherit`
- `Monaco, Menlo, Consolas, "Courier New", monospace`
- `FontAwesome`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Source Sans Pro, Helvetica Neue, Helvetica, Arial, sans-serif | 14px | bold | 20px | -1px |
| Heading | Helvetica Neue, Helvetica, Arial, sans-serif | 18px | normal | 0 | 0.021em |
| Sub-heading | inherit | 12px | 200 | 1 | 0.021em |
| Body | Monaco, Menlo, Consolas, Courier New, monospace | 0.0 | 300 | 30px | 0.021em |
| Caption | FontAwesome | 10px | 100 | 40px | 0.021em |
| Button | FontAwesome | 20px | 500 | normal | 0.021em |
| Mono | FontAwesome | 16px | 500 | normal | 0.021em |
| Label | FontAwesome | 21px | 500 | normal | 0.021em |

## 4. Component Stylings

### Navigation
- **Selectors:** `nav`, `.navbar`, `header`
- **Traits:** top navigation; brand + links
### Buttons
- **Selectors:** `button`, `.btn`, `a.button`
- **Traits:** primary actions; hover states
### Cards
- **Selectors:** `.card`, `.panel`, `.thumbnail`, `.product`
- **Traits:** content containers
### Forms
- **Selectors:** `form`, `input`, `textarea`, `select`
- **Traits:** data input; interactive controls

## 5. Layout Principles

### Spacing Scale
0–30px (12 steps)

### Border Radius Scale
0–15px (10 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `inset 0 1px 1px rgba(0, 0, 0, 0.075)` |
| 2 | `0 2px 4px rgba(220, 218, 216, 0.75)` |
| 3 | `inset 0 2px 4px rgba(0, 0, 0, 0.15), 0 1px 2px rgba(0, 0, 0, 0.05)` |
| 4 | `none` |
| 5 | `0 5px 10px rgba(0, 0, 0, 0.2)` |
| 6 | `0 1px 3px rgba(0, 0, 0, 0.1)` |
| 7 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 8px rgba(82, 168, 236, 0.6)` |
| 8 | `inset 0 1px 2px rgba(0, 0, 0, 0.025)` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#0088cc` as the primary accent for CTAs and interactive elements.
- Use `Source Sans Pro` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media (min-width:768px) and (max-width:979px)`
- `@media (max-width:767px)`
- `@media print`
- `@media (max-width:480px)`
- `@media (min-width:1200px)`
- `@media (max-width:979px)`
- `@media (min-width:980px)`
- `@media (min-width: 768px) and (max-width: 979px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `cpts 1072 bpf` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** White (`#ffffff`)
- **CTA / Accent:** Vivid Blue (`#0088cc`)
- **Border:** White 2 (`#ffffff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.