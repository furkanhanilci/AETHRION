# Go-Live Kontrol Listesi

## Zorunlu girişler

- [ ] WP-001–119 ilgili durumlarıyla `COMMISSIONED`.
- [ ] ACC-01–ACC-40 aynı release candidate üzerinde PASS.
- [ ] Açık Critical finding = 0.
- [ ] Açık High finding = 0 veya Commissioning Board tarafından süreli ve non-waivable olmayan açık residual risk.
- [ ] İki bağımsız restore tatbikatı tamamlandı; RPO 0 workflow state, restore RTO hedefi karşılandı.
- [ ] Temporal replay ve açık workflow versioning testi geçti.
- [ ] NATS duplicate/replay/DLQ ve transactional outbox testleri geçti.
- [ ] Sandbox escape, default-deny egress, secret exfiltration ve D3/D4 route negatif testleri geçti.
- [ ] Source Registry↔Zotero full resync duplicate/overwrite üretmedi.
- [ ] Critical claim lineage ve LiteratureSetManifest completeness %100.
- [ ] Critical workflow clean-room reproduction tanımlı toleransta.
- [ ] Model admission, fallback, no-eligible-route ve revoke/impact testleri geçti.
- [ ] Budget %80 ve hard-stop davranışı test edildi.
- [ ] Audit export; policy, model, tool, source, claim, run, cost ve decision zincirini doğruladı.
- [ ] On-call, incident commander, break-glass ve escalation listesi güncel.
- [ ] Capacity/load test sonucu approved workload envelope'ı karşılıyor.
- [ ] Runbook'lar staging'de uygulanmış ve owner tarafından imzalanmış.
- [ ] Cutover rehearsal aynı prosedürle başarılı.
- [ ] Rollback/abort eşikleri ve karar sahipleri açık.

## Cutover kararı

Go-live toplantısı sunum onayı değildir. Commissioning Dossier içindeki test, açık risk, restore, kapasite, security ve assurance kanıtları gözden geçirilir. Karar kaydı şunları taşır:

- release candidate digest;
- policy/schema/model/tool bundle sürümleri;
- geçen ACC senaryoları ve evidence referansları;
- residual riskler ve owner/expiry;
- cutover penceresi ve abort yetkilisi;
- rollback point ve doğrulama sorguları;
- hypercare süresi ve exit kriterleri.

Herhangi bir non-waivable blocker toplantı sırasında keşfedilirse sonuç `BLOCKED` olur; koşullu production açılışı yapılmaz.
