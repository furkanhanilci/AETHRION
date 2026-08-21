# WP-134 — Eskalasyon ve Paging

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-134` |
| Workstream | `13_TOOLING_INTEGRATION` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | SRE Lead |
| Bağımsız doğrulayıcı | Assurance Lead |
| Hard dependencies | WP-131, WP-132, WP-004 (İnsan kararı SLA) |
| İlgili gate | G0–G10 |
| İlgili kontroller | CTL-GOV-03, CTL-OBS-01 |
| İlgili ACC senaryoları | ACC-26, ACC-43 |
| İlgili skill | `escalating-and-paging` |

## Amaç ve beklenen sonuç

SLA aşımı, bütçe hard-stop, bütünlük şüphesi ve hat durdurma olayları
tanımlı bir zincirde yükseltilir.

> **Değişmez:** Zaman aşımı **asla otomatik onaya dönüşmez.** Ya bir üst role
> eskale olur ya da workflow pause kalır.

Her basamakta **onaylama (acknowledgement) zorunludur**. Onaylanmayan eskalasyon
bir sonraki basamağa çıkar; kaybolmaz.

`CRITICAL` şiddetindeki olaylar **sessiz saat politikasını deler**: bütünlük
şüphesi, sandbox kaçış girişimi, bütçe hard limiti ve negatif kontrolde bulgu
beklemez.

## Kapsam dışı

- Eskalasyon kararının içeriği (ilgili gate paketinin işi)

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: WP-131, WP-132, WP-004 (İnsan kararı SLA)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Tamamlanma kanıtı |
|---|---|---|
| WP-134-T01 | Eskalasyon zincirini ve basamak SLA'larını tanımla | Zincir kaydı |
| WP-134-T02 | Tetikleyici → şiddet → kanal matrisini kur | Matris + her satır için test |
| WP-134-T03 | Onaylama (ack) mekanizması ve onaylanmayan eskalasyonun yükselmesi | Ack'siz eskalasyon üst basamağa çıkar |
| WP-134-T04 | Sessiz saat politikası ve `CRITICAL` delme kuralı | Sessiz saatte CRITICAL gönderilir |
| WP-134-T05 | Gürültü kontrolü: aynı olay için tekrar birleştirilir | Tekrar eden eskalasyon çoğaltılmaz |
| WP-134-T06 | Eskalasyon telemetrisi (yanıt süresi, ack oranı, yanlış pozitif) | Ölçüm Metascience'a akar |

## Zorunlu teslimatlar

- Eskalasyon zinciri ve SLA kaydı
- Tetikleyici → şiddet → kanal matrisi
- Acknowledgement mekanizması
- Sessiz saat politikası
- Eskalasyon telemetrisi

## Test ve doğrulama planı

- **Auto-approve yok:** SLA dolduğunda durum kendiliğinden ilerlemiyor (negatif test)
- **Ack zinciri:** onaylanmayan eskalasyon N dakika sonra üst basamağa çıkar
- **CRITICAL delme:** sessiz saatte CRITICAL bildirimi bastırılmaz
- **Birleştirme:** aynı olay için 10 tetikleme → 1 bildirim + sayaç

## Kabul kriterleri

- [ ] SLA aşımından sonra hiçbir gate kendiliğinden geçmiyor
- [ ] Onaylanmayan her eskalasyon üst basamağa çıkıyor; hiçbiri kaybolmuyor
- [ ] `CRITICAL` sessiz saatte bastırılmıyor
- [ ] Yanlış pozitif oranı ölçülüyor ve eşikler ona göre ayarlanıyor
- [ ] Bütün zorunlu testler aynı target revision üzerinde geçmiştir.
- [ ] Açık Critical/High finding yoktur.
- [ ] Bağımsız verifier kanıt paketini kabul etmiştir.

## Riskler ve kontrol noktaları

- Eskalasyon yorgunluğu eskalasyonun kendisinden tehlikelidir; yanlış pozitif oranı izlenir
- Eşik kapatma yasaktır; eşik **ölçerek** ayarlanır
- Paket tamamlandı beyanı acceptance değildir; verifier kararı olmadan yalnız `TECH_COMPLETE` olabilir.

## Rollback / compensation

Eskalasyon kanalı devre dışı bırakılırsa workflow **pause** olur — sessizce
ilerlemez. Bu davranış non-waivable'dır.

## Handoff ve sonraki paketlere giriş

WP-135 karar bekleyen olayların yönlendirmesini bu zincire bağlar.
