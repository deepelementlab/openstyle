# Design System: moban4576

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a deep dark gray with white canvas, using Green as the primary accent for interactive elements. The typography is anchored by `layui-icon`, creating a consistent reading experience. The type scale spans 12px to 30px across 7 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Primary typeface: `layui-icon`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **White** (`#fff`): Primary surface color
### Accent
- **Green** (`#5FB878`): CTAs, links, and interactive highlights
- **Dark Vivid Teal** (`#009688`): CTAs, links, and interactive highlights
- **Vivid Orange** (`#f7941d`): CTAs, links, and interactive highlights
- **Vivid Red** (`#FF5722`): CTAs, links, and interactive highlights
- **Vivid Amber** (`#FFB800`): CTAs, links, and interactive highlights
- **Vivid Blue** (`#1E9FFF`): CTAs, links, and interactive highlights
### Neutral
- **White 2** (`#fff`): Structural background
- **Mid Gray** (`#999`): Border and divider color
- **Dark Gray** (`#666`): Structural background
- **Light Gray** (`#d2d2d2`): Border and divider color
- **Charcoal** (`#333`): Structural background
- **Light Gray 2** (`#f2f2f2`): Structural background
- **Light Gray 3** (`#e2e2e2`): Structural background
- **Black** (`#000`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `layui-icon` (Primary)
- `"宋体"`
- `"Arial"`
- `inherit`
- `Sim sun`
- `Courier New`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | layui-icon | 14px | 400 | 20px | normal |
| Heading | 宋体 | 12px | bold | 22px | normal |
| Sub-heading | Arial | 0.0 | inherit | 30px | normal |
| Body | inherit | 16px | 300 | 18px | normal |
| Caption | Sim sun | 20px | 500 | 24px | normal |
| Button | Courier New | 30px | 700 | 32px | normal |
| Mono | Courier New | 18px | 700 | 32px | normal |
| Label | Courier New | 24px | 700 | 32px | normal |

## 4. Component Stylings

### Cards
- **Selectors:** `.card`, `.panel`, `.thumbnail`, `.product`
- **Traits:** content containers

## 5. Layout Principles

### Spacing Scale
0–20px (11 steps)

### Border Radius Scale
0–100px (10 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `0 2px 4px rgba(0, 0, 0, 0.12)` |
| 2 | `none` |
| 3 | `0 0 1px #888` |
| 4 | `0 0 5px #999` |
| 5 | `0 1px 2px 0 rgba(0, 0, 0, 0.05)` |
| 6 | `0 -1px 8px rgba(0, 0, 0, 0.08)` |
| 7 | `-1px 0 8px rgba(0, 0, 0, 0.08)` |
| 8 | `1px 1px 20px rgba(0, 0, 0, 0.15)` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#5FB878` as the primary accent for CTAs and interactive elements.
- Use `layui-icon` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 6 media query breakpoint(s):
- `@media screen and (max-width:768px)`
- `@media screen and (min-width:768px)`
- `@media screen and (min-width:992px)`
- `@media screen and (min-width:1200px)`
- `@media screen and (max-width:450px)`
- `@media \0screen`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `moban4576` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** White (`#fff`)
- **CTA / Accent:** Green (`#5FB878`)
- **Border:** White 2 (`#fff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.