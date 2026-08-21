# WP-133 — Giden Bildirim ve Periyodik Digest

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-133` |
| Workstream | `13_TOOLING_INTEGRATION` |
| İlk efor sınıfı | **S** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | SRE Lead |
| Bağımsız doğrulayıcı | Metascience Lead |
| Hard dependencies | WP-131, WP-132 |
| İlgili gate | G10 |
| İlgili kontroller | CTL-OBS-01 |
| İlgili ACC senaryoları | ACC-41 |
| İlgili skill | `notifying-humans`, `publishing-digests` |

## Amaç ve beklenen sonuç

Operasyonel bildirimler ve periyodik özetler yayınlanır. Özet **salt-okunur
bir türevdir**: karar taşımaz, hiçbir durumu değiştirmez.

Ritim:

| Sıklık | İçerik | Alıcı |
|---|---|---|
| Günlük | Açık kararlar, SLA riski, dünkü koşumlar, bütçe, dikkat bütçesi kullanımı | Decision Owner |
| Haftalık | Portföy, gate akışı, bloke işler, açık bulgular | Tüm roller |
| **Aylık** | **Metascience karnesi**: kalibrasyon, uyum, gate yield, kontrol FP/FN, claim survival | Assurance + Metascience |
| Çeyreklik | Maliyet, model requalification, olay analizi | FinOps + Platform |

> Aylık metascience özeti laboratuvarın karnesidir. Kötü görünüyorsa gizlenmez;
> özetin başında görünür.

## Kapsam dışı

- Metascience ölçümlerinin kendisi (ayrı workstream)
- Karar yetkilendirme (WP-135)

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: WP-131, WP-132
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Tamamlanma kanıtı |
|---|---|---|
| WP-133-T01 | Bildirim tiplerini ve şablonlarını tanımla | Şablon kaydı |
| WP-133-T02 | Aciliyet → kanal eşlemesini kur | Eşleme tablosu + test |
| WP-133-T03 | Günlük ve haftalık digest üreticisi | Üretim hiçbir durumu değiştirmez (kanıt) |
| WP-133-T04 | Aylık metascience digest'i | `UNCALIBRATED` alanlar sayı gibi sunulmaz |
| WP-133-T05 | Digest kaynaklarının salt-okunur olduğunu zorla | Yazma denemesi testte reddedilir |

## Zorunlu teslimatlar

- Bildirim şablon kaydı
- Aciliyet → kanal eşlemesi
- Günlük / haftalık / aylık / çeyreklik digest üreticileri
- Salt-okunur kaynak garantisi

## Test ve doğrulama planı

- **Yan etkisizlik:** digest üretimi öncesi/sonrası kanonik durum hash'i aynı
- **Kalibrasyon dürüstlüğü:** yetersiz veri olan boyut `UNCALIBRATED` olarak render edilir
- **Kanal eşlemesi:** her aciliyet seviyesi doğru kanala gider
- Boş veri, kısmi veri ve hata durumunda digest üretimi çökmeden eksik alanı işaretler

## Kabul kriterleri

- [ ] Digest üretimi hiçbir canonical kaydı değiştirmiyor (hash kanıtı)
- [ ] `UNCALIBRATED` alanlar sayı olarak gösterilmiyor
- [ ] Kötü metrikler ekte değil, özetin başında
- [ ] Günlük özet dikkat bütçesi kullanımını gösteriyor
- [ ] Bütün zorunlu testler aynı target revision üzerinde geçmiştir.
- [ ] Açık Critical/High finding yoktur.
- [ ] Bağımsız verifier kanıt paketini kabul etmiştir.

## Riskler ve kontrol noktaları

- Digest yorgunluğu: çok sık veya çok uzun özet okunmaz hale gelir; okunma oranı izlenir
- Özet üretimi bir durum değiştirirse bu bir Critical bulgudur
- Paket tamamlandı beyanı acceptance değildir; verifier kararı olmadan yalnız `TECH_COMPLETE` olabilir.

## Rollback / compensation

Digest yayını durdurulur; kaynak veriler etkilenmez.

## Handoff ve sonraki paketlere giriş

WP-134 aynı kanal eşlemesini eskalasyon için kullanır.
