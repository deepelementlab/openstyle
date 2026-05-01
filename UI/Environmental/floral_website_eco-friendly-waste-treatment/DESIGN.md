# Design System: hdsn 19 industrial

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a deep dark vivid blue with white canvas, using Vivid Blue as the primary accent for interactive elements. The typography is anchored by `-apple-system`, creating a consistent reading experience. The type scale spans 14px to 20px across 8 levels.

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
- **Dark Vivid Blue** (`#02185b`): Primary text color
### Accent
- **Vivid Blue** (`#007bff`): CTAs, links, and interactive highlights
- **Red** (`#dc3545`): CTAs, links, and interactive highlights
- **Green** (`#28a745`): CTAs, links, and interactive highlights
- **Vivid Amber** (`#ffc107`): CTAs, links, and interactive highlights
- **Cyan** (`#17a2b8`): CTAs, links, and interactive highlights
- **Vivid Blue 2** (`rgba(0,123,255,.25)`): CTAs, links, and interactive highlights
### Neutral
- **White** (`#fff`): Structural background
- **Black** (`#000`): Structural background
- **Mid Gray** (`#6c757d`): Border and divider color
- **Deep Muted Blue** (`#212529`): Structural background
- **Pale Muted Blue** (`#dee2e6`): Structural background
- **Pale Muted Blue 2** (`#f8f9fa`): Structural background
- **White 2** (`rgba(255,255,255,.5)`): Structural background
- **Dark Muted Blue** (`#343a40`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol"` (Primary)
- `inherit`
- `SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace`
- `sans-serif`
- `monospace, monospace`
- `"Open Sans", sans-serif`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol | 17px | 400 | 1.5 | normal |
| Heading | inherit | 20px | 700 | 28px | 0 |
| Sub-heading | SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace | 14px | 500 | 1 | 0 |
| Body | sans-serif | 16px | 300 | 1.2 | 0 |
| Caption | monospace, monospace | 16px | normal | inherit | 0 |
| Button | Open Sans, sans-serif | 18px | bold | 0 | 0 |
| Mono | Open Sans, sans-serif | 16px | bold | 0 | 0 |
| Label | Open Sans, sans-serif | 16px | bold | 0 | 0 |

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
| 1 | `0 0 0 0.2rem rgba(0, 123, 255, 0.25)` |
| 2 | `0 0 0 0.2rem rgba(0, 123, 255, 0.5)` |
| 3 | `0 0 0 0.2rem rgba(108, 117, 125, 0.5)` |
| 4 | `0 0 0 0.2rem rgba(40, 167, 69, 0.5)` |
| 5 | `0 0 0 0.2rem rgba(23, 162, 184, 0.5)` |
| 6 | `0 0 0 0.2rem rgba(255, 193, 7, 0.5)` |
| 7 | `0 0 0 0.2rem rgba(220, 53, 69, 0.5)` |
| 8 | `0 0 0 0.2rem rgba(248, 249, 250, 0.5)` |

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
- `@media (min-width:992px)`
- `@media (min-width:768px)`
- `@media (min-width:1200px)`
- `@media screen and (prefers-reduced-motion:reduce)`
- `@media (max-width:575.98px)`
- `@media (max-width:767.98px)`
- `@media (max-width:991.98px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `hdsn 19 industrial` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** Dark Vivid Blue (`#02185b`)
- **CTA / Accent:** Vivid Blue (`#007bff`)
- **Border:** White (`#fff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.