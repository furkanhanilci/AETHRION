# WP-140 — Servis Canlılık İzleme ve Dead-Man's Switch

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-140` |
| Workstream | `13_TOOLING_INTEGRATION` |
| İlk efor sınıfı | **S** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | SRE Lead |
| Bağımsız doğrulayıcı | Metascience Lead |
| Hard dependencies | WP-101 (Service SLO), WP-131, WP-134 |
| İlgili gate | Platform, G10 |
| İlgili kontroller | CTL-OBS-01 |
| İlgili ACC senaryoları | ACC-43 |
| İlgili skill | `escalating-and-paging` |

## Amaç ve beklenen sonuç

Periyodik işlerin **çalışmadığını** fark eden bir mekanizma kurulur.

Sessiz ölüm, bu mimarinin en tehlikeli arıza biçimidir: bir besleme, bir timer
veya bir sync durduğunda hiçbir hata üretmez — yalnız hiçbir şey olmaz. Denetim
raporundaki **H1/H2** bulguları (sessiz eksik senkron, silinen kaynağın hayalet
kalması) bu sınıftandır.

**Dead-man's switch deseni:** her periyodik iş, başarıyla bittiğinde bir
"hâlâ hayattayım" sinyali gönderir. Sinyal beklenen pencerede gelmezse
**alarm üretilir** — işin kendisi hata vermemiş olsa bile.

Kapsanacak işler: Zotero sync timer, G10 besleme taramaları, kalibrasyon
koşuları, digest üreticileri, kontrol enjeksiyonu, yedekleme işleri.

## Kapsam dışı

- İşin kendi iç doğruluğu (ilgili paketin işi)

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: WP-101 (Service SLO), WP-131, WP-134
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Tamamlanma kanıtı |
|---|---|---|
| WP-140-T01 | Periyodik iş envanteri ve beklenen aralık kaydı | Envanter dosyası |
| WP-140-T02 | Her iş için başarı sinyali (heartbeat) yayını | Sinyal kaydı |
| WP-140-T03 | Sinyal gelmediğinde alarm (self-hosted izleyici) | Test: işi durdur → alarm gelir |
| WP-140-T04 | Kısmi başarı ayrımı: `SUCCEEDED` vs `PARTIAL` | Eksik senkron `SUCCEEDED` sayılmaz |
| WP-140-T05 | Alarm eskalasyonunu WP-134 zincirine bağla | Onaylanmayan alarm yükselir |
| WP-140-T06 | Canlılık panosu ve son çalışma zamanları | Her iş için son başarı görünür |

## Zorunlu teslimatlar

- Periyodik iş envanteri
- Heartbeat yayını ve izleyici (ör. self-hosted Uptime Kuma / Healthchecks)
- Kısmi başarı ayrımı
- Canlılık panosu

## Test ve doğrulama planı

- **Sessiz ölüm:** işi durdur → beklenen pencerede alarm üretiliyor
- **Kısmi başarı:** eksik kayıt işlenen koşu `PARTIAL` işaretleniyor, `SUCCEEDED` değil
- **İzleyicinin kendisi:** izleyici durursa bu da tespit ediliyor (meta-heartbeat)
- **Alarm eskalasyonu:** onaylanmayan alarm üst basamağa çıkıyor

## Kabul kriterleri

- [ ] Her periyodik iş için beklenen aralık tanımlı ve izleniyor
- [ ] Bir iş sessizce durduğunda **saatler içinde** alarm üretiliyor
- [ ] Kısmi başarı `SUCCEEDED` olarak raporlanamıyor
- [ ] İzleyicinin kendi ölümü de tespit ediliyor
- [ ] Bütün zorunlu testler aynı target revision üzerinde geçmiştir.
- [ ] Açık Critical/High finding yoktur.
- [ ] Bağımsız verifier kanıt paketini kabul etmiştir.

## Riskler ve kontrol noktaları

- İzleyici tek arıza noktası olmamalı; meta-heartbeat zorunlu
- Alarm eşikleri çok dar olursa gürültü, çok geniş olursa geç tespit — ölçerek ayarlanır
- Paket tamamlandı beyanı acceptance değildir; verifier kararı olmadan yalnız `TECH_COMPLETE` olabilir.

## Rollback / compensation

İzleme devre dışı bırakılırsa periyodik işler çalışmaya devam eder ama
sessiz ölüm görünmez hale gelir. Bu bir **High** risktir ve açık waiver gerektirir.

## Handoff ve sonraki paketlere giriş

WP-137 besleme canlılığını, WP-134 alarm eskalasyonunu bu mekanizmaya bağlar.
Metascience düzlemi canlılık verisini gate yield ölçümünde kullanır.
