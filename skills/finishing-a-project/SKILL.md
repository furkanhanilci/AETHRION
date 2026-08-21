---
name: finishing-a-project
version: 1.0.0
description: Use when work appears complete, when a project is about to be closed, published, superseded, retracted or abandoned
gates: [G8, G9]
roles: [Project Decision Owner, Assurance Lead]
assurance_classes: [R1, R2, R3]
non_waivable: true
requires_skills: [verification-before-completion, scope-discipline]
emits: [DecisionRecord, PublicationPackage]
mechanical_checks: [all_verifications_green, exact_confirmation_word_received]
---

# Finishing a Project

## Genel ilke

Kapanış bir sunum onayı değildir. Doğrulama kırmızıysa menü **gösterilmez**.

## Kapanış kontrol listesi

1. **Tam doğrulama paketini çalıştır** — taze koşum
   - Testler, şema kontrolleri, mekanik adli kontroller (statcheck, GRIM)
   - Scope conformance
   - Manifest/hash bütünlüğü
   - **Herhangi biri kırmızıysa DUR ve raporla**
2. **Ortam durumunu yakala** — hangi target, hangi bundle sürümleri
3. **Baz referansı doğrula** — hangi manifest'ten türedi
4. **Açık bulguları listele** — `FindingLedger`'da statüsüz satır var mı?
5. **İNSANA MENÜ SUN**
6. Seçimi uygula
7. Temizlik — kanıt hariç

## İnsan menüsü

| Seçenek | Sonuç |
|---|---|
| `ACCEPT` | `DecisionRecord` imzalanır, G9'a geçer |
| `CONDITIONAL_ACCEPT` | Kapsam kısıtı ile kabul; `obligations` yazılır |
| `REVISE` | Belirli değişiklik istenir; hangi gate'e döneceği yazılır |
| `ADDITIONAL_EVIDENCE` | Ek koşum/review istenir |
| `REJECT` | Yalnız protokol ihlali, bütünlük sorunu veya G7 başarısızlığı gerekçesiyle |

> **`REJECT` gerekçesi "sonuç beklediğim gibi değil" olamaz.**
> Bkz. `preregistration-discipline` ve in-principle acceptance.

## Tam kelime onayı — yıkıcı işlemler

Aşağıdaki işlemler **yalnız tam kelime yazıldığında** yetkilendirilir:

| İşlem | Gerekli kelime |
|---|---|
| Claim geri çekme | `RETRACT` |
| Yayın supersede | `SUPERSEDE` |
| Proje iptali | `ABANDON` |
| Literature set çözme | `UNFREEZE` |

> "Tamam kaldır", "olur iptal et", "evet sil" **yetki değildir.**

## Zaman aşımı

Karar SLA'sı dolduğunda **auto-approve yoktur.** Ya bir üst role eskale olur
ya da workflow pause kalır.

## Kırmızı bayraklar

- Menü doğrulama kırmızıyken sunulmuş
- Açık bulgular listelenmeden karar istenmiş
- Yıkıcı işlem için tam kelime alınmamış
- Karar süresi anormal kısa (bkz. dikkat bütçesi telemetrisi)
