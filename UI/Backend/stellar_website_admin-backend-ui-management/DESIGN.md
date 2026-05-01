# Design System: dash 4 Stellar

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a deep deep muted blue with light vivid amber canvas, using Cyan as the primary accent for interactive elements. The typography is anchored by `Open Sans`, creating a consistent reading experience. The type scale spans 12px to 20px across 8 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Row-based section composition present.
- Primary typeface: `Open Sans`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **Light Vivid Amber** (`#ffde73`): Primary surface color
### Accent
- **Cyan** (`#1bdbe0`): CTAs, links, and interactive highlights
- **Soft Vivid Red** (`#ff4d6b`): CTAs, links, and interactive highlights
- **Green** (`#38ce3c`): CTAs, links, and interactive highlights
- **Vivid Indigo** (`#8e32e9`): CTAs, links, and interactive highlights
- **Dark Muted Blue** (`#3e4b5b`): CTAs, links, and interactive highlights
- **Vivid Blue** (`#007bff`): CTAs, links, and interactive highlights
### Neutral
- **White** (`#ffffff`): Structural background
- **White 2** (`#fff`): Structural background
- **Pale Muted Blue** (`#e8ecf1`): Structural background
- **Deep Muted Blue** (`#212529`): Structural background
- **Light Gray** (`#d8d8d8`): Border and divider color
- **Pale Muted Blue 2** (`#f8f9fa`): Structural background
- **Mid Gray** (`#6c757d`): Border and divider color
- **Dark Muted Blue 2** (`#343a40`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"Open Sans", sans-serif` (Primary)
- `"simple-line-icons"`
- `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"`
- `SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace`
- `inherit`
- `arial`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Open Sans, sans-serif | 14px | 400 | 1.5 | normal |
| Heading | simple-line-icons | 12px | 600 | 1 | normal |
| Sub-heading | -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, Noto Sans, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji | 20px | 300 | 1.2 | normal |
| Body | SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace | 16px | 700 | inherit | normal |
| Caption | inherit | 16px | bold | 1em | normal |
| Button | arial | 12px | bolder | 24px | normal |
| Mono | arial | 16px | bolder | 24px | normal |
| Label | arial | 13px | bolder | 24px | normal |

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
0–15px (12 steps)

### Border Radius Scale
0–100px (10 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `0 0 0 0.2rem rgba(0, 123, 255, 0.25)` |
| 2 | `none` |
| 3 | `0 0 0 0.2rem rgba(40, 167, 69, 0.25)` |
| 4 | `0 0 0 0.2rem rgba(220, 53, 69, 0.25)` |
| 5 | `0 0 0 0.2rem rgba(27, 219, 224, 0.5)` |
| 6 | `0 0 0 0.2rem rgba(216, 216, 216, 0.5)` |
| 7 | `0 0 0 0.2rem rgba(56, 206, 60, 0.5)` |
| 8 | `0 0 0 0.2rem rgba(142, 50, 233, 0.5)` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#1bdbe0` as the primary accent for CTAs and interactive elements.
- Use `Open Sans` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media (min-width: 576px)`
- `@media (prefers-reduced-motion: reduce)`
- `@media (min-width: 992px)`
- `@media (min-width: 768px)`
- `@media (max-width: 991px)`
- `@media (min-width: 1200px)`
- `@media screen and (max-width: 767px)`
- `@media screen and (max-width: 1199px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `dash 4 Stellar` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** Light Vivid Amber (`#ffde73`)
- **CTA / Accent:** Cyan (`#1bdbe0`)
- **Border:** White (`#ffffff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.