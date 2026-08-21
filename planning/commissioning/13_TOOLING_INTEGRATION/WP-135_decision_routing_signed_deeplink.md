# WP-135 — Karar Yönlendirme ve İmzalı Derin Bağlantı

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-135` |
| Workstream | `13_TOOLING_INTEGRATION` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Governance Lead |
| Bağımsız doğrulayıcı | Platform Security Lead |
| Hard dependencies | WP-131, WP-132, WP-055 (SPIFFE/Vault kimlik), WP-093 (Decision Queue UI) |
| İlgili gate | G1, G4, G8, G9 |
| İlgili kontroller | CTL-GOV-01, CTL-SEC-04 |
| İlgili ACC senaryoları | ACC-25, ACC-26 |
| İlgili skill | `routing-decision-requests` |

## Amaç ve beklenen sonuç

İnsan kararı gerektiren olaylar bildirimle **duyurulur**, ama karar
kimlik doğrulamalı bir yüzeyde verilir.

> **Değişmez:** Mesajlaşma bir **bildirim kanalıdır**, yetkilendirme kanalı
> değildir. Hiçbir karar bir sohbet cevabıyla verilemez.

Gerekçe: Telegram/Discord/WhatsApp/e-posta hesapları ele geçirilebilir, taklit
edilebilir, iletilebilir. `DecisionRecord` imzalı ve bağlayıcı bir kayıttır;
kanıt zincirinin sonunu bir sohbet mesajına bağlamak tüm zinciri o kanalın
güvenliğine indirger. Bu, **ACC-25 (Human Approval Forgery)** senaryosunun
önleyici tarafıdır.

Sohbet cevabı **yapabilir**: okundu bilgisi, ek bilgi talebi, SLA uzatma talebi.
**Yapamaz**: onay, ret, yıkıcı işlem.

## Kapsam dışı

- Karar yüzeyinin UI'ı (WP-093)
- Kararın içeriği ve rubriği (ilgili gate paketi)

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: WP-131, WP-132, WP-055 (SPIFFE/Vault kimlik), WP-093 (Decision Queue UI)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Tamamlanma kanıtı |
|---|---|---|
| WP-135-T01 | İmzalı, süreli, tek kullanımlık derin bağlantı üretimi | Süre dolduğunda bağlantı geçersiz |
| WP-135-T02 | Bağlantının yetkiyi değil **yüzeye erişimi** taşıdığını zorla | Bağlantı tek başına karar veremez |
| WP-135-T03 | Kullanıcı-bağlı doğrulama (iletilen bağlantı geçersiz) | Farklı kimlikle açılan bağlantı reddedilir |
| WP-135-T04 | Sohbet kanalından gelen onay/ret girişimini reddet | Girişim loglanır ve reddedilir |
| WP-135-T05 | İnsan dikkat bütçesi kotasını uygula | Kota dolunca kuyruk bekler, auto-approve yok |
| WP-135-T06 | Karar telemetrisi (süre, açılan bölüm, geri alma oranı) | Ölçüm Metascience'a akar |

## Zorunlu teslimatlar

- İmzalı derin bağlantı üretici ve doğrulayıcı
- Kimlik doğrulamalı karar yüzeyi bağlantısı
- Sohbet kanalı onay reddi
- Dikkat bütçesi kotası
- Karar telemetrisi

## Test ve doğrulama planı

- **Sohbetten onay:** kanal üzerinden gelen "onaylıyorum" mesajı karar üretmez
- **Bağlantı süresi:** TTL sonrası bağlantı geçersiz
- **Tek kullanım:** ikinci kullanım reddedilir
- **İletme:** başka kimlikle açılan bağlantı reddedilir
- **Kota:** haftalık kota dolduğunda yeni karar isteği kuyrukta bekler; auto-approve yok

## Kabul kriterleri

- [ ] Hiçbir `DecisionRecord`'un kaynağı bir mesajlaşma kanalı olamaz
- [ ] Derin bağlantı süreli, tek kullanımlık ve kullanıcı-bağlı
- [ ] Kota dolduğunda sistem **bekler**; hızlı gözden geçirme modu yoktur
- [ ] Karar süresi dağılımı ve G10 geri alma oranı ölçülüyor
- [ ] Bütün zorunlu testler aynı target revision üzerinde geçmiştir.
- [ ] Açık Critical/High finding yoktur.
- [ ] Bağımsız verifier kanıt paketini kabul etmiştir.

## Riskler ve kontrol noktaları

- Kota, laboratuvarın çıktı hızını sınırlar. **Bu bir hata değil, tasarımdır.**
- Bağlantı sızıntısı: TTL kısa tutulur; kullanım sonrası iptal edilir
- Paket tamamlandı beyanı acceptance değildir; verifier kararı olmadan yalnız `TECH_COMPLETE` olabilir.

## Rollback / compensation

Derin bağlantı mekanizması devre dışı bırakılırsa kararlar yalnız yüzeyden
verilir; bildirim içeriksiz tetikleyiciye düşer. Karar akışı durmaz.

## Handoff ve sonraki paketlere giriş

WP-136 gelen kanaldan gelen onay girişimlerini reddetme kuralını devralır.
