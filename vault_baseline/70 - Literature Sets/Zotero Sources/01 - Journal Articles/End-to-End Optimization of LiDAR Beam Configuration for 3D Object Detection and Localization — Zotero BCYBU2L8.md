---
airl_id: "SRC-ZOT-3329949F9C92130B"
type: source
status: ingested
source_category: "01 - Journal Articles"
zotero_item_key: "BCYBU2L8"
zotero_version: 0
doi: "10.1109/lra.2022.3142738"
source_url: ""
content_hash: "sha256:d10e2b5e741eb1c1977d7632e69995628e5cc20f2c74ba1bf753d11399ecc871"
generated_at: "2026-08-22T11:17:38.072757+00:00"
provenance: airl-bridge-api
zotero_tags:
  - "Laser beams"
  - "Laser radar"
  - "Location awareness"
  - "Object detection"
  - "Optimization"
  - "Task analysis"
  - "Three-dimensional displays"
creators:
  - "Niclas Vodisch"
  - "Ozan Unal"
  - "Ke Li"
  - "Luc Van Gool"
  - "Dengxin Dai"
---

<h1>End-to-End Optimization of LiDAR Beam Configuration for 3D Object Detection and Localization</h1>

> [!warning] Generated Zotero view
> This file is regenerated from the canonical source registry; do not edit it by hand. Keep human synthesis under `20 - Source Notes`.

- Zotero: [BCYBU2L8](zotero://select/library/items/BCYBU2L8)
- Publication date: <code>2022-04-01</code>
- Item type: <code>journalArticle</code>

## Abstract from Zotero

<pre>Existing learning methods for LiDAR-based applications use 3D points scanned under a pre-determined beam configuration, e.g., the elevation angles of beams are often evenly distributed. Those fixed configurations are task-agnostic, so simply using them can lead to sub-optimal performance. In this work, we take a new route to learn to optimize the LiDAR beam configuration for a given application. Specifically, we propose a reinforcement learning-based learning-to-optimize (RL-L2O) framework to automatically optimize the beam configuration in an end-to-end manner for different LiDAR-based applications. The optimization is guided by the final performance of the target task and thus our method can be integrated easily with any LiDAR-based application as a simple drop-in module. The method is especially useful when a low-resolution (low-cost) LiDAR is needed, for instance, for system deployment at a massive scale. We use our method to search for the beam configuration of a low-resolution LiDAR for two important tasks: 3D object detection and localization. Experiments show that the proposed RL-L2O method improves the performance in both tasks significantly compared to the baseline methods. We believe that a combination of our method with the recent advances of programmable LiDARs can start a new research direction for LiDAR-based active perception. The code is publicly available at &lt;uri&gt;github.com/vniclas/lidar_beam_selection&lt;/uri&gt;.</pre>
