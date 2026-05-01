# Design System: site

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a deep dark muted blue with vivid blue canvas, using Vivid Blue as the primary accent for interactive elements. The typography is anchored by `proxima-nova`, creating a consistent reading experience. The type scale spans 16px to 55px across 4 levels.

**Key Characteristics:**
- Sectioned page architecture with repeated blocks.
- Primary typeface: `proxima-nova`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **Vivid Blue** (`#2d91ea`): Primary surface color
### Accent
- **Vivid Blue 2** (`#2d91ea`): CTAs, links, and interactive highlights
- **Soft Vivid Red** (`#f33e6f`): CTAs, links, and interactive highlights
- **Mid Gray** (`#767c8d`): CTAs, links, and interactive highlights
- **Cyan** (`#46bfbd`): CTAs, links, and interactive highlights
- **Soft Vivid Orange** (`#fdb45c`): CTAs, links, and interactive highlights
- **Vivid Red** (`#f2265d`): CTAs, links, and interactive highlights
### Neutral
- **Light Gray** (`#ebebeb`): Structural background
- **Dark Muted Blue** (`#282b36`): Structural background
- **White** (`#fff`): Structural background
- **Black** (`rgba(0, 0, 0, 0.25)`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"proxima-nova", sans-serif` (Primary)
- `"proxima-nova", sans-serif sans-serif`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | proxima-nova, sans-serif | 18px | 600 | 40px | normal |
| Heading | proxima-nova, sans-serif sans-serif | 55px | 400 | 24px | normal |
| Sub-heading | proxima-nova, sans-serif sans-serif | 26px | 400 | 24px | normal |
| Body | proxima-nova, sans-serif sans-serif | 16px | 400 | 24px | normal |

## 4. Component Stylings

### Navigation
- **Selectors:** `nav`, `.navbar`, `header`
- **Traits:** top navigation; brand + links
### Buttons
- **Selectors:** `button`, `.btn`, `a.button`
- **Traits:** primary actions; hover states

## 5. Layout Principles

### Spacing Scale
0–40px (3 steps)

### Border Radius Scale
- `5px`

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `inset 1px 1px 4px rgba(0, 0, 0, 0.25)` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#2d91ea` as the primary accent for CTAs and interactive elements.
- Use `proxima-nova` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

- No explicit media query breakpoints detected — the layout may rely on framework defaults or fluid sizing.

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `site` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** Vivid Blue (`#2d91ea`)
- **CTA / Accent:** Vivid Blue (`#2d91ea`)
- **Border:** Light Gray (`#ebebeb`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.