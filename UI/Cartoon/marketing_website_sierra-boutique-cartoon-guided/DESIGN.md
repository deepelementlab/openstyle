# Design System: dgfp 14 sierra

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a deep deep blue with white canvas, using Light Vivid Blue as the primary accent for interactive elements. The typography is anchored by `Roboto`, creating a consistent reading experience. The type scale spans 12px to 30px across 8 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Row-based section composition present.
- Sectioned page architecture with repeated blocks.
- Primary typeface: `Roboto`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **Deep Blue** (`#0b1033`): Primary text color
### Accent
- **Light Vivid Blue** (`#9b8aff`): CTAs, links, and interactive highlights
- **Mid Gray** (`#7c8d93`): CTAs, links, and interactive highlights
- **Vivid Blue** (`#007bff`): CTAs, links, and interactive highlights
- **Soft Vivid Blue** (`#6ebdfe`): CTAs, links, and interactive highlights
- **Soft Vivid Blue 2** (`#70bafe`): CTAs, links, and interactive highlights
- **Red** (`#dc3545`): CTAs, links, and interactive highlights
### Neutral
- **White** (`#fff`): Structural background
- **White 2** (`rgba(255, 255, 255, 1.00)`): Structural background
- **White 3** (`rgba(255,255,255,1.00)`): Structural background
- **Black** (`#000`): Structural background
- **Black 2** (`rgba(0, 0, 0, 1.00)`): Structural background
- **Mid Gray 2** (`#868e96`): Border and divider color
- **Charcoal** (`rgba(51, 51, 51, 1.00)`): Structural background
- **White 4** (`rgba(255,255,255,1)`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"Roboto", sans-serif` (Primary)
- `Raleway`
- `Roboto`
- `Lato`
- `"Open Sans"`
- `Arial`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Roboto, sans-serif | 15px | 500 | 20px | 2px |
| Heading | Raleway | 12px | 400 | 30px | 1px |
| Sub-heading | Roboto | 20px | 300 | 28px | 3px |
| Body | Lato | 13px | 700 | 70px | 5px |
| Caption | Open Sans | 25px | 600 | 1.5 | 0 |
| Button | Arial | 14px | 900 | 60px | 10px |
| Mono | Arial | 30px | 900 | 60px | 10px |
| Label | Arial | 17px | 900 | 60px | 10px |

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
0–35px (12 steps)

### Border Radius Scale
0–100px (10 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `none` |
| 2 | `inset 5px 5px 10px 0 rgba(0, 0, 0, 0.25)` |
| 3 | `0 0 0 0.2rem rgba(0, 123, 255, 0.5)` |
| 4 | `0 0 0 0.2rem rgba(134, 142, 150, 0.5)` |
| 5 | `0 0 0 0.2rem rgba(40, 167, 69, 0.5)` |
| 6 | `0 0 0 0.2rem rgba(23, 162, 184, 0.5)` |
| 7 | `0 0 0 0.2rem rgba(255, 193, 7, 0.5)` |
| 8 | `0 0 0 0.2rem rgba(220, 53, 69, 0.5)` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#9b8aff` as the primary accent for CTAs and interactive elements.
- Use `Roboto` as the base font family to preserve the template's typographic identity.

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
- `@media print`
- `@media only screen and (max-width: 960px)`
- `@media only screen and (max-width: 768px)`
- `@media only screen and (max-width: 767px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `dgfp 14 sierra` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** Deep Blue (`#0b1033`)
- **CTA / Accent:** Light Vivid Blue (`#9b8aff`)
- **Border:** White (`#fff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.