# Design System: bpus 10 showtracker

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a mid gray with white canvas, using Red as the primary accent for interactive elements. The typography is anchored by `-apple-system`, creating a consistent reading experience. The type scale spans 14px to 24px across 8 levels.

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
- **Red** (`#dc3545`): CTAs, links, and interactive highlights
- **Green** (`#28a745`): CTAs, links, and interactive highlights
- **Vivid Indigo** (`#540CFA`): CTAs, links, and interactive highlights
- **Vivid Blue** (`#007bff`): CTAs, links, and interactive highlights
- **Vivid Amber** (`#ffc107`): CTAs, links, and interactive highlights
- **Cyan** (`#17a2b8`): CTAs, links, and interactive highlights
### Neutral
- **White 2** (`#fff`): Structural background
- **Mid Gray** (`#6c757d`): Border and divider color
- **Deep Muted Blue** (`#212529`): Structural background
- **Pale Muted Blue** (`#f8f9fa`): Structural background
- **Dark Muted Blue** (`#343a40`): Structural background
- **Pale Muted Blue 2** (`#dee2e6`): Structural background
- **Pale Muted Blue 3** (`#e9ecef`): Structural background
- **Black** (`rgba(0,0,0,.5)`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol"` (Primary)
- `inherit`
- `SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace`
- `sans-serif`
- `monospace, monospace`
- `"Ionicons"`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol | 14px | 700 | 1.5 | normal |
| Heading | inherit | 16px | 400 | 1.2 | 0.12rem |
| Sub-heading | SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace | 20px | 300 | 1 | 0.12rem |
| Body | sans-serif | 16px | bolder | inherit | 0.12rem |
| Caption | monospace, monospace | 24px | 500 | 0 | 0.12rem |
| Button | Ionicons | 16px | normal | 1.25 | 0.12rem |
| Mono | Ionicons | 16px | normal | 1.25 | 0.12rem |
| Label | Ionicons | 16px | normal | 1.25 | 0.12rem |

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
0–2px (12 steps)

### Border Radius Scale
0–50px (8 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `0 0 0 0.2rem rgba(108, 117, 125, 0.5)` |
| 2 | `0 0 0 0.2rem rgba(40, 167, 69, 0.5)` |
| 3 | `0 0 0 0.2rem rgba(23, 162, 184, 0.5)` |
| 4 | `0 0 0 0.2rem rgba(255, 193, 7, 0.5)` |
| 5 | `0 0 0 0.2rem rgba(220, 53, 69, 0.5)` |
| 6 | `0 0 0 0.2rem rgba(248, 249, 250, 0.5)` |
| 7 | `0 0 0 0.2rem rgba(52, 58, 64, 0.5)` |
| 8 | `0 0 0 0.2rem rgba(0, 123, 255, 0.25)` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#dc3545` as the primary accent for CTAs and interactive elements.
- Use `-apple-system` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media (min-width:576px)`
- `@media (min-width:992px)`
- `@media (max-width: 991.98px)`
- `@media (min-width:768px)`
- `@media (min-width:1200px)`
- `@media screen and (prefers-reduced-motion:reduce)`
- `@media (max-width:575.98px)`
- `@media (max-width:767.98px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `bpus 10 showtracker` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** White (`#fff`)
- **CTA / Accent:** Red (`#dc3545`)
- **Border:** White 2 (`#fff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.