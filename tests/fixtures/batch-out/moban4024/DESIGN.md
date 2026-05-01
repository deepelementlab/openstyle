# Design System: moban4024

## 1. Visual Theme & Atmosphere

该模板呈现出以结构化模块为核心的网页风格，页面由多个内容分区组成，并通过清晰的导航、标题和行动按钮建立信息层级。整体视觉基调偏向实用型商业站点，强调可读性与组件复用。

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Row-based section composition present.
- 组件风格由模板内真实 CSS 规则提取，适合作为二次主题化与系统化改造基础。

## 2. Color Palette & Roles

### Primary
- **#fcf8e3** (`#fcf8e3`): 用途分组 `primary`，出现频次约 8。
### Accent
- **#337ab7** (`#337ab7`): 用途分组 `accent`，出现频次约 25。
- **#1d2f3b** (`#1d2f3b`): 用途分组 `accent`，出现频次约 15。
- **#3c763d** (`#3c763d`): 用途分组 `accent`，出现频次约 14。
- **#8a6d3b** (`#8a6d3b`): 用途分组 `accent`，出现频次约 14。
- **#a94442** (`#a94442`): 用途分组 `accent`，出现频次约 14。
- **#d9534f** (`#d9534f`): 用途分组 `accent`，出现频次约 11。
### Neutral
- **#fff** (`#fff`): 用途分组 `neutral`，出现频次约 116。
- **rgba(255, 255, 255, 0.15)** (`rgba(255, 255, 255, 0.15)`): 用途分组 `neutral`，出现频次约 45。
- **#000** (`#000`): 用途分组 `neutral`，出现频次约 36。
- **#ddd** (`#ddd`): 用途分组 `neutral`，出现频次约 30。
- **#777777** (`#777777`): 用途分组 `neutral`，出现频次约 17。
- **#333** (`#333`): 用途分组 `neutral`，出现频次约 16。
- **rgba(0, 0, 0, 0.075)** (`rgba(0, 0, 0, 0.075)`): 用途分组 `neutral`，出现频次约 16。
- **#eeeeee** (`#eeeeee`): 用途分组 `neutral`，出现频次约 14。
### Semantic
- 无明显颜色令牌。

## 3. Typography Rules

| Role | Font | Size(px) | Weight | Line Height | Letter Spacing |
|------|------|----------|--------|-------------|----------------|
| Display | "Josefin Slab", Arial, serif | 12.0 | normal | 1.42857 | normal |
| Heading | "Helvetica Neue", Helvetica, Arial, sans-serif | 18.0 | bold | 1.5 | 3px |
| Sub-heading | "Sacramento", cursive | 14.0 | 700 | 1 | 0 |
| Body | "icomoon" | 20.0 | 400 | 0 | 2px |
| Caption | inherit | 16.0 | 300 | 1.33333 | 2px |
| Button | "flexslider-icon" | 24.0 | 500 | 30px | 2px |
| Mono | "flexslider-icon" | 13.0 | 500 | 30px | 2px |
| Label | "flexslider-icon" | 40.0 | 500 | 30px | 2px |

## 4. Component Stylings

### Navigation
- Selectors: `nav`, `.navbar`, `header`
- Traits: top navigation; brand + links
## 5. Layout Principles

### Spacing Scale
- `0`
- `20px`
- `10px`
- `5px`
- `15px`
- `40px`
- `8px`
- `4px`
- `9px`
- `30px`
- `2px`
- `3px`

### Border Radius Scale
- `4px`
- `6px`
- `0`
- `3px`
- `50%`
- `10px`
- `4px 4px 0 0`
- `1px`
- `15px`
- `0.25em`

## 6. Depth & Elevation

| Level | Shadow Token |
|------|--------------|
| 1 | `none` |
| 2 | `inset 0 1px 1px rgba(0, 0, 0, 0.075)` |
| 3 | `inset 0 3px 5px rgba(0, 0, 0, 0.125)` |
| 4 | `0 0 8px rgba(0, 0, 0, 0.6)` |
| 5 | `inset 0 -1px 0 rgba(0, 0, 0, 0.25)` |
| 6 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 8px rgba(102, 175, 233, 0.6)` |
| 7 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168` |
| 8 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b` |

## 7. Do's and Don'ts

### Do
- 优先复用已提取的颜色与字体令牌。
- 在新组件中保持与现有间距、圆角尺度一致。
- 将交互状态（hover/focus/active）纳入主题变量管理。

### Don't
- 不要直接硬编码大量新色值，避免破坏原模板识别度。
- 不要混用多个不相关字体族，保持统一排版语言。
- 不要在暗色模式直接复用亮色阴影参数。

## 8. Responsive Behavior

检测到的媒体查询（前若干）：
- `@media (min-width: 768px)`
- `@media screen and (max-width: 768px)`
- `@media (max-width: 767px)`
- `@media (min-width: 1200px)`
- `@media print`
- `@media (min-width: 768px) and (max-width: 991px)`
- `@media (min-width: 992px) and (max-width: 1199px)`
- `@media screen and (max-width: 480px)`

## 9. Agent Prompt Guide

### Quick Prompt
- “基于 `moban4024` 模板，使用上方色板与排版层级，生成一个包含导航、hero、卡片和表单的现代化落地页，输出亮色与暗色双主题。”

### Iteration Checklist
1. 先锁定主色/中性色，再扩展强调色。
2. 用已提取的字号与权重构建标题-正文-说明三级层级。
3. 在预览页中验证按钮、表单、卡片在双主题下可读性。