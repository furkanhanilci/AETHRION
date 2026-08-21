# Mimari Kapsam → İş Paketi Karşılık Matrisi

Bu matris, “bir bileşen veya yönetişim alanı plan dışında kaldı mı?” sorusunun hızlı denetimidir. Ayrıntılı bağımlılıklar `03_PAKET_KATALOGU.md` ve `paket_bagimlilik_matrisi.csv` içindedir.

| Hedef mimari alanı | Birincil iş paketleri | Entegrasyon/kabul |
|---|---|---|
| Program, kapsam, NFR, ADR | WP-001–002, WP-010 | WP-115, WP-120 |
| Roller, RACI, human decision | WP-003–004 | WP-102, WP-106, ACC-25–26 |
| Risk/assurance | WP-005, WP-008 | WP-102, WP-105 |
| ExecutionProfile: data/code/effect/network | WP-006 | WP-112, ACC-15–18 |
| Independence matrix | WP-007 | WP-105, ACC-06–08, ACC-38 |
| Control ve exception | WP-009, WP-016, WP-056 | WP-112, WP-123 |
| Kimlik/correlation | WP-011 | WP-096, ACC-40 |
| Canonical field authority | WP-012 | WP-103, ACC-03/22/28 |
| Task/role/agent contracts | WP-013, WP-047 | WP-102, WP-107 |
| Artifact/dataset immutability | WP-014, WP-026 | WP-104, ACC-23 |
| Event/outbox/NATS | WP-015, WP-028, WP-039 | WP-111, ACC-12/34 |
| Source/literature schemas | WP-017 | WP-061–072 |
| Claim/review/decision schemas | WP-018 | WP-075–090 |
| Run/environment/repro schemas | WP-019 | WP-081–085 |
| Schema registry/SDK | WP-020 | Bütün servis contract testleri |
| Dev/staging/prod ve network | WP-021, WP-051 | WP-112/114/119 |
| Repository/worktree/CI | WP-022–024 | WP-107 |
| PostgreSQL/object store/MLflow | WP-025–026, WP-029 | WP-104/114 |
| Derived graph/vector/search | WP-030 | WP-095, ACC-21 |
| Temporal ve G0–G10 | WP-031–040 | WP-102–106, ACC-13–14 |
| LiteLLM/Capability/Admission | WP-041–045 | WP-124, ACC-10/11/36/37 |
| LangGraph ve runtime adapter | WP-046–048 | WP-107 |
| Tool Broker/connectors | WP-049–050 | ACC-05/12/35 |
| Kubernetes/Kueue/gVisor | WP-052–054 | WP-116/117, ACC-15/33 |
| SPIFFE/Vault/OPA/egress | WP-055–057 | WP-112, ACC-16/18/25/26/32 |
| Content quarantine | WP-058 | ACC-05 |
| Sigstore/SLSA/supply chain | WP-027, WP-059 | ACC-17 |
| Agentic red team | WP-060 | WP-112/123 |
| Source Registry/resolver/status | WP-061–063 | WP-103/108, ACC-03/04 |
| Zotero library/seed/write/sync | WP-064–068 | WP-103/125, ACC-01/02/03/28 |
| İki yönlü literatür/screening | WP-069–071 | WP-103, ACC-01–03 |
| Immutable LiteratureSetManifest | WP-072 | WP-103/106, ACC-01/30 |
| Obsidian human/generated zones | WP-073–074 | WP-113/125, ACC-22 |
| Claim/Evidence Ledger | WP-075–080 | WP-104–106, ACC-04/08/30 |
| Protocol/run/experiment | WP-081–083 | WP-104, ACC-09/33/39 |
| Clean-room ve dört doğrulama türü | WP-084–085 | WP-105/113, ACC-19/20 |
| Blind review/verifier/arbitration | WP-086–089 | WP-105/126, ACC-06/07/08/38 |
| Publication/RO-Crate | WP-090 | WP-106, ACC-30/31/40 |
| Cockpit/decision/literature/claim UI | WP-091–095 | Dikey dilimler ve pilot |
| OTel/Langfuse/Grafana | WP-096–098 | WP-116/121/122 |
| WORM audit | WP-099 | ACC-40 |
| Cost/FinOps | WP-100 | WP-111/127, ACC-09/29 |
| Service SLO/runbooks | WP-101 | WP-118/122 |
| Dikey entegrasyon | WP-102–108 | WP-109–115 |
| Kırk acceptance senaryosu | WP-109–114, `12_ACCEPTANCE_SCENARIOS/` | WP-115 |
| Chaos/capacity/operational readiness | WP-116–118 | WP-119–120 |
| Pilot/cutover/hypercare | WP-119–121 | Production |
| Sürekli assurance ve işletim | WP-122–130 | Day-2 control evidence |
| **Bildirim ve insan erişimi** | **WP-131–135** | **ACC-25, ACC-26, ACC-41–43** |
| **Gelen içerik ve dış besleme** | **WP-136–137** | **ACC-04, ACC-05, ACC-31, ACC-36, ACC-44** |
| **Dış kayıt ve kanıt mührü** | **WP-138–139** | **ACC-23, ACC-30, ACC-40, ACC-45** |
| **Servis canlılığı** | **WP-140** | **ACC-43** |

## Eksiksizlik kuralı

Yeni bir mimari alanı veya bağlayıcı invariant eklendiğinde bu matriste birincil uygulama paketi, entegrasyon paketi ve kabul/işletim kanıtı bulunmadan değişiklik baseline'a alınmaz.

