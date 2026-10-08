# Append-only nedir?

*Sözlük · Veri & Altyapı · Son güncelleme: 24 Ağustos 2026*

Verilerin sadece sona eklenebildiği, değiştirilemediği veya silinemediği bir kayıt yöntemidir.

## Tanım

Bir veri tabanına veya dosyaya bilgi eklerken, eski verileri değiştirmek yerine her yeni bilgiyi listenin sonuna ekleme prensibidir. Bu yöntem, verinin geçmişini korumak ve güvenliğini sağlamak için kritiktir. Hiçbir veri silinmediği için sistemdeki tüm hareketlerin izini sürmek mümkündür.

*Bir muhasebe defterine kurşun kalemle yazmak yerine, tükenmez kalemle her işlemi bir alt satıra yazmak gibidir; eski sayfaları karalayamazsınız.*

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

- [Database](https://trescout.com/dictionary/database/)
- [Logs](https://trescout.com/dictionary/logs/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/append-only/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
