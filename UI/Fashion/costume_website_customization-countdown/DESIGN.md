# Design System: moban2904

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a vivid red with pale vivid cyan canvas, using Vivid Red as the primary accent for interactive elements. The typography is anchored by `PT Sans`, creating a consistent reading experience. The type scale spans 16px to 16px across 8 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Primary typeface: `PT Sans`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **Pale Vivid Cyan** (`#dcffff`): Primary surface color
- **Vivid Red** (`#A80000`): Primary text color
### Accent
- **Vivid Red 2** (`#ff0000`): CTAs, links, and interactive highlights
- **Vivid Red 3** (`#bc0000`): CTAs, links, and interactive highlights
- **Blue** (`#223f99`): CTAs, links, and interactive highlights
- **Dark Blue** (`rgba(47, 40, 88, 0.3686274509803922)`): CTAs, links, and interactive highlights
- **Blue 2** (`rgba(34, 63, 153, 0.17)`): CTAs, links, and interactive highlights
- **Vivid Red 4** (`#BC0000`): CTAs, links, and interactive highlights
### Neutral
- **White** (`#fff`): Structural background
- **White 2** (`#ffffff`): Structural background
- **Light Gray** (`#ededed`): Structural background
- **Mid Gray** (`#777`): Border and divider color
- **Black** (`#000`): Structural background
- **Light Gray 2** (`#dedede`): Structural background
- **White 3** (`#fdfdfd`): Structural background
- **Black 2** (`rgba(0, 0, 0, 0.4)`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"PT Sans", sans-serif` (Primary)
- `"Great Vibes", cursive`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | PT Sans, sans-serif | 16px | 600 | 2em | 1px |
| Heading | Great Vibes, cursive | 16px | 500 | 1.5 | 3px |
| Sub-heading | Great Vibes, cursive | 16px | normal | 0.75em | 4px |
| Body | Great Vibes, cursive | 16px | bold | inherit | 0.5px |
| Caption | Great Vibes, cursive | 16px | bold | 1.2em | 2px |
| Button | Great Vibes, cursive | 16px | bold | 1.2em | 2px |
| Mono | Great Vibes, cursive | 16px | bold | 1.2em | 2px |
| Label | Great Vibes, cursive | 16px | bold | 1.2em | 2px |

## 4. Component Stylings

### Forms
- **Selectors:** `form`, `input`, `textarea`, `select`
- **Traits:** data input; interactive controls

## 5. Layout Principles

### Spacing Scale
0–10px (12 steps)

### Border Radius Scale
0–19px (3 steps)

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
- `@media screen and (max-width: 1050px)`
- `@media screen and (max-width: 991px)`
- `@media screen and (max-width: 800px)`
- `@media screen and (max-width: 768px)`
- `@media screen and (max-width: 667px)`
- `@media screen and (max-width: 600px)`
- `@media screen and (max-width: 568px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `moban2904` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** Pale Vivid Cyan (`#dcffff`)
- **CTA / Accent:** Vivid Red (`#ff0000`)
- **Border:** White (`#fff`)
- **Surface:** Vivid Red (`#A80000`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.