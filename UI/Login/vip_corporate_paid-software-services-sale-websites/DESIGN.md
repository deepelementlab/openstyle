# Design System: wsdp 10 knight

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a vivid yellow with light vivid teal canvas, using Vivid Teal as the primary accent for interactive elements. The typography is anchored by `Inter UI`, creating a consistent reading experience. The type scale spans 14px to 24px across 8 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Row-based section composition present.
- Sectioned page architecture with repeated blocks.
- Primary typeface: `Inter UI`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **Vivid Yellow** (`#ffea00`): Primary surface color
- **Light Vivid Teal** (`#c0f9eb`): Primary surface color
### Accent
- **Vivid Teal** (`#1de9b6`): CTAs, links, and interactive highlights
- **Vivid Red** (`#ff1744`): CTAs, links, and interactive highlights
- **Vivid Teal 2** (`#00e676`): CTAs, links, and interactive highlights
- **Vivid Cyan** (`#00e5ff`): CTAs, links, and interactive highlights
- **Muted Cyan** (`#546E7A`): CTAs, links, and interactive highlights
- **Muted Blue** (`#78909C`): CTAs, links, and interactive highlights
### Neutral
- **White** (`#ffffff`): Structural background
- **Deep Muted Blue** (`#11171a`): Structural background
- **Pale Muted Blue** (`#ECEFF1`): Structural background
- **Black** (`#000000`): Structural background
- **Light Muted Cyan** (`#CFD8DC`): Border and divider color
- **Dark Muted Blue** (`#263238`): Structural background
- **Black 2** (`rgba(0, 0, 0, 0.075)`): Structural background
- **White 2** (`rgba(255, 255, 255, 0.5)`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"Inter UI", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol"` (Primary)
- `inherit`
- `SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace`
- `sans-serif`
- `monospace, monospace`
- `FontAwesome`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Inter UI, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol | 14px | 400 | 1.5 | normal |
| Heading | inherit | 16px | 700 | 1 | normal |
| Sub-heading | SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace | 20px | 500 | inherit | normal |
| Body | sans-serif | 16px | 300 | 0 | normal |
| Caption | monospace, monospace | 16px | 600 | 1.15 | normal |
| Button | FontAwesome | 16px | bolder | 3.5rem | normal |
| Mono | FontAwesome | 24px | bolder | 3.5rem | normal |
| Label | FontAwesome | 16px | bolder | 3.5rem | normal |

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
### Hero
- **Selectors:** `.hero`, `#hero`, `.banner`, `.slider`, `#home`
- **Traits:** intro section; headline + call-to-action

## 5. Layout Principles

### Spacing Scale
0–15px (12 steps)

### Border Radius Scale
0–50px (9 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `none` |
| 2 | `0 0 0 0.2rem rgba(29, 233, 182, 0.5)` |
| 3 | `0 0 0 0.2rem rgba(255, 255, 255, 0.5)` |
| 4 | `0 0 0 0.2rem rgba(0, 230, 118, 0.5)` |
| 5 | `0 0 0 0.2rem rgba(0, 229, 255, 0.5)` |
| 6 | `0 0 0 0.2rem rgba(255, 234, 0, 0.5)` |
| 7 | `0 0 0 0.2rem rgba(255, 23, 68, 0.5)` |
| 8 | `0 0 0 0.2rem rgba(236, 239, 241, 0.5)` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#1de9b6` as the primary accent for CTAs and interactive elements.
- Use `Inter UI` as the base font family to preserve the template's typographic identity.

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
- `@media screen and (prefers-reduced-motion: reduce)`
- `@media (max-width: 767.98px)`
- `@media (max-width: 575.98px)`
- `@media (max-width: 991.98px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `wsdp 10 knight` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** Vivid Yellow (`#ffea00`)
- **CTA / Accent:** Vivid Teal (`#1de9b6`)
- **Border:** White (`#ffffff`)
- **Surface:** Light Vivid Teal (`#c0f9eb`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.