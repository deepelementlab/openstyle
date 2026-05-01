# Design System: cpts 1196 xh

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a charcoal with red canvas, using Red as the primary accent for interactive elements. The typography is anchored by `Arial`, creating a consistent reading experience. The type scale spans 13px to 16px across 8 levels.

**Key Characteristics:**
- Grid system detected via column classes.
- Sectioned page architecture with repeated blocks.
- Primary typeface: `Arial`
- Accent palette driven by 3 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **Red** (`#D54F30`): Primary surface color
### Accent
- **Red 2** (`#D54F30`): CTAs, links, and interactive highlights
- **Soft Vivid Red** (`#F75633`): CTAs, links, and interactive highlights
- **Red 3** (`#C94848`): CTAs, links, and interactive highlights
### Neutral
- **White** (`#FFF`): Structural background
- **Charcoal** (`#333`): Structural background
- **Light Gray** (`#D9D9D9`): Structural background
- **White 2** (`#F4F4F4`): Structural background
- **Light Gray 2** (`#F1F1F1`): Structural background
- **Mid Gray** (`#999`): Border and divider color
- **Dark Gray** (`#555`): Structural background
- **Light Gray 3** (`#E0E0E0`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `Arial, Helvetica, sans-serif` (Primary)
- `"AmbleRegular"`
- `"Arial", sans-serif`
- `verdana, arial, helvetica, helve, sans-serif`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Arial, Helvetica, sans-serif | 13px | bold | 1.6em | -1px |
| Heading | AmbleRegular | 16px | normal | 21px | 1px |
| Sub-heading | Arial, sans-serif | 14px | normal | 1.8em | 1px |
| Body | verdana, arial, helvetica, helve, sans-serif | 16px | normal | 18px | 1px |
| Caption | verdana, arial, helvetica, helve, sans-serif | 16px | normal | 18px | 1px |
| Button | verdana, arial, helvetica, helve, sans-serif | 16px | normal | 18px | 1px |
| Mono | verdana, arial, helvetica, helve, sans-serif | 16px | normal | 18px | 1px |
| Label | verdana, arial, helvetica, helve, sans-serif | 16px | normal | 18px | 1px |

## 4. Component Stylings

### Buttons
- **Selectors:** `button`, `.btn`, `a.button`
- **Traits:** primary actions; hover states
### Forms
- **Selectors:** `form`, `input`, `textarea`, `select`
- **Traits:** data input; interactive controls

## 5. Layout Principles

### Spacing Scale
0–20px (12 steps)

### Border Radius Scale
2–5px (4 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `inset 1px 4px 4px rgba(227, 227, 227, 0.5)` |
| 2 | `0 0 15px #E3E3E3` |
| 3 | `0 0 6px #999` |
| 4 | `inset 0 0 3px #999` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#D54F30` as the primary accent for CTAs and interactive elements.
- Use `Arial` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media only screen and (max-width: 1024px)`
- `@media only screen and (max-width: 480px)`
- `@media only screen and (max-width: 640px)`
- `@media only screen and (max-width: 640px) and (min-width: 480px)`
- `@media (max-width:1366px)`
- `@media (max-width:1280px)`
- `@media (max-width:1024px)`
- `@media (max-width:800px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `cpts 1196 xh` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** Red (`#D54F30`)
- **CTA / Accent:** Red (`#D54F30`)
- **Border:** White (`#FFF`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.