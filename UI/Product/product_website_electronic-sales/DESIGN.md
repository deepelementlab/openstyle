# Design System: moban3284

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a charcoal with white canvas, using Vivid Orange as the primary accent for interactive elements. The typography is anchored by `Ionicons`, creating a consistent reading experience. The type scale spans 12px to 24px across 8 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Row-based section composition present.
- Primary typeface: `Ionicons`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **White** (`#fff`): Primary surface color
### Accent
- **Vivid Orange** (`#ff6a00`): CTAs, links, and interactive highlights
- **Vivid Red** (`#e40046`): CTAs, links, and interactive highlights
- **Vivid Blue** (`#007bff`): CTAs, links, and interactive highlights
- **Blue** (`#1e56a0`): CTAs, links, and interactive highlights
- **Indigo** (`#613f99`): CTAs, links, and interactive highlights
- **Red** (`#dc3545`): CTAs, links, and interactive highlights
### Neutral
- **White 2** (`#fff`): Structural background
- **Charcoal** (`#333`): Structural background
- **Mid Gray** (`#6c757d`): Border and divider color
- **Light Gray** (`#ebebeb`): Structural background
- **Light Gray 2** (`#ededed`): Structural background
- **Deep Muted Blue** (`#212529`): Structural background
- **Pale Muted Blue** (`#dee2e6`): Structural background
- **Black** (`#000`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"Ionicons"` (Primary)
- `FontAwesome`
- `inherit`
- `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol"`
- `"Montserrat", sans-serif`
- `"Rubik", sans-serif`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Ionicons | 14px | 500 | 1.5 | normal |
| Heading | FontAwesome | 16px | 700 | 1 | 1px |
| Sub-heading | inherit | 12px | 400 | 25px | 0.4px |
| Body | -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol | 18px | 600 | 40px | 10px |
| Caption | Montserrat, sans-serif | 13px | normal | 26px | 10px |
| Button | Rubik, sans-serif | 20px | 300 | 24px | 10px |
| Mono | Rubik, sans-serif | 24px | 300 | 24px | 10px |
| Label | Rubik, sans-serif | 20px | 300 | 24px | 10px |

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
0–40px (12 steps)

### Border Radius Scale
0–100px (10 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `none` |
| 2 | `2px 2px 11px 0 rgba(0, 0, 0, 0.1)` |
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
- Use `#ff6a00` as the primary accent for CTAs and interactive elements.
- Use `Ionicons` as the base font family to preserve the template's typographic identity.

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
- `@media (max-width:575.98px)`
- `@media (max-width:767.98px)`
- `@media (max-width:991.98px)`
- `@media (max-width:1199.98px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `moban3284` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** White (`#fff`)
- **CTA / Accent:** Vivid Orange (`#ff6a00`)
- **Border:** White 2 (`#fff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.