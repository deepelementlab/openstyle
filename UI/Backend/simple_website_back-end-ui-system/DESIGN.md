# Design System: moban3730

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a deep deep muted blue with white canvas, using Vivid Blue as the primary accent for interactive elements. The typography is anchored by `-apple-system`, creating a consistent reading experience. The type scale spans 11px to 24px across 8 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Row-based section composition present.
- Primary typeface: `-apple-system`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **White** (`#fff`): Primary surface color
### Accent
- **Vivid Blue** (`#007bff`): CTAs, links, and interactive highlights
- **Teal** (`#17c671`): CTAs, links, and interactive highlights
- **Red** (`#c4183c`): CTAs, links, and interactive highlights
- **Vivid Amber** (`#ffb400`): CTAs, links, and interactive highlights
- **Vivid Cyan** (`#00b8d8`): CTAs, links, and interactive highlights
- **Red 2** (`#dc3545`): CTAs, links, and interactive highlights
### Neutral
- **White 2** (`#fff`): Structural background
- **Deep Muted Blue** (`#212529`): Structural background
- **Dark Gray** (`rgba(90,97,105,.1)`): Structural background
- **Mid Gray** (`#6c757d`): Border and divider color
- **Pale Muted Blue** (`#e1e5eb`): Structural background
- **Mid Gray 2** (`#868e96`): Border and divider color
- **Dark Gray 2** (`#5a6169`): Structural background
- **Pale Muted Blue 2** (`#e9ecef`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif` (Primary)
- `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"`
- `SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace`
- `inherit`
- `"Roboto Mono", Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace`
- `Font Awesome\ 5 Brands`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif | 16px | 500 | 1.5 | normal |
| Heading | -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji | 14px | 400 | 1 | -0.0625rem |
| Sub-heading | SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace | 12px | 300 | inherit | 0.0938rem |
| Body | inherit | 20px | 700 | 1.2 | 0.125rem |
| Caption | Roboto Mono, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace | 13px | 900 | 0 | 0.0625rem |
| Button | Font Awesome\ 5 Brands | 11px | bolder | 1.5rem | 3px |
| Mono | Font Awesome\ 5 Brands | 16px | bolder | 1.5rem | 3px |
| Label | Font Awesome\ 5 Brands | 24px | bolder | 1.5rem | 3px |

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
### Forms
- **Selectors:** `form`, `input`, `textarea`, `select`
- **Traits:** data input; interactive controls

## 5. Layout Principles

### Spacing Scale
0–20px (12 steps)

### Border Radius Scale
0–50px (10 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `none` |
| 2 | `inset 0 3px 5px rgba(0, 0, 0, 0.125)` |
| 3 | `0 0.46875rem 2.1875rem rgba(90, 97, 105, 0.1), 0 0.9375rem 1.40625rem rgba(90, 97, 105, 0.1), 0 0.25rem 0.53125rem rgba(90, 97, 105, 0.12), 0 0.125rem 0.1875rem rgba(90, 97, 105, 0.1)` |
| 4 | `0 0.313rem 0.719rem rgba(0, 123, 255, 0.1), 0 0.156rem 0.125rem rgba(0, 0, 0, 0.06)` |
| 5 | `0 3px 15px rgba(90, 97, 105, 0.1), 0 2px 3px rgba(90, 97, 105, 0.2)` |
| 6 | `0 0 0 0.2rem rgba(0, 123, 255, 0.25)` |
| 7 | `0 0 0 0.2rem rgba(0, 123, 255, 0.5)` |
| 8 | `0 0 0 0.2rem rgba(108, 117, 125, 0.5)` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#007bff` as the primary accent for CTAs and interactive elements.
- Use `-apple-system` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media (min-width:576px)`
- `@media screen and (prefers-reduced-motion:reduce)`
- `@media (min-width:992px)`
- `@media (min-width:768px)`
- `@media (min-width:1200px)`
- `@media (max-width:575.98px)`
- `@media (max-width:767.98px)`
- `@media (max-width:991.98px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `moban3730` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** White (`#fff`)
- **CTA / Accent:** Vivid Blue (`#007bff`)
- **Border:** White 2 (`#fff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.