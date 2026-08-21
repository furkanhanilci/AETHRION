# Definition of Ready ve Definition of Done

## Definition of Ready — bütün paketler

Bir paket `READY` olmak için aşağıdakilerin tamamını karşılamalıdır:

- Paket amacı ve tek teslim sınırı anlaşılır.
- Kapsam dışı maddeler yazılıdır.
- Accountable Owner, implementer ve bağımsız verifier atanmıştır.
- Hard dependency paketleri `ACCEPTED` veya açıkça izin verilen mock contract durumundadır.
- Etkilenen canonical owner ve interface'ler belirlenmiştir.
- DataClass, ToolEffect, CodeTrust ve Network/Credential kapsamı sınıflanmıştır.
- Gerekli environment ve test fixtures erişilebilirdir.
- Acceptance kriterleri ölçülebilir ve test komut/ senaryo sahibi bellidir.
- Migration, rollback veya compensation davranışı tanımlıdır.
- Efor üç nokta tahmini ve kapasite sahibi vardır.
- Açık blocker ve varsayımlar görünürdür.

## Teknik tamamlanma

`TECH_COMPLETE`, yalnız uygulamanın hazır olduğunu söyler:

- Kod/policy/schema/IaC review'a hazırdır.
- Unit ve package-level integration testleri çalışmıştır.
- Gerekli migration ve rollback dry-run yapılmıştır.
- Telemetry, correlation ve audit sinyalleri eklenmiştir.
- Dokümantasyon ve runbook değişiklikleri commit'tedir.
- Evidence manifest taslağı oluşturulmuştur.

## Definition of Done — paket kabulü

- Bütün acceptance kriterleri aynı target revision üzerinde geçmiştir.
- Test sonuçları artifact hash ve environment manifest ile bağlıdır.
- Verifier üreticiden bağımsız doğrulama yapmıştır.
- Security/data/policy negative testleri geçmiştir.
- Contract compatibility ve downstream consumer testleri yeşildir.
- Açık kritik/yüksek bulgu yoktur; kabul edilen orta/düşük riskler named owner ve süre taşır.
- Rollback/compensation davranışı en az bir kez denenmiştir.
- Observability dashboard/alert veya audit query ile çalışma kanıtlanmıştır.
- Evidence manifest imzalanmış ve immutable store'a yazılmıştır.
- Paket durumu `ACCEPTED`; bağımlı dikey dilim geçince `INTEGRATED` olarak kaydedilmiştir.

## Commissioned tanımı

Paket `ACCEPTED` olsa bile production-ready değildir. `COMMISSIONED` olmak için paketi kullanan ilgili ACC senaryolarının tamamı aynı release candidate üzerinde geçmelidir. Kritik pakette bir senaryonun `SKIPPED` olması pass sayılmaz.

## Kabul edilmeyen kanıtlar

- Agent'ın veya implementer'ın serbest metin “başarılı” beyanı.
- Farklı revision/commit üzerinde alınmış test çıktılarının karıştırılması.
- Hash veya environment bilgisi olmayan ekran görüntüsü.
- Reviewer'ın producer trace'ini görerek verdiği bağımsızlık iddiası.
- Mock servisle geçen testin gerçek entegrasyon testi olarak kullanılması.
- Yalnız happy-path demo.
