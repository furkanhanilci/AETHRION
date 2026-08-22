---
airl_id: "SRC-ZOT-BC7C7490A7319B7D"
type: source
status: ingested
source_category: "01 - Journal Articles"
zotero_item_key: "U33TLMRS"
zotero_version: 0
doi: "10.1109/access.2024.3521334"
source_url: ""
content_hash: "sha256:94c2b2cc4a3cc14b6e1be11cb1d4024c5ea8e574d62af0d2006c04e7b4caa973"
generated_at: "2026-08-22T19:32:38.074921+00:00"
provenance: airl-bridge-api
tags:
  - aethrion/source
  - aethrion/source-category/01-journal-articles
  - aethrion/item-type/journalarticle
  - aethrion/has-doi
zotero_tags:
  - "3D LiDAR"
  - "contrastive learning"
  - "multi-object tracking"
  - "reinforcement learning"
creators:
  - "Minho Cho"
  - "Euntai Kim"
cssclasses:
  - aethrion-source
---

<h1>3D LiDAR Multi-Object Tracking Using Multi Positive Contrastive Learning and Deep Reinforcement Learning</h1>

> [!warning] Generated Zotero view
> This file is regenerated from the canonical source registry; do not edit it by hand. Keep human synthesis under `20 - Source Notes`.

- Zotero: [U33TLMRS](zotero://select/library/items/U33TLMRS)
- Publication date: <code>2024</code>
- Item type: <code>journalArticle</code>

## Abstract from Zotero

<pre>Due to its precise distance measurement capabilities, 3D LiDAR is a critical sensor in autonomous systems, including autonomous vehicles and self-driving robots. It plays a key role in Multi-Object Tracking (MOT). Current MOT methods typically employ a Tracking-by-Detection(TbD) approach, where objects are detected in each frame and matched across frames. However, 3D LiDAR-based tracking faces challenges such as sparsity and occlusion, often leading to ID-switching errors where object identities are incorrectly swapped due to incomplete data. This paper presents a novel 3D LiDAR-based MOT method to address these challenges and enhance tracking accuracy. We propose refining object similarity using contrastive learning, leveraging the distinct shapes of detected objects at varying distances. Additionally, we tackle occlusion issues through reinforcement learning, modeling occlusion dynamics to ensure that re-detected objects retain their original IDs thus improving tracking consistency. Our method is evaluated using the KITTI MOT dataset, demonstrating improved higher-order tracking Accuracy (HOTA) and reduced ID-switching compared to existing 3D LiDAR and camera-LiDAR fusion methods. These findings underscore the effectiveness of our approach across diverse road environments.</pre>
