# Design System: {{ brand_name }}

## 1. Visual Theme & Atmosphere

{{ visual_theme_description }}

**Key Characteristics:**
{% for note in layout_notes %}
- {{ note }}
{% endfor %}
{% if primary_font %}
- Primary typeface: `{{ primary_font }}`
{% endif %}
{% if accent_colors %}
- Accent palette driven by {{ accent_colors | length }} distinct highlight colors
{% endif %}
- Component styles extracted from real CSS declarations — suitable as a foundation for systematic theming and customization

## 2. Color Palette & Roles

{% for section, items in color_sections.items() %}
### {{ section | capitalize }}
{% if items %}
{% for c in items %}
- **{{ c.semantic_name }}** (`{{ c.value }}`): {{ c.description }}
{% endfor %}
{% else %}
- No distinct color tokens detected in this category.
{% endif %}
{% endfor %}

## 3. Typography Rules

{% if typography_rows %}
### Font Families
{% set families = [] %}
{% for row in typography_rows %}
{% if row.family not in families %}
{% if families.append(row.family) %}{% endif %}
{% endif %}
{% endfor %}
{% for fam in families %}
- `{{ fam }}`{% if loop.first %} (Primary){% endif %}

{% endfor %}
### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
{% for row in typography_rows -%}
| {{ row.usage }} | {{ row.family | replace('"', '') }} | {{ "%.0fpx" | format(row.size) if row.size >= 10 else row.size }} | {{ row.weight }} | {{ row.line_height }} | {{ row.letter_spacing }} |
{% endfor %}
{% else %}
- No typography tokens extracted.
{% endif %}

## 4. Component Stylings

{% if components %}
{% for comp in components %}
### {{ comp.name }}
- **Selectors:** `{% for s in comp.selectors %}{{ s }}{% if not loop.last %}`, `{% endif %}{% endfor %}`
- **Traits:** {% for t in comp.traits %}{{ t }}{% if not loop.last %}; {% endif %}{% endfor %}

{% endfor %}
{% else %}
- No specific components detected from HTML structure analysis.
{% endif %}

## 5. Layout Principles

### Spacing Scale
{% if spacing_scale_clean %}
{{ spacing_scale_clean }}
{% else %}
{% for s in spacing_scale %}
- `{{ s }}`
{% endfor %}
{% endif %}

### Border Radius Scale
{% if radius_scale_clean %}
{{ radius_scale_clean }}
{% else %}
{% for r in radius_scale %}
- `{{ r }}`
{% endfor %}
{% endif %}

## 6. Depth & Elevation

{% if shadows %}
| Level | Shadow Token |
|-------|-------------|
{% for sh in shadows -%}
| {{ loop.index }} | `{{ sh }}` |
{% endfor %}
{% else %}
- No significant shadow system detected.
{% endif %}

## 7. Do's and Don'ts

### Do
- Reuse the extracted color and typography tokens for consistency.
- Maintain spacing and radius scale values when building new components.
- Manage interaction states (hover / focus / active) through theme variables.
{% if accent_colors %}
- Use `{{ accent_colors[0].value }}` as the primary accent for CTAs and interactive elements.
{% endif %}
{% if primary_font %}
- Use `{{ primary_font }}` as the base font family to preserve the template's typographic identity.
{% endif %}

### Don't
- Avoid hard-coding arbitrary new color values that break the original palette's coherence.
- Don't mix unrelated font families — keep a unified typographic language.
- Don't reuse light-mode shadow parameters directly in dark mode.

## 8. Responsive Behavior

{% if breakpoints %}
Detected {{ breakpoints | length }} media query breakpoint(s):
{% for bp in breakpoints %}
- `{{ bp }}`
{% endfor %}
{% else %}
- No explicit media query breakpoints detected — the layout may rely on framework defaults or fluid sizing.
{% endif %}

## 9. Agent Prompt Guide

### Quick Prompt
> "Based on the `{{ brand_name }}` design system, use the color palette and typography hierarchy above to generate a modern landing page with navigation, hero section, card grid, and form — output both light and dark themes."

### Key Token Reference
{% if color_sections.get("primary") and color_sections["primary"] %}
- **Text:** {{ color_sections["primary"][0].semantic_name }} (`{{ color_sections["primary"][0].value }}`)
{% endif %}
{% if accent_colors %}
- **CTA / Accent:** {{ accent_colors[0].semantic_name }} (`{{ accent_colors[0].value }}`)
{% endif %}
{% if color_sections.get("neutral") and color_sections["neutral"] %}
- **Border:** {{ color_sections["neutral"][0].semantic_name }} (`{{ color_sections["neutral"][0].value }}`)
{% endif %}
{% if color_sections.get("primary") and color_sections["primary"] | length > 1 %}
- **Surface:** {{ color_sections["primary"][1].semantic_name }} (`{{ color_sections["primary"][1].value }}`)
{% endif %}

### Iteration Checklist
1. Lock down primary / neutral colors first, then extend with accent colors.
2. Use the extracted font sizes and weights to build a heading → body → caption hierarchy.
3. Validate buttons, forms, and cards in both light and dark themes on the preview page.
4. Ensure spacing values follow the detected scale for visual consistency.
