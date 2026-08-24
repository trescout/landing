# O que é Append-only?

Verilerin sadece sona eklenebildiği, değiştirilemediği veya silinemediği bir kayıt yöntemidir.

## Definição
Bir veri tabanına veya dosyaya bilgi eklerken, eski verileri değiştirmek yerine her yeni bilgiyi listenin sonuna ekleme prensibidir. Bu yöntem, verinin geçmişini korumak ve güvenliğini sağlamak için kritiktir. Hiçbir veri silinmediği için sistemdeki tüm hareketlerin izini sürmek mümkündür.

## Como funciona
Sistem, veriyi güncelleyen bir komut yerine sadece 'ekle' komutunu kabul eder. Bu sayede verinin tarihçesi her zaman korunmuş olur.

## Onde é usado
Blokzincir teknolojilerinde, günlük (log) tutma sistemlerinde ve denetlenebilir veri tabanlarında kullanılır.

## Costuma ser confundido com
Geleneksel veri tabanları ile karıştırılabilir; geleneksel olanlar veriyi güncelleyebilir, bu yöntem ise asla izin vermez.

## Perguntas frequentes
**O que acontece se eu cometer um erro?**
Hatalı veriyi silmek yerine, hatayı düzelten yeni bir kayıt daha eklersiniz.

**Neden bu kadar güvenli?**
Veri değiştirilemediği için geçmişe dönük manipülasyon yapmak imkansıza yakındır.


## Termos relacionados
- [Database](/pt/dictionary/database/)
- [Logs](/pt/dictionary/logs/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/append-only/
