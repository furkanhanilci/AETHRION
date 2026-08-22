---
airl_id: "SRC-ZOT-230208B024D2FCA3"
type: source
status: ingested
source_category: "01 - Journal Articles"
zotero_item_key: "7WFCETX8"
zotero_version: 0
doi: "10.1007/s00371-022-02672-2"
source_url: ""
content_hash: "sha256:57da7ce8986941916dd12c56decc5624dc4271d686feb7095856db373367ad18"
generated_at: "2026-08-22T11:17:38.072144+00:00"
provenance: airl-bridge-api
zotero_tags:
  - "3D object detection"
  - "Point-voxel feature interaction"
  - "PV-RCNN++"
  - "Semantic segmentation"
  - "Voxel query"
creators:
  - "Peng Wu"
  - "Lipeng Gu"
  - "Xuefeng Yan"
  - "Haoran Xie"
  - "Fu Lee Wang"
  - "Gary Cheng"
  - "Mingqiang Wei"
---

<h1>PV-RCNN++: semantical point-voxel feature interaction for 3D object detection</h1>

> [!warning] Generated Zotero view
> This file is regenerated from the canonical source registry; do not edit it by hand. Keep human synthesis under `20 - Source Notes`.

- Zotero: [7WFCETX8](zotero://select/library/items/7WFCETX8)
- Publication date: <code>2023-06-01</code>
- Item type: <code>journalArticle</code>

## Abstract from Zotero

<pre>Large imbalance often exists between the foreground points (i.e., objects) and the background points in outdoor LiDAR point clouds. It hinders cutting-edge detectors from focusing on informative areas to produce accurate 3D object detection results. This paper proposes a novel object detection network by semantical point-voxel feature interaction, dubbed PV-RCNN++. Unlike most of existing methods, PV-RCNN++ explores the semantic information to enhance the quality of object detection. First, a semantic segmentation module is proposed to retain more discriminative foreground keypoints. Such a module will guide our PV-RCNN++ to integrate more object-related point-wise and voxel-wise features in the pivotal areas. Then, to make points and voxels interact efficiently, we utilize voxel query based on Manhattan distance to quickly sample voxel-wise features around keypoints. Such the voxel query will reduce the time complexity from O(N) to O(K), compared to the ball query. Further, to avoid being stuck in learning only local features, an attention-based residual PointNet module is designed to expand the receptive field to adaptively aggregate the neighboring voxel-wise features into keypoints. Extensive experiments on the KITTI dataset show that PV-RCNN++ achieves 81.60% , 40.18% , 68.21% 3D mAP on Car, Pedestrian, and Cyclist, achieving comparable or even better performance to the state-of-the-arts.</pre>
