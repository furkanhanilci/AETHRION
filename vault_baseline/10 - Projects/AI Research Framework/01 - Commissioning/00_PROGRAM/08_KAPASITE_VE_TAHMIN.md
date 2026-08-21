# Kapasite ve Tahmin Modeli

## Neden sabit takvim yok?

Hedef sistem ekip büyüklüğü, mevcut altyapı, yönetilen servis tercihleri, veri sınıfları ve kurum kontrollerine göre büyük ölçüde değişir. Bu nedenle dosyalar efor sınıfı taşır; takvim WP-001 sonrası gerçek kapasiteyle hesaplanır.

## Üç nokta tahmini

Her paket refinement'ta şu değerleri alır:

- `O`: Contract ve altyapı hazırsa iyimser kişi-gün.
- `M`: Beklenen kişi-gün.
- `P`: Migration, güvenlik veya entegrasyon sürprizi varsa kötümser kişi-gün.
- PERT: `(O + 4M + P) / 6`.

## Kapasite havuzları

| Havuz | Örnek roller | Korunacak kapasite |
|---|---|---|
| Architecture/Contracts | Chief Architect, schema owner | Contract ve ADR review |
| Platform/SRE | Platform, DB, network, SRE | Foundation, HA, DR |
| Security/Governance | Security, Safety, IAM, privacy | Policy, threat test, approval |
| Research/Knowledge | Method, evidence, librarian | Literature ve claim semantics |
| Assurance/Eval | Reviewer, verifier, reproducer | Bağımsız kabul; feature ekibine tüketilmez |
| Product/Experience | UI, CLI, UX, accessibility | Cockpit ve decision surfaces |

## WIP sınırları

- Bir owner aynı anda en fazla iki `IN_PROGRESS` paket taşır.
- Assurance havuzu kapasitesinin en az %25'i correction ve re-verification için ayrılır.
- Critical-path paketleri için bağımlı ekip takviminde önceden entegrasyon penceresi ayrılır.
- Foundation dalgasında UI veya raporlama nedeniyle control/evidence contract geciktirilmez.
- Cutover öncesi son iki commissioning döngüsünde yeni feature paketi açılmaz.

## Takvime çevirme

1. Tüm READY paketleri üç nokta tahminle ölçün.
2. Rol havuzu başına gerçek haftalık kapasiteyi tatil/on-call/BAU düşülmüş hesaplayın.
3. Hard dependency grafında kritik yolu çıkarın.
4. Review/reproduction gecikmesini ayrı queue olarak modelleyin.
5. En az %20 entegrasyon ve correction rezervi koyun.
6. Production tarihini WP-115 acceptance burn-down ve WP-119 rehearsal sonucuna göre doğrulayın.

Takvim baskısı hedef yetenekleri sonraya atmak için kullanılamaz. Gerekirse kapsam değil, production tarihi değişir.
