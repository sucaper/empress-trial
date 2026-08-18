"""生成成员页面：读取 data/members.json，生成 members/ 与 en/members/ 下个人主页与总览页。
用法：python scripts/build_members.py
新增成员/修改信息 → 编辑 data/members.json → 重新运行本脚本 → quarto render
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
members = json.loads((ROOT / "data" / "members.json").read_text(encoding="utf-8"))

ROLE_ORDER_ZH = ["cofirst", "corresponding", "collab"]
ROLE_ORDER_EN = ["cofirst", "corresponding", "collab"]
ROLE_SECTION_ZH = {"cofirst": "共同第一作者", "corresponding": "通讯作者", "collab": "协作作者"}
ROLE_SECTION_EN = {"cofirst": "Co-first Authors", "corresponding": "Corresponding Authors", "collab": "Collaborating Authors"}

def photo_html(m, lang):
    img = ROOT / "images" / "members" / f"{m['id']}.jpg"
    if img.exists():
        return f'<img class="member-photo-img" src="../../images/members/{m["id"]}.jpg" alt="{m["name_en"]}" />'
    ph = "头像待上传" if lang == "zh" else "Photo to be added"
    return f'<span class="photo-placeholder">{ph}</span>'

def display_name(m, lang):
    if lang == "zh" and m["name_zh"]:
        return f'{m["name_zh"]} <span class="name-en">{m["name_en"]}</span>'
    return m["name_en"]

def profile(m, lang):
    pre = "" if lang == "zh" else "../"
    switch = {"zh": f'<a href="{pre}en/members/{m["id"]}.html">English</a>',
              "en":  f'<a href="{pre}members/{m["id"]}.html">中文</a>'}[lang]
    role = m["role_zh"] if lang == "zh" else m["role_en"]
    aff = m["aff_zh"] if lang == "zh" else m["aff_en"]
    bio = (m["bio_zh"] if lang == "zh" else m["bio_en"]).strip() or ("（个人简介待补充）" if lang == "zh" else "Biography to be added.")
    email_html = f'<p class="member-email"><a href="mailto:{m["email"]}">{m["email"]}</a></p>' if m["email"] else ""
    study = "EMPRESS 研究（早期亚甲蓝治疗高剂量升压药依赖感染性休克的多中心随机对照试验）" if lang == "zh" else "EMPRESS Study (Early Methylene Blue for Mortality Reduction in High-Dose VasoPREssor-Dependent Septic Shock, a multicenter randomized controlled trial)"
    lang_name = "zh-CN" if lang == "zh" else "en"
    return f"""---
title: "{m['name_en']}"
lang: {lang_name}
---

<div class="lang-switch">{switch}</div>

<div class="member-header">
  <div class="member-photo">{photo_html(m, lang)}</div>
  <div class="member-info">
    <h1 class="member-name">{display_name(m, lang)}</h1>
    <p class="member-role">{role}</p>
    <p class="member-affil">{aff}</p>
    {email_html}
  </div>
</div>

## {"个人简介" if lang == "zh" else "Biography"}

{bio}

## {"参与研究" if lang == "zh" else "Research involvement"}

- {study}
"""

def listing(lang):
    pre = "" if lang == "zh" else "../"
    switch = {"zh": '<a href="' + pre + 'en/members/index.html">English</a>',
              "en":  '<a href="' + pre + 'members/index.html">中文</a>'}[lang]
    title = "成员 Members" if lang == "zh" else "Members"
    intro = ("本网络团队成员来自中国、英国、智利、墨西哥与法国。以下 13 位研究者为 EMPRESS 研究方案作者（名单以发表版为准）；"
             "指导委员会、协调委员会与数据安全监查委员会成员见[治理架构](" + pre + "governance.html)。") if lang == "zh" else \
            ("Members of the network come from China, the United Kingdom, Chile, Mexico, and France. "
             "The 13 investigators below are the authors of the EMPRESS protocol (as published); members of the Steering, Coordinating, "
             "and Data Safety Monitoring Committees are listed under [Governance](" + pre + "governance.html).")
    lang_name = "zh-CN" if lang == "zh" else "en"
    sec_title = "团队作者（EMPRESS 研究方案）" if lang == "zh" else "Protocol authors (EMPRESS study)"
    out = [f"---\ntitle: \"{title}\"\nlang: {lang_name}\n---\n",
           f'<div class="lang-switch">{switch}</div>\n',
           f"## {sec_title}\n\n{intro}\n"]
    for role in ROLE_ORDER_ZH:
        group = [m for m in members if m["role"] == role]
        if not group:
            continue
        out.append(f"### {ROLE_SECTION_ZH[role] if lang=='zh' else ROLE_SECTION_EN[role]}\n")
        out.append('<div class="member-grid">')
        for m in group:
            aff = m["aff_zh"] if lang == "zh" else m["aff_en"]
            href = f'{m["id"]}.html' if lang == "zh" else f'{m["id"]}.html'
            out.append(f"""<div class="member-card">
  <a class="member-card-link" href="{href}">
    <div class="member-photo">{photo_html(m, lang)}</div>
    <div class="member-card-name">{display_name(m, lang)}</div>
    <div class="member-card-affil">{aff}</div>
  </a>
</div>""")
        out.append("</div>\n")
    out.append("\n<div class=\"footnote-note\">成员页面由 <code>data/members.json</code> 生成：编辑数据后运行 <code>python scripts/build_members.py</code> 再 <code>quarto render</code>。</div>\n")
    return "\n".join(out)

for lang in ["zh", "en"]:
    for m in members:
        content = profile(m, lang)
        out_path = ROOT / ("members" if lang == "zh" else "en/members") / f"{m['id']}.qmd"
        out_path.write_text(content, encoding="utf-8")
    out_path = ROOT / ("members/index.qmd" if lang == "zh" else "en/members/index.qmd")
    out_path.write_text(listing(lang), encoding="utf-8")

print("成员页面生成完成：")
for p in sorted((ROOT / "members").glob("*.qmd")) + sorted((ROOT / "en/members").glob("*.qmd")):
    print(" ", p.relative_to(ROOT))
