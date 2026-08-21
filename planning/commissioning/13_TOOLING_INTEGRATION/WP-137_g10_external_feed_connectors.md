# WP-137 — G10 Dış Besleme Konnektörleri

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-137` |
| Workstream | `13_TOOLING_INTEGRATION` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Knowledge Monitoring Lead |
| Bağımsız doğrulayıcı | Citation Auditor |
| Hard dependencies | WP-037 (G10 ImpactScan), WP-063 (Source status), WP-136 |
| İlgili gate | G10 |
| İlgili kontroller | CTL-EPI-04 |
| İlgili ACC senaryoları | ACC-04, ACC-31, ACC-36 |
| İlgili skill | `monitoring-external-feeds` |

## Amaç ve beklenen sonuç

Yayın sonrası izleme beslemeleri bağlanır ve sürümlenir.

| Besleme | Ne izler |
|---|---|
| Crossref + Retraction Watch | Atıf verilen kaynak geri çekildi mi? |
| Crossmark | Düzeltme bildirimi |
| PubMed / alan repository | Düzeltme, geri çekme |
| Dataset registry | Veri seti sürüm/geri çekme |
| CVE / güvenlik danışmanlığı | Kullanılan araçta zafiyet |
| Sağlayıcı changelog | Model profili değişti/kaldırıldı |
| Atıf takibi | Bizi kim çürüttü? |

> **Değişmez:** Sessiz supersession yoktur. Material bir sinyal `ImpactCase`
> açar ve insan kararı gerektirir. "Önemsiz" demek bir karardır ve denetlenir.

## Kapsam dışı

- ImpactCase çözüm kararının kendisi (WP-108)

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: WP-037 (G10 ImpactScan), WP-063 (Source status), WP-136
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Tamamlanma kanıtı |
|---|---|---|
| WP-137-T01 | Besleme kaydı: kaynak, sürüm, erişim tarihi, çekme sıklığı | Kayıt dosyası |
| WP-137-T02 | Crossref + Retraction Watch konnektörü | Geri çekme testte yakalanır |
| WP-137-T03 | Dataset registry ve CVE beslemeleri | Sürüm değişimi yakalanır |
| WP-137-T04 | Sağlayıcı model changelog izleme | Model profili değişimi requalification tetikler |
| WP-137-T05 | Materiality skorlama ve gerekçe zorunluluğu | Gerekçesiz materiality kararı reddedilir |
| WP-137-T06 | Besleme canlılık kontrolü (dead-man's switch) | Çalışmayan besleme alarm üretir |

## Zorunlu teslimatlar

- Besleme kaydı (sürüm + erişim tarihi)
- Konnektör implementasyonları
- Materiality skorlama ve gerekçe kaydı
- Besleme canlılık izleme

## Test ve doğrulama planı

- **Geri çekme:** test DOI'si geri çekildiğinde `ImpactCase` açılıyor
- **Cascade:** geri çekilen kaynak → span → claim → yayın → atıf verenler zinciri tam
- **Materiality:** gerekçesiz `material=false` kararı reddediliyor
- **Sessiz ölüm:** besleme N gün çalışmazsa alarm üretiliyor
- Gelen besleme içeriği `receiving-external-messages` kurallarına tabi

## Kabul kriterleri

- [ ] Material sinyal loglanıp geçilemiyor; `ImpactCase` zorunlu
- [ ] Her materiality kararının yazılı gerekçesi var
- [ ] Besleme aylarca çalışmadan fark edilmeden kalamıyor
- [ ] Cascade zinciri uçtan uca test edilmiş
- [ ] Bütün zorunlu testler aynı target revision üzerinde geçmiştir.
- [ ] Açık Critical/High finding yoktur.
- [ ] Bağımsız verifier kanıt paketini kabul etmiştir.

## Riskler ve kontrol noktaları

- Besleme sessizce ölürse izleme kağıt üzerinde kalır; canlılık kontrolü non-waivable
- Besleme içeriği güvenilmezdir; WP-136 kurallarına tabidir
- Paket tamamlandı beyanı acceptance değildir; verifier kararı olmadan yalnız `TECH_COMPLETE` olabilir.

## Rollback / compensation

Besleme durdurulur; açık `ImpactCase`'ler kapanmaz, insan kararına kalır.
Kaçırılan pencere açıkça kaydedilir.

## Handoff ve sonraki paketlere giriş

WP-108 (retraction/drift dikey dilimi) bu beslemeleri tüketir.
