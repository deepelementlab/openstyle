# Design System: moban2398

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a black with white canvas, using Vivid Pink as the primary accent for interactive elements. The typography is anchored by `Open Sans`, creating a consistent reading experience. The type scale spans 12px to 30px across 8 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Row-based section composition present.
- Primary typeface: `Open Sans`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **White** (`#fff`): Primary surface color
### Accent
- **Vivid Pink** (`#ec005f`): CTAs, links, and interactive highlights
- **Blue** (`#337ab7`): CTAs, links, and interactive highlights
- **Soft Vivid Amber** (`rgb(255, 214, 88)`): CTAs, links, and interactive highlights
- **Muted Green** (`#3c763d`): CTAs, links, and interactive highlights
- **Amber** (`#8a6d3b`): CTAs, links, and interactive highlights
- **Red** (`#a94442`): CTAs, links, and interactive highlights
### Neutral
- **White 2** (`#fff`): Structural background
- **Black** (`#000`): Structural background
- **Light Gray** (`#ddd`): Structural background
- **White 3** (`rgba(255,255,255,0.15)`): Structural background
- **Charcoal** (`#333`): Structural background
- **Mid Gray** (`#777`): Border and divider color
- **Light Gray 2** (`#e5e5e5`): Structural background
- **White 4** (`rgb(255, 255, 255)`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"Open Sans"` (Primary)
- `"Open Sans", sans-serif`
- `Arial`
- `"revicons"`
- `Montserrat, Arial, Helvetica, sans-serif`
- `FontAwesome`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Open Sans | 12px | 700 | 1.428571 | 5px |
| Heading | Open Sans, sans-serif | 14px | bold | 40px | normal |
| Sub-heading | Arial | 20px | 300 | 20px | 8px |
| Body | revicons | 18px | normal | 30px | 0 |
| Caption | Montserrat, Arial, Helvetica, sans-serif | 30px | 800 | 60px | 1px |
| Button | FontAwesome | 16px | 400 | 1 | 20px |
| Mono | FontAwesome | 13px | 400 | 1 | 20px |
| Label | FontAwesome | 15px | 400 | 1 | 20px |

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
0–30px (12 steps)

### Border Radius Scale
0–100px (10 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `none` |
| 2 | `0 0 20px 0 rgba(0, 0, 0, 0.15)` |
| 3 | `inset 0 1px 1px rgba(0, 0, 0, 0.075)` |
| 4 | `inset 0 3px 5px rgba(0, 0, 0, 0.125)` |
| 5 | `0 0 20px rgba(0, 0, 0, 0.5)` |
| 6 | `inset 0 -1px 0 rgba(0, 0, 0, 0.25)` |
| 7 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 8px rgba(102, 175, 233, 0.6)` |
| 8 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#ec005f` as the primary accent for CTAs and interactive elements.
- Use `Open Sans` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media (min-width:768px)`
- `@media (max-width:767px)`
- `@media (min-width:1200px)`
- `@media print`
- `@media (min-width:768px) and (max-width:991px)`
- `@media (min-width:992px) and (max-width:1199px)`
- `@media only screen and (min-width: 480px) and (max-width: 767px)`
- `@media only screen and (min-width: 0px) and (max-width: 479px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `moban2398` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** White (`#fff`)
- **CTA / Accent:** Vivid Pink (`#ec005f`)
- **Border:** White 2 (`#fff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.