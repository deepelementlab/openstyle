# Design System: moban2437

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a black with white canvas, using Green as the primary accent for interactive elements. The typography is anchored by `Playfair Display`, creating a consistent reading experience. The type scale spans 13px to 24px across 8 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Row-based section composition present.
- Primary typeface: `Playfair Display`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **White** (`#fff`): Primary surface color
### Accent
- **Green** (`#5cb85c`): CTAs, links, and interactive highlights
- **Soft Cyan** (`#5bc0de`): CTAs, links, and interactive highlights
- **Vivid Blue** (`#1140c9`): CTAs, links, and interactive highlights
- **Cyan** (`#31b0d5`): CTAs, links, and interactive highlights
- **Green 2** (`#449d44`): CTAs, links, and interactive highlights
- **Vivid Blue 2** (`#0275d8`): CTAs, links, and interactive highlights
### Neutral
- **White 2** (`#fff`): Structural background
- **Black** (`#171717`): Structural background
- **Charcoal** (`#252525`): Structural background
- **Light Gray** (`#eceeef`): Structural background
- **Mid Gray** (`#818a91`): Border and divider color
- **Mid Gray 2** (`#999`): Border and divider color
- **Black 2** (`#000`): Structural background
- **Charcoal 2** (`#444`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `Playfair Display, serif` (Primary)
- `inherit`
- `Work Sans, sans-serif`
- `sans-serif`
- `monospace, monospace`
- `-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Playfair Display, serif | 16px | 500 | 1 | 0.004em |
| Heading | inherit | 20px | 700 | inherit | 0.2em |
| Sub-heading | Work Sans, sans-serif | 15px | 400 | 1.25 | 0.012em |
| Body | sans-serif | 16px | 300 | 0.75em | 0.012em |
| Caption | monospace, monospace | 16px | bolder | 2em | 0.012em |
| Button | -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif | 14px | 100 | 1.2 | 0.012em |
| Mono | -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif | 13px | 100 | 1.2 | 0.012em |
| Label | -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif | 24px | 100 | 1.2 | 0.012em |

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
0–30px (12 steps)

### Border Radius Scale
0–50px (10 steps)

## 6. Depth & Elevation

| Level | Shadow Token |
|-------|-------------|
| 1 | `0 0 0 5px #09f` |
| 2 | `0 10px` |
| 3 | `0 0 20px 0 rgba(0, 0, 0, 0.08)` |
| 4 | `0 0 20px 0 rgba(0, 0, 0, 0.03)` |

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#5cb85c` as the primary accent for CTAs and interactive elements.
- Use `Playfair Display` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media (min-width:576px)`
- `@media (min-width:576px) and (min-width:576px)`
- `@media (min-width:768px) and (min-width:768px)`
- `@media (min-width:992px) and (min-width:992px)`
- `@media (max-width:767px)`
- `@media (min-width:768px)`
- `@media (min-width:992px)`
- `@media (max-width:1199px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `moban2437` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** White (`#fff`)
- **CTA / Accent:** Green (`#5cb85c`)
- **Border:** White 2 (`#fff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.