# AI Research Framework Yerel Bilgi Mimarisi — V0

## Amaç

Bu dikey dilim Zotero'yu kaynak otoritesi, SQLite kayıt defterini kanonik
entegrasyon katmanı, Obsidian'ı okunabilir bilgi çalışma alanı ve Hermes'i
salt-okunur agent erişim yüzeyi olarak kullanır.

```text
Zotero Local API (salt-okunur)
        |
        v
AIRL Bridge API @ 127.0.0.1:8765
        |
        +--> SQLite/WAL kanonik kaynak kayıt defteri
        |
        +--> Obsidian: 70 - Literatür Setleri/Zotero Kaynakları
        |
        +--> Hermes MCP: beş salt-okunur araç
```

## Obsidian yerleşimi

```text
00 - Ana Sayfa/
  AI Research Framework Ana Sayfa.md
01 - Gelen Kutusu/
10 - Projeler/
  AI Research Framework/
    AI Research Framework — Mevcut Durum ve Yol Haritası.md
    00 - Plan Navigasyonu ve Yürütme Kokpiti.md
    01 - Commissioning Planı/
20 - Kaynak Notları/                 # insan sentezi
30 - Kavramlar/
40 - İddialar/
50 - Kararlar/
60 - Çalıştırmalar/
70 - Literatür Setleri/
  Literatür Setleri.md               # insan kürasyonu
  Zotero Kaynakları/                 # otomatik yönetilen dal
    00 - Kontrol Panosu/
    01 - Dergi Makaleleri/
    02 - Konferans Bildirileri/
    03 - Raporlar ve Ön Baskılar/
90 - Arşiv/
_Şablonlar/
```

## Değişmezler

1. Bridge ve Zotero bağlantıları yalnız yerel makinede dinler.
2. Zotero'dan veri alma salt-okunurdur; API anahtarı ve yazma işlemi yoktur.
3. `Zotero Kaynakları` dalı yeniden üretilebilir ve elle düzenlenmez.
4. İnsan sentezi `20 - Kaynak Notları`, kürasyonlu setler `70 - Literatür
   Setleri` kökü altında tutulur.
5. Üretilen dosyalar makale başlığıyla adlandırılır; yalnız aynı başlık
   çakışmalarında kararlı `Zotero ITEMKEY` eki kullanılır.
6. Olası kopyalar raporlanır; otomatik silme veya birleştirme yapılmaz.
7. Hermes'e yalnız durum, arama, ayrıntı, kategori ve kopya raporu araçları
   açılır.
8. Senkron tekrarlanabilir; aynı Zotero öğesi aynı kanonik kimliği korur.

## Yetki sınırları

| Bileşen | Okuma | Yazma |
|---|---|---|
| Zotero Local API | Kaynak metadata | Yok |
| Bridge API | Kaynak kayıtları | Yerel SQLite ve otomatik Obsidian dalı |
| Hermes MCP | Beş katalog işlemi | Yok |
| İnsan | Tüm vault görünümü | Otomatik Zotero dalı dışındaki bilgi alanları |

## Ertelenen kapsam

Zotero write-back, otomatik kopya birleştirme, iki yönlü Obsidian senkronu,
uzak API yayını, Temporal/LangGraph/Kubernetes ve üretim kimlik altyapısı V0
kapsamında değildir. Bunlar ayrı kabul ölçütleri ve geri alma planı olmadan
etkinleştirilmemelidir.
