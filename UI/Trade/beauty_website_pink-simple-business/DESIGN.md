# Design System: cpts 665 cdr

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a white canvas with Pink as the primary accent for interactive elements. The typography is anchored by `Oswald`, creating a consistent reading experience. The type scale spans 12px to 36px across 7 levels.

**Key Characteristics:**
- Custom layout structure without explicit framework classes.
- Primary typeface: `Oswald`
- Accent palette driven by 6 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **White** (`#ffffff`): Primary surface color
### Accent
- **Pink** (`#dd31ae`): CTAs, links, and interactive highlights
- **Vivid Cyan** (`#00c0ff`): CTAs, links, and interactive highlights
- **Dark Muted Pink** (`#45303f`): CTAs, links, and interactive highlights
- **Soft Vivid Cyan** (`#33cdff`): CTAs, links, and interactive highlights
- **Vivid Cyan 2** (`#1ac6ff`): CTAs, links, and interactive highlights
- **Pink 2** (`#d02aa3`): CTAs, links, and interactive highlights
### Neutral
- **White 2** (`#ffffff`): Structural background
- **Mid Gray** (`#939191`): Border and divider color
- **Light Gray** (`#ebebeb`): Structural background
- **Light Gray 2** (`#f1f1f1`): Structural background
- **Silver** (`#b6b6b6`): Border and divider color
- **Light Gray 3** (`#ececec`): Structural background
- **White 3** (`#f5f5f5`): Structural background
- **Light Gray 4** (`#dddddd`): Structural background
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"Oswald", sans-serif` (Primary)
- `"Pontano Sans", sans-serif`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Oswald, sans-serif | 14px | normal | 40px | normal |
| Heading | Pontano Sans, sans-serif | 16px | normal | 80px | normal |
| Sub-heading | Pontano Sans, sans-serif | 22px | normal | 140px | normal |
| Body | Pontano Sans, sans-serif | 18px | normal | 0 | normal |
| Caption | Pontano Sans, sans-serif | 12px | normal | 36px | normal |
| Button | Pontano Sans, sans-serif | 36px | normal | 100px | normal |
| Mono | Pontano Sans, sans-serif | 0.0 | normal | 100px | normal |
| Label | Pontano Sans, sans-serif | 20px | normal | 100px | normal |

## 4. Component Stylings

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
0–30px (9 steps)

### Border Radius Scale

## 6. Depth & Elevation

- No significant shadow system detected.

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#dd31ae` as the primary accent for CTAs and interactive elements.
- Use `Oswald` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

- No explicit media query breakpoints detected — the layout may rely on framework defaults or fluid sizing.

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `cpts 665 cdr` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** White (`#ffffff`)
- **CTA / Accent:** Pink (`#dd31ae`)
- **Border:** White 2 (`#ffffff`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.