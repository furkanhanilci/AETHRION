# WP-138 — Dış Kayıt ve Kalıcı Kimlik

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-138` |
| Workstream | `13_TOOLING_INTEGRATION` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Data Steward |
| Bağımsız doğrulayıcı | Project Decision Owner |
| Hard dependencies | WP-014 (Artifact manifest), WP-090 (Publication package), WP-131 |
| İlgili gate | G2, G9 |
| İlgili kontroller | CTL-EPI-01 |
| İlgili ACC senaryoları | ACC-30, ACC-45 |
| İlgili skill | `submitting-external-records` |

## Amaç ve beklenen sonuç

İç kayıtlar kendi kendini doğrular; **dış kayıt bağımsız bir tanıktır.**

| Kayıt | Hedef | Gate | Kazanç |
|---|---|---|---|
| Ön-kayıt (protokol + analiz planı) | **OSF Registries** | **G2** | Zaman damgalı, değiştirilemez kayıt + kalıcı DOI, ambargo seçeneği |
| Kod + ortam | Zenodo / Software Heritage | G9 | Kalıcı arşiv + DOI |
| Veri seti | Zenodo / alan repository | G9 | DOI + Croissant metadata |
| Yayın paketi | Zenodo / kurum repository | G9 | RO-Crate + DOI |
| Yazar kimliği | ORCID | G9 | Kalıcı yazar kimliği |

**Neden G2'de dış ön-kayıt:** İç `AnalysisPlanManifest` hash'i sizin
sisteminizde tutulur. Dış bir kayıt, **sizin sisteminize güvenmeyen** birine
karşı da kanıttır. In-principle acceptance'ın dış çapası budur.

> **Değişmez:** Dış gönderim geri alınamaz. Her biri **tam kelime** insan onayı
> gerektirir (`SUBMIT`).

## Kapsam dışı

- Ön baskı gönderimi tam otomatikleştirilemez (arXiv insan adımı gerektirir)
- Yayın içeriğinin kendisi (WP-090)

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: WP-014 (Artifact manifest), WP-090 (Publication package), WP-131
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Tamamlanma kanıtı |
|---|---|---|
| WP-138-T01 | OSF Registries ön-kayıt akışı ve ambargo seçeneği | G2'de zaman damgalı kayıt + DOI |
| WP-138-T02 | Zenodo deposit akışı (kod, veri, yayın) | DOI döner ve manifest'e yazılır |
| WP-138-T03 | ORCID yazar kimliği bağlama | Yayın paketinde ORCID görünür |
| WP-138-T04 | `CITATION.cff` + `CodeMeta` + Croissant üretimi | Metadata dosyaları doğrulanır |
| WP-138-T05 | Tam kelime onay kapısı (`SUBMIT`) | Onaysız gönderim imkânsız |
| WP-138-T06 | Dönen DOI'nin `EvidenceManifest`'e yazılması | Kaydedilmeyen DOI kabul edilmez |

## Zorunlu teslimatlar

- OSF / Zenodo / ORCID konnektörleri
- `ExternalRegistrationRecord` ve `DOIRecord` şemaları
- `CITATION.cff`, `CodeMeta`, Croissant üreticileri
- Tam kelime onay kapısı

## Test ve doğrulama planı

- **Onay kapısı:** `SUBMIT` yazılmadan gönderim yapılmıyor
- **Veri sınıfı:** D2+ içerik dış kayda gidemiyor
- **DOI kaydı:** dönen DOI manifest'e yazılmadan paket kapanmıyor
- **Ambargo:** ambargo seçeneği gönderim anında uygulanıyor
- **Geri alınamazlık:** rollback testi yeni sürüm üretiyor, silme yapmıyor

## Kabul kriterleri

- [ ] Dış gönderim ajan tarafından tetiklenemiyor
- [ ] Her gönderim için tam kelime insan onayı kaydı var
- [ ] Dönen her DOI `EvidenceManifest`'e yazılmış
- [ ] G2 ön-kaydı zaman damgalı ve değiştirilemez
- [ ] Bütün zorunlu testler aynı target revision üzerinde geçmiştir.
- [ ] Açık Critical/High finding yoktur.
- [ ] Bağımsız verifier kanıt paketini kabul etmiştir.

## Riskler ve kontrol noktaları

- Dış kayıt geri alınamaz; düzeltme yeni sürümdür, silme değildir
- Sağlayıcı API'sinin programatik gönderim yolu uygulama öncesi doğrulanmalıdır
- Paket tamamlandı beyanı acceptance değildir; verifier kararı olmadan yalnız `TECH_COMPLETE` olabilir.

## Rollback / compensation

Gönderilmiş kayıt geri alınamaz. Yeni bir sürüm yayınlanır ve eskisi
`SUPERSEDED` olarak işaretlenir. Bu yüzden gönderim öncesi kontroller
non-waivable'dır.

## Handoff ve sonraki paketlere giriş

WP-139 iç kanıt mühürlemesini, WP-090 yayın paketini bu kayıtlara bağlar.
