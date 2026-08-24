# Rapor snapshot sözleşmesi

**Durum:** App tarafından üretilen rapor JSON’u ile landing rapor görünümünün provenance sözleşmesi.

Günlük rapor, kaynaklardan okunduğu anda oluşan **immutable bir snapshot**tır. Keşif kataloğu ise aynı repository veya kaynağın sonradan yenilenebilen canlı görünümüdür. Rapor sayfası ve PDF, rapor JSON’undaki sabit kaydı gösterir; Keşif sayfaları daha güncel canlı değerleri gösterebilir.

## WebReport alanları

| Alan | Anlam |
|---|---|
| `date` | Raporun takvim etiketi |
| `capturedAt` | Kaynak batch’inin ISO 8601 çekim anı; eski arşivlerde bulunmayabilir |
| `snapshotVersion: 1` | Yapılandırılmış snapshot sözleşmesinin sürümü |
| `sections[].items[].snapshot` | `sourceId`, item-level `capturedAt` ve çekim anındaki `metadata` kopyası |
| `sections[].items[].meta` | Çekim anındaki metadata’dan formatlanmış geriye dönük uyumlu görünüm satırı |

Yerelleştirilmiş JSON’lar `snapshotVersion`, report-level `capturedAt` ve item-level `snapshot` bloklarını Türkçe kaynak JSON’dan aynen taşır. Localization renderer kaynak URL’sini, başlığı, facts ve çekim zamanını çevirmemeli veya yenilememelidir.

## Renderer kuralları

`build-reports-en.js` ve aynı yolu kullanan diğer diller, chip sayılarını ilgili dilin immutable WebReport JSON’undaki `sections[].items` uzunluklarından üretir. Türkçe cover HTML’inden scrape etmek veya `discover` kataloğundaki canlı popularity, release ya da benzeri değerleri rapor chip’lerine taşımak yasaktır.

`capturedAt` geçerli olduğunda rapor detayında snapshot açıklaması gösterilir. Alan eski raporlarda yoksa açıklama gösterilmez. HTML’e JSON’dan gelen değerler güvenli HTML kaçışıyla yazılır; snapshot alanı mevcut değilse legacy JSON renderer’ı çalışmaya devam eder.

> Rapor belirli bir çekim anındaki kayıttır. Keşif, daha sonra güncellenmiş canlı kaynak değerlerini gösterebilir.

## Tarihçe ve güvenlik sınırı

Eski JSON/PDF arşivleri yeniden üretilmez. Yapılandırılmış `snapshotVersion: 1` yalnızca yeni veya açıkça yeniden oluşturulan arşivlerde bulunur; eski `meta` satırları tarihsel kayıt olarak korunur. Bu değişiklik canlı kaynak çağrısı eklemez, e-posta gönderimini açmaz ve erken erişim kayıt akışına dokunmaz.
