# Design System: ccps 15 tengxunchanpinfabu

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a vivid yellow with white canvas, using Vivid Blue as the primary accent for interactive elements. The typography is anchored by `icomoon`, creating a consistent reading experience. The type scale spans 14px to 50px across 8 levels.

**Key Characteristics:**
- Sectioned page architecture with repeated blocks.
- Primary typeface: `icomoon`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **Vivid Yellow** (`#fffc00`): Primary surface color
### Accent
- **Vivid Blue** (`#1792fa`): CTAs, links, and interactive highlights
- **Dark Cyan** (`#305d73`): CTAs, links, and interactive highlights
- **Vivid Yellow 2** (`#acb800`): CTAs, links, and interactive highlights
- **Vivid Orange** (`#f67400`): CTAs, links, and interactive highlights
- **Soft Cyan** (`#73bddc`): CTAs, links, and interactive highlights
- **Vivid Blue 2** (`#1541c2`): CTAs, links, and interactive highlights
### Neutral
- **White** (`#fff`): Structural background
- **Black** (`#000`): Structural background
- **Charcoal** (`#333`): Structural background
- **Dark Gray** (`#616161`): Structural background
- **Dark Gray 2** (`#666`): Structural background
- **Light Gray** (`#ededed`): Structural background
- **Silver** (`#c2c2c2`): Border and divider color
- **Charcoal 2** (`#2d2d2d`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `icomoon` (Primary)
- `inherit`
- `"Microsoft Yahei", "ST Heiti", Tahoma, sans-serif`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | icomoon | 14px | 700 | 2em | -0.35em |
| Heading | inherit | 16px | 400 | 1.8em | normal |
| Sub-heading | Microsoft Yahei, ST Heiti, Tahoma, sans-serif | 16px | inherit | 0 | normal |
| Body | Microsoft Yahei, ST Heiti, Tahoma, sans-serif | 16px | 500 | 1em | normal |
| Caption | Microsoft Yahei, ST Heiti, Tahoma, sans-serif | 16px | 500 | 18px | normal |
| Button | Microsoft Yahei, ST Heiti, Tahoma, sans-serif | 16px | 500 | 1.2 | normal |
| Mono | Microsoft Yahei, ST Heiti, Tahoma, sans-serif | 50px | 500 | 1.2 | normal |
| Label | Microsoft Yahei, ST Heiti, Tahoma, sans-serif | 16px | 500 | 1.2 | normal |

## 4. Component Stylings

- No specific components detected from HTML structure analysis.

## 5. Layout Principles

### Spacing Scale
0–40px (12 steps)

### Border Radius Scale

## 6. Depth & Elevation

- No significant shadow system detected.

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#1792fa` as the primary accent for CTAs and interactive elements.
- Use `icomoon` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

- No explicit media query breakpoints detected — the layout may rely on framework defaults or fluid sizing.

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `ccps 15 tengxunchanpinfabu` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** Vivid Yellow (`#fffc00`)
- **CTA / Accent:** Vivid Blue (`#1792fa`)
- **Border:** White (`#fff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.