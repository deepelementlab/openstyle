# Design System: moban2733

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a deep deep vivid red with pale vivid cyan canvas, using Vivid Red as the primary accent for interactive elements. The typography is anchored by `PT Sans`, creating a consistent reading experience. The type scale spans 16px to 16px across 8 levels.

**Key Characteristics:**
- Custom layout structure without explicit framework classes.
- Primary typeface: `PT Sans`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **Deep Vivid Red** (`#4c0e03`): Primary text color
- **Pale Vivid Cyan** (`#dcffff`): Primary surface color
### Accent
- **Vivid Red** (`#ff0000`): CTAs, links, and interactive highlights
- **Vivid Red 2** (`#bc0000`): CTAs, links, and interactive highlights
- **Vivid Amber** (`#ffb900`): CTAs, links, and interactive highlights
- **Deep Vivid Blue** (`#002f50`): CTAs, links, and interactive highlights
- **Deep Vivid Blue 2** (`#003556`): CTAs, links, and interactive highlights
- **Red** (`#a63d56`): CTAs, links, and interactive highlights
### Neutral
- **White** (`#fff`): Structural background
- **Black** (`#000`): Structural background
- **White 2** (`#ffffff`): Structural background
- **Light Gray** (`#ededed`): Structural background
- **Mid Gray** (`#777`): Border and divider color
- **Light Gray 2** (`#dedede`): Structural background
- **Silver** (`#cccccc`): Border and divider color
- **Light Gray 3** (`#EBEBEB`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"PT Sans", sans-serif` (Primary)
- `"Pacifico", cursive`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | PT Sans, sans-serif | 16px | 600 | 2 | 1px |
| Heading | Pacifico, cursive | 16px | normal | 1 | 0.5px |
| Sub-heading | Pacifico, cursive | 16px | 500 | 2.2em | 3px |
| Body | Pacifico, cursive | 16px | bold | 25px | 10px |
| Caption | Pacifico, cursive | 16px | bold | 1.2em | 2px |
| Button | Pacifico, cursive | 16px | bold | 0.75em | 2px |
| Mono | Pacifico, cursive | 16px | bold | 0.75em | 2px |
| Label | Pacifico, cursive | 16px | bold | 0.75em | 2px |

## 4. Component Stylings

### Forms
- **Selectors:** `form`, `input`, `textarea`, `select`
- **Traits:** data input; interactive controls

## 5. Layout Principles

### Spacing Scale
0–12px (12 steps)

### Border Radius Scale
0–50px (4 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `4px 4px 4px #888` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#ff0000` as the primary accent for CTAs and interactive elements.
- Use `PT Sans` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media screen and (max-width: 1366px)`
- `@media screen and (max-width: 1280px)`
- `@media screen and (max-width: 1080px)`
- `@media screen and (max-width: 1050px)`
- `@media screen and (max-width: 991px)`
- `@media screen and (max-width: 900px)`
- `@media screen and (max-width: 800px)`
- `@media screen and (max-width: 768px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `moban2733` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** Deep Vivid Red (`#4c0e03`)
- **CTA / Accent:** Vivid Red (`#ff0000`)
- **Border:** White (`#fff`)
- **Surface:** Pale Vivid Cyan (`#dcffff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.