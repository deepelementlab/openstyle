# Design System: moban3554

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a mid gray with white canvas, using Vivid Blue as the primary accent for interactive elements. The typography is anchored by `-apple-system`, creating a consistent reading experience. The type scale spans 13px to 20px across 8 levels.

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
- **White** (`#fff`): Primary surface color
### Accent
- **Vivid Blue** (`#007bff`): CTAs, links, and interactive highlights
- **Red** (`#dc3545`): CTAs, links, and interactive highlights
- **Green** (`#28a745`): CTAs, links, and interactive highlights
- **Vivid Amber** (`#ffc107`): CTAs, links, and interactive highlights
- **Cyan** (`#17a2b8`): CTAs, links, and interactive highlights
- **Soft Vivid Red** (`#f0546a`): CTAs, links, and interactive highlights
### Neutral
- **White 2** (`#fff`): Structural background
- **Mid Gray** (`#6c757d`): Border and divider color
- **Deep Muted Blue** (`#212529`): Structural background
- **Pale Muted Blue** (`#f8f9fa`): Structural background
- **Black** (`#000`): Structural background
- **Dark Muted Blue** (`#343a40`): Structural background
- **Pale Muted Blue 2** (`#dee2e6`): Structural background
- **Pale Muted Blue 3** (`#e9ecef`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol"` (Primary)
- `inherit`
- `"Oxygen", sans-serif`
- `"Lato", sans-serif`
- `sans-serif`
- `monospace, monospace`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol | 15px | 600 | 1.5 | 1px |
| Heading | inherit | 20px | 400 | 1 | 2px |
| Sub-heading | Oxygen, sans-serif | 14px | 700 | inherit | normal |
| Body | Lato, sans-serif | 16px | 300 | 1.2 | 4px |
| Caption | sans-serif | 16px | 500 | 0 | 0.5px |
| Button | monospace, monospace | 14px | bold | 1.15 | 0.5px |
| Mono | monospace, monospace | 16px | bold | 1.15 | 0.5px |
| Label | monospace, monospace | 13px | bold | 1.15 | 0.5px |

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
### Hero
- **Selectors:** `.hero`, `#hero`, `.banner`, `.slider`, `#home`
- **Traits:** intro section; headline + call-to-action

## 5. Layout Principles

### Spacing Scale
0–14px (12 steps)

### Border Radius Scale
0–50px (8 steps)

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
- `@media (min-width: 576px)`
- `@media (min-width: 992px)`
- `@media (min-width: 768px)`
- `@media (min-width: 1200px)`
- `@media(max-width: 991px)`
- `@media(max-width: 768px)`
- `@media (max-width: 575.98px)`
- `@media (max-width: 767.98px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `moban3554` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** White (`#fff`)
- **CTA / Accent:** Vivid Blue (`#007bff`)
- **Border:** White 2 (`#fff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.