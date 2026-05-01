# Design System: gbts 4 Material Theme

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a black with white canvas, using Soft Red as the primary accent for interactive elements. The typography is anchored by `sans-serif`, creating a consistent reading experience. The type scale spans 13px to 32px across 7 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Row-based section composition present.
- Sectioned page architecture with repeated blocks.
- Primary typeface: `sans-serif`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **White** (`#fff`): Primary surface color
### Accent
- **Soft Red** (`#ee6e73`): CTAs, links, and interactive highlights
- **Vivid Teal** (`#0f9d58`): CTAs, links, and interactive highlights
- **Vivid Cyan** (`#03a9f4`): CTAs, links, and interactive highlights
- **Green** (`#4CAF50`): CTAs, links, and interactive highlights
- **Vivid Blue** (`#0089ec`): CTAs, links, and interactive highlights
- **Light Vivid Blue** (`#b1dcfb`): CTAs, links, and interactive highlights
### Neutral
- **White 2** (`#fff`): Structural background
- **Black** (`#000000`): Structural background
- **White 3** (`#f5f5f5`): Structural background
- **White 4** (`#FFF`): Structural background
- **Light Gray** (`#ddd`): Structural background
- **White 5** (`#ffffff`): Structural background
- **Light Gray 2** (`#e0e0e0`): Structural background
- **Mid Gray** (`#9e9e9e`): Border and divider color
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `sans-serif` (Primary)
- `monospace, monospace`
- `"Material-Design-Icons"`
- `"Roboto", sans-serif`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | sans-serif | 16px | 300 | inherit | -0.3 |
| Heading | monospace, monospace | 32px | 500 | 1.5rem | 0.8px |
| Sub-heading | Material-Design-Icons | 0.0 | 400 | 56px | 0.5px |
| Body | Roboto, sans-serif | 13px | bold | 48px | 0.4 |
| Caption | Roboto, sans-serif | 19px | 100 | 3rem | 0.5 |
| Button | Roboto, sans-serif | 26px | normal | 0 | 7px |
| Mono | Roboto, sans-serif | 16px | normal | 0 | 7px |
| Label | Roboto, sans-serif | 16px | normal | 0 | 7px |

## 4. Component Stylings

### Navigation
- **Selectors:** `nav`, `.navbar`, `header`
- **Traits:** top navigation; brand + links
### Buttons
- **Selectors:** `button`, `.btn`, `a.button`
- **Traits:** primary actions; hover states
### Cards
- **Selectors:** `.card`, `.panel`, `.thumbnail`, `.product`
- **Traits:** content containers

## 5. Layout Principles

### Spacing Scale
0–20px (12 steps)

### Border Radius Scale
0–50px (10 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `none` |
| 2 | `0 2px 5px 0 rgba(0, 0, 0, 0.16), 0 2px 10px 0 rgba(0, 0, 0, 0.12)` |
| 3 | `0 5px 11px 0 rgba(0, 0, 0, 0.18), 0 4px 15px 0 rgba(0, 0, 0, 0.15)` |
| 4 | `0 8px 17px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)` |
| 5 | `0 12px 15px 0 rgba(0, 0, 0, 0.24), 0 17px 50px 0 rgba(0, 0, 0, 0.19)` |
| 6 | `0 16px 28px 0 rgba(0, 0, 0, 0.22), 0 25px 55px 0 rgba(0, 0, 0, 0.21)` |
| 7 | `0 27px 24px 0 rgba(0, 0, 0, 0.2), 0 40px 77px 0 rgba(0, 0, 0, 0.22)` |
| 8 | `0 1px 0 0 #4CAF50` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#ee6e73` as the primary accent for CTAs and interactive elements.
- Use `sans-serif` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media only screen and (max-width : 992px)`
- `@media only screen and (max-width : 600px)`
- `@media only screen and (min-width : 993px)`
- `@media only screen and (min-width : 601px)`
- `@media (min-height: 28.875em)`
- `@media only screen and (min-width: 360px)`
- `@media only screen and (min-width: 390px)`
- `@media only screen and (min-width: 420px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `gbts 4 Material Theme` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** White (`#fff`)
- **CTA / Accent:** Soft Red (`#ee6e73`)
- **Border:** White 2 (`#fff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.