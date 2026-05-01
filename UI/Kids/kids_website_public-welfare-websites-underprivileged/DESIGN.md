# Design System: moban2995

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a white canvas with Vivid Cyan as the primary accent for interactive elements.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Row-based section composition present.
- Sectioned page architecture with repeated blocks.
- Primary typeface: `system-ui`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **White** (`#fff`): Primary surface color
### Accent
- **Vivid Cyan** (`#0AAAA0`): CTAs, links, and interactive highlights
- **Teal** (`#41C3AC`): CTAs, links, and interactive highlights
- **Red** (`#AF4D32`): CTAs, links, and interactive highlights
- **Teal 2** (`#1ABC9C`): CTAs, links, and interactive highlights
- **Blue** (`#3498DB`): CTAs, links, and interactive highlights
- **Purple** (`#9B59B6`): CTAs, links, and interactive highlights
### Neutral
- **White 2** (`#fff`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `system-ui` (Primary)
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | system-ui | 16px | 400 | 1.5 | normal |

## 4. Component Stylings

### Navigation
- **Selectors:** `nav`, `.navbar`, `header`
- **Traits:** top navigation; brand + links
### Buttons
- **Selectors:** `button`, `.btn`, `a.button`
- **Traits:** primary actions; hover states
### Forms
- **Selectors:** `form`, `input`, `textarea`, `select`
- **Traits:** data input; interactive controls

## 5. Layout Principles

### Spacing Scale

### Border Radius Scale

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `0 0 0 3px #0AAAA0 inset` |
| 2 | `0 0 0 3px #41C3AC inset` |
| 3 | `0 0 0 3px #AF4D32 inset` |
| 4 | `0 0 0 3px #1ABC9C inset` |
| 5 | `0 0 0 3px #3498DB inset` |
| 6 | `0 0 0 3px #9B59B6 inset` |
| 7 | `0 0 0 3px #34495E inset` |
| 8 | `0 0 0 3px #E67E22 inset` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#0AAAA0` as the primary accent for CTAs and interactive elements.
- Use `system-ui` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

- No explicit media query breakpoints detected — the layout may rely on framework defaults or fluid sizing.

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `moban2995` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** White (`#fff`)
- **CTA / Accent:** Vivid Cyan (`#0AAAA0`)
- **Border:** White 2 (`#fff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.