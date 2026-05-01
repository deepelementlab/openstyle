# Design System: moban4005

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a deep dark vivid blue with white canvas, using Dark Vivid Blue as the primary accent for interactive elements. The typography is anchored by `-apple-system`, creating a consistent reading experience. The type scale spans 14px to 35px across 8 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Row-based section composition present.
- Sectioned page architecture with repeated blocks.
- Primary typeface: `-apple-system`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **Dark Vivid Blue** (`#021b79`): Primary text color
### Accent
- **Dark Vivid Blue 2** (`#02298a`): CTAs, links, and interactive highlights
- **Vivid Blue** (`#0575e6`): CTAs, links, and interactive highlights
- **Vivid Blue 2** (`#0b5eca`): CTAs, links, and interactive highlights
- **Vivid Blue 3** (`#0b47af`): CTAs, links, and interactive highlights
- **Dark Vivid Blue 3** (`#083194`): CTAs, links, and interactive highlights
- **Vivid Orange** (`#fd6c1e`): CTAs, links, and interactive highlights
### Neutral
- **White** (`#ffffff`): Structural background
- **White 2** (`#fff`): Structural background
- **Black** (`#141414`): Structural background
- **Mid Gray** (`#777777`): Border and divider color
- **Mid Gray 2** (`#6c757d`): Border and divider color
- **Deep Muted Blue** (`#212529`): Structural background
- **Pale Muted Blue** (`#dee2e6`): Structural background
- **Light Gray** (`#eeeeee`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"` (Primary)
- `Flaticon`
- `SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace`
- `inherit`
- `"Font Awesome 5 Free"`
- `"slick"`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, Noto Sans, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji | 14px | 600 | 1.5 | normal |
| Heading | Flaticon | 22px | 700 | initial | 0.1em |
| Sub-heading | SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace | 15px | 400 | 1 | 0.1em |
| Body | inherit | 14px | normal | 0 | 0.1em |
| Caption | Font Awesome 5 Free | 16px | 300 | inherit | 0.1em |
| Button | slick | 20px | 500 | 1.2 | 0.1em |
| Mono | slick | 16px | 500 | 1.2 | 0.1em |
| Label | slick | 35px | 500 | 1.2 | 0.1em |

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
0–30px (12 steps)

### Border Radius Scale
0–50px (10 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `unset` |
| 2 | `0 2px 28px 0 rgba(0, 0, 0, 0.06)` |
| 3 | `0 0 0 0.2rem rgba(0, 123, 255, 0.25)` |
| 4 | `0 0 1.25rem rgba(108, 118, 134, 0.1)` |
| 5 | `0 0 0 0.2rem rgba(40, 167, 69, 0.25)` |
| 6 | `0 0 0 0.2rem rgba(220, 53, 69, 0.25)` |
| 7 | `0 0 0 0.2rem rgba(0, 123, 255, 0.5)` |
| 8 | `0 0 0 0.2rem rgba(108, 117, 125, 0.5)` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#02298a` as the primary accent for CTAs and interactive elements.
- Use `-apple-system` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media (prefers-reduced-motion:reduce)`
- `@media (min-width:576px)`
- `@media (min-width:992px)`
- `@media (min-width:1200px)`
- `@media (min-width:768px)`
- `@media (max-width:575.98px)`
- `@media (max-width:767.98px)`
- `@media (max-width:991.98px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `moban4005` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** Dark Vivid Blue (`#021b79`)
- **CTA / Accent:** Dark Vivid Blue (`#02298a`)
- **Border:** White (`#ffffff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.