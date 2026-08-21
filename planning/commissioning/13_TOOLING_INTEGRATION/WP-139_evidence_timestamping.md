# WP-139 — Kanıt Zaman Damgalama ve Bağımsız Mühür

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-139` |
| Workstream | `13_TOOLING_INTEGRATION` |
| İlk efor sınıfı | **S** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Data Platform Lead |
| Bağımsız doğrulayıcı | Research Integrity Officer |
| Hard dependencies | WP-014 (Artifact manifest), WP-026 (Object store WORM) |
| İlgili gate | G2, G5, G9 |
| İlgili kontroller | CTL-DAT-03, CTL-SUP-01 |
| İlgili ACC senaryoları | ACC-23, ACC-40 |
| İlgili skill | `verification-before-completion` |

## Amaç ve beklenen sonuç

Bir `EvidenceManifest`'in belirli bir zamanda var olduğu, **sizin
sisteminize güvenmeden** kanıtlanabilir hale getirilir.

Bu, WP-000 (Interim Evidence Policy) probleminin altyapısız çözümüdür:
imzalı manifest ve immutable store hazır olmadan da zaman kanıtı üretilebilir.

| Yöntem | Güvenilir üçüncü taraf | Maliyet | Not |
|---|---|---|---|
| **OpenTimestamps** | **gerekmiyor** | ücretsiz | Yalnız hash gönderilir; dosya makineden çıkmaz. Bitcoin'e çapalanır, herkes bağımsız doğrular |
| **RFC 3161 TSA** | gerekli (TSA) | ücretsiz seçenekler var | TSA anahtarı süresi dolarsa ek kanıt gerekir |
| Sigstore / cosign | Sigstore altyapısı | ücretsiz | WP-027/059 ile birlikte |
| Git tag imzası | anahtar sahibi | ücretsiz | Zayıf: saat manipüle edilebilir |

> **Öneri:** OpenTimestamps birincil, RFC 3161 ikincil. İkisi birlikte
> hem üçüncü-taraf-bağımsız hem hızlı doğrulanabilir bir mühür verir.

**Kritik kullanım:** `AnalysisPlanManifest` G2'de kilitlendiğinde hash'i
zaman damgalanır. Bu, ön-kayıt disiplininin "plan sonuçtan önce vardı"
iddiasını **dışarıdan doğrulanabilir** kılar.

## Kapsam dışı

- Manifest içeriğinin kendisi (WP-014)
- İmza altyapısı (WP-027, WP-059)

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: WP-014 (Artifact manifest), WP-026 (Object store WORM)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Tamamlanma kanıtı |
|---|---|---|
| WP-139-T01 | `EvidenceManifest` hash'ini OpenTimestamps'e gönder | `.ots` kanıt dosyası üretilir |
| WP-139-T02 | RFC 3161 TSA ikincil damgası | `.tsr` yanıtı saklanır |
| WP-139-T03 | Damga dosyalarını manifest'e ve object store'a bağla | Damgasız manifest kabul edilmez |
| WP-139-T04 | Doğrulama komutu ve runbook | Üçüncü taraf bağımsız doğrulayabilir |
| WP-139-T05 | G2 analiz planı kilidinde otomatik damgalama | Plan kilidi = damga anı |
| WP-139-T06 | Damga gecikmesi ve olgunlaşma takibi | Bekleyen damgalar izlenir |

## Zorunlu teslimatlar

- OpenTimestamps ve RFC 3161 damgalama akışı
- `.ots` / `.tsr` kanıt dosyalarının saklanması
- Doğrulama komutu ve runbook
- G2 otomatik damgalama entegrasyonu

## Test ve doğrulama planı

- **Bağımsız doğrulama:** üçüncü bir makinede, framework olmadan damga doğrulanıyor
- **Ön-kayıt kanıtı:** plan damgası sonuç artifact'ının damgasından **önce**
- **Damgasız manifest:** kabul edilmiyor (negatif test)
- **Olgunlaşma:** bekleyen OpenTimestamps kanıtı takip ediliyor ve tamamlanıyor
- **Saat manipülasyonu:** yerel saat değiştirildiğinde damga bunu yansıtmıyor

## Kabul kriterleri

- [ ] Bir `EvidenceManifest`'in varlık zamanı, framework'e güvenmeden doğrulanabiliyor
- [ ] `AnalysisPlanManifest` kilidi otomatik damgalanıyor
- [ ] Damga dosyaları manifest ve object store ile birlikte saklanıyor
- [ ] Doğrulama runbook'u üçüncü bir tarafça uygulanabilir
- [ ] Bütün zorunlu testler aynı target revision üzerinde geçmiştir.
- [ ] Açık Critical/High finding yoktur.
- [ ] Bağımsız verifier kanıt paketini kabul etmiştir.

## Riskler ve kontrol noktaları

- OpenTimestamps damgası olgunlaşana kadar birkaç saat sürebilir; bu süre içinde
  RFC 3161 damgası köprü görevi görür
- Damga yalnız **varlık zamanını** kanıtlar, içeriğin doğruluğunu değil
- Paket tamamlandı beyanı acceptance değildir; verifier kararı olmadan yalnız `TECH_COMPLETE` olabilir.

## Rollback / compensation

Damgalama devre dışı bırakılırsa yeni manifest'ler damgasız kalır; eski damgalar
geçerliliğini korur. Geriye dönük damgalama **yapılamaz** — bu, damganın anlamıdır.

## Handoff ve sonraki paketlere giriş

WP-000 (Interim Evidence Policy) bu mekanizmayı geçici kanıt deposunun
zaman kanıtı olarak kullanır. WP-138 dış kayıtla birlikte iki bağımsız tanık verir.
