# Design System: cpts 1106 bqn

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a black with light vivid yellow canvas, using Vivid Orange as the primary accent for interactive elements. The typography is anchored by `verdana`, creating a consistent reading experience. The type scale spans 11px to 20px across 8 levels.

**Key Characteristics:**
- Custom layout structure without explicit framework classes.
- Primary typeface: `verdana`
- Accent palette driven by 3 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **Light Vivid Yellow** (`#ff9`): Primary surface color
### Accent
- **Vivid Orange** (`#f40`): CTAs, links, and interactive highlights
- **Vivid Orange 2** (`#f50`): CTAs, links, and interactive highlights
- **Soft Vivid Red** (`#ff5640`): CTAs, links, and interactive highlights
### Neutral
- **Light Gray** (`#eee`): Structural background
- **White** (`#fff`): Structural background
- **Light Gray 2** (`#ddd`): Structural background
- **Mid Gray** (`#9c9c9c`): Border and divider color
- **White 2** (`#f5f5f5`): Structural background
- **Black** (`#000`): Structural background
- **White 3** (`#f3f3f3`): Structural background
- **Light Gray 3** (`#dcdcdc`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `verdana, Arial` (Primary)
- `FontAwesome`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | verdana, Arial | 12px | lighter | 28px | 1px |
| Heading | FontAwesome | 14px | bold | 35px | 5px |
| Sub-heading | FontAwesome | 16px | normal | 30px | 5px |
| Body | FontAwesome | 11px | normal | 40px | 5px |
| Caption | FontAwesome | 15px | normal | 50px | 5px |
| Button | FontAwesome | 16px | normal | 1 | 5px |
| Mono | FontAwesome | 16px | normal | 1 | 5px |
| Label | FontAwesome | 20px | normal | 1 | 5px |

## 4. Component Stylings

### Cards
- **Selectors:** `.card`, `.panel`, `.thumbnail`, `.product`
- **Traits:** content containers
### Forms
- **Selectors:** `form`, `input`, `textarea`, `select`
- **Traits:** data input; interactive controls

## 5. Layout Principles

### Spacing Scale
0–40px (12 steps)

### Border Radius Scale
0–80px (9 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `1px 1px 1px #dfdfdf` |
| 2 | `1px 0 1px #ddd` |
| 3 | `0 2px 2px #eee` |
| 4 | `2px 2px 2px #e1e1e1` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#f40` as the primary accent for CTAs and interactive elements.
- Use `verdana` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

- No explicit media query breakpoints detected — the layout may rely on framework defaults or fluid sizing.

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `cpts 1106 bqn` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** Light Vivid Yellow (`#ff9`)
- **CTA / Accent:** Vivid Orange (`#f40`)
- **Border:** Light Gray (`#eee`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.