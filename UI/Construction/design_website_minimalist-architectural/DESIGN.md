# Design System: moban2114

## 1. Visual Theme & Atmosphere

This template presents a structured, modular web design built on a deep deep vivid cyan with pale vivid amber canvas, using Light Vivid Amber as the primary accent for interactive elements. The typography is anchored by `Play`, creating a consistent reading experience. The type scale spans 11px to 50px across 8 levels.

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Row-based section composition present.
- Primary typeface: `Play`
- Accent palette driven by 2 distinct highlight colors
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

### Primary
- **Deep Vivid Cyan** (`#002829`): Primary text color
- **Pale Vivid Amber** (`#fff3e0`): Primary surface color
### Accent
- **Light Vivid Amber** (`#ffcc80`): CTAs, links, and interactive highlights
- **Vivid Blue** (`#2196f3`): CTAs, links, and interactive highlights
### Neutral
- **White** (`#fff`): Structural background
- **Charcoal** (`#28292e`): Structural background
- **White 2** (`#fafafa`): Structural background
- **Black** (`#000`): Structural background
- **Dark Gray** (`#616161`): Structural background
- **Black 2** (`rgba(0, 0, 0, 0.25)`): Structural background
- **Silver** (`#ccc`): Border and divider color
- **Mid Gray** (`#93948f`): Border and divider color
### Semantic
- No distinct color tokens detected in this category.

## 3. Typography Rules

### Font Families
- `"Play"` (Primary)
- `"Montserrat"`
- `"Ionicons"`
- `monospace, sans-serif`
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Play | 13px | 700 | 0 | normal |
| Heading | Montserrat | 12px | normal | 30px | normal |
| Sub-heading | Ionicons | 14px | bold | 1 | normal |
| Body | monospace, sans-serif | 50px | 400 | 42px | normal |
| Caption | monospace, sans-serif | 20px | 400 | 20px | normal |
| Button | monospace, sans-serif | 40px | 400 | 24px | normal |
| Mono | monospace, sans-serif | 16px | 400 | 24px | normal |
| Label | monospace, sans-serif | 11px | 400 | 24px | normal |

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
0–100px (12 steps)

### Border Radius Scale
3–5px (2 steps)

## 6. Depth & Elevation

- No significant shadow system detected.

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
- Use `#ffcc80` as the primary accent for CTAs and interactive elements.
- Use `Play` as the base font family to preserve the template's typographic identity.

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

Detected 8 media query breakpoint(s):
- `@media (max-width: 768px)`
- `@media (max-width: 430px)`
- `@media (max-width: 580px)`
- `@media (max-width: 330px)`
- `@media (max-width: 850px)`
- `@media (max-width: 480px)`
- `@media (max-width: 940px)`
- `@media (max-width: 1080px)`

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `moban2114` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
- **Text:** Deep Vivid Cyan (`#002829`)
- **CTA / Accent:** Light Vivid Amber (`#ffcc80`)
- **Border:** White (`#fff`)
- **Surface:** Pale Vivid Amber (`#fff3e0`)

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.