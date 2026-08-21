# WP-131 — Notification Broker Temeli

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-131` |
| Workstream | `13_TOOLING_INTEGRATION` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Platform Security Lead |
| Bağımsız doğrulayıcı | Safety & Governance Owner |
| Hard dependencies | WP-049 (Tool Registry/Broker), WP-016 (PolicyDecision şemaları) |
| İlgili gate | Platform |
| İlgili kontroller | CTL-SEC-04, CTL-DAT-02 |
| İlgili ACC senaryoları | ACC-41, ACC-42 |
| İlgili skill | `notifying-humans` |

## Amaç ve beklenen sonuç

Ajanların insanlara ulaşması için **Tool Broker'ın bir alt sınıfı** kurulur.
Ajan bir bildirim **niyeti** üretir; gönderimi yalnız broker yapar.

> **Değişmez:** Ajan hiçbir mesajı doğrudan göndermez. Her gönderim
> kimlik → policy → veri sınıfı → DLP → idempotency → gönderim →
> `NotificationReceipt` zincirinden geçer.

Bildirim `T3` yan etki sınıfındadır (dış sistem mutasyonu) ve ExecutionProfile'ın
varsayılan-reddet ağ politikasında **açık bir egress istisnası** gerektirir.

## Kapsam dışı

- Kanal başına konnektör implementasyonu (WP-132)
- Gelen mesaj işleme (WP-136)
- Karar yetkilendirme (WP-135)

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: WP-049 (Tool Registry/Broker), WP-016 (PolicyDecision şemaları)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Tamamlanma kanıtı |
|---|---|---|
| WP-131-T01 | Broker arayüzünü ve `NotificationIntent` şemasını tanımla | Şema dosyası + contract testi |
| WP-131-T02 | Policy kontrol zincirini kur (kimlik, TaskContract, veri sınıfı) | Zincirin her adımı için negatif test |
| WP-131-T03 | Idempotency anahtarı üretimi ve tekrar-gönderim engeli | Aynı anahtarla ikinci çağrı gönderim yapmaz |
| WP-131-T04 | `NotificationReceipt` ve `ToolReceipt` üretimi | Her gönderim için kayıt; kayıtsız gönderim imkânsız |
| WP-131-T05 | Rate limit ve sessiz saat politikası | Eşik aşımında gönderim ertelenir, düşmez |
| WP-131-T06 | Taşıyıcı soyutlaması (Apprise veya eşdeğeri) arkasına konur | Kanal değişimi broker sözleşmesini değiştirmez |

## Zorunlu teslimatlar

- `NotificationBroker` servis arayüzü ve implementasyonu
- `NotificationIntent` ve `NotificationReceipt` şemaları
- Policy zinciri ve idempotency kayıt defteri
- Egress allowlist tanımı
- Güncellenmiş runbook ve servis ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- **Ajan doğrudan gönderemez:** broker dışından yapılan gönderim denemesi reddedilir
- **Idempotency:** aynı anahtarla iki çağrı → tek gönderim, iki receipt aynı `sent_id`
- **Timeout davranışı:** yanıt gelmezse körlemesine tekrar yok; durum sorgulanır
- **Rate limit:** eşik aşımında kuyruğa alınır, sessizce düşmez
- Yetkisiz, eksik, duplicate ve partial-failure girdileri için negatif test

## Kabul kriterleri

- [ ] Broker dışından yapılan hiçbir gönderim başarılı olamaz (statik + runtime kontrol)
- [ ] Her gönderim tam olarak bir `NotificationReceipt` üretir; receiptsiz gönderim yoktur
- [ ] Aynı idempotency anahtarıyla N çağrı → tam olarak 1 gönderim
- [ ] Timeout sonrası otomatik tekrar gönderim **sıfırdır**
- [ ] Bütün zorunlu testler aynı target revision üzerinde geçmiştir.
- [ ] Açık Critical/High finding yoktur.
- [ ] Bağımsız verifier kanıt paketini kabul etmiştir.

## Riskler ve kontrol noktaları

- Broker devre dışıyken bildirim **sessizce kaybolmaz**; kuyruğa alınır ve kuyruk derinliği izlenir
- Egress allowlist genişletmesi Safety/Data Owner onayı gerektirir
- Paket tamamlandı beyanı acceptance değildir; verifier kararı olmadan yalnız `TECH_COMPLETE` olabilir.

## Rollback / compensation

Broker devre dışı bırakılır; bekleyen bildirimler kuyrukta kalır ve yeniden etkinleştirmede
sırayla gönderilir. Gönderilmiş bildirim geri alınamaz — bu yüzden gönderim öncesi kontroller
non-waivable'dır.

## Handoff ve sonraki paketlere giriş

WP-132 kanal kaydını, WP-133 giden akışları, WP-134 eskalasyonu ve WP-135 karar
yönlendirmesini bu broker üzerine kurar. Hiçbiri broker olmadan başlatılmaz.
