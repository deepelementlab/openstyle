# Design System: moban3188

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a black with white canvas, using Vivid Amber as the primary accent for interactive elements. The typography is anchored by `Lato`, creating a consistent reading experience. The type scale spans 12px to 28px across 8 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Row-based section composition present.
- Primary typeface: `Lato`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **Black** (`#1B1B1B`): Primary text color
### Accent
- **Vivid Amber** (`#FA0`): CTAs, links, and interactive highlights
- **Red** (`#C54846`): CTAs, links, and interactive highlights
- **Lime** (`#8EC63F`): CTAs, links, and interactive highlights
- **Blue** (`#2F85D7`): CTAs, links, and interactive highlights
- **Pink** (`#ce4e79`): CTAs, links, and interactive highlights
- **Vivid Yellow** (`#FFD500`): CTAs, links, and interactive highlights
### Neutral
- **Black 2** (`#1B1B1B`): Structural background
- **Charcoal** (`#292929`): Structural background
- **White** (`#FFF`): Structural background
- **White 2** (`#fff`): Structural background
- **White 3** (`rgba(255,255,255,.15)`): Structural background
- **Mid Gray** (`#777`): Border and divider color
- **Silver** (`#AAA`): Border and divider color
- **Light Gray** (`#ddd`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `Lato, Arial, Helvetica, sans-serif` (Primary)
- `sans-serif`
- `"Press Start 2P", "Courier New", cursive`
- `"Glyphicons Halflings"`
- `inherit`
- `Menlo, Monaco, Consolas, "Courier New", monospace`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Lato, Arial, Helvetica, sans-serif | 14px | 400 | 1 | normal |
| Heading | sans-serif | 18px | 700 | 1.428571 | normal |
| Sub-heading | Press Start 2P, Courier New, cursive | 16px | 600 | 1.5 | normal |
| Body | Glyphicons Halflings | 24px | 300 | 1.333333 | normal |
| Caption | inherit | 20px | 500 | 33px | normal |
| Button | Menlo, Monaco, Consolas, Courier New, monospace | 28px | 200 | 45px | normal |
| Mono | Menlo, Monaco, Consolas, Courier New, monospace | 12px | 200 | 45px | normal |
| Label | Menlo, Monaco, Consolas, Courier New, monospace | 16px | 200 | 45px | normal |

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
0–30px (12 steps)

### Border Radius Scale
0–100px (10 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `none` |
| 2 | `inset 0 1px 1px rgba(0, 0, 0, 0.075)` |
| 3 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #5c5c5c` |
| 4 | `inset 0 3px 5px rgba(0, 0, 0, 0.125)` |
| 5 | `inset 0 -1px 0 rgba(0, 0, 0, 0.25)` |
| 6 | `0 6px 12px rgba(0, 0, 0, 0.175)` |
| 7 | `inset 0 1px 0 rgba(255, 255, 255, 0.1)` |
| 8 | `inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1)` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#FA0` as the primary accent for CTAs and interactive elements.
- Use `Lato` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media (min-width:768px)`
- `@media (max-width:767px)`
- `@media (min-width:992px)`
- `@media (min-width:1200px)`
- `@media print`
- `@media (max-width:479px)`
- `@media (max-width:360px)`
- `@media (max-width:1199px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `moban3188` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** Black (`#1B1B1B`)
- **CTA / Accent:** Vivid Amber (`#FA0`)
- **Border:** Black 2 (`#1B1B1B`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.