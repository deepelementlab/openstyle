# Design System: wsdp 11 lambda

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a deep dark vivid red with light green canvas, using Vivid Green as the primary accent for interactive elements. The typography is anchored by `Open Sans`, creating a consistent reading experience. The type scale spans 13px to 19px across 8 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Row-based section composition present.
- Sectioned page architecture with repeated blocks.
- Primary typeface: `Open Sans`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **Light Green** (`#a3ecc1`): Primary surface color
- **Dark Vivid Red** (`#a20000`): Primary text color
### Accent
- **Vivid Green** (`#00c853`): CTAs, links, and interactive highlights
- **Vivid Red** (`#d50000`): CTAs, links, and interactive highlights
- **Vivid Yellow** (`#ffd600`): CTAs, links, and interactive highlights
- **Vivid Cyan** (`#00b8d4`): CTAs, links, and interactive highlights
- **Vivid Green 2** (`rgba(0, 200, 83, 0.5)`): CTAs, links, and interactive highlights
- **Dark Vivid Green** (`#00953e`): CTAs, links, and interactive highlights
### Neutral
- **White** (`#ffffff`): Structural background
- **Pale Muted Blue** (`#f8f9fa`): Structural background
- **Deep Muted Blue** (`#212529`): Structural background
- **Dark Gray** (`#495057`): Structural background
- **White 2** (`#fff`): Structural background
- **Black** (`#000000`): Structural background
- **Mid Gray** (`#868e96`): Border and divider color
- **Light Muted Blue** (`#ced4da`): Border and divider color
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"Open Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol"` (Primary)
- `inherit`
- `sans-serif`
- `monospace, monospace`
- `SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace`
- `"FontAwesome"`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Open Sans, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol | 15px | 600 | 1.5 | normal |
| Heading | inherit | 19px | 400 | 1 | normal |
| Sub-heading | sans-serif | 13px | 300 | inherit | normal |
| Body | monospace, monospace | 16px | bolder | 0 | normal |
| Caption | SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace | 14px | 700 | 40px | normal |
| Button | FontAwesome | 16px | 700 | 1.15 | normal |
| Mono | FontAwesome | 16px | 700 | 1.15 | normal |
| Label | FontAwesome | 16px | 700 | 1.15 | normal |

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
### Hero
- **Selectors:** `.hero`, `#hero`, `.banner`, `.slider`, `#home`
- **Traits:** intro section; headline + call-to-action

## 5. Layout Principles

### Spacing Scale
0–15px (12 steps)

### Border Radius Scale
0–50px (8 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `0 0 0 0.2rem rgba(0, 200, 83, 0.5)` |
| 2 | `none` |
| 3 | `0 0 0 0.2rem rgba(255, 255, 255, 0.5)` |
| 4 | `0 0 0 0.2rem rgba(0, 184, 212, 0.5)` |
| 5 | `0 0 0 0.2rem rgba(255, 214, 0, 0.5)` |
| 6 | `0 0 0 0.2rem rgba(213, 0, 0, 0.5)` |
| 7 | `0 0 0 0.2rem rgba(248, 249, 250, 0.5)` |
| 8 | `0 0 0 0.2rem rgba(33, 37, 41, 0.5)` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#00c853` as the primary accent for CTAs and interactive elements.
- Use `Open Sans` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media (min-width: 576px)`
- `@media (min-width: 768px)`
- `@media (min-width: 992px)`
- `@media (min-width: 1200px)`
- `@media (max-width: 575.98px)`
- `@media (max-width: 767.98px)`
- `@media (max-width: 991.98px)`
- `@media (max-width: 1199.98px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `wsdp 11 lambda` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** Light Green (`#a3ecc1`)
- **CTA / Accent:** Vivid Green (`#00c853`)
- **Border:** White (`#ffffff`)
- **Surface:** Dark Vivid Red (`#a20000`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.