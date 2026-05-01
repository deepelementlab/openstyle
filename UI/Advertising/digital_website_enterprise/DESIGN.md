# Design System: moban4374

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a mid gray with white canvas, using Soft Vivid Blue as the primary accent for interactive elements. The typography is anchored by `Titillium Web`, creating a consistent reading experience. The type scale spans 14px to 30px across 8 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Row-based section composition present.
- Sectioned page architecture with repeated blocks.
- Primary typeface: `Titillium Web`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **White** (`#fff`): Primary surface color
### Accent
- **Soft Vivid Blue** (`#3d60f4`): CTAs, links, and interactive highlights
- **Vivid Blue** (`#007bff`): CTAs, links, and interactive highlights
- **Red** (`#dc3545`): CTAs, links, and interactive highlights
- **Green** (`#28a745`): CTAs, links, and interactive highlights
- **Vivid Amber** (`#ffc107`): CTAs, links, and interactive highlights
- **Cyan** (`#17a2b8`): CTAs, links, and interactive highlights
### Neutral
- **White 2** (`#fff`): Structural background
- **Mid Gray** (`#6c757d`): Border and divider color
- **Deep Muted Blue** (`#212529`): Structural background
- **Pale Muted Blue** (`#dee2e6`): Structural background
- **Pale Muted Blue 2** (`#f8f9fa`): Structural background
- **Dark Muted Blue** (`#343a40`): Structural background
- **Pale Muted Blue 3** (`#e9ecef`): Structural background
- **Black** (`#000`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"Titillium Web", sans-serif` (Primary)
- `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol"`
- `SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace`
- `inherit`
- `"Open Sans", sans-serif`
- `sans-serif`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Titillium Web, sans-serif | 14px | 400 | 1.5 | 0 |
| Heading | -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol | 20px | 700 | 1 | normal |
| Sub-heading | SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace | 14px | 600 | 0 | 0.5px |
| Body | inherit | 16px | 300 | 1.2 | 0.5px |
| Caption | Open Sans, sans-serif | 16px | bolder | 18px | 0.5px |
| Button | sans-serif | 18px | 500 | inherit | 0.5px |
| Mono | sans-serif | 30px | 500 | inherit | 0.5px |
| Label | sans-serif | 16px | 500 | inherit | 0.5px |

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
0–100px (10 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `0 0 40px 0 rgba(0, 0, 0, 0.1)` |
| 2 | `none` |
| 3 | `0 20px 30px 0 rgba(0, 0, 0, 0.08)` |
| 4 | `0 0 0 0.2rem rgba(0, 123, 255, 0.25)` |
| 5 | `0 0 0 0.2rem rgba(0, 123, 255, 0.5)` |
| 6 | `0 0 0 0.2rem rgba(108, 117, 125, 0.5)` |
| 7 | `0 0 0 0.2rem rgba(40, 167, 69, 0.5)` |
| 8 | `0 0 0 0.2rem rgba(23, 162, 184, 0.5)` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#3d60f4` as the primary accent for CTAs and interactive elements.
- Use `Titillium Web` as the base font family to preserve the template's typographic identity.

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
> "Based on the `moban4374` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** White (`#fff`)
- **CTA / Accent:** Soft Vivid Blue (`#3d60f4`)
- **Border:** White 2 (`#fff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.