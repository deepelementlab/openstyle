# Design System: moban3854

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a vivid yellow with silver canvas, using Red as the primary accent for interactive elements. The typography is anchored by `Cabin`, creating a consistent reading experience. The type scale spans 12px to 37px across 7 levels.

**Key Characteristics:**
- Grid system detected via column classes.
- Primary typeface: `Cabin`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **Vivid Yellow** (`#ff0`): Primary surface color
### Accent
- **Red** (`#c03b2b`): CTAs, links, and interactive highlights
- **Mid Gray** (`#6e7784`): CTAs, links, and interactive highlights
- **Red 2** (`#962e22`): CTAs, links, and interactive highlights
- **Dark Red** (`#6d2118`): CTAs, links, and interactive highlights
- **Red 3** (`#9a2f23`): CTAs, links, and interactive highlights
- **Blue** (`#428bca`): CTAs, links, and interactive highlights
### Neutral
- **Silver** (`#9fa5af`): Border and divider color
- **Dark Gray** (`#444a52`): Structural background
- **White** (`#fff`): Structural background
- **Pale Muted Amber** (`#f5f4f0`): Structural background
- **Black** (`#000`): Structural background
- **Light Gray** (`#d1d4d9`): Border and divider color
- **Black 2** (`#1b1d20`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `Cabin, Avenir, "Avenir Next", Trebuchet, Verdana, sans-serif` (Primary)
- `"Playfair Display", Times, serif`
- `monospace, monospace`
- `sans-serif`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Cabin, Avenir, Avenir Next, Trebuchet, Verdana, sans-serif | 16px | 700 | 1.6rem | 1px |
| Heading | Playfair Display, Times, serif | 16px | 400 | inherit | 1px |
| Sub-heading | monospace, monospace | 0.0 | inherit | 1 | 1px |
| Body | sans-serif | 37px | bolder | 1.15 | 1px |
| Caption | sans-serif | 21px | bolder | 0 | 1px |
| Button | sans-serif | 12px | bolder | 0 | 1px |
| Mono | sans-serif | 16px | bolder | 0 | 1px |
| Label | sans-serif | 16px | bolder | 0 | 1px |

## 4. Component Stylings

### Navigation
- **Selectors:** `nav`, `.navbar`, `header`
- **Traits:** top navigation; brand + links
### Hero
- **Selectors:** `.hero`, `#hero`, `.banner`, `.slider`, `#home`
- **Traits:** intro section; headline + call-to-action

## 5. Layout Principles

### Spacing Scale
0–1px (6 steps)

### Border Radius Scale
0–50px (6 steps)

## 6. Depth & Elevation

- No significant shadow system detected.

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#c03b2b` as the primary accent for CTAs and interactive elements.
- Use `Cabin` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 3 media query breakpoint(s):
- `@media screen and (min-width:1200px)`
- `@media screen and (max-width:1200px)`
- `@media screen and (max-width:500px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `moban3854` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** Vivid Yellow (`#ff0`)
- **CTA / Accent:** Red (`#c03b2b`)
- **Border:** Silver (`#9fa5af`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.