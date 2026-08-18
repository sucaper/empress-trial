# 组件库 Components

本目录存放可复用页面组件（HTML 片段）。**以下划线开头的目录不会被 Quarto 渲染**，组件只通过页面引用生效。

## 使用方式

方式一：`include` 短代码（静态片段，路径相对引用页）：

```markdown
{{< include _components/study_card.html >}}
```

注意：嵌套页面（如 `en/studies/empress.qmd`）引用时需写相对路径 `../../_components/study_card.html`。

方式二：作为模板参考——成员卡片等由 `scripts/build_members.py` 生成，修改模板后重新运行生成器即可批量生效。

## 现有组件

| 组件 | 文件 | 说明 |
|:---|:---|:---|
| 研究卡片 | `study_card.html` | 首页研究项目卡片 |
| 治理卡片 | `gov_card.html` | 治理机构卡片 |
| 时间线 | `timeline.html` | 里程碑时间线（li 结构参考） |
| 语言切换 | `lang_switch.html` | 中英切换按钮（每页需手动指定对应页面链接） |
| 下载按钮 | `btn_dl.html` | 文件下载按钮（primary/outline 两式） |

## 新增组件的步骤

1. 在 `_components/` 新建 `xxx.html`（样式类统一加到 `styles/custom.css`）
2. 在页面中用 `{{< include _components/xxx.html >}}` 引用（注意嵌套路径）
3. 若组件需要数据驱动（如成员列表），在 `scripts/` 写生成逻辑并注册到 README
