# Design System: moban2603

## 1. Visual Theme & Atmosphere

该模板呈现出以结构化模块为核心的网页风格，页面由多个内容分区组成，并通过清晰的导航、标题和行动按钮建立信息层级。整体视觉基调偏向实用型商业站点，强调可读性与组件复用。

**Key Characteristics:**
- Uses container-based layout wrappers.
- Grid system detected via column classes.
- Row-based section composition present.
- Sectioned page architecture with repeated blocks.
- 组件风格由模板内真实 CSS 规则提取，适合作为二次主题化与系统化改造基础。

## 2. Color Palette & Roles

### Primary
- **#ffffff** (`#ffffff`): 用途分组 `primary`，出现频次约 85。
### Accent
- **#FECE1A** (`#FECE1A`): 用途分组 `accent`，出现频次约 29。
- **#0088cc** (`#0088cc`): 用途分组 `accent`，出现频次约 22。
- **#f89406** (`#f89406`): 用途分组 `accent`，出现频次约 16。
- **#ee5f5b** (`#ee5f5b`): 用途分组 `accent`，出现频次约 12。
### Neutral
- **#ffffff** (`#ffffff`): 用途分组 `neutral`，出现频次约 85。
- **rgba(255, 255, 255, 0.15)** (`rgba(255, 255, 255, 0.15)`): 用途分组 `neutral`，出现频次约 78。
- **#181A1C** (`#181A1C`): 用途分组 `neutral`，出现频次约 36。
- **rgba(0, 0, 0, 0.1)** (`rgba(0, 0, 0, 0.1)`): 用途分组 `neutral`，出现频次约 33。
- **rgba(0, 0, 0, 0.075)** (`rgba(0, 0, 0, 0.075)`): 用途分组 `neutral`，出现频次约 30。
- **#999999** (`#999999`): 用途分组 `neutral`，出现频次约 27。
- **rgba(0, 0, 0, 0.25)** (`rgba(0, 0, 0, 0.25)`): 用途分组 `neutral`，出现频次约 27。
- **#fff** (`#fff`): 用途分组 `neutral`，出现频次约 26。
### Semantic
- 无明显颜色令牌。

## 3. Typography Rules

| Role | Font | Size(px) | Weight | Line Height | Letter Spacing |
|------|------|----------|--------|-------------|----------------|
| Display | "Helvetica Neue", Helvetica, Arial, sans-serif | 14.0 | normal | 20px | -1px |
| Heading | "Porta" | 20.0 | bold | 0 | -1px |
| Sub-heading | "porta" | 17.5 | 200 | 30px | -1px |
| Body | Arial | 11.9 | 100 | 1 | -1px |
| Caption | inherit | 0.0 | lighter | 40px | -1px |
| Button | Monaco, Menlo, Consolas, "Courier New", monospace | 12.0 | 300 | normal | -1px |
| Mono | Monaco, Menlo, Consolas, "Courier New", monospace | 15.0 | 300 | normal | -1px |
| Label | Monaco, Menlo, Consolas, "Courier New", monospace | 10.5 | 300 | normal | -1px |

## 4. Component Stylings

### Navigation
- Selectors: `nav`, `.navbar`, `header`
- Traits: top navigation; brand + links### Buttons
- Selectors: `button`, `.btn`, `a.button`
- Traits: primary actions; hover states### Cards
- Selectors: `.card`, `.panel`, `.thumbnail`, `.product`
- Traits: content containers### Forms
- Selectors: `form`, `input`, `textarea`, `select`
- Traits: data input; interactive controls### Hero
- Selectors: `.hero`, `#hero`, `.banner`, `.slider`, `#home`
- Traits: intro section; headline + call-to-action
## 5. Layout Principles

### Spacing Scale
- `0`
- `10px`
- `15px`
- `5px`
- `20px`
- `4px`
- `9px`
- `3px`
- `8px`
- `0px`
- `2px`
- `14px`

### Border Radius Scale
- `4px`
- `0`
- `6px`
- `3px`
- `0 4px 4px 0`
- `4px 0 0 4px`
- `5px`
- `15px`
- `0 0 6px 6px`
- `500px`

## 6. Depth & Elevation

| Level | Shadow Token |
|------|--------------|
| 1 | `inset 0 1px 1px rgba(0, 0, 0, 0.075)` |
| 2 | `none` |
| 3 | `0 5px 10px rgba(0, 0, 0, 0.2)` |
| 4 | `inset 0 2px 4px rgba(0, 0, 0, 0.15), 0 1px 2px rgba(0, 0, 0, 0.05)` |
| 5 | `0 1px 3px rgba(0, 0, 0, 0.1)` |
| 6 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 8px rgba(82, 168, 236, 0.6)` |
| 7 | `inset 0 1px 2px rgba(0, 0, 0, 0.025)` |
| 8 | `inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #dbc59e` |

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
- `@media (max-width: 767px)`
- `@media (max-width: 979px)`
- `@media print`
- `@media (min-width: 768px) and (max-width: 979px)`
- `@media (min-width: 1200px)`
- `@media (max-width: 480px)`
- `@media (min-width: 980px)`
- `@media screen and (-webkit-min-device-pixel-ratio:0)`

## 9. Agent Prompt Guide

### Quick Prompt
- “基于 `moban2603` 模板，使用上方色板与排版层级，生成一个包含导航、hero、卡片和表单的现代化落地页，输出亮色与暗色双主题。”

### Iteration Checklist
1. 先锁定主色/中性色，再扩展强调色。
2. 用已提取的字号与权重构建标题-正文-说明三级层级。
3. 在预览页中验证按钮、表单、卡片在双主题下可读性。