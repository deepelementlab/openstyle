# Design System: moban4304

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a black with pale yellow canvas, using Muted Green as the primary accent for interactive elements. The typography is anchored by `FontAwesome`, creating a consistent reading experience. The type scale spans 12px to 18px across 8 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Row-based section composition present.
- Sectioned page architecture with repeated blocks.
- Primary typeface: `FontAwesome`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **Pale Yellow** (`#F9F6E5`): Primary surface color
### Accent
- **Muted Green** (`#6bb071`): CTAs, links, and interactive highlights
- **Red** (`#e0404b`): CTAs, links, and interactive highlights
- **Soft Muted Green** (`#7EBF84`): CTAs, links, and interactive highlights
- **Light Vivid Red** (`#ff797c`): CTAs, links, and interactive highlights
- **Muted Green 2** (`rgba(71,110,77,0.35)`): CTAs, links, and interactive highlights
- **Muted Green 3** (`#6BB071`): CTAs, links, and interactive highlights
### Neutral
- **Black** (`rgba(0,0,0,0)`): Structural background
- **White** (`#fff`): Structural background
- **Light Gray** (`#e1e1e1`): Structural background
- **Charcoal** (`#333`): Structural background
- **Silver** (`#ccc`): Border and divider color
- **Silver 2** (`#cccccc`): Border and divider color
- **Dark Gray** (`#666`): Structural background
- **White 2** (`#FFF`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `FontAwesome` (Primary)
- `"Libre Baskerville", serif`
- `"fontawesome"`
- `"Dosis", sans-serif`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | FontAwesome | 16px | 800 | 1 | 2px |
| Heading | Libre Baskerville, serif | 16px | 600 | 0 | 0.09em |
| Sub-heading | fontawesome | 16px | 500 | 1.8 | 1px |
| Body | Dosis, sans-serif | 16px | normal | 1.3 | 1px |
| Caption | Dosis, sans-serif | 16px | 700 | 200px | 1px |
| Button | Dosis, sans-serif | 12px | inherit | 18px | 1px |
| Mono | Dosis, sans-serif | 18px | inherit | 18px | 1px |
| Label | Dosis, sans-serif | 16px | inherit | 18px | 1px |

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
0–20px (12 steps)

### Border Radius Scale
0–100px (10 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `0 0 1px rgba(0, 0, 0, 0)` |
| 2 | `0 0 8px rgba(0, 0, 0, 0.6)` |
| 3 | `inset 0 0 0 4px #e1e1e1, 0 0 1px rgba(0, 0, 0, 0)` |
| 4 | `0 0 1px #bfbfbf, 0 0 1px #fff inset` |
| 5 | `0 0 2px 0 rgba(0, 0, 0, 0.5)` |
| 6 | `inset 0 -1px rgba(0, 0, 0, 0.1)` |
| 7 | `inset 0 -1px rgba(0, 0, 0, 0.1), inset 0 1px rgba(0, 0, 0, 0.1)` |
| 8 | `inset 0 -1px rgba(0, 0, 0, 0)` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#6bb071` as the primary accent for CTAs and interactive elements.
- Use `FontAwesome` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media only screen and (max-width: 1024px)`
- `@media only screen and (max-width: 768px)`
- `@media only screen and (max-width: 600px)`
- `@media only screen and (max-width: 568px)`
- `@media only screen and (max-width: 480px)`
- `@media only screen and (max-width: 384px)`
- `@media only screen and (max-width: 320px)`
- `@media only screen and (max-width: 240px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `moban4304` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** Pale Yellow (`#F9F6E5`)
- **CTA / Accent:** Muted Green (`#6bb071`)
- **Border:** Black (`rgba(0,0,0,0)`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.