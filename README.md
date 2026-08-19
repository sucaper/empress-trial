# EMPRESS Research Network 网站

以感染性休克与血管麻痹研究为核心的多中心临床研究网络官网。第一个研究项目：EMPRESS 多中心随机对照试验。

## 技术栈与部署

- **Quarto 网站**（本机 1.10.18；Cloudflare Pages 构建时在线安装）
- **GitHub** 存源码 + **Cloudflare Pages** 免费托管
- **中英双语**：两个 Quarto 项目——中文项目在根目录（导航中文），英文项目在 `en/`（导航英文）；**语言切换按钮固定在导航栏**（`_components/lang_toggle.html` 注入，按当前页面自动互跳）
- Logo 位于导航栏左上方（`images/logo.jpg`，CSS 中可调大小）

## 目录结构

```
_quarto.yml            # 中文项目配置（导航/页脚/主题/logo）
index.qmd              # 机构首页（中文）
about.qmd              # 关于网络
members.qmd            # 相关成员：指导委员会/协调委员会/项目管理/DSMB（委员会名录）
studies/empress.qmd    # EMPRESS 研究详情（含「相关文件发布」：一行一个文件）
contact.qmd            # 联系我们
en/_quarto.yml         # 英文项目配置（输出到 _site/en）
en/                    # 英文页面镜像
_components/           # 组件库（含使用说明）
_admin/                # 记忆文件与编辑权限说明（不参与渲染）
files/protocols/       # 方案 PDF（发布文件实际存放）
files/sap/             # SAP（待发布）
files/interim-reports/ # 中期报告（待发布）
styles/                # 主题（theme.scss）与自定义样式（custom.css）
```

## 常用操作

- 本地预览：`quarto render` 后打开 `_site/index.html`，或 `quarto preview`
- 发布文件：文件放入 `files/` 对应目录 → 在 `studies/empress.qmd` 的「相关文件发布」列表登记 → 推送
- 添加组件：见 `_components/README.md`
- 编辑权限与红线：见 `_admin/编辑权限说明.md`

## Cloudflare Pages 构建配置

- Build command：
  `curl -sSL https://github.com/quarto-dev/quarto-cli/releases/download/v1.10.18/quarto-1.10.18-linux-amd64.tar.gz -o ~/quarto.tar.gz && mkdir -p ~/quarto && tar -xzf ~/quarto.tar.gz -C ~/quarto --strip-components=1 && export PATH=~/quarto/bin:$PATH && quarto render && quarto render en`
- Build output directory：`_site`
