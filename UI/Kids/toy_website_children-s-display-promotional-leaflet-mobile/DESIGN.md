# Design System: atpp 5 tinker

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a vivid yellow with silver canvas, using Teal as the primary accent for interactive elements. The typography is anchored by `Lato`, creating a consistent reading experience. The type scale spans 11px to 21px across 7 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Sectioned page architecture with repeated blocks.
- Primary typeface: `Lato`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **Vivid Yellow** (`#ff0`): Primary surface color
### Accent
- **Teal** (`#3cdaa7`): CTAs, links, and interactive highlights
- **Teal 2** (`#24bf8d`): CTAs, links, and interactive highlights
- **Muted Blue** (`#5a636e`): CTAs, links, and interactive highlights
- **Muted Blue 2** (`#87919d`): CTAs, links, and interactive highlights
- **Vivid Yellow 2** (`#fad808`): CTAs, links, and interactive highlights
- **Vivid Orange** (`#f87527`): CTAs, links, and interactive highlights
### Neutral
- **Silver** (`#babfc6`): Border and divider color
- **White** (`#fff`): Structural background
- **Dark Muted Blue** (`#31363c`): Structural background
- **Pale Muted Blue** (`#eceef0`): Structural background
- **Black** (`#000`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `Lato, Trebuchet, sans-serif` (Primary)
- `Poppins, Avenir, "Avenir Next", Trebuchet, Verdana, sans-serif`
- `monospace, monospace`
- `sans-serif`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Lato, Trebuchet, sans-serif | 16px | 700 | 1.6rem | normal |
| Heading | Poppins, Avenir, Avenir Next, Trebuchet, Verdana, sans-serif | 16px | 400 | inherit | normal |
| Sub-heading | monospace, monospace | 0.0 | inherit | 1 | normal |
| Body | sans-serif | 21px | bolder | 1.15 | normal |
| Caption | sans-serif | 11px | 300 | 0 | normal |
| Button | sans-serif | 16px | 300 | 0 | normal |
| Mono | sans-serif | 16px | 300 | 0 | normal |
| Label | sans-serif | 16px | 300 | 0 | normal |

## 4. Component Stylings

### Navigation
- **Selectors:** `nav`, `.navbar`, `header`
- **Traits:** top navigation; brand + links

## 5. Layout Principles

### Spacing Scale
0–1px (7 steps)

### Border Radius Scale
0–50px (6 steps)

## 6. Depth & Elevation

- No significant shadow system detected.

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#3cdaa7` as the primary accent for CTAs and interactive elements.
- Use `Lato` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 3 media query breakpoint(s):
- `@media screen and (min-width:40em)`
- `@media screen and (max-width:50em)`
- `@media screen and (max-width:40em)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `atpp 5 tinker` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** Vivid Yellow (`#ff0`)
- **CTA / Accent:** Teal (`#3cdaa7`)
- **Border:** Silver (`#babfc6`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.