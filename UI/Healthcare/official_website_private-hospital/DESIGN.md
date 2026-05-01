# Design System: moban4653

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a charcoal with white canvas, using Teal as the primary accent for interactive elements. The typography is anchored by `Exo`, creating a consistent reading experience. The type scale spans 13px to 36px across 8 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Row-based section composition present.
- Sectioned page architecture with repeated blocks.
- Primary typeface: `Exo`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **White** (`#ffffff`): Primary surface color
### Accent
- **Teal** (`#1cba9f`): CTAs, links, and interactive highlights
- **Dark Blue** (`#223a66`): CTAs, links, and interactive highlights
- **Blue** (`#558DCA`): CTAs, links, and interactive highlights
- **Vivid Blue** (`#007bff`): CTAs, links, and interactive highlights
- **Soft Vivid Red** (`rgba(255, 102, 102, .8)`): CTAs, links, and interactive highlights
- **Red** (`#dc3545`): CTAs, links, and interactive highlights
### Neutral
- **White 2** (`#ffffff`): Structural background
- **White 3** (`#fff`): Structural background
- **White 4** (`rgba(255,255,255,0)`): Structural background
- **Charcoal** (`#222222`): Structural background
- **Black** (`#000`): Structural background
- **Mid Gray** (`#6c757d`): Border and divider color
- **Deep Muted Blue** (`#212529`): Structural background
- **Black 2** (`rgba(0,0,0,0.10)`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"Exo", sans-serif` (Primary)
- `"Lato", sans-serif`
- `"Flaticon"`
- `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol"`
- `"Poppins", sans-serif`
- `SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Exo, sans-serif | 16px | 700 | 1.3em | normal |
| Heading | Lato, sans-serif | 14px | 500 | 1.5 | 1px |
| Sub-heading | Flaticon | 15px | 400 | 1em | -0.02em |
| Body | -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol | 18px | 300 | 1.8em | -0.02em |
| Caption | Poppins, sans-serif | 22px | normal | 1.7em | -0.02em |
| Button | SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace | 13px | 600 | 1 | -0.02em |
| Mono | SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace | 36px | 600 | 1 | -0.02em |
| Label | SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace | 28px | 600 | 1 | -0.02em |

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
0–100px (12 steps)

### Border Radius Scale
0–50px (10 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `none` |
| 2 | `0 0 0 0 rgba(255, 102, 102, 0.8)` |
| 3 | `0 0 0 0.2rem rgba(0, 123, 255, 0.25)` |
| 4 | `0 0 0 0.2rem rgba(0, 123, 255, 0.5)` |
| 5 | `0 0 0 0.2rem rgba(108, 117, 125, 0.5)` |
| 6 | `0 0 0 0.2rem rgba(40, 167, 69, 0.5)` |
| 7 | `0 0 0 0.2rem rgba(23, 162, 184, 0.5)` |
| 8 | `0 0 0 0.2rem rgba(255, 193, 7, 0.5)` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#1cba9f` as the primary accent for CTAs and interactive elements.
- Use `Exo` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media (min-width:576px)`
- `@media (min-width:992px)`
- `@media (min-width:768px)`
- `@media (min-width:1200px)`
- `@media screen and (prefers-reduced-motion:reduce)`
- `@media (max-width:575.98px)`
- `@media (max-width:767.98px)`
- `@media (max-width:991.98px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `moban4653` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** White (`#ffffff`)
- **CTA / Accent:** Teal (`#1cba9f`)
- **Border:** White 2 (`#ffffff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.