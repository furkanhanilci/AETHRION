# Architecture Index

Hedef mimari, repository haritası ve operasyonel skill katmanı.

## Belgeler

| Belge | Cevapladığı soru |
|---|---|
| [[10 - Projects/AI Research Framework/04 - Architecture/framework_repository_and_obsidian_map\|Repository and Obsidian Map]] | Ne nerede tutuluyor? |
| [[10 - Projects/AI Research Framework/04 - Architecture/airl_os_ideal_structure\|AIRL-OS İdeal Yapı]] | **Ne** eklenmeli? |
| [[10 - Projects/AI Research Framework/04 - Architecture/airl_os_skill_layer\|AIRL-OS Skill Layer]] | **Nasıl** yürütülmeli? |
| [[10 - Projects/AI Research Framework/04 - Architecture/airl_os_role_model_assignment\|Rol → Model Atama]] | **Kim** yürütür — insan / model / kod? |

## Altı düzlem + öneri

| Düzlem | Sahibi | Durum |
|---|---|---|
| Experience | Obsidian + Cockpit | V0 kurulu |
| Control | Temporal | planlandı |
| Event | NATS JetStream | planlandı |
| Cognition | LangGraph + RoleContract | planlandı |
| Execution | K8s + Broker + Sandbox | planlandı |
| Evidence & Ops | Registries + WORM | V0 kısmi (SQLite) |
| **Metascience & Calibration** | **önerildi** | **karar bekliyor** |

## Kanonik kopya sınırı

Bu notların kanonik kopyaları `docs/architecture/` altındadır.
Buradakiler wikilink dışında içerik olarak aynı olan Obsidian aynasıdır.
İçerik değişecekse **önce kanonik dosya** değişir.
