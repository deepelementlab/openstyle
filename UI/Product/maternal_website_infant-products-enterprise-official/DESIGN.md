# Design System: moban3873

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a black with white canvas, using Soft Cyan as the primary accent for interactive elements. The typography is anchored by `Fredericka the Great`, creating a consistent reading experience. The type scale spans 14px to 45px across 7 levels.

**Key Characteristics:**
- Grid system detected via column classes.
- Row-based section composition present.
- Sectioned page architecture with repeated blocks.
- Primary typeface: `Fredericka the Great`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **White** (`#ffffff`): Primary surface color
### Accent
- **Soft Cyan** (`#4cb6ea`): CTAs, links, and interactive highlights
- **Soft Red** (`#E0768C`): CTAs, links, and interactive highlights
- **Cyan** (`#2FBFCA`): CTAs, links, and interactive highlights
- **Soft Vivid Red** (`#fc5b78`): CTAs, links, and interactive highlights
- **Vivid Yellow** (`#E8D01D`): CTAs, links, and interactive highlights
- **Green** (`#17AD4A`): CTAs, links, and interactive highlights
### Neutral
- **White 2** (`#ffffff`): Structural background
- **White 3** (`#fff`): Structural background
- **Black** (`#000000`): Structural background
- **Light Gray** (`#eee`): Structural background
- **Charcoal** (`#333`): Structural background
- **Charcoal 2** (`#3F3F3F`): Structural background
- **Dark Gray** (`#666`): Structural background
- **Black 2** (`#000`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"Fredericka the Great", cursive` (Primary)
- `"Open Sans", sans-serif`
- `"Source Sans Pro", sans-serif`
- `FontAwesome`
- `"PT Sans", sans-serif`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Fredericka the Great, cursive | 16px | bold | 0 | -1px |
| Heading | Open Sans, sans-serif | 20px | normal | 1.2 | 0 |
| Sub-heading | Source Sans Pro, sans-serif | 0.0 | 500 | 1 | 1px |
| Body | FontAwesome | 16px | 900 | 30px | 1px |
| Caption | PT Sans, sans-serif | 14px | 400 | 20px | 1px |
| Button | PT Sans, sans-serif | 16px | 700 | 16px | 1px |
| Mono | PT Sans, sans-serif | 25px | 700 | 16px | 1px |
| Label | PT Sans, sans-serif | 45px | 700 | 16px | 1px |

## 4. Component Stylings

### Buttons
- **Selectors:** `button`, `.btn`, `a.button`
- **Traits:** primary actions; hover states

## 5. Layout Principles

### Spacing Scale
0–60px (12 steps)

### Border Radius Scale
0–50px (6 steps)

## 6. Depth & Elevation

- No significant shadow system detected.

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#4cb6ea` as the primary accent for CTAs and interactive elements.
- Use `Fredericka the Great` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 4 media query breakpoint(s):
- `@media only screen and (min-width: 960px) and (max-width: 1199px)`
- `@media only screen and (min-width: 768px) and (max-width: 959px)`
- `@media only screen and (max-width: 767px)`
- `@media all and (max-width: 800px), only screen and (-webkit-min-device-pixel-ratio: 2) and (max-width: 1024px), only screen and (min--moz-device-pixel-ratio: 2) and (max-width: 1024px), only screen and (-o-min-device-pixel-ratio: 2/1) and (max-width: 1024px), only screen and (min-device-pixel-ratio: 2) and (max-width: 1024px), only screen and (min-resolution: 192dpi) and (max-width: 1024px), only screen and (min-resolution: 2dppx) and (max-width: 1024px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `moban3873` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** White (`#ffffff`)
- **CTA / Accent:** Soft Cyan (`#4cb6ea`)
- **Border:** White 2 (`#ffffff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.