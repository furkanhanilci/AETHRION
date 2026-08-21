---
name: writing-skills
version: 1.0.0
description: Use when authoring, editing or reviewing any AIRL-OS skill, or when a rule keeps being bypassed by agents
gates: []
roles: [Metascience Lead, Assurance Lead]
assurance_classes: [R1, R2, R3]
non_waivable: true
emits: [Skill, BaselineTestRecord]
---

# Writing Skills

## Genel ilke

Skill, dokümantasyona uygulanmış TDD'dir. Önce ajanın **nasıl başarısız
olduğunu izle**, sonra o spesifik başarısızlıkları kapatan minimum belgeyi yaz.

## Demir kural

> **BAŞARISIZ BİR BASELINE TESTİ OLMADAN SKILL YAZILMAZ.**

İstisna yok: "basit ekleme", "sadece güncelleme", "test edilmemiş küçük
düzeltme". Test edilmemiş iş silinir, baştan başlanır.

## Prosedür

**RED** — Skill olmadan baseline senaryoyu çalıştır. Ajanın davranışını ve
ürettiği gerekçeleri **kelimesi kelimesine** kaydet (`baselines/`).

**GREEN** — Yalnız o başarısızlıkları kapatan minimum skill'i yaz. Yeniden
çalıştır, uyum sağladığını doğrula.

**REFACTOR** — Yeni kaçamak gerekçelerini bul, açıkça kapat, tekrar test et.

## `description` kuralı — kritik

`description` **yalnız tetikleyici koşulu** anlatır, asla prosedürü.

- ✅ `Use when a ClaimCandidate exists without a linked EvidenceSpan`
- ❌ `Use for evidence extraction — find source, extract span, score confidence`

**Sebep:** Prosedürü özetleyen açıklama, ajanın skill'i okumak yerine özeti
izlemesine yol açar. Bu deneysel olarak gözlenmiş bir hata modudur.

## Disiplin skill'leri için zorunlu bölümler

- **Demir kural** — tek cümle, istisnasız
- **Rasyonalizasyon tablosu** — baseline'da gözlenen gerçek gerekçeler + hüküm
- **Kırmızı bayraklar** — skill'in atlandığını gösteren işaretler

Zayıf: *"Plan olmadan analiz mi yaptın? Etiketle."*
Güçlü: *"Plan olmadan analiz mi yaptın? `exploratory`. Kalıcı olarak. İstisna yok: referans diye saklama, 'ön analizdi' deme, 'küçüktü' deme."*

## Boyut sınırı

Giriş skill'leri `<150` kelime. Sık yüklenenler `<200`. Diğerleri `<500`.

## Bileşim

Bağımlı skill'e **referans ver, gömme**:
`**GEREKLİ ARKA PLAN:** airl:anchoring-spans`

## Kırmızı bayraklar

- Baseline testi olmayan skill → geçersiz, birleştirilmez
- Rasyonalizasyon tablosu olmayan disiplin skill'i → dayanıksız
- Birden çok skill'i test etmeden toplu üretmek → ihlal
