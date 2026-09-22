# MCP nedir, ne demek?

> Model Context Protocol

**Kategori:** Yapay Zekâ  
**Son güncelleme:** 2026-09-22

MCP (**Model Context Protocol**), yapay zekâ uygulamalarının dış veri ve araçlara standart yolla bağlanmasını sağlayan açık protokoldür.

## Tanım ve Kelime Kökeni
Her uygulama için ayrı bağlantı yazmak yerine tek standart kullanılır. Protokol, yapay zekâ ekosisteminin birlikte çalışabilirliğini artırmak için geliştirilmiş açık bir standarttır. Priz benzetmesi yerindedir: Her cihazın aynı fişle çalışması gibi, farklı veri kaynakları da yapay zekâya aynı yolla bağlanır.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Asistanlar:** Yapay zekâ uygulamasının takviminizi ve dosyalarınızı okuması.
- **Geliştirme:** Kod editörünün depo ve dokümantasyona bağlanması.
- **Raporlama:** Canlı veritabanından özet çıkarılması.

## Teknik Derinlik ve Mimari
Mimari üç parçadan oluşur:
- **Host:** Yapay zekâ uygulaması (ör. masaüstü asistan veya editör).
- **Client:** Host içindeki bağlantı yöneticisi.
- **Server:** Veri veya aracı sunan küçük program (dosya sistemi, veritabanı, GitHub).

Sunucular üç yetenek sunar:
- **Tool:** Modelin çağırabileceği işlev (dosya arama, sorgu çalıştırma).
- **Resource:** Modelin okuyabileceği veri (belge, şema).
- **Prompt:** Hazır görev şablonu.

Tipik bir istemci ayarı şöyledir:

```
{
  "mcpServers": {
    "dosya": {
      "command": "npx",
      "args": ["-y", "ornek-mcp-dosya"]
    }
  }
}
```

Güvenlik kuralı: Sunucu yalnızca izin verilen klasör ve işlemlere erişir. Modelin her isteği kullanıcı onayından geçebilmelidir.

## Sık Karıştırılanlar
API ile karıştırılır. API tek bir kapıdır, MCP ise bu kapıdan geçen verinin standart dilde konuşulmasını sağlayan kural setidir. API sunucuya özeldir, MCP sunucular arası ortaktır.

## Farklı Disiplinlerde Kullanımı
- **Elektrik:** Her cihazın uyduğu priz standardı.
- **Demiryolu:** Vagonları birleştiren kanca standardı.
- **Dil:** Diplomaside kullanılan ortak protokol dili.

## Bir benzetmeyle
Bir priz standardı gibidir; her cihazın aynı fişle çalışması gibi, farklı veri kaynaklarının da yapay zekâya kolayca bağlanmasını sağlar.

## Sıkça sorulanlar

**MCP neden gereklidir?**  
Her uygulama için ayrı bağlantı yazmak yerine standart yol izlenir. Bu, güvenliği ve bakımı kolaylaştırır.

**MCP açık kaynak mı?**  
Evet. Açık standarttır, farklı uygulamalar kendi istemci ve sunucularını yazabilir.

**API yerine neden MCP kullanılsın?**  
API sunucuya özeldir, her biri ayrı öğrenilir. MCP ortak dil sunar, model yeni sunucuya hazır bağlanır.

**Güvenli midir?**  
Tasarımı izin temellidir, ancak sunucunun erişim kapsamını dar tutmanız ve yazma işlemlerinde onay istemeniz gerekir.

## İlgili terimler
- [API](/dictionary/api/)
- [Data Pipeline](/dictionary/data-pipeline/)
- [AI Agent](/dictionary/ai-agent/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/mcp/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
