# What is Append-only?

Verilerin sadece sona eklenebildiği, değiştirilemediği veya silinemediği bir kayıt yöntemidir.

## Overview
Bir veri tabanına veya dosyaya bilgi eklerken, eski verileri değiştirmek yerine her yeni bilgiyi listenin sonuna ekleme prensibidir. Bu yöntem, verinin geçmişini korumak ve güvenliğini sağlamak için kritiktir. Hiçbir veri silinmediği için sistemdeki tüm hareketlerin izini sürmek mümkündür.

*Analogy: Bir muhasebe defterine kurşun kalemle yazmak yerine, tükenmez kalemle her işlemi bir alt satıra yazmak gibidir; eski sayfaları karalayamazsınız.*

## How it works
Sistem, veriyi güncelleyen bir komut yerine sadece 'ekle' komutunu kabul eder. Bu sayede verinin tarihçesi her zaman korunmuş olur.

## Where it is used
Blokzincir teknolojilerinde, günlük (log) tutma sistemlerinde ve denetlenebilir veri tabanlarında kullanılır.

## Commonly confused with
Geleneksel veri tabanları ile karıştırılabilir; geleneksel olanlar veriyi güncelleyebilir, bu yöntem ise asla izin vermez.

## Frequently asked questions
**What happens if I make a mistake?**
Hatalı veriyi silmek yerine, hatayı düzelten yeni bir kayıt daha eklersiniz.

**Neden bu kadar güvenli?**
Veri değiştirilemediği için geçmişe dönük manipülasyon yapmak imkansıza yakındır.


## Related terms
- [Database](/en/dictionary/database/)
- [Logs](/en/dictionary/logs/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/append-only/
