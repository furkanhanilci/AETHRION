---
airl_id: "SRC-ZOT-D2DBDEFC6244EF78"
type: source
status: ingested
source_category: "01 - Journal Articles"
zotero_item_key: "MB6YKEJX"
zotero_version: 0
doi: ""
source_url: "http://arxiv.org/abs/2501.15228"
content_hash: "sha256:ff3140b3b40b3686fb0d9eed4087951546a48fbae026b3ccbdd4d149903c4851"
generated_at: "2026-08-22T19:32:38.074209+00:00"
provenance: airl-bridge-api
tags:
  - aethrion/source
  - aethrion/source-category/01-journal-articles
  - aethrion/item-type/journalarticle
zotero_tags:
  []
creators:
  - "Yiqun Chen"
  - "Lingyong Yan"
  - "Weiwei Sun"
  - "Xinyu Ma"
  - "Yi Zhang"
  - "Shuaiqiang Wang"
  - "Dawei Yin"
  - "Yiming Yang"
  - "Jiaxin Mao"
cssclasses:
  - aethrion-source
---

<h1>Improving Retrieval-Augmented Generation through Multi-Agent Reinforcement Learning</h1>

> [!warning] Generated Zotero view
> This file is regenerated from the canonical source registry; do not edit it by hand. Keep human synthesis under `20 - Source Notes`.

- Zotero: [MB6YKEJX](zotero://select/library/items/MB6YKEJX)
- Publication date: <code>2025-01-25</code>
- Item type: <code>journalArticle</code>

## Abstract from Zotero

<pre>Retrieval-augmented generation (RAG) is extensively utilized to incorporate external, current knowledge into large language models, thereby minimizing hallucinations. A standard RAG pipeline may comprise several components, such as query rewriting, document retrieval, document filtering, and answer generation. However, these components are typically optimized separately through supervised fine-tuning, which can lead to misalignments between the objectives of individual modules and the overarching aim of generating accurate answers in question-answering (QA) tasks. Although recent efforts have explored reinforcement learning (RL) to optimize specific RAG components, these approaches often focus on overly simplistic pipelines with only two components or do not adequately address the complex interdependencies and collaborative interactions among the modules. To overcome these challenges, we propose treating the RAG pipeline as a multi-agent cooperative task, with each component regarded as an RL agent. Specifically, we present MMOA-RAG, a Multi-Module joint Optimization Algorithm for RAG, which employs multi-agent reinforcement learning to harmonize all agents&#x27; goals towards a unified reward, such as the F1 score of the final answer. Experiments conducted on various QA datasets demonstrate that MMOA-RAG improves the overall pipeline performance and outperforms existing baselines. Furthermore, comprehensive ablation studies validate the contributions of individual components and the adaptability of MMOA-RAG across different RAG components and datasets. The code of MMOA-RAG is on https://github.com/chenyiqun/MMOA-RAG.</pre>
