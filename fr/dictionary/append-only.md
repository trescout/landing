# Qu'est-ce que Append-only ?

Verilerin sadece sona eklenebildiği, değiştirilemediği veya silinemediği bir kayıt yöntemidir.

## Définition
Bir veri tabanına veya dosyaya bilgi eklerken, eski verileri değiştirmek yerine her yeni bilgiyi listenin sonuna ekleme prensibidir. Bu yöntem, verinin geçmişini korumak ve güvenliğini sağlamak için kritiktir. Hiçbir veri silinmediği için sistemdeki tüm hareketlerin izini sürmek mümkündür.

## Comment ça marche
Sistem, veriyi güncelleyen bir komut yerine sadece 'ekle' komutunu kabul eder. Bu sayede verinin tarihçesi her zaman korunmuş olur.

## Où est-ce utilisé
Blokzincir teknolojilerinde, günlük (log) tutma sistemlerinde ve denetlenebilir veri tabanlarında kullanılır.

## Souvent confondu avec
Geleneksel veri tabanları ile karıştırılabilir; geleneksel olanlar veriyi güncelleyebilir, bu yöntem ise asla izin vermez.

## Questions fréquentes
**Que se passe-t-il si je fais une erreur ?**
Hatalı veriyi silmek yerine, hatayı düzelten yeni bir kayıt daha eklersiniz.

**Neden bu kadar güvenli?**
Veri değiştirilemediği için geçmişe dönük manipülasyon yapmak imkansıza yakındır.


## Termes liés
- [Database](/fr/dictionary/database/)
- [Logs](/fr/dictionary/logs/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/append-only/
