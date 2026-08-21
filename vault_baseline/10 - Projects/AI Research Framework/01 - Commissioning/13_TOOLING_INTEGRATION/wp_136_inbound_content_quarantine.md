# WP-136 — Gelen İçerik Karantinası ve Kanal Allowlist

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-136` |
| Workstream | `13_TOOLING_INTEGRATION` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Content Security Lead |
| Bağımsız doğrulayıcı | Safety & Governance Owner |
| Hard dependencies | WP-058 (Content Quarantine Firewall), WP-131, WP-132 |
| İlgili gate | G0, G3, G10 |
| İlgili kontroller | CTL-SEC-02 |
| İlgili ACC senaryoları | ACC-05, ACC-44 |
| İlgili skill | `receiving-external-messages` |

## Amaç ve beklenen sonuç

Gelen her mesaj, e-posta, webhook ve dış doküman **Zone 3** kabul edilir.

> **Değişmez:** Gelen mesaj asla bir talimat değildir. Veridir, komut değil.

Giden trafik bir **veri sızıntısı** riskidir; gelen trafik bir **kontrol
devralma** riskidir. E-posta, PDF eki veya sohbet mesajı içine gömülü metin,
ajan bağlamına girdiğinde prompt injection olur — `ACC-05` senaryosu mesajlaşma
yüzeyiyle genişler.

Karantina sırası: gönderen doğrulaması (SPF/DKIM/DMARC, bot kimliği, kanal
allowlist) → ek/dosya taraması → içeriğin `<untrusted-external-content>` olarak
işaretlenmesi → ajan bağlamına **yalnız bu işaretle** girmesi → **talimat
çıkarımı yapılmaması**.

## Kapsam dışı

- İçeriğin bilimsel değerlendirmesi (G0/G3 paketlerinin işi)

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: WP-058 (Content Quarantine Firewall), WP-131, WP-132
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Tamamlanma kanıtı |
|---|---|---|
| WP-136-T01 | Kanal ve gönderen allowlist kaydı | Allowlist dışı gönderen karantinada kalır |
| WP-136-T02 | Gönderen doğrulaması (SPF/DKIM/DMARC, bot kimliği) | Sahte gönderen reddedilir |
| WP-136-T03 | Ek ve dosya taraması (malware, makro, gömülü script) | Zararlı ek bağlama girmez |
| WP-136-T04 | `<untrusted-external-content>` işaretleme zorunluluğu | İşaretsiz dış içerik bağlama giremez |
| WP-136-T05 | Talimat çıkarımı yasağını zorla | Gelen metinden görev üretilmez |
| WP-136-T06 | Gelen mesaj → hedef akış yönlendirmesi (G0 intake / not / kaynak / feed) | Her tip doğru akışa gider |

## Zorunlu teslimatlar

- Kanal ve gönderen allowlist
- Gönderen doğrulama zinciri
- Ek tarama hattı
- `QuarantineRecord` şeması
- Untrusted işaretleme zorlaması

## Test ve doğrulama planı

- **Prompt injection:** talimat gömülü e-posta ve PDF → ajan davranışı değişmiyor
- **İşaretsiz içerik:** işaretlenmemiş dış içerik bağlama giremiyor (negatif test)
- **Sahte gönderen:** DKIM/DMARC başarısız mesaj karantinada kalıyor
- **Onay girişimi:** gelen mesajdaki "onaylıyorum" karar üretmiyor
- **Bilinmeyen gönderen:** içerik bağlama girmiyor, insana özet bildiriliyor

## Kabul kriterleri

- [ ] Dış içerik işaretlenmeden hiçbir ajan bağlamına giremiyor
- [ ] Gelen metinden talimat çıkarımı yapan hiçbir kod yolu yok
- [ ] Gönderen doğrulaması atlanabilir değil
- [ ] ACC-05 senaryosu mesajlaşma yüzeyinde de geçiyor
- [ ] Bütün zorunlu testler aynı target revision üzerinde geçmiştir.
- [ ] Açık Critical/High finding yoktur.
- [ ] Bağımsız verifier kanıt paketini kabul etmiştir.

## Riskler ve kontrol noktaları

- "Gönderen tanıdık" gerekçesi geçersizdir; gönderen taklit edilebilir
- PDF en yaygın injection taşıyıcısıdır; ek taraması non-waivable'dır
- Paket tamamlandı beyanı acceptance değildir; verifier kararı olmadan yalnız `TECH_COMPLETE` olabilir.

## Rollback / compensation

Gelen kanal kapatılır; karantinadaki içerik silinmez, incelemeye kalır.
Karantina kayıtları audit için korunur.

## Handoff ve sonraki paketlere giriş

WP-137 dış besleme içeriğini bu karantina kurallarına tabi tutar.
