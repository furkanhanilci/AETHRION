---
airl_id: "SRC-ZOT-8D5CCD39A2A2E88D"
type: source
status: ingested
source_category: "01 - Journal Articles"
zotero_item_key: "XTBFGCIR"
zotero_version: 0
doi: "10.1109/tits.2024.3491784"
source_url: ""
content_hash: "sha256:0c1632f45376beb4325d8fdaca2d296f3b0ad3337bb50cb8bc15cda52510dc57"
generated_at: "2026-08-22T13:51:52.773624+00:00"
provenance: airl-bridge-api
zotero_tags:
  - "3D object detection"
  - "infrastructure-side point cloud"
  - "lidar"
  - "multi-frame"
creators:
  - "Ye Yue"
  - "Honggang Qi"
  - "Yongqiang Deng"
  - "Juanjuan Li"
  - "Hao Liang"
  - "Jun Miao"
---

<h1>Infrastructure-Side Point Cloud Object Detection via Multi-Frame Aggregation and Multi-Scale Fusion</h1>

> [!warning] Generated Zotero view
> This file is regenerated from the canonical source registry; do not edit it by hand. Keep human synthesis under `20 - Source Notes`.

- Zotero: [XTBFGCIR](zotero://select/library/items/XTBFGCIR)
- Publication date: <code>2024</code>
- Item type: <code>journalArticle</code>

## Abstract from Zotero

<pre>In recent years, with the advancement of artificial intelligence technology, autonomous driving technologies have gradually emerged. 3D object detection using point clouds has become a key in this field. Multi-frame fusion of point clouds is a promising technique to enhance 3D object detection for autonomous driving systems. However, most existing multi-frame detection methods focus primarily on utilizing vehicle-side lidar data. Infrastructure-side detection remains relatively unexplored, yet can enhance vital vehicle-road coordination capabilities. To help with this coordination, we propose an efficient multi-frame aggregation multi-scale fusion network specifically for infrastructure-side 3D object detection. First, our key innovation is a novel multi-frame feature aggregation module that effectively integrates information from multiple past point cloud frames to improve detection accuracy. This module comprises a feature pyramid network to fuse multi-scale features, as well as a cross-attention mechanism to learn semantic correlations between different frames over time. Next, we incorporate deformable attention, which reduces the computational overhead of aggregation by sampling locations. We designed Multi-frame and Multi-scale modules, thereby we named the model MAMF-Net. Finally, through extensive experiments on two infrastructure-side datasets including the V2X-Seq-SPD dataset which was released by Baidu corporation, we demonstrate that MAMF-Net delivers consistent accuracy improvements over single frame detectors such as PointPillars, PV-RCNN and TED-S, especially boosting pedestrian detection by 5%. Our approach also surpasses other multi-frame methods designed for vehicle-side point clouds such as MPPNet.</pre>
