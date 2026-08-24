# navigation_attention_ARHUD：AR-HUD 导航环境下的注意冲突与行人预警可见性研究

## 项目概要

本子项目聚焦于研究主题：

> **AR-HUD 持续导航信息加入对行人碰撞预警感知的影响——注意捕获 vs 信号抑制策略的实证比较**

源起于草稿 `../250618AR-HUD碰撞预警导航加入.pptx`，是对该草稿"想法明确但缺乏文献依据"的系统化补充。

## 核心研究问题

```
传统 HUD（事件触发预警）→ 视觉竞争少 → 注意捕获主导
                              ↓
                          (技术演进)
                              ↓
AR-HUD（导航持续叠加）→ 视觉资源竞争 → 非注意盲视风险
                              ↓
                       (待解决的设计问题)
                              ↓
策略 1: 注意捕获 (高亮行人) | 策略 2: 信号抑制 (弱化导航) | 策略 3: 组合
```

## 与主课题的关系

- **主课题** `/home/gezhuocheng/moe/HUD/`：HUD/AR-HUD 行人预警的**时间-空间设计规范**（40 篇）
- **本子项目**：AR-HUD 导航与预警**注意冲突机制**（50+ 篇）
- 二者互补：主课题给出"什么样的预警最有效"，本子项目回答"在导航持续叠加时如何让有效预警依然有效"

## 目录结构

```
navigation_attention_ARHUD/
├── README.md                           ← 本文档
├── 00_检索方案.md                      ← 数据库/关键词/纳入标准
├── 01_文献检索日志.md                  ← 实际检索过程记录
├── 02_文献清单.csv / .md               ← 80 篇候选文献元数据
├── metadata_raw.json                   ← OpenAlex 原始 514 条
├── metadata_filtered.json              ← 评分排序后 Top-80
├── download_log.json                   ← PDF 下载日志
├── papers/                             ← 全文 PDF
├── extracted_text/                     ← 文本提取
├── summaries/                          ← 详细中文笔记（每篇 1500-2500 字）
├── thematic_review/                    ← 5 篇主题综合分析
│   ├── T1_AR-HUD导航设计综述.md
│   ├── T2_注意捕获理论与AR-HUD应用.md
│   ├── T3_信号抑制假说与界面设计.md
│   ├── T4_非注意盲视与多重信息竞争.md
│   └── T5_与主课题时空设计调研的衔接.md
├── proposal/                           ← 开题文档
│   ├── 文献综述_硕士论文风格.md        ← 仿音乐论文格式
│   ├── 开题报告_大纲.md
│   └── 开题报告_PPT.pptx
├── scripts/
│   ├── crawl_metadata.py               ← OpenAlex 检索
│   ├── filter_metadata.py              ← 评分筛选
│   ├── build_paper_list.py             ← 文献清单生成
│   ├── download_pdfs.py                ← Sci-Hub 下载
│   ├── extract_text.py                 ← PyMuPDF 文本提取
│   └── build_pptx.py                   ← 开题 PPT 生成
└── workflow_log.md                     ← 整体工作流日志
```

## 关键里程碑

| 阶段 | 状态 | 输出 |
|---|---|---|
| B-1 检索方案 | ✅ | `00_检索方案.md` |
| B-2 元数据爬取 | ✅ | 514 条 → Top-80 |
| B-3 PDF 下载 | 🔄 进行中 | 目标 ≥ 50 篇 |
| B-4 文本提取 + summaries | ⏳ | 50+ 篇详细笔记 |
| B-5 5 篇主题综合 | ⏳ | thematic_review/ |
| B-6 文献综述 | ⏳ | proposal/文献综述_硕士论文风格.md (≥20000 CJK) |
| B-7 开题 PPT | ⏳ | proposal/开题报告_PPT.pptx (38-44 slides) |

## 关键起点文献（已识别）

1. **Hou, Dong, & Wang (2024)** – 草稿 *"Hou et al., 2025"* 真实身份 ★★★★★
   *The Effect of Dynamic Effects and Color Transparency of AR-HUD Navigation Graphics on Driving Behavior Regarding Inattentional Blindness*
   IJHCI, DOI: 10.1080/10447318.2024.2400376
2. **Wang & Wu (2021)** – AR-HUD 中的非注意盲视
3. **Chen et al. (2023)** – AR-HUD 中对未预期危险的非注意盲视
4. **Merenda et al. (2018)** – Goal-directed 与 Stimulus-driven AR 界面设计
5. **Bauerfeind et al. (2022)** – AR 导航对 glance behavior 影响

## 复用的经典理论文献

| 文献 | 用途 |
|---|---|
| Theeuwes (1992) | 注意捕获经典 |
| Yantis & Hillstrom (1994) | 注意捕获经典 |
| Mack & Rock (1998) | 非注意盲视经典 |
| Gaspelin & Luck (2018) | 信号抑制假说 |
| Wickens (2002, 2008) | 多资源理论 |
| Endsley (1995) | 情境意识 |
| Wolfe (1994) | Guided Search 视觉搜索 |

---

*创建日期：2026-06-28*
