# Design System: samples

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a vivid blue with silver canvas, using Vivid Blue as the primary accent for interactive elements. The typography is anchored by `monospace`, creating a consistent reading experience. The type scale spans 10px to 16px across 6 levels.

**Key Characteristics:**
- Custom layout structure without explicit framework classes.
- Primary typeface: `monospace`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **Vivid Blue** (`#0782C1`): Primary text color
### Accent
- **Vivid Blue 2** (`#0782C1`): CTAs, links, and interactive highlights
- **Soft Vivid Orange** (`#FFA54E`): CTAs, links, and interactive highlights
- **Vivid Red** (`#ff0000`): CTAs, links, and interactive highlights
- **Vivid Orange** (`#FF7E00`): CTAs, links, and interactive highlights
- **Orange** (`#DA8028`): CTAs, links, and interactive highlights
- **Orange 2** (`#C97626`): CTAs, links, and interactive highlights
### Neutral
- **Silver** (`#ccc`): Border and divider color
- **Light Gray** (`#ddd`): Structural background
- **White** (`#f3f3f3`): Structural background
- **White 2** (`#fff`): Structural background
- **Black** (`#000000`): Structural background
- **Charcoal** (`#333333`): Structural background
- **White 3** (`#F7F7F7`): Structural background
- **Light Gray 2** (`#D7D7D7`): Border and divider color
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `monospace, monospace` (Primary)
- `Arial, Helvetica, sans-serif`
- `Georgia, Times, "Times New Roman", serif`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | monospace, monospace | 16px | bold | 1.5em | normal |
| Heading | Arial, Helvetica, sans-serif | 16px | normal | 1.5em | normal |
| Sub-heading | Georgia, Times, Times New Roman, serif | 10px | normal | 1.5em | normal |
| Body | Georgia, Times, Times New Roman, serif | 16px | normal | 1.5em | normal |
| Caption | Georgia, Times, Times New Roman, serif | 16px | normal | 1.5em | normal |
| Button | Georgia, Times, Times New Roman, serif | 16px | normal | 1.5em | normal |

## 4. Component Stylings

- No specific components detected from HTML structure analysis.

## 5. Layout Principles

### Spacing Scale
0–40px (11 steps)

### Border Radius Scale
- `3px`

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `0 2px 3px 0 #FFA54E inset` |
| 2 | `inset 0 0 20px 3px #ddd, inset 0 0 1px #000` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#0782C1` as the primary accent for CTAs and interactive elements.
- Use `monospace` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

- No explicit media query breakpoints detected — the layout may rely on framework defaults or fluid sizing.

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `samples` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** Vivid Blue (`#0782C1`)
- **CTA / Accent:** Vivid Blue (`#0782C1`)
- **Border:** Silver (`#ccc`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.