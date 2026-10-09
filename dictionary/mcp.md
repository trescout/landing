# MCP nedir, ne demek?

*Sözlük · Yapay Zekâ · Son güncelleme: 22 Eylül 2026*

> Model Context Protocol

MCP (**Model Context Protocol**), yapay zekâ uygulamalarının dış veri ve araçlara standart yolla bağlanmasını sağlayan açık protokoldür.

## Tanım ve Kelime Kökeni

Her uygulama için ayrı bağlantı yazmak yerine tek standart kullanılır. Protokol, yapay zekâ ekosisteminin birlikte çalışabilirliğini artırmak için geliştirilmiş açık bir standarttır. Priz benzetmesi yerindedir: Her cihazın aynı fişle çalışması gibi, farklı veri kaynakları da yapay zekâya aynı yolla bağlanır.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?

**Asistanlar:** Yapay zekâ uygulamasının takviminizi ve dosyalarınızı okuması.
**Geliştirme:** Kod editörünün depo ve dokümantasyona bağlanması.
**Raporlama:** Canlı veritabanından özet çıkarılması.

## Teknik Derinlik ve Mimari

Mimari üç parçadan oluşur:

**Host:** Yapay zekâ uygulaması (ör. masaüstü asistan veya editör).
**Client:** Host içindeki bağlantı yöneticisi.
**Server:** Veri veya aracı sunan küçük program (dosya sistemi, veritabanı, GitHub).

Sunucular üç yetenek sunar:

**Tool:** Modelin çağırabileceği işlev (dosya arama, sorgu çalıştırma).
**Resource:** Modelin okuyabileceği veri (belge, şema).
**Prompt:** Hazır görev şablonu.

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

API ile karıştırılabilir. API tek bir kapıdır, MCP ise bu kapıdan geçen verinin standart dilde konuşulmasını sağlayan kural setidir. API sunucuya özeldir, MCP sunucular arası ortaktır.

## Farklı Disiplinlerde Kullanımı

**Elektrik:** Her cihazın uyduğu priz standardı.
**Demiryolu:** Vagonları birleştiren kanca standardı.
**Dil:** Diplomaside kullanılan ortak protokol dili.

*Bir priz standardı gibidir; her cihazın aynı fişle çalışması gibi, farklı veri kaynaklarının da yapay zekâya kolayca bağlanmasını sağlar.*

## Sıkça Sorulanlar

**MCP neden gereklidir?**

Her uygulama için ayrı bağlantı yazmak yerine standart yol izlenir. Bu, güvenliği ve bakımı kolaylaştırır.

**MCP açık kaynak mı?**

Evet. Açık standarttır, farklı uygulamalar kendi istemci ve sunucularını yazabilir.

**API yerine neden MCP kullanılsın?**

API sunucuya özeldir, her biri ayrı öğrenilir. MCP ortak dil sunar, model yeni sunucuya hazır bağlanır.

**Güvenli midir?**

Tasarımı izin temellidir, ancak sunucunun erişim kapsamını dar tutmanız ve yazma işlemlerinde onay istemeniz gerekir.

## İlgili terimler

- [API](https://trescout.com/dictionary/api/)
- [Data Pipeline](https://trescout.com/dictionary/data-pipeline/)
- [AI Agent](https://trescout.com/dictionary/ai-agent/)

## İlgili araçlar

- [Langflow](https://trescout.com/discover/langflow/)
- [Servers](https://trescout.com/discover/servers/)
- [OpenCut](https://trescout.com/discover/opencut/)
- [AI Engineering from Scratch](https://trescout.com/discover/ai-engineering-from-scratch/)
- [Goose](https://trescout.com/discover/goose/)
- [Chrome Devtools MCP](https://trescout.com/discover/chrome-devtools-mcp/)
- [Codebase Memory MCP](https://trescout.com/discover/codebase-memory-mcp/)
- [REA](https://trescout.com/discover/rea/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/mcp/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
