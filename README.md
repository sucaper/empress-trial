# EMPRESS Research Network 网站

以感染性休克与血管麻痹研究为核心的多中心临床研究网络官网。第一个研究项目：EMPRESS 多中心随机对照试验。

## 技术栈与部署

- **Quarto 网站**（本机 1.10.18；Cloudflare Pages 构建时在线安装）
- **GitHub** 存源码 + **Cloudflare Pages** 免费托管
- 中英双语：中文在根目录，英文在 `en/`；每页右上角语言切换按钮

## 目录结构

```
_quarto.yml            # 站点配置（导航/页脚/主题）
index.qmd              # 机构首页（中文）
about.qmd              # 关于网络
governance.qmd         # 治理架构：指导委员会/协调委员会/DSMB
studies/empress.qmd    # EMPRESS 研究详情
members/               # 成员总览 + 个人主页（由脚本生成，勿手改）
documents.qmd          # 发布文件（方案/SAP/中期报告/发表文献）
contact.qmd            # 联系我们
en/                    # 英文镜像（结构与中文一致）
data/members.json      # 成员数据（编辑入口）
scripts/build_members.py  # 成员页生成器
_components/           # 组件库（含使用说明）
_admin/                # 记忆文件与编辑权限说明（不参与渲染）
files/protocols/       # 方案 PDF（发布文件实际存放）
files/sap/             # SAP（待发布）
files/interim-reports/ # 中期报告（待发布）
styles/                # 主题（theme.scss）与自定义样式（custom.css）
```

## 常用操作

- 本地预览：`quarto render` 后打开 `_site/index.html`，或 `quarto preview`
- 更新成员：改 `data/members.json` → `python scripts/build_members.py` → `quarto render`
- 发布文件：文件放入 `files/` 对应目录 → 在 `documents.qmd` 登记 → 推送
- 添加组件：见 `_components/README.md`
- 编辑权限与红线：见 `_admin/编辑权限说明.md`

## Cloudflare Pages 构建配置

- Build command：
  `curl -sSL https://quarto.org/download/latest.tar.gz -o /tmp/quarto.tar.gz && mkdir -p /opt/quarto && tar -xzf /tmp/quarto.tar.gz -C /opt/quarto --strip-components=1 && export PATH=/opt/quarto/bin:$PATH && quarto render`
- Build output directory：`_site`
