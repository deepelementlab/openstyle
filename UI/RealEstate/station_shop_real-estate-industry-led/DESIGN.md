# Design System: apple 11 station shop

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a charcoal with white canvas, using Vivid Cyan as the primary accent for interactive elements. The typography is anchored by `Tahoma`, creating a consistent reading experience. The type scale spans 10px to 30px across 8 levels.

**Key Characteristics:**
- Custom layout structure without explicit framework classes.
- Primary typeface: `Tahoma`
- Accent palette driven by 4 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **White** (`#fff`): Primary surface color
### Accent
- **Vivid Cyan** (`#08aee3`): CTAs, links, and interactive highlights
- **Cyan** (`#21bdd0`): CTAs, links, and interactive highlights
- **Vivid Cyan 2** (`#0ec4f7`): CTAs, links, and interactive highlights
- **Vivid Lime** (`#8fb410`): CTAs, links, and interactive highlights
### Neutral
- **White 2** (`#fff`): Structural background
- **Silver** (`#ccc`): Border and divider color
- **Mid Gray** (`#999`): Border and divider color
- **Charcoal** (`#333`): Structural background
- **Black** (`#000`): Structural background
- **Charcoal 2** (`#222`): Structural background
- **Dark Gray** (`#636363`): Structural background
- **Dark Gray 2** (`#666`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `Tahoma, Geneva, sans-serif` (Primary)
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Tahoma, Geneva, sans-serif | 12px | 700 | 28px | normal |
| Heading | Tahoma, Geneva, sans-serif | 14px | normal | 1.4em | normal |
| Sub-heading | Tahoma, Geneva, sans-serif | 11px | 400 | 24px | normal |
| Body | Tahoma, Geneva, sans-serif | 16px | bold | 26px | normal |
| Caption | Tahoma, Geneva, sans-serif | 10px | bold | 40px | normal |
| Button | Tahoma, Geneva, sans-serif | 30px | bold | 30px | normal |
| Mono | Tahoma, Geneva, sans-serif | 26px | bold | 30px | normal |
| Label | Tahoma, Geneva, sans-serif | 20px | bold | 30px | normal |

## 4. Component Stylings

### Cards
- **Selectors:** `.card`, `.panel`, `.thumbnail`, `.product`
- **Traits:** content containers
### Forms
- **Selectors:** `form`, `input`, `textarea`, `select`
- **Traits:** data input; interactive controls

## 5. Layout Principles

### Spacing Scale
0–50px (12 steps)

### Border Radius Scale

## 6. Depth & Elevation

- No significant shadow system detected.

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#08aee3` as the primary accent for CTAs and interactive elements.
- Use `Tahoma` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

- No explicit media query breakpoints detected — the layout may rely on framework defaults or fluid sizing.

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `apple 11 station shop` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** White (`#fff`)
- **CTA / Accent:** Vivid Cyan (`#08aee3`)
- **Border:** White 2 (`#fff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.