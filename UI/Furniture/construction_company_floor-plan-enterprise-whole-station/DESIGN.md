# Design System: bart 5 ArchiPlus

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a deep dark gray with white canvas, using Soft Indigo as the primary accent for interactive elements. The typography is anchored by `Muli`, creating a consistent reading experience. The type scale spans 12px to 40px across 8 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Row-based section composition present.
- Primary typeface: `Muli`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **White** (`#fff`): Primary surface color
### Accent
- **Soft Indigo** (`#8260E3`): CTAs, links, and interactive highlights
- **Blue** (`#337ab7`): CTAs, links, and interactive highlights
- **Vivid Teal** (`#05CBB8`): CTAs, links, and interactive highlights
- **Muted Green** (`#3c763d`): CTAs, links, and interactive highlights
- **Amber** (`#8a6d3b`): CTAs, links, and interactive highlights
- **Red** (`#a94442`): CTAs, links, and interactive highlights
### Neutral
- **White 2** (`#fff`): Structural background
- **White 3** (`#FFF`): Structural background
- **White 4** (`rgba(255,255,255,.15)`): Structural background
- **Dark Gray** (`#464D50`): Structural background
- **Light Gray** (`#ddd`): Structural background
- **Mid Gray** (`#777`): Border and divider color
- **Charcoal** (`#333`): Structural background
- **Black** (`#000`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `Muli, sans-serif` (Primary)
- `"Source Sans Pro", sans-serif`
- `"Helvetica Neue", Helvetica, Arial, sans-serif`
- `inherit`
- `sans-serif`
- `monospace, monospace`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Muli, sans-serif | 18px | 600 | 1 | -2px |
| Heading | Source Sans Pro, sans-serif | 16px | 400 | 28px | normal |
| Sub-heading | Helvetica Neue, Helvetica, Arial, sans-serif | 40px | 300 | 1.428571 | 1px |
| Body | inherit | 14px | 500 | 1.5 | 1px |
| Caption | sans-serif | 12px | 700 | 1.2 | 1px |
| Button | monospace, monospace | 20px | 800 | 1.333333 | 1px |
| Mono | monospace, monospace | 30px | 800 | 1.333333 | 1px |
| Label | monospace, monospace | 15px | 800 | 1.333333 | 1px |

## 4. Component Stylings

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
0–100px (12 steps)

### Border Radius Scale
0–100px (10 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `none` |
| 2 | `inset 0 1px 1px rgba(0, 0, 0, 0.075)` |
| 3 | `0 10px 30px 0 rgba(5, 203, 184, 0.32)` |
| 4 | `inset 0 3px 5px rgba(0, 0, 0, 0.125)` |
| 5 | `inset 0 -1px 0 rgba(0, 0, 0, 0.25)` |
| 6 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 8px rgba(102, 175, 233, 0.6)` |
| 7 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168` |
| 8 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#8260E3` as the primary accent for CTAs and interactive elements.
- Use `Muli` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media (min-width:768px)`
- `@media (min-width:1200px)`
- `@media (max-width:767px)`
- `@media print`
- `@media (min-width:992px)`
- `@media (min-width:768px) and (max-width:991px)`
- `@media (min-width:992px) and (max-width:1199px)`
- `@media only screen and (max-width:1366px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `bart 5 ArchiPlus` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** White (`#fff`)
- **CTA / Accent:** Soft Indigo (`#8260E3`)
- **Border:** White 2 (`#fff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.