# Append-only nedir?

**Kategori:** Veri & Altyapı  
**Son güncelleme:** 2026-08-24

Verilerin sadece sona eklenebildiği, değiştirilemediği veya silinemediği bir kayıt yöntemidir.

## Tanım
Bir veri tabanına veya dosyaya bilgi eklerken, eski verileri değiştirmek yerine her yeni bilgiyi listenin sonuna ekleme prensibidir. Bu yöntem, verinin geçmişini korumak ve güvenliğini sağlamak için kritiktir. Hiçbir veri silinmediği için sistemdeki tüm hareketlerin izini sürmek mümkündür.

## Bir benzetmeyle
Bir muhasebe defterine kurşun kalemle yazmak yerine, tükenmez kalemle her işlemi bir alt satıra yazmak gibidir; eski sayfaları karalayamazsınız.

## Nasıl çalışır?
Sistem, veriyi güncelleyen bir komut yerine sadece 'ekle' komutunu kabul eder. Bu sayede verinin tarihçesi her zaman korunmuş olur.

## Nerede kullanılır?
Blokzincir teknolojilerinde, günlük (log) tutma sistemlerinde ve denetlenebilir veri tabanlarında kullanılır.

## Sık karıştırılanlar
Geleneksel veri tabanları ile karıştırılabilir; geleneksel olanlar veriyi güncelleyebilir, bu yöntem ise asla izin vermez.

## Sıkça sorulanlar

**Hata yaparsam ne olur?**  
Hatalı veriyi silmek yerine, hatayı düzelten yeni bir kayıt daha eklersiniz.

**Neden bu kadar güvenli?**  
Veri değiştirilemediği için geçmişe dönük manipülasyon yapmak imkansıza yakındır.

## İlgili terimler
- [Database](/dictionary/database/)
- [Logs](/dictionary/logs/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/append-only/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
