---
airl_id: AI-RESEARCH-FRAMEWORK-PLAN-COCKPIT
type: project
status: active
owner: otonom
created_at: "2026-08-21"
updated_at: "2026-08-21T23:12:00+03:00"
canonical_plan_root: planning/commissioning
obsidian_plan_root: 10 - Projects/AI Research Framework/01 - Commissioning
plan_markdown_count: 184
tags:
  - ai-framework/project
  - ai-framework/plan
  - ai-framework/cockpit
---

# AI Research Framework — Navigation and Execution Cockpit

> [!important] Her adımda kullanım kuralı
> Her maddi çalışma adımından önce sırasıyla bu kokpit, [[10 - Projects/AI Research Framework/ai_research_framework_current_status_and_roadmap|Yaşayan Durum ve Yol Haritası]], aktif görev kaydı ve ilgili WP/ACC planı okunur. Adım tamamlandıktan sonra kanıt doğrulanır; yaşayan durum belgesi ve bu kokpitteki “Güncel yürütme işareti” güncellenir.

## Otorite ve senkron sınırı

- Verilen planın Git içindeki kanonik kopyası: `planning/commissioning/`.
- Obsidian aynası: `10 - Projects/AI Research Framework/01 - Commissioning/`.
- Plan aynasında 184 Markdown dosyası vardır; 13 bölüm ve kök README hiyerarşisi korunmuştur.
- Obsidian plan dosyaları okuma/navigasyon kopyasıdır. Plan içeriği değiştirilecekse önce kanonik Git dosyası değiştirilir, sonra kontrollü olarak aynalanır.
- Gerçek tamamlanma durumu niyet metninden değil Git SHA, komut çıktısı, artifact ve gerekiyorsa bağımsız review kanıtından alınır.

## Güncel yürütme işareti

| Alan | Güncel değer |
|---|---|
| Son maddi adım | FIX-005 bağımsız review handoff hazırlığı |
| SILBO kanıt commit'i | `b14b0b34a115e7cc088008d0a29cf1769f912169` |
| Durum | `ACTIVE / PRE-INFERENCE / TEST+MUTATION PASS` |
| Sıradaki exact adım | `b14b0b3` / `3dd52e0` exact çiftini bağımsız Fable review’a gönder; review olmadan inference yok |
| Yasak sınır | Dry-run/readiness commit'i olmadan inference yok; SILBO remote push yok; training yok |
| Son Obsidian senkronu | 2026-08-21 23:12 +03 — FIX-005 handoff hazır; inference başlatılmadı |

## Önce okunacak program belgeleri

1. [[10 - Projects/AI Research Framework/01 - Commissioning/readme|Program README]]
2. [[10 - Projects/AI Research Framework/01 - Commissioning/00_PROGRAM/00_how_to_use|Planın Kullanımı]]
3. [[10 - Projects/AI Research Framework/01 - Commissioning/00_PROGRAM/01_target_state_and_invariants|Hedef Durum ve İnvariantlar]]
4. [[10 - Projects/AI Research Framework/01 - Commissioning/00_PROGRAM/02_wave_and_dependency_map|Dalga ve Bağımlılık Haritası]]
5. [[10 - Projects/AI Research Framework/01 - Commissioning/00_PROGRAM/03_package_catalog|Paket Kataloğu]]
6. [[10 - Projects/AI Research Framework/01 - Commissioning/00_PROGRAM/05_definition_of_ready_done|Definition of Ready / Done]]
7. [[10 - Projects/AI Research Framework/01 - Commissioning/00_PROGRAM/06_evidence_and_acceptance_strategy|Kanıt ve Kabul Stratejisi]]
8. [[10 - Projects/AI Research Framework/01 - Commissioning/00_PROGRAM/07_program_risk_register|Program Risk Register]]
9. [[10 - Projects/AI Research Framework/01 - Commissioning/00_PROGRAM/09_change_and_configuration_control|Değişiklik ve Konfigürasyon Kontrolü]]
10. [[10 - Projects/AI Research Framework/01 - Commissioning/00_PROGRAM/11_scope_coverage_matrix|Kapsam Karşılık Matrisi]]

## Bölüm haritası

| Bölüm | Kapsam | Markdown |
|---|---|---:|
| `00_PROGRAM` | Program kullanımı, invariantlar, dalgalar, katalog, rol, DoR/DoD, kanıt, risk, kapasite, değişiklik, go-live | 12 |
| `01_GOVERNANCE` | WP-001–010 governance ve commissioning charter | 10 |
| `02_CONTRACTS` | WP-011–020 kimlik, authority, schema ve registry sözleşmeleri | 10 |
| `03_FOUNDATION` | WP-021–030 ortam, repo, CI, veri ve altyapı temelleri | 10 |
| `04_CONTROL_EVENT` | WP-031–040 Temporal, gate, event, replay ve failure suite | 10 |
| `05_MODEL_AGENT_TOOL` | WP-041–050 model gateway, agent runtime ve tool broker | 10 |
| `06_EXECUTION_SECURITY` | WP-051–060 cluster, sandbox, identity, policy, egress ve saldırı testleri | 10 |
| `07_LITERATURE_KNOWLEDGE` | WP-061–074 Zotero, kaynak kimliği, tarama, manifest ve Obsidian | 14 |
| `08_EVIDENCE_ASSURANCE` | WP-075–090 claim/evidence, run, reproducibility, review ve publication | 16 |
| `09_EXPERIENCE_OBSERVABILITY` | WP-091–101 cockpit, trace, Grafana, maliyet ve SLO | 11 |
| `10_INTEGRATION_CUTOVER` | WP-102–121 dikey dilimler, kabul, rehearsal, cutover ve hypercare | 20 |
| `11_DAY2_OPERATIONS` | WP-122–130 işletim, requalification, DR ve continuous assurance | 9 |
| `12_ACCEPTANCE_SCENARIOS` | ACC-01–40 ve senaryo README | 41 |
| Kök | Program README | 1 |
| **Toplam** |  | **184** |

## Aktif işe göre plan yönlendirmesi

| İş türü | Öncelikli planlar |
|---|---|
| Görev aktivasyonu / yönetişim | WP-001, WP-003, WP-005–010 |
| Git, worktree, CI ve kalite kapıları | WP-022–024 |
| Model/evaluation yeterlilikleri | WP-043–045, WP-083, WP-085, WP-087–089 |
| Tool/runtime ve recovery | WP-046–050, ACC-09, ACC-10, ACC-35, ACC-36 |
| Zotero / Obsidian / literatür | WP-061–074, ACC-01–05, ACC-22, ACC-28, ACC-37 |
| Kanıt ve bağımsız review | WP-075–090, ACC-06–08, ACC-19–21, ACC-30–31, ACC-39–40 |
| Production kararı | WP-109–121 ve ACC-01–40 aynı target üzerinde |

## Adım kapanış kontrolü

- [ ] İlgili WP/ACC ve aktif görev okundu.
- [ ] Yetki, maliyet, güvenlik ve geri alma sınırı çözüldü.
- [ ] Komut/test/artifact çıktısı kaydedildi.
- [ ] Durum yalnız kanıt düzeyinde güncellendi.
- [ ] Yaşayan durum belgesi güncellendi.
- [ ] Bu kokpitteki güncel yürütme işareti güncellendi.
- [ ] Git baseline ve Obsidian kopyaları byte-identik doğrulandı.
