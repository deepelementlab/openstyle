# Design System: cpts 1188 cqo

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a black with yellow canvas, using Yellow as the primary accent for interactive elements. The typography is anchored by `Electrolize`, creating a consistent reading experience. The type scale spans 14px to 16px across 8 levels.

**Key Characteristics:**
- Custom layout structure without explicit framework classes.
- Primary typeface: `Electrolize`
- Accent palette driven by 1 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **Yellow** (`#DFD428`): Primary surface color
### Accent
- **Yellow 2** (`#DFD428`): CTAs, links, and interactive highlights
### Neutral
- **White** (`#FFF`): Structural background
- **Black** (`#000`): Structural background
- **Mid Gray** (`#7c7979`): Border and divider color
- **Mid Gray 2** (`#999`): Border and divider color
- **Charcoal** (`#333`): Structural background
- **Charcoal 2** (`#282A27`): Structural background
- **White 2** (`#ffffff`): Structural background
- **Light Gray** (`#ececec`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"Electrolize", sans-serif` (Primary)
- `Verdana, Geneva, Arial, Helvetica, sans-serif`
- `Arial, Helvetica, sans-serif`
- `verdana, arial, helvetica, helve, sans-serif`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Electrolize, sans-serif | 16px | bold | 1.8em | normal |
| Heading | Verdana, Geneva, Arial, Helvetica, sans-serif | 16px | bold | 0 | normal |
| Sub-heading | Arial, Helvetica, sans-serif | 16px | bold | 1.6em | normal |
| Body | verdana, arial, helvetica, helve, sans-serif | 16px | bold | 1.8 | normal |
| Caption | verdana, arial, helvetica, helve, sans-serif | 16px | bold | 1.8 | normal |
| Button | verdana, arial, helvetica, helve, sans-serif | 16px | bold | 1.8 | normal |
| Mono | verdana, arial, helvetica, helve, sans-serif | 16px | bold | 1.8 | normal |
| Label | verdana, arial, helvetica, helve, sans-serif | 14px | bold | 1.8 | normal |

## 4. Component Stylings

### Navigation
- **Selectors:** `nav`, `.navbar`, `header`
- **Traits:** top navigation; brand + links
### Forms
- **Selectors:** `form`, `input`, `textarea`, `select`
- **Traits:** data input; interactive controls
### Hero
- **Selectors:** `.hero`, `#hero`, `.banner`, `.slider`, `#home`
- **Traits:** intro section; headline + call-to-action

## 5. Layout Principles

### Spacing Scale
0–30px (12 steps)

### Border Radius Scale
5–50px (4 steps)

## 6. Depth & Elevation

- No significant shadow system detected.

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#DFD428` as the primary accent for CTAs and interactive elements.
- Use `Electrolize` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 5 media query breakpoint(s):
- `@media all and (max-width:1024px)`
- `@media all and (max-width:800px)`
- `@media all and (max-width:640px)`
- `@media all and (max-width:480px)`
- `@media all and (max-width:320px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `cpts 1188 cqo` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** Yellow (`#DFD428`)
- **CTA / Accent:** Yellow (`#DFD428`)
- **Border:** White (`#FFF`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.