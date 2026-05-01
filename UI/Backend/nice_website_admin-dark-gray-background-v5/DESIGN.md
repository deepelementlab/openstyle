# Design System: btzero 15 NiceAdmin

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a white canvas with Muted Teal as the primary accent for interactive elements. The typography is anchored by `Lato`, creating a consistent reading experience. The type scale spans 11px to 20px across 8 levels.

**Key Characteristics:**
- Grid system detected via column classes.
- Row-based section composition present.
- Sectioned page architecture with repeated blocks.
- Primary typeface: `Lato`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **White** (`#fff`): Primary surface color
### Accent
- **Muted Teal** (`#688a7e`): CTAs, links, and interactive highlights
- **Vivid Blue** (`#007aff`): CTAs, links, and interactive highlights
- **Green** (`#4cd964`): CTAs, links, and interactive highlights
- **Blue** (`#428bca`): CTAs, links, and interactive highlights
- **Soft Vivid Red** (`#ff2d55`): CTAs, links, and interactive highlights
- **Cyan** (`#34aadc`): CTAs, links, and interactive highlights
### Neutral
- **White 2** (`#fff`): Structural background
- **White 3** (`#ffffff`): Structural background
- **White 4** (`rgba(255,255,255,0.15)`): Structural background
- **White 5** (`rgba(255, 255, 255, 0.15)`): Structural background
- **Light Gray** (`#ddd`): Structural background
- **Silver** (`#ccc`): Border and divider color
- **Mid Gray** (`#999`): Border and divider color
- **White 6** (`#fafafa`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"Lato", sans-serif` (Primary)
- `inherit`
- `Lato`
- `monospace`
- `"ElegantIcons"`
- `"FontAwesome"`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Lato, sans-serif | 16px | 300 | 1.428571 | 0 |
| Heading | inherit | 12px | normal | 1 | 0 |
| Sub-heading | Lato | 14px | bold | 20px | 0 |
| Body | monospace | 18px | 400 | normal | 0 |
| Caption | ElegantIcons | 13px | 600 | 1.5 | 0 |
| Button | FontAwesome | 11px | 200 | 0 | 0 |
| Mono | FontAwesome | 16px | 200 | 0 | 0 |
| Label | FontAwesome | 20px | 200 | 0 | 0 |

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

## 5. Layout Principles

### Spacing Scale
0–20px (11 steps)

### Border Radius Scale
0–50px (10 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `none` |
| 2 | `inset 0 1px 1px rgba(0, 0, 0, 0.075)` |
| 3 | `0 1px 1px rgba(0, 0, 0, 0.1)` |
| 4 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ffe066` |
| 5 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ff93a8` |
| 6 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #a0ebad` |
| 7 | `0 6px 12px rgba(0, 0, 0, 0.175)` |
| 8 | `inset 0 3px 5px rgba(0, 0, 0, 0.125)` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#688a7e` as the primary accent for CTAs and interactive elements.
- Use `Lato` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media(min-width:768px)`
- `@media (min-width: 768px)`
- `@media(max-width:767px)`
- `@media (max-width: 767px)`
- `@media(min-width:1200px)`
- `@media (min-width: 1200px)`
- `@media(min-width:768px) and (max-width:991px)`
- `@media(min-width:992px) and (max-width:1199px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `btzero 15 NiceAdmin` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** White (`#fff`)
- **CTA / Accent:** Muted Teal (`#688a7e`)
- **Border:** White 2 (`#fff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.