<img width="2493" height="829" alt="Screenshot - 2026-05-01 02 11 35" src="https://github.com/user-attachments/assets/995b7ce4-aba9-4bbe-a26e-6bd1a81f7a50" />

<div align="center">
  
# OpenStyle

</div>


<p align="center">
  <strong>Automated Design System Extractor for HTML Templates. Automatically extract design tokens from any HTML/CSS website template and generate structured design specifications with interactive preview pages.</strong>
</p>

<p align="center">
  <a href="README.md">English</a> |
  <a href="README.zh.md">简体中文</a>
</p>

---

## Overview

OpenStyle is a Python CLI tool that parses CSS stylesheets and DOM structures from HTML website templates, automatically identifies design tokens (colors, typography, spacing, border-radius, shadows), and outputs:

| Output File | Description |
|-------------|-------------|
| `DESIGN.md` | Nine-section design specification (visual theme, color palette, typography, components, layout, elevation, best practices, responsive behavior, AI prompt guide) |
| `preview.html` | Light-mode interactive design token catalog (colors, typography, buttons, cards, forms, spacing, radius, elevation) |
| `preview-dark.html` | Dark-mode interactive design token catalog (auto-mapped dark tokens) |
| `README.md` | English documentation (auto-generated in batch mode) |

### Key Features

- **Semantic Color Naming** — HSL-based analysis generates semantic names (Deep Navy, Vivid Amber, Soft Green)
- **Intelligent Dark Mode** — Auto-maps light tokens to dark scheme (bg/fg inversion, shadow/border adaptation)
- **Typography Hierarchy** — Extracts font families, sizes, weights, line-heights, letter-spacing; classifies as Display → Body → Caption
- **Component Detection** — HTML DOM analysis identifies navigation, buttons, cards, forms, hero sections
- **Interactive Previews** — Generated HTML includes Google Fonts, responsive layout, anchor navigation
- **Multilingual Translation** — Auto-translates Chinese directory names to English slugs (MyMemory / Google API, pinyin fallback)
- **Batch Categorized Processing** — 52 industry/type categories with automatic classification

---

## Installation

```bash
cd openstyle
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
```

### Dependencies

| Package | Purpose |
|---------|---------|
| `beautifulsoup4` | HTML DOM parsing & component detection |
| `cssutils` | CSS stylesheet parsing |
| `jinja2` | Template rendering (DESIGN.md / preview.html) |
| `colormath` | Color space conversion (HSL analysis, luminance calculation) |
| `click` | CLI command framework |
| `deep-translator` | Chinese → English translation (MyMemory / Google) |
| `pypinyin` | Pinyin fallback (when translation fails) |
| `pytest` | Unit testing |

---

## Quick Start

### Single Template Analysis

```bash
python -m openstyle analyze "E:\OpenStyle\3C数码电子产品网站模板_www.mobancss.com\moban2603"
```

### Specify Output Directory

```bash
python -m openstyle analyze "E:\OpenStyle\...\moban2603" -o "E:\OpenStyle\UI"
```

### Batch Processing

```bash
# Scan all templates under root directory
python -m openstyle batch "E:\OpenStyle" -o "E:\OpenStyle\UI"

# Batch export with English directory names + README
python -m openstyle batch-openstyle "E:\OpenStyle" -o "E:\OpenStyle\UI" --skip-existing

# Offline mode (no translation API, pinyin-based naming)
python -m openstyle batch-openstyle "E:\OpenStyle" -o "E:\OpenStyle\UI" --no-translate
```

### Preview Only

```bash
python -m openstyle preview "E:\OpenStyle\UI\sample\DESIGN.md" -o "E:\OpenStyle\UI\sample"
```

---

## Project Structure

```
openstyle/
├── src/openstyle/
│   ├── __init__.py              # Package entry, exports OpenStylePipeline
│   ├── __main__.py              # python -m openstyle entry point
│   ├── cli.py                   # Click CLI commands (analyze / batch / batch-openstyle / preview)
│   ├── pipeline.py              # Core pipeline: analyze → generate DESIGN.md → generate preview
│   ├── models.py                # Data models (ColorToken / TypographyToken / DesignTokens / ComponentSpec)
│   ├── naming.py                # Directory name cleaning, translation cache, pinyin conversion, slug dedup
│   ├── readme_en.py             # English README generator
│   ├── analyzer/
│   │   ├── css_parser.py        # CSS parser: colors, fonts, spacing, radius, shadows, media queries
│   │   ├── html_parser.py       # HTML parser: component detection, layout inference
│   │   └── color_extractor.py   # Color classifier: HSL-based primary/accent/neutral/semantic grouping
│   ├── generators/
│   │   ├── design_md.py         # DESIGN.md generator (Jinja2 rendering + semantic color naming)
│   │   ├── preview_html.py      # preview.html generator
│   │   └── token_mapper.py      # Token mapping: HSL semantic naming, dark mode conversion, role descriptions
│   └── templates/
│       ├── design_template.md   # DESIGN.md Jinja2 template
│       └── preview_template.html # preview.html Jinja2 template
├── tests/
│   ├── conftest.py
│   ├── test_pipeline.py
│   └── fixtures/
├── batch_run.py                 # Batch processing script (root-level)
├── batch_category.py            # Categorized batch processing script
├── requirements.txt
├── README.md                    # Chinese documentation
└── README_EN.md                 # English documentation (this file)
```

---

## Processing Pipeline

```
HTML Template Directory
    │
    ▼
┌─────────────────────────────┐
│  1. CSS Parsing (CSSParser)  │  ← Extract colors, fonts, spacing, radius, shadows, breakpoints
│  2. HTML Parsing (HTMLParser)│  ← Detect components (nav/buttons/cards/forms/hero), layout patterns
│  3. Color Classification     │  ← HSL analysis → primary / accent / neutral / semantic
│     (ColorExtractor)         │
└──────────┬──────────────────┘
           │
           ▼
┌─────────────────────────────┐
│  4. Token Building (Pipeline)│  ← DesignTokens data model
│     - Semantic color naming  │  ← "Vivid Amber", "Deep Navy", "Mid Gray"
│     - Typography hierarchy   │  ← Display → Heading → Body → Caption
│     - Spacing/Radius/Shadow  │
└──────────┬──────────────────┘
           │
           ▼
┌─────────────────────────────┐
│  5. Output Generation        │
│     - DESIGN.md (Jinja2)     │  ← Nine-section design specification
│     - preview.html           │  ← Light-mode interactive preview
│     - preview-dark.html      │  ← Dark-mode interactive preview (auto-mapped)
│     - README.md              │  ← English documentation
└─────────────────────────────┘
```

---

## Category Reference

OpenStyle supports categorized template processing across **52 categories**, covering **270+ template design systems**.

### Full Category List

| Category | Directory Name | Description | Example Output |
|----------|---------------|-------------|----------------|
| Advertising | `Advertising` | Ad agencies, marketing promotions | `marketing_agency_digital-promotion` |
| Agriculture | `Agriculture` | Farming, agricultural products | — |
| Animals & Pets | `Animal` | Pet shops, animal welfare | `pet_shop_animal` |
| App Landing | `App` | Mobile app landing pages | `app_landing_mobile` |
| Automobile | `Automobile` | Car sales, auto repair | `automotive_website_car-sales` |
| Backend / Admin | `Backend` | Admin panels, dashboards | `backend_admin_dashboard` |
| Beauty & Salon | `Beauty` | Beauty salons, hair studios | `beauty_website_salon` |
| Blog | `Blog` | Personal blogs, content sites | `blog_website_personal` |
| Brand Showcase | `Brand` | Brand websites, VI displays | `brand_website_showcase` |
| Business Consulting | `Business` | Business services, consulting firms | `business_website_consulting` |
| Cartoon Style | `Cartoon` | Cartoon illustrations, fun design | `cartoon_website_illustration` |
| Charity | `Charity` | Non-profits, foundations | `charity_foundation_donation` |
| Corporate | `Company` | Company websites, corporate profiles | `company_website_enterprise` |
| Construction | `Construction` | Building companies, engineering | `construction_company_building` |
| E-Commerce | `ECommerce` | Online shops, marketplaces | `ecommerce_shop_online-store` |
| Education | `Education` | Schools, training institutions | `education_website_training` |
| Electronics | `Electronics` | 3C digital, consumer electronics | `3c_website` |
| Entertainment | `Entertainment` | Venues, leisure activities | `entertainment_website_club` |
| Environmental | `Environmental` | Green organizations, floristry | `floral_website_garden` |
| Fashion | `Fashion` | Fashion design, clothing brands | `fashion_company` |
| Film & Video | `Film` | Movies, video production, cinemas | `movie_website_cinema` |
| Food & Restaurant | `Food` | Restaurants, cafés, food & beverage | `restaurant_website_food` |
| Furniture | `Furniture` | Furniture sales, interior design | `furniture_website_interior` |
| Gaming | `Game` | Game studios, gaming portals | `game_company_robo` |
| Healthcare | `Healthcare` | Hospitals, health services | `medical_website_healthcare` |
| Hosting & Domains | `Hosting` | Web hosting, domain registration | `hosting_website_server` |
| Hotel & Hospitality | `Hotel` | Hotels, B&B bookings | `hotel_website_booking` |
| Housekeeping | `Housekeeping` | Cleaning services, maid agencies | `cleaning_company_housekeeping` |
| Investment & Finance | `Investment` | Financial investment, wealth management | `investment_website_finance` |
| Kids & Baby | `Kids` | Baby products, children's education | `kids_website_baby` |
| Law & Legal | `Law` | Law firms, legal consulting | `legal_website_law-firm` |
| Login & Registration | `Login` | Login pages, signup forms | `login_website_registration` |
| Logistics & Shipping | `Logistics` | Logistics companies, freight transport | `logistics_company_shipping` |
| Machinery & Industrial | `Machinery` | Manufacturing, industrial equipment | `industrial_website_machinery` |
| Music | `Music` | Music events, concerts | `music_website_concert` |
| News & Media | `News` | News portals, media sites | `news_website_portal` |
| Official / Government | `Official` | Government agencies, official websites | `official_website_government` |
| Other / General | `Other` | Multi-purpose, general use | `other_website_general` |
| Photography | `Photography` | Photo studios, galleries | `photography_website_studio` |
| Portal | `Portal` | Web portals, directory sites | `portal_website_navigation` |
| Product Showcase | `Product` | Product pages, hardware devices | `product_website_showcase` |
| Real Estate | `RealEstate` | Property listings, real estate agencies | `villa_market_second-hand` |
| Responsive | `Responsive` | General-purpose responsive templates | `responsive_website_general` |
| Single Page | `SinglePage` | Landing pages, campaign pages | `single_landing_promotion` |
| Sports & Fitness | `Sports` | Gyms, sports clubs | `fitness_website_gym` |
| Studio / Creative | `Studio` | Design studios, creative teams | `design_website_studio` |
| Technology & IT | `Technology` | Tech companies, software development | `technology_company_software` |
| Trade / Export | `Trade` | Trading companies, import/export | `trade_website_export` |
| Training & Courses | `Training` | Training programs, educational courses | `training_website_course` |
| Travel & Tourism | `Travel` | Travel agencies, tourism guides | `travel_agency_tour` |
| Wedding | `Wedding` | Wedding planning, bridal photography | `wedding_website_planning` |
| Women's Interest | `Women` | Women's portals, fashion & lifestyle | `women_website_fashion` |

---

## DESIGN.md Nine-Section Structure

Each generated `DESIGN.md` contains nine standardized sections:

| Section | Content |
|---------|---------|
| **1. Visual Theme & Atmosphere** | Dynamically generated visual theme description with primary color, background, fonts, and type scale range |
| **2. Color Palette & Roles** | Colors grouped by Primary / Accent / Neutral / Semantic, each with semantic name and role description |
| **3. Typography Rules** | Font family list + typography hierarchy table (Display → Heading → Body → Caption → Button → Label) |
| **4. Component Stylings** | HTML-detected components (navigation, buttons, cards, forms, hero) with selectors and traits |
| **5. Layout Principles** | Spacing scale and border-radius scale (with summary ranges) |
| **6. Depth & Elevation** | Shadow level table |
| **7. Do's and Don'ts** | Auto-generated best practice recommendations based on extracted tokens |
| **8. Responsive Behavior** | Detected media query breakpoints |
| **9. Agent Prompt Guide** | AI agent quick prompt + key token reference + iteration checklist |

---

## Preview Page Features

Generated `preview.html` and `preview-dark.html` include:

- **Google Fonts** — Auto-loaded Inter typeface
- **Sticky Navigation** — Anchor links (Colors / Typography / Buttons / Cards / Forms / Spacing / Radius / Elevation)
- **Hero Section** — Design system title + description + dual CTA buttons
- **Color Palette** — Grouped swatches with semantic names, hex values, hover effects
- **Typography Showcase** — Actual font rendering with metadata labels
- **Button Variants** — Primary / Outlined / Ghost styles
- **Card Grid** — Content cards with category tags
- **Form States** — Default / Focus / Error input states + Textarea
- **Spacing Visualization** — Bar chart showing spacing scale
- **Radius Visualization** — Squares showing different border-radius values
- **Elevation Showcase** — Flat + multi-level shadow cards
- **Footer** — Brand information
- **Responsive** — 768px breakpoint adaptation

---

## Batch Processing Scripts

### batch_run.py — Root-Level Batch Processing

```bash
cd openstyle
python batch_run.py
```

- Scans all first-level template directories under `e:\OpenStyle`
- Auto-translates Chinese directory names to English slugs
- Outputs to `e:\OpenStyle\UI\<english-slug>/`

### batch_category.py — Categorized Batch Processing

```bash
cd openstyle
python batch_category.py
```

- Reads templates from `e:\OpenStyle\UI\input\category\<Category>/`
- Outputs to `e:\OpenStyle\UI\output\category\<Category>\<english-slug>/`
- Each output directory contains `DESIGN.md` + `preview.html` + `preview-dark.html` + `README.md`

### Directory Naming Convention

```
{category}_{site-type}_{keywords-separated-by-hyphens}
```

Examples:
- `3c_website` ← 3C Digital Electronics Website
- `fashion_company` ← FASHION Fashion Design Company
- `logistics_company_big-things-transportation` ← Large Cargo Transportation Company
- `fitness_website_ever-cool-black-ui-aerobic` ← Ever Cool Black UI Aerobic Fitness

---

## Testing

```bash
pytest -q
```

Test coverage:
- Template analysis (token extraction, color classification, typography hierarchy)
- Full pipeline generation (DESIGN.md + preview files)
- Multi-template support (moban2603 / moban4024)

---

## Technical Architecture

### Semantic Color Naming Algorithm

```python
# HSL color space analysis
Color → RGB → HSL → {
  Saturation < 10%  → Grayscale series (White / Light Gray / Silver / Mid Gray / Charcoal / Black)
  Saturation ≥ 10%  → {
    Hue → Name (Red / Orange / Amber / Yellow / Green / Cyan / Blue / Indigo / Purple / Pink)
    Lightness → Prefix (Deep / Dark / Soft / Light / Pale)
    Saturation → Prefix (Muted / Vivid)
  }
}
```

### Dark Mode Mapping

```python
Light Token                   Dark Token
────────────                  ────────────
--bg: #ffffff           →    --bg: #0f1117
--fg: #171717           →    --fg: #eef0f5
--accent: #0072f5       →    --accent: #0072f5 (preserved)
--border: #e0e0e0       →    --border: auto-darkened
--weak: rgba(...)        →    --weak: auto-inverted
--surface: #f8fafc      →    --surface: auto-darkened
```

---

## License

This project is for learning and research purposes only. Extracted design tokens are derived from publicly available HTML templates. Original template copyrights belong to their respective authors.
