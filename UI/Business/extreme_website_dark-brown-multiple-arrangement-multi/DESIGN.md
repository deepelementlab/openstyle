# Design System: bigger 6 extreme

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a deep dark vivid red with white canvas, using Light Muted Amber as the primary accent for interactive elements. The typography is anchored by `Georgia`, creating a consistent reading experience. The type scale spans 13px to 40px across 7 levels.

**Key Characteristics:**
- Custom layout structure without explicit framework classes.
- Primary typeface: `Georgia`
- Accent palette driven by 4 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **Dark Vivid Red** (`#990000`): Primary text color
### Accent
- **Light Muted Amber** (`#d8d3bd`): CTAs, links, and interactive highlights
- **Vivid Orange** (`#CC6600`): CTAs, links, and interactive highlights
- **Muted Blue** (`#5f6675`): CTAs, links, and interactive highlights
- **Light Orange** (`#e2d1be`): CTAs, links, and interactive highlights
### Neutral
- **White** (`#fff`): Structural background
- **Black** (`#000`): Structural background
- **Silver** (`#CCC`): Border and divider color
- **Black 2** (`#000000`): Structural background
- **Pale Amber** (`#f6f2e6`): Structural background
- **Charcoal** (`#333`): Structural background
- **Silver 2** (`#ccc`): Border and divider color
- **Silver 3** (`#AAAAAA`): Border and divider color
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `Georgia, "Times New Roman", Times, serif` (Primary)
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Georgia, Times New Roman, Times, serif | 14px | normal | 1.5em | 2px |
| Heading | Georgia, Times New Roman, Times, serif | 13px | bold | 1.5em | 2px |
| Sub-heading | Georgia, Times New Roman, Times, serif | 40px | bold | 1.5em | 2px |
| Body | Georgia, Times New Roman, Times, serif | 24px | bold | 1.5em | 2px |
| Caption | Georgia, Times New Roman, Times, serif | 21px | bold | 1.5em | 2px |
| Button | Georgia, Times New Roman, Times, serif | 18px | bold | 1.5em | 2px |
| Mono | Georgia, Times New Roman, Times, serif | 16px | bold | 1.5em | 2px |
| Label | Georgia, Times New Roman, Times, serif | 0.0 | bold | 1.5em | 2px |

## 4. Component Stylings

- No specific components detected from HTML structure analysis.

## 5. Layout Principles

### Spacing Scale
0–45px (12 steps)

### Border Radius Scale

## 6. Depth & Elevation

- No significant shadow system detected.

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#d8d3bd` as the primary accent for CTAs and interactive elements.
- Use `Georgia` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

- No explicit media query breakpoints detected — the layout may rely on framework defaults or fluid sizing.

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `bigger 6 extreme` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** Dark Vivid Red (`#990000`)
- **CTA / Accent:** Light Muted Amber (`#d8d3bd`)
- **Border:** White (`#fff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.