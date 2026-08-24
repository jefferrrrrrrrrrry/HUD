# 工作流日志：navigation_attention_ARHUD 子项目

## 项目时间轴

### Day 1 - 2026-06-28

#### 14:00-14:30 阶段 B-1：项目初始化与检索方案
- ✅ 创建目录结构 `navigation_attention_ARHUD/`（papers/extracted_text/summaries/thematic_review/proposal/scripts）
- ✅ 撰写检索方案 `00_检索方案.md`（6 主题组 × 关键词分组 + 纳入/排除标准）
- ✅ 撰写项目 README

#### 14:30-15:30 阶段 B-2：OpenAlex 元数据爬取
- ✅ 实现 `scripts/crawl_metadata.py`（基于 OpenAlex API + 代理）
- ⚠️ 第一次尝试因 `host_venue` 字段弃用失败（HTTP 400）
- ✅ 修正字段为 `primary_location.source` 后成功
- ✅ 24 个查询（6 组 × 4 关键词）共获取 600 hits
- ✅ 去重后 514 条原始记录

#### 15:30-16:00 阶段 B-2.5：相关性评分与筛选
- ✅ 实现 `scripts/filter_metadata.py`（关键词权重 + 引用加成 + venue 加成）
- ✅ 排除主课题 17 篇 DOI 重复
- ✅ 排除明显无关（医学/航空/农业等）约 220 条
- ✅ 保留 271 条相关记录
- ✅ 取 Top-80 作为下载候选
- ✅ Top-1 命中：Hou et al. 2024 AR-HUD navigation × inattentional blindness

#### 16:00-17:00 阶段 B-3：PDF 下载（后台）
- ✅ 实现 `scripts/download_pdfs.py`（5 个 Sci-Hub 镜像 fallback）
- ✅ 80 篇尝试，成功 48 篇（60%）
- 失败 32 篇主要因：① Sci-Hub 收录滞后（2023+ 文献）② DDoS-Guard 拦截

#### 17:00-17:30 阶段 B-3b：文本提取 + Jina Fallback
- ✅ 实现 `scripts/extract_text.py`（PyMuPDF + Jina 兜底）
- ✅ 48 篇 PDF 文本提取
- ✅ 23 篇 Jina 抓取补全
- ✅ 9 篇仅元数据
- ✅ 总计 80 个文件可用

#### 17:30-19:00 阶段 B-4：批量生成 summaries
- ✅ 第一批 1-10（10 篇核心文献，质量达标）
- 🔄 第二批 11-24（14 篇，后台运行）
- 🔄 第三批 26-40（15 篇，后台运行）
- 🔄 第四批 41-60（19 篇，后台运行）
- 已存在：#25 Yang、#49 Kiss（之前部分成功保留）

## 中间产物

| 文件 | 大小 | 说明 |
|---|---|---|
| `metadata_raw.json` | ~2 MB | 514 条 OpenAlex 原始记录 |
| `metadata_filtered.json` | ~500 KB | Top-80 评分排序结果 |
| `02_文献清单.csv/.md` | ~80 KB | 人类可读的清单 |
| `download_log.json` | ~50 KB | PDF 下载日志 |
| `papers/` | 91 MB | 48 个 PDF |
| `extracted_text/` | ~5 MB | 80 个文本文件 |

## 关键决策记录

### D-1：选择 OpenAlex 而非 WoS/Scopus
- 原因：OpenAlex 免费、API 友好、覆盖广（含 IEEE/ACM/会议）
- 局限：缺乏 JCR 分区信息（但有 cited_by_count 可代替）

### D-2：Top-80 而非 Top-50
- 原因：考虑 60% Sci-Hub 成功率 → 80 × 0.6 = 48 → 接近目标 50 篇
- 实际：48 PDF + 23 Jina = 71 可用文件，超出预期

### D-3：跳过主课题 17 篇重复
- 原因：避免重复劳动；主课题 40 篇仍可引用，不重复爬取/笔记

### D-4：每批 10-19 篇 summary agents
- 原因：单个 agent 处理 12 篇时间约 30-40 分钟，但 5 个并行被取消
- 策略：3 个并行（保守），每批 14-19 篇

## 阶段 B-5 至 B-7 计划（未完成）

- **B-5**：5 篇主题综合分析
  - T1_AR-HUD导航设计综述
  - T2_注意捕获理论与AR-HUD应用
  - T3_信号抑制假说与界面设计
  - T4_非注意盲视与多重信息竞争
  - T5_与主课题时空设计调研的衔接

- **B-6**：文献综述（仿音乐论文格式）
  - 目标 20000+ CJK 字符
  - 60+ 条参考文献
  - 含 4-7 章结构（背景/综述/问题提出/实验设计）

- **B-7**：开题 PPT（仿周颖-0830）
  - 38-44 slides
  - 6 大 sections
  - 可编辑 .pptx

---

*最后更新：2026-06-28*
