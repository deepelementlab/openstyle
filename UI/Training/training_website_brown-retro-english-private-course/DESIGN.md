# Design System: cpts 610 bbt

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a deep deep muted blue with white canvas, using Orange as the primary accent for interactive elements. The typography is anchored by `Abel`, creating a consistent reading experience. The type scale spans 12px to 18px across 8 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Primary typeface: `Abel`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **Deep Muted Blue** (`#1B242F`): Primary text color
- **Dark Pink** (`#52112F`): Primary text color
- **Dark Pink 2** (`#500F2D`): Primary text color
- **Dark Pink 3** (`#531132`): Primary text color
### Accent
- **Orange** (`#a43d14`): CTAs, links, and interactive highlights
- **Muted Green** (`#3c763d`): CTAs, links, and interactive highlights
- **Amber** (`#8a6d3b`): CTAs, links, and interactive highlights
- **Red** (`#a94442`): CTAs, links, and interactive highlights
- **Cyan** (`#31708f`): CTAs, links, and interactive highlights
- **Soft Muted Orange** (`#A49087`): CTAs, links, and interactive highlights
### Neutral
- **White** (`#fff`): Structural background
- **Light Gray** (`#ddd`): Structural background
- **White 2** (`rgba(255, 255, 255, .15)`): Structural background
- **Mid Gray** (`#999`): Border and divider color
- **Black** (`#000`): Structural background
- **Charcoal** (`#333`): Structural background
- **Black 2** (`rgba(0, 0, 0, .075)`): Structural background
- **White 3** (`#f5f5f5`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"Abel", sans-serif` (Primary)
- `inherit`
- `sans-serif`
- `monospace, monospace`
- `"Helvetica Neue", Helvetica, Arial, sans-serif`
- `Menlo, Monaco, Consolas, "Courier New", monospace`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Abel, sans-serif | 12px | 400 | 1.428571 | 2px |
| Heading | inherit | 16px | normal | 1.8em | 2px |
| Sub-heading | sans-serif | 14px | bold | 1 | 2px |
| Body | monospace, monospace | 18px | 500 | 1.5 | 2px |
| Caption | Helvetica Neue, Helvetica, Arial, sans-serif | 16px | 200 | 1.33 | 2px |
| Button | Menlo, Monaco, Consolas, Courier New, monospace | 16px | 600 | 20px | 2px |
| Mono | Menlo, Monaco, Consolas, Courier New, monospace | 16px | 600 | 20px | 2px |
| Label | Menlo, Monaco, Consolas, Courier New, monospace | 16px | 600 | 20px | 2px |

## 4. Component Stylings

### Forms
- **Selectors:** `form`, `input`, `textarea`, `select`
- **Traits:** data input; interactive controls
### Hero
- **Selectors:** `.hero`, `#hero`, `.banner`, `.slider`, `#home`
- **Traits:** intro section; headline + call-to-action

## 5. Layout Principles

### Spacing Scale
0–20px (12 steps)

### Border Radius Scale
0–50px (10 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `inset 0 1px 1px rgba(0, 0, 0, 0.075)` |
| 2 | `none` |
| 3 | `inset 0 3px 5px rgba(0, 0, 0, 0.125)` |
| 4 | `inset 0 -1px 0 rgba(0, 0, 0, 0.25)` |
| 5 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 8px rgba(102, 175, 233, 0.6)` |
| 6 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168` |
| 7 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b` |
| 8 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#a43d14` as the primary accent for CTAs and interactive elements.
- Use `Abel` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media (min-width: 768px)`
- `@media (max-width: 767px)`
- `@media (min-width: 1200px)`
- `@media print`
- `@media (min-width: 992px)`
- `@media screen and (min-width: 768px)`
- `@media (min-width: 768px) and (max-width: 991px)`
- `@media (min-width: 992px) and (max-width: 1199px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `cpts 610 bbt` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** Deep Muted Blue (`#1B242F`)
- **CTA / Accent:** Orange (`#a43d14`)
- **Border:** White (`#fff`)
- **Surface:** Dark Pink (`#52112F`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.