# 第二阶段任务总结报告

## 任务回顾

用户要求三件事：
1. **用科研通和sci-hub再次尝试下载剩余21篇PDF**
2. **按时间维度（出现时间/持续时长/分级间隔）和空间维度（平面：色彩/动效/形状；立体：空间分布/视野/相对位置）重新整理表格**
3. **标注每个数据点来源（原文 vs 仅摘要，仅摘要需标记待补齐）**

---

## 完成情况

### ① PDF下载——最终成果

| 状态 | 数量 | 占比 | 论文 idx |
|------|------|------|---------|
| ✓ PDF全文 | 31 | 79.5% | 第一阶段18篇 + sci-hub.ren新下载10篇(02/05/10/11/14/15/16/18/28/30) + IEEE Access 2篇(27/36) + Cambridge Apollo 1篇(32) |
| ◐ Jina Reader全文 | 6 | 15.4% | 08/09/23/24/31 (MDPI) + 19 (Tandfonline review) |
| ◑ 中文姊妹篇PDF | 1 | 2.6% | #12 (英文Tandfonline锁，中文版华南理工大学学报2024可获取) |
| ★ 仅摘要(待补齐) | 1 | 2.6% | #07 (Tandfonline 2024 IJHCI - Cloudflare保护，sci-hub未收录) |

**数据可用性 = 38/39 = 97.4%**

### 下载技术路径
- **sci-hub.ren** (镜像) → sci.bban.top: 10/21 成功 (51%)
- **IEEE Xplore stamp.jsp + curl_cffi chrome131 impersonation**: 2/2 成功 (IEEE Access OA papers)  
- **Cambridge Apollo bitstreams**: 1/1 成功 (Wiley adma.202110463)
- **Jina AI Reader (r.jina.ai)**: 11/11 成功获取markdown内容 (含MDPI 5篇 + Tandfonline 3篇landing pages)
- **sciopen.com**: 1/1 找到paper #12中文姊妹篇PDF全文

### 反爬遇到的拦阻
- MDPI: Akamai 403 (代理IP被block)，所有curl_cffi impersonation失败
- Tandfonline: Cloudflare Turnstile + Anubis JS challenge
- Wiley: Cloudflare CAPTCHA  
- ResearchGate: Cloudflare 1020
- web.archive.org Jina: 被Jina标记为"DDoS abuse"屏蔽至2035-09-30

### ② 新表格结构

**核心字段（19列）**：

```
基础信息：idx | 数据源 | 作者(年份) | 标题 | DOI | Venue | JCR分区 | 场景简述

时间维度（5列）：
  T1_出现时机 — TTC/距离阈值（如2.5s/16.7m）
  T2_持续时长 — 警示在屏幕上停留多久
  T3_是否分级 — Yes/No
  T4_L1→L2间隔 — 一级到二级警告的TTC间隔
  T5_L2→L3间隔 — 二级到三级警告的TTC间隔

空间-平面维度（3列）：
  S1_色彩 — RGB/HSL/分级配色
  S2_动效 — 动态/静态/跟随/缩放/闪烁
  S3_形状 — bounding box / dome+tether / icon等

空间-立体维度（3列）：
  S4_空间分布 — 垂直面/水平面/混合/屏幕固定
  S5_视野FOV — HUD虚像视角
  S6_相对位置 — 屏幕固定/行人锁定/路面锁定/世界锁定

附加：关键发现 | 待审查项
```

### ③ 数据来源标注

每个数据点的"value/source"对中显式标注：
- `[来源:原文§7.2.5]` 引自具体章节/页码/图表
- `[来源:abstract未报告]` 仅abstract可读
- `[来源:中文版P3-4 §1.2]` 中文姊妹篇引用
- `[来源:未报告]` 论文中明确未涉及

**视觉标记**：
- `✓ 全文(PDF)` — PDF全文提取
- `◐ Jina全文` — Jina Reader获取
- `◑ 中文姊妹篇PDF` — 英文锁文但中文版可获取
- `★【仅摘要】` — 仅abstract可读，**待补齐**

---

## 关键发现亮点

### 时间元素设计参数最完整的论文
1. **#14 (Lübbe 2017 J Safety Res)**: 显式二级分级 — TTC=2.5s cautionary HUD → TTC=1.8s imminent audio-visual，间隔0.7s
2. **#27 (Ma 2021 IEEE Access)**: 警告时长3s常规/10-15s紧急；视场角随车速分级(65°/40°)
3. **#01/#04 (Kim 2018/2016)**: TTC=2.5s/5.0s双距离条件，virtual shadow持续显示直至危险解除
4. **#21 (Huo & Alla 2025)**: TTC=2.5s/34.72m触发，flashing动态明确

### 空间元素设计参数最完整的论文
1. **#29 (Teng 2023)**: 4色HEX(#2979FF/#FE0000/#4ADE80/#F26D21)；6区布局；视场角随车速分级(85°/65°/40°)
2. **#34 (Zhong 2022)**: 7色×3描边×2照度的Lv/CIE色坐标/Likert评分；FOV=12°×5°
3. **#08 (Wu 2024)**: 红色RGB(255,0,0)；BD/BR/BW三种空间策略对比
4. **#06 (Ma 2024)**: 三色编码绿=safe/黄=Phase1/红=Phase2，配Saturation渐变

### 待补齐论文清单

**仅abstract可读，必须补齐PDF**：
- **#07** Chen et al. 2024 IJHCI — `10.1080/10447318.2024.2327197`
  - 缺失: T_onset/T_duration/S_planar_color/S_3d_fov等
  - 建议: 通过机构订阅、ResearchGate请求、科研通文献互助提交申请

**部分字段缺失（论文性质决定，非可补齐）**：
- 综述论文 (#19/#31/#32/#35) — 综述层面归纳，无单一研究参数
- 工程系统论文 (#05/#18/#22/#37/#38) — 聚焦算法/网络性能，无人因UI细节
- 方法论提案 (#11/#13) — 设计框架阶段，无量化实验参数

---

## 输出文件清单

```
/home/gezhuocheng/moe/HUD/
├── HUD_AR-HUD_行人预警_时空设计_新表.md         ← 本次主要输出（118行Markdown表）
├── HUD_AR-HUD_行人预警_时空设计_新表.csv         ← 79KB CSV（含UTF-8 BOM便于Excel）
├── HUD_AR-HUD_行人预警_时空设计_新表.tsv         ← TSV格式
├── 数据源提供性_汇总.md                         ← 39篇按数据源分类
├── agent_outputs/
│   ├── group1.json (idx 1-8)
│   ├── group2.json (idx 9-16，含#12中文版补全数据)
│   ├── group3.json (idx 17-24)
│   ├── group4.json (idx 25-32)
│   └── group5.json (idx 33-39)
├── papers/                       ← 31个PDF
├── extracted_text/               ← 50个文本文件 (39篇 + 11个Jina md + 12中文版)
├── 时间元素设计参数_专题分析.md   ← 第一阶段保留
├── HUD_AR-HUD_行人预警_文献综合表.{csv,md,tsv}  ← 第一阶段保留
├── papers_metadata.json          ← 39篇OpenAlex元数据
└── temporal_spatial_params.json  ← 第一阶段提取数据（已被新表superseded）
```

---

## 用户后续行动建议

1. **审阅新表**: `HUD_AR-HUD_行人预警_时空设计_新表.md`
2. **重点查看`待补齐清单`部分** — 区分"必须补齐(#07)"vs"无法补齐(综述/工程系统的天然缺失)"
3. 如需进一步补齐 #07 全文，建议:
   - 通过组织订阅访问 Tandfonline
   - 提交科研通(ablesci.com)文献互助申请（异步流程）
   - 联系作者(王婷 Chen, Wanting@浙江大学; 通讯作者Hongting Li)
