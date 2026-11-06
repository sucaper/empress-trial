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
  `curl -sSL https://github.com/quarto-dev/quarto-cli/releases/download/v1.10.18/quarto-1.10.18-linux-amd64.tar.gz -o ~/quarto.tar.gz && mkdir -p ~/quarto && tar -xzf ~/quarto.tar.gz -C ~/quarto --strip-components=1 && export PATH=~/quarto/bin:$PATH && quarto render && quarto render en && cp 6ffd11306a1a90cbf56022a7365c2a3c.txt _site/`
- Build output directory：`_site`

## 搜索引擎收录（SEO，2026-11-06 加）

目标：让 Google 与 Bing 能发现并收录本站。域名 `https://empress-trial.pages.dev/`。

| 文件 | 作用 |
|---|---|
| `robots.txt` | 允许抓取，并用 `Sitemap:` 声明站点地图 |
| `sitemap.xml` | 手工维护的 12 个中英页面清单，含 `hreflang` 互指；**新增页面时必须同步加一条** |
| `404.html` | 修正 Cloudflare Pages 把不存在路径一律返回「200 + 首页」的问题，让未知路径返回真 404 |
| `734b6caf8f93eddf535b1ba6dabf7c15.txt` | IndexNow key（内容 = 文件名），用于主动通知 Bing 等引擎 |
| `_components/lang_toggle.html` 末尾 | 全站 head 注入 SEO meta；**站长验证标签占位在这里**，拿到验证码后填入 |
| `notify-search.bat` | 双击即可把 sitemap 里全部网址推送给 IndexNow（Bing 等） |

- 上线方式：`_quarto.yml` 的 `project.resources` 会把这些文件随渲染复制到 `_site/`；`robots.txt`、`404.html` Quarto 本身也会自动复制。**不需要改 Cloudflare 构建命令。**
- 各 qmd 的 `description-meta` 生成搜索结果摘要；中英 hreflang 在 sitemap 里声明。
- 网站所有权验证：在 Google Search Console / Bing Webmaster Tools 选「HTML 标记」，把验证码填进 `_components/lang_toggle.html` 的两行占位后推送；Bing 可从 Search Console 一键导入，不必单独验证。
- 日常更新流程：改 qmd → `git push` → Cloudflare 自动部署 → 双击 `notify-search.bat`。

