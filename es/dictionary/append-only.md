# ¿Qué es Append-only?

Verilerin sadece sona eklenebildiği, değiştirilemediği veya silinemediği bir kayıt yöntemidir.

## Definición
Bir veri tabanına veya dosyaya bilgi eklerken, eski verileri değiştirmek yerine her yeni bilgiyi listenin sonuna ekleme prensibidir. Bu yöntem, verinin geçmişini korumak ve güvenliğini sağlamak için kritiktir. Hiçbir veri silinmediği için sistemdeki tüm hareketlerin izini sürmek mümkündür.

## Cómo funciona
Sistem, veriyi güncelleyen bir komut yerine sadece 'ekle' komutunu kabul eder. Bu sayede verinin tarihçesi her zaman korunmuş olur.

## Dónde se usa
Blokzincir teknolojilerinde, günlük (log) tutma sistemlerinde ve denetlenebilir veri tabanlarında kullanılır.

## Suele confundirse con
Geleneksel veri tabanları ile karıştırılabilir; geleneksel olanlar veriyi güncelleyebilir, bu yöntem ise asla izin vermez.

## Preguntas frecuentes
**¿Qué pasa si cometo un error?**
Hatalı veriyi silmek yerine, hatayı düzelten yeni bir kayıt daha eklersiniz.

**Neden bu kadar güvenli?**
Veri değiştirilemediği için geçmişe dönük manipülasyon yapmak imkansıza yakındır.


## Términos relacionados
- [Database](/es/dictionary/database/)
- [Logs](/es/dictionary/logs/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/append-only/
