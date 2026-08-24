# Was ist Append-only?

Verilerin sadece sona eklenebildiği, değiştirilemediği veya silinemediği bir kayıt yöntemidir.

## Definition
Bir veri tabanına veya dosyaya bilgi eklerken, eski verileri değiştirmek yerine her yeni bilgiyi listenin sonuna ekleme prensibidir. Bu yöntem, verinin geçmişini korumak ve güvenliğini sağlamak için kritiktir. Hiçbir veri silinmediği için sistemdeki tüm hareketlerin izini sürmek mümkündür.

## So funktioniert es
Sistem, veriyi güncelleyen bir komut yerine sadece 'ekle' komutunu kabul eder. Bu sayede verinin tarihçesi her zaman korunmuş olur.

## Wo es eingesetzt wird
Blokzincir teknolojilerinde, günlük (log) tutma sistemlerinde ve denetlenebilir veri tabanlarında kullanılır.

## Häufig verwechselt mit
Geleneksel veri tabanları ile karıştırılabilir; geleneksel olanlar veriyi güncelleyebilir, bu yöntem ise asla izin vermez.

## Häufige Fragen
**Was passiert, wenn ich einen Fehler mache?**
Hatalı veriyi silmek yerine, hatayı düzelten yeni bir kayıt daha eklersiniz.

**Neden bu kadar güvenli?**
Veri değiştirilemediği için geçmişe dönük manipülasyon yapmak imkansıza yakındır.


## Verwandte Begriffe
- [Database](/de/dictionary/database/)
- [Logs](/de/dictionary/logs/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/append-only/
