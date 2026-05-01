# Design System: fonts

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a black with silver canvas. The typography is anchored by `themify`, creating a consistent reading experience. The type scale spans 1px to 16px across 3 levels.

**Key Characteristics:**
- Custom layout structure without explicit framework classes.
- Primary typeface: `themify`
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **Black** (`#000`): Primary text color
### Accent
- No distinct color tokens detected in this category.
### Neutral
- **Black 2** (`#000`): Structural background
- **Silver** (`#aaa`): Border and divider color
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"themify"` (Primary)
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | themify | 1.4 | normal | 1 | 1px |
| Heading | themify | 16px | normal | 1 | 1px |
| Sub-heading | themify | 16px | normal | 1 | 1px |

## 4. Component Stylings

- No specific components detected from HTML structure analysis.

## 5. Layout Principles

### Spacing Scale
0–30px (4 steps)

### Border Radius Scale

## 6. Depth & Elevation

- No significant shadow system detected.

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `themify` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

- No explicit media query breakpoints detected — the layout may rely on framework defaults or fluid sizing.

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `fonts` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** Black (`#000`)
- **Border:** Black 2 (`#000`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.