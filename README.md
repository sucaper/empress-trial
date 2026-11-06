# EMPRESS Research Network · EMPRESS 研究网络

> 以感染性休克（septic shock）与血管麻痹性休克研究为核心的多中心、国际协作临床研究网络官网。
> 首个研究项目：**EMPRESS 多中心随机对照试验**。

**官网 / Official website：<https://empress-trial.pages.dev/>**
（English: <https://empress-trial.pages.dev/en/>）

---

## 关于 EMPRESS 研究 / About the EMPRESS Trial

EMPRESS 研究全称：**早期应用亚甲蓝改善依赖高剂量升压药支持的感染性休克患者病死率的多中心随机对照试验**。

感染性休克患者在使用大剂量血管活性药物后仍难以维持血压时，病死率显著升高。亚甲蓝（methylene blue）通过抑制一氧化氮介导的血管舒张通路，可能改善这类患者的血管麻痹状态。EMPRESS 研究旨在通过多中心随机对照设计，评价早期应用亚甲蓝能否降低这类患者的病死率。

This is a multicentre, randomised, controlled trial evaluating whether **early administration of methylene blue** reduces mortality in patients with septic shock requiring high-dose vasopressor support.

## 关键信息 / Key facts

| 项目 | 内容 |
|---|---|
| 研究名称 | EMPRESS 多中心随机对照试验 |
| 研究设计 | 多中心、随机、对照临床试验（RCT） |
| 计划样本量 | 566 例 |
| 目标人群 | 依赖高剂量升压药支持的感染性休克患者 |
| 干预措施 | 早期应用亚甲蓝（methylene blue） |
| 主要结局 | 病死率 |
| 临床试验注册号 | **ChiCTR2500112352** |
| 方案论文 DOI | **10.1186/s13049-026-01563-y** |
| 牵头单位 | 四川省医学科学院·四川省人民医院 重症医学中心 |
| 主要研究者 | 罗竞超（Jing-chao Lawrence Luo），副主任医师 |
| 当前进度 | 截至 2026 年 11 月 6 日已入组第 82 例，约半数中心启动 |

## 研究方向 / Research focus

感染性休克 · 脓毒症 · 血管麻痹性休克 · 亚甲蓝 · 糖皮质激素 · 血流动力学监测 · 重症医学大数据分析

septic shock · sepsis · vasoplegic shock · methylene blue · corticosteroids · haemodynamics · critical care

## 网站页面 / Pages

- [首页](https://empress-trial.pages.dev/) — 网络概览与研究进展
- [关于网络](https://empress-trial.pages.dev/about) — 定位、使命与治理架构
- [EMPRESS 研究](https://empress-trial.pages.dev/studies/empress) — 研究方案、入排标准、里程碑
- [相关成员](https://empress-trial.pages.dev/members) — 指导委员会、协调委员会、DSMB、参与中心
- [罗竞超](https://empress-trial.pages.dev/luo-jingchao) — 主要研究者简介
- [联系](https://empress-trial.pages.dev/contact) — 合作与参与

## 引用 / Citation

> EMPRESS Research Network. *EMPRESS trial: early methylene blue in septic shock requiring high-dose vasopressors* (ChiCTR2500112352). Sichuan Provincial People's Hospital. https://empress-trial.pages.dev/

---

<details>
<summary><b>维护者文档（技术细节，点开）</b></summary>

### 技术栈与部署

- **Quarto 网站**（本机 1.10.18；Cloudflare Pages 构建时在线安装）
- **GitHub** 存源码 + **Cloudflare Pages** 免费托管
- **中英双语**：两个 Quarto 项目——中文项目在根目录（导航中文），英文项目在 `en/`（导航英文）；**语言切换按钮固定在导航栏**（`_components/lang_toggle.html` 注入，按当前页面自动互跳）
- Logo 位于导航栏左上方（`images/logo.jpg`，CSS 中可调大小）

### 目录结构

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

### 常用操作

- 本地预览：`quarto render` 后打开 `_site/index.html`，或 `quarto preview`
- 发布文件：文件放入 `files/` 对应目录 → 在 `studies/empress.qmd` 的「相关文件发布」列表登记 → 推送
- 添加组件：见 `_components/README.md`
- 编辑权限与红线：见 `_admin/编辑权限说明.md`

### Cloudflare Pages 构建配置

- Build command：
  `curl -sSL https://github.com/quarto-dev/quarto-cli/releases/download/v1.10.18/quarto-1.10.18-linux-amd64.tar.gz -o ~/quarto.tar.gz && mkdir -p ~/quarto && tar -xzf ~/quarto.tar.gz -C ~/quarto --strip-components=1 && export PATH=~/quarto/bin:$PATH && quarto render && quarto render en && cp 6ffd11306a1a90cbf56022a7365c2a3c.txt _site/`
- Build output directory：`_site`

### 搜索引擎与 AI 检索（2026-11-06 加）

目标：让 Google、Bing 以及 DeepSeek 等 AI 联网检索能发现并读懂本站。域名 `https://empress-trial.pages.dev/`。

| 文件 | 作用 |
|---|---|
| `robots.txt` | 允许抓取，并用 `Sitemap:` 声明站点地图 |
| `sitemap-empress.xml` | 手工维护的 12 个中英页面清单，含 `hreflang` 互指；**新增页面时必须同步加一条** |
| `_redirects` | 把习惯性的 `/sitemap.xml` 地址重写到上面的文件 |
| `404.html` | 修正 Cloudflare Pages 把不存在路径一律返回「200 + 首页」的问题 |
| `llms.txt` | **给 AI 爬虫的站点说明书**：关键事实、页面清单、引用建议。新增重要页面时同步更新 |
| `734b6caf8f93eddf535b1ba6dabf7c15.txt` | IndexNow key，用于主动通知 Bing |
| `_components/lang_toggle.html` | 全站 head 注入：JSON-LD 结构化数据（Organization / Person / MedicalTrial / ScholarlyArticle）、canonical、hreflang、og 标签。**实体信息必须写静态 JSON-LD**，勿改成 JS 动态生成——纯抓取的 AI 爬虫不执行 JS |
| `notify-search.bat` | 双击即可把 sitemap 里全部网址推送给 IndexNow（Bing 等） |

- 上线方式：`_quarto.yml` 的 `project.resources` 会把这些文件随渲染复制到 `_site/`；**不需要改 Cloudflare 构建命令**。
- 站点所有权验证：Google 用根目录 HTML 文件（`google936a01c80ab0fda6.html`，**不可删除**），Bing 从 Search Console 一键导入。两者都不需要 meta 验证标签，**不要在 head 里留空的验证码占位**。
- 日常更新流程：改 qmd → `git push` → Cloudflare 自动部署（约 40 秒）→ 双击 `notify-search.bat`。

</details>
