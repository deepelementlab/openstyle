# Design System: et line font

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design. The typography is anchored by `et-line`, creating a consistent reading experience.

**Key Characteristics:**
- Sectioned page architecture with repeated blocks.
- Primary typeface: `et-line`
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- No distinct color tokens detected in this category.
### Accent
- No distinct color tokens detected in this category.
### Neutral
- No distinct color tokens detected in this category.
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"et-line"` (Primary)
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | et-line | 16px | normal | 1 | normal |

## 4. Component Stylings

### Navigation
- **Selectors:** `nav`, `.navbar`, `header`
- **Traits:** top navigation; brand + links
### Forms
- **Selectors:** `form`, `input`, `textarea`, `select`
- **Traits:** data input; interactive controls

## 5. Layout Principles

### Spacing Scale

### Border Radius Scale

## 6. Depth & Elevation

- No significant shadow system detected.

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `et-line` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

- No explicit media query breakpoints detected — the layout may rely on framework defaults or fluid sizing.

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `et line font` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.