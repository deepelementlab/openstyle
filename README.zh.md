<!-- <img width="2493" height="829" alt="Screenshot - 2026-05-01 02 11 35" src="https://github.com/user-attachments/assets/995b7ce4-aba9-4bbe-a26e-6bd1a81f7a50" /> -->
<img width="2220" height="1080" alt="openstyle 00h00m00s-00h00m05s" src="https://github.com/user-attachments/assets/76427503-e6ec-40cd-bc07-6c4d51268946" />


<div align="center">
  
# OpenStyle

</div>

<p align="center">
  <strong>从任意 HTML/CSS 网站模板中自动提取设计令牌，生成结构化的设计规范文档与交互式预览页面。</strong>
</p>

<p align="center">
  <a href="README.md">English</a> |
  <a href="README.zh.md">简体中文</a>
</p>

---

## 概述

OpenStyle 是一个 Python 命令行工具，能够解析 HTML 网站模板中的 CSS 样式表和 DOM 结构，自动识别颜色、字体、间距、圆角、阴影等设计令牌，并输出：

| 输出文件 | 说明 |
|----------|------|
| `DESIGN.md` | 九段式设计规范文档（视觉主题、色板、排版、组件、布局、阴影、最佳实践、响应式、AI 提示词） |
| `preview.html` | 亮色模式交互式设计令牌预览页（颜色、排版、按钮、卡片、表单、间距、圆角、阴影） |
| `preview-dark.html` | 暗色模式交互式设计令牌预览页（自动映射暗色令牌） |
| `README.md` | 英文说明文档（批量模式自动生成） |

### 核心特性

- **颜色语义命名** — 基于 HSL 色彩空间分析，自动为颜色生成语义名称（如 Deep Navy、Vivid Amber、Soft Green）
- **智能暗色模式** — 自动将亮色令牌映射为暗色方案（背景/前景反转、阴影/边框适配）
- **排版层级识别** — 从 CSS 中提取字体族、字号、字重、行高、字间距，并按 Display → Body → Caption 分级
- **组件检测** — 通过 HTML DOM 分析识别导航、按钮、卡片、表单、Hero 等组件模式
- **交互式预览** — 生成的 HTML 预览页包含 Google Fonts、响应式布局、锚点导航
- **多语言翻译** — 支持中文目录名自动翻译为英文 slug（MyMemory / Google 翻译 API，拼音 fallback）
- **批量分类处理** — 按行业/类型自动分类，支持 52 个分类目录

---

## 安装

```bash
cd openstyle
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
```

### 依赖项

| 包名 | 用途 |
|------|------|
| `beautifulsoup4` | HTML DOM 解析与组件检测 |
| `cssutils` | CSS 样式表解析 |
| `jinja2` | 模板渲染（DESIGN.md / preview.html） |
| `colormath` | 色彩空间转换（HSL 分析、亮度计算） |
| `click` | CLI 命令行框架 |
| `deep-translator` | 中文→英文翻译（MyMemory / Google） |
| `pypinyin` | 拼音 fallback（翻译失败时） |
| `pytest` | 单元测试 |

---

## 快速开始

### 单模板分析

```bash
python -m openstyle analyze "E:\OpenStyle\3C数码电子产品网站模板_www.mobancss.com\moban2603"
```

### 指定输出目录

```bash
python -m openstyle analyze "E:\OpenStyle\...\moban2603" -o "E:\OpenStyle\UI"
```

### 批量扫描处理

```bash
# 扫描根目录下所有模板
python -m openstyle batch "E:\OpenStyle" -o "E:\OpenStyle\UI"

# 按 OpenStyle 根目录一级文件夹批量导出（英文目录名 + README）
python -m openstyle batch-openstyle "E:\OpenStyle" -o "E:\OpenStyle\UI" --skip-existing

# 离线模式（不调翻译接口，使用拼音命名）
python -m openstyle batch-openstyle "E:\OpenStyle" -o "E:\OpenStyle\UI" --no-translate
```

### 仅生成预览页

```bash
python -m openstyle preview "E:\OpenStyle\UI\sample\DESIGN.md" -o "E:\OpenStyle\UI\sample"
```

---

## 项目结构

```
openstyle/
├── src/openstyle/
│   ├── __init__.py              # 包入口，导出 OpenStylePipeline
│   ├── __main__.py              # python -m openstyle 入口
│   ├── cli.py                   # Click CLI 命令定义（analyze / batch / batch-openstyle / preview）
│   ├── pipeline.py              # 核心流水线：分析 → 生成 DESIGN.md → 生成 preview
│   ├── models.py                # 数据模型（ColorToken / TypographyToken / DesignTokens / ComponentSpec）
│   ├── naming.py                # 目录名清洗、翻译缓存、拼音转换、slug 去重
│   ├── readme_en.py             # 英文 README 生成器
│   ├── analyzer/
│   │   ├── css_parser.py        # CSS 解析器：颜色、字体、间距、圆角、阴影、媒体查询
│   │   ├── html_parser.py       # HTML 解析器：组件检测、布局推断
│   │   └── color_extractor.py   # 颜色分类器：基于饱和度/亮度自动分 primary/accent/neutral/semantic
│   ├── generators/
│   │   ├── design_md.py         # DESIGN.md 生成器（Jinja2 渲染 + 语义颜色命名）
│   │   ├── preview_html.py      # preview.html 生成器
│   │   └── token_mapper.py      # 令牌映射：HSL 语义命名、暗色模式转换、角色描述生成
│   └── templates/
│       ├── design_template.md   # DESIGN.md Jinja2 模板
│       └── preview_template.html # preview.html Jinja2 模板
├── tests/
│   ├── conftest.py
│   ├── test_pipeline.py
│   └── fixtures/
├── batch_run.py                 # 批量处理脚本（根目录级）
├── batch_category.py            # 分类批量处理脚本
├── requirements.txt
└── README.md
```

---

## 处理流水线

```
HTML 模板目录
    │
    ▼
┌─────────────────────────────┐
│  1. CSS 解析 (CSSParser)     │  ← 提取颜色、字体、间距、圆角、阴影、断点
│  2. HTML 解析 (HTMLParser)   │  ← 检测组件（导航/按钮/卡片/表单/Hero）、布局模式
│  3. 颜色分类 (ColorExtractor)│  ← HSL 分析 → primary / accent / neutral / semantic
└──────────┬──────────────────┘
           │
           ▼
┌─────────────────────────────┐
│  4. 令牌构建 (Pipeline)      │  ← DesignTokens 数据模型
│     - 颜色语义命名           │  ← "Vivid Amber"、"Deep Navy"、"Mid Gray"
│     - 排版层级               │  ← Display → Heading → Body → Caption
│     - 间距/圆角/阴影令牌     │
└──────────┬──────────────────┘
           │
           ▼
┌─────────────────────────────┐
│  5. 输出生成                 │
│     - DESIGN.md (Jinja2)     │  ← 九段式设计规范
│     - preview.html           │  ← 亮色交互预览
│     - preview-dark.html      │  ← 暗色交互预览（自动映射）
│     - README.md              │  ← 英文说明文档
└─────────────────────────────┘
```

---

## 输出目录分类说明

OpenStyle 支持将模板按行业/类型自动分类处理，当前涵盖 **52 个分类**，共 **270+ 套模板设计系统**。

### 分类一览

| 分类 | 英文名 | 说明 | 典型输出示例 |
|------|--------|------|-------------|
| 广告/营销 | `Advertising` | 广告公司、营销推广 | `marketing_agency_digital-promotion` |
| 农业 | `Agriculture` | 农业种植、农产品 | — |
| 动物/宠物 | `Animal` | 宠物店、动物保护 | `pet_shop_animal` |
| APP 应用 | `App` | 移动应用着陆页 | `app_landing_mobile` |
| 汽车 | `Automobile` | 汽车销售、维修保养 | `automotive_website_car-sales` |
| 后台管理 | `Backend` | 管理面板、仪表盘 | `backend_admin_dashboard` |
| 美容美发 | `Beauty` | 美容院、美发沙龙 | `beauty_website_salon` |
| 博客 | `Blog` | 个人博客、内容站 | `blog_website_personal` |
| 品牌展示 | `Brand` | 品牌官网、VI展示 | `brand_website_showcase` |
| 商务咨询 | `Business` | 商务服务、咨询公司 | `business_website_consulting` |
| 卡通风格 | `Cartoon` | 卡通插画、趣味设计 | `cartoon_website_illustration` |
| 公益慈善 | `Charity` | 公益组织、基金会 | `charity_foundation_donation` |
| 企业公司 | `Company` | 企业官网、公司介绍 | `company_website_enterprise` |
| 建筑施工 | `Construction` | 建筑公司、工程施工 | `construction_company_building` |
| 电子商务 | `ECommerce` | 商城、网购平台 | `ecommerce_shop_online-store` |
| 教育培训 | `Education` | 学校、培训机构 | `education_website_training` |
| 数码电子 | `Electronics` | 3C数码、电子产品 | `3c_website` |
| 娱乐休闲 | `Entertainment` | 娱乐场所、休闲活动 | `entertainment_website_club` |
| 环保绿化 | `Environmental` | 环保机构、花卉种植 | `floral_website_garden` |
| 时尚服装 | `Fashion` | 时装设计、服装品牌 | `fashion_company` |
| 影视视频 | `Film` | 电影、视频、影院 | `movie_website_cinema` |
| 餐饮美食 | `Food` | 餐厅、咖啡、美食 | `restaurant_website_food` |
| 家具家装 | `Furniture` | 家具销售、室内设计 | `furniture_website_interior` |
| 游戏 | `Game` | 游戏公司、游戏门户 | `game_company_robo` |
| 医疗健康 | `Healthcare` | 医院、健康服务 | `medical_website_healthcare` |
| 主机域名 | `Hosting` | 主机商、域名注册 | `hosting_website_server` |
| 酒店住宿 | `Hotel` | 酒店、民宿预订 | `hotel_website_booking` |
| 家政保洁 | `Housekeeping` | 家政服务、保洁公司 | `cleaning_company_housekeeping` |
| 投资理财 | `Investment` | 金融投资、理财 | `investment_website_finance` |
| 母婴儿童 | `Kids` | 母婴用品、儿童教育 | `kids_website_baby` |
| 法律律师 | `Law` | 律所、法律咨询 | `legal_website_law-firm` |
| 登录注册 | `Login` | 登录页、注册表单 | `login_website_registration` |
| 物流运输 | `Logistics` | 物流公司、货运 | `logistics_company_shipping` |
| 机械工业 | `Machinery` | 机械制造、工业设备 | `industrial_website_machinery` |
| 音乐 | `Music` | 音乐活动、演唱会 | `music_website_concert` |
| 新闻媒体 | `News` | 新闻门户、媒体网站 | `news_website_portal` |
| 政府/官方 | `Official` | 政府机构、官方网站 | `official_website_government` |
| 其他 | `Other` | 综合类、多用途 | `other_website_general` |
| 摄影 | `Photography` | 摄影工作室、相册 | `photography_website_studio` |
| 门户网站 | `Portal` | 综合门户、导航站 | `portal_website_navigation` |
| 产品展示 | `Product` | 产品介绍、硬件设备 | `product_website_showcase` |
| 房地产 | `RealEstate` | 楼盘、二手房交易 | `villa_market_second-hand` |
| 响应式 | `Responsive` | 通用响应式模板 | `responsive_website_general` |
| 单页 | `SinglePage` | 单页着陆、活动页 | `single_landing_promotion` |
| 体育运动 | `Sports` | 健身房、运动俱乐部 | `fitness_website_gym` |
| 工作室 | `Studio` | 设计工作室、创意团队 | `design_website_studio` |
| 科技 IT | `Technology` | 科技公司、软件开发 | `technology_company_software` |
| 外贸 | `Trade` | 外贸公司、进出口 | `trade_website_export` |
| 培训教育 | `Training` | 培训课程、教育机构 | `training_website_course` |
| 旅游旅行 | `Travel` | 旅行社、旅游攻略 | `travel_agency_tour` |
| 婚庆 | `Wedding` | 婚礼策划、婚纱摄影 | `wedding_website_planning` |
| 女性专题 | `Women` | 女性门户、时尚女性 | `women_website_fashion` |

---

## DESIGN.md 九段式结构

每个生成的 `DESIGN.md` 包含以下九个标准化章节：

| 章节 | 内容 |
|------|------|
| **1. Visual Theme & Atmosphere** | 动态生成的视觉主题描述，包含主色、背景色、字体和排版范围 |
| **2. Color Palette & Roles** | 按 Primary / Accent / Neutral / Semantic 分组，每个颜色带语义名称和角色描述 |
| **3. Typography Rules** | 字体族列表 + 排版层级表（Display → Heading → Body → Caption → Button → Label） |
| **4. Component Stylings** | 从 HTML 检测到的组件（导航、按钮、卡片、表单、Hero）及其选择器和特征 |
| **5. Layout Principles** | 间距标尺和圆角标尺（含汇总摘要） |
| **6. Depth & Elevation** | 阴影层级表 |
| **7. Do's and Don'ts** | 基于提取令牌自动生成的最佳实践建议 |
| **8. Responsive Behavior** | 检测到的媒体查询断点列表 |
| **9. Agent Prompt Guide** | AI 代理快速提示词 + 关键令牌速查 + 迭代检查清单 |

---

## 预览页面特性

生成的 `preview.html` 和 `preview-dark.html` 包含：

- **Google Fonts** — 自动加载 Inter 字体
- **粘性导航栏** — 含锚点链接（Colors / Typography / Buttons / Cards / Forms / Spacing / Radius / Elevation）
- **Hero 区域** — 设计系统标题 + 描述 + 双按钮
- **颜色色板** — 按分组展示，带语义名称和 hex 值，hover 效果
- **排版展示** — 实际字体渲染 + 元数据标签
- **按钮变体** — Primary / Outlined / Ghost 三种样式
- **卡片网格** — 带分类标签的内容卡片
- **表单状态** — Default / Focus / Error 三种输入状态 + Textarea
- **间距可视化** — 柱状图展示间距标尺
- **圆角可视化** — 方块展示不同圆角值
- **阴影展示** — Flat + 多层级阴影卡片
- **Footer** — 品牌信息
- **响应式** — 768px 断点自适应

---

## 批量处理脚本

### batch_run.py — 根目录级批量处理

```bash
cd openstyle
python batch_run.py
```

- 扫描 `e:\OpenStyle` 下的所有一级模板目录
- 自动翻译中文目录名为英文 slug
- 输出到 `e:\OpenStyle\UI\<english-slug>/`

### batch_category.py — 分类批量处理

```bash
cd openstyle
python batch_category.py
```

- 读取 `e:\OpenStyle\UI\input\category\<分类>` 下的模板
- 输出到 `e:\OpenStyle\UI\output\category\<分类>\<english-slug>/`
- 每个输出目录包含 `DESIGN.md` + `preview.html` + `preview-dark.html` + `README.md`

### 目录命名格式

```
{类别}_{站点类型}_{关键词-以连字符分隔}
```

示例：
- `3c_website` ← 3C数码电子产品网站
- `fashion_company` ← FASHION时装设计公司
- `logistics_company_big-things-transportation` ← 大件物流运输公司
- `fitness_website_ever-cool-black-ui-aerobic` ← Ever酷炫黑色有氧健身

---

## 开发测试

```bash
pytest -q
```

测试覆盖：
- 模板分析（令牌提取、颜色分类、排版层级）
- 全流水线生成（DESIGN.md + preview 文件）
- 多模板支持（moban2603 / moban4024）

---

## 技术架构

### 颜色语义命名算法

```python
# 基于 HSL 色彩空间分析
颜色 → RGB → HSL → {
  饱和度 < 10%  → 灰度系列 (White / Light Gray / Silver / Mid Gray / Charcoal / Black)
  饱和度 ≥ 10%  → {
    色相 → 色名 (Red / Orange / Amber / Yellow / Green / Cyan / Blue / Indigo / Purple / Pink)
    亮度 → 前缀 (Deep / Dark / Soft / Light / Pale)
    饱和度 → 前缀 (Muted / Vivid)
  }
}
```

### 暗色模式映射

```python
亮色令牌                    暗色令牌
─────────                  ─────────
--bg: #ffffff         →    --bg: #0f1117
--fg: #171717         →    --fg: #eef0f5
--accent: #0072f5     →    --accent: #0072f5 (保持)
--border: #e0e0e0     →    --border: 自动变暗
--weak: rgba(...)      →    --weak: 自动反转
--surface: #f8fafc    →    --surface: 自动变暗
```

---

## 许可

本项目仅供学习和研究使用。提取的设计令牌来源于公开的 HTML 模板，原始模板版权归原作者所有。
