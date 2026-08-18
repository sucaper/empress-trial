# EMPRESS 研究发布主页

早期应用亚甲蓝改善依赖高剂量升压药支持的感染性休克患者病死率（EMPRESS）——多中心随机对照试验方案的发布页面。

## 站点结构

- `_quarto.yml` — Quarto 网站配置（导航、主题、页脚）
- `index.qmd` — 中文首页
- `en/index.qmd` — 英文首页
- `styles/theme.scss` — 主题变量（主色 #0B2AC0）
- `styles/custom.css` — 自定义样式（Hero/时间线/下载按钮等）
- `images/logo.jpg` — 研究 Logo
- `protocol/EMPRESS_protocol_zh.pdf` — 中文版方案（最终发表版）
- `protocol/EMPRESS_protocol_en.pdf` — 英文版方案（SJTREM 2026;34:44）

## 本地预览

```bash
quarto render    # 输出到 _site/
quarto preview   # 本地预览
```

## 部署（Cloudflare Pages）

1. 推送本仓库到 GitHub（公开仓库）
2. Cloudflare Pages → Create project → 连接该 GitHub 仓库
3. 构建配置：
   - Build command:
     `curl -sSL https://quarto.org/download/latest.tar.gz -o /tmp/quarto.tar.gz && mkdir -p /opt/quarto && tar -xzf /tmp/quarto.tar.gz -C /opt/quarto --strip-components=1 && export PATH=/opt/quarto/bin:$PATH && quarto render`
   - Build output directory: `_site`
4. 保存后自动部署，首次部署后可绑定自定义域名

## 更新内容

改 `index.qmd` / `en/index.qmd` → 本地 `quarto render` 验证 → `git add` / `commit` / `push` → Cloudflare Pages 自动构建部署。
