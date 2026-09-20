# Tools ne demek, nedir?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

Tools (araçlar), bilişim ve yazılım dünyasında iki kritik alanda vazgeçilmez bir kavramdır: Yazılımcıların kod yazma, hata ayıklama ve dağıtım süreçlerini otomatikleştiren geliştirici araçları (DevTools); ve yapay zekâ modellerinin harici API'ler, veritabanları veya fonksiyonları çağırarak fiziksel ve dijital dünyayla etkileşime girmesini sağlayan eylem yetenekleridir (Tool Use / Function Calling).

## Etimoloji ve Bilişimdeki Araç Metaforu
İngilizce kökenli *tool* sözcüğü, köken olarak Eski İngilizce *tol* (iş yapmak için kullanılan alet, gereç) kelimesine dayanır. İnsanlık tarihinde alet yapımı biyolojik evrimin sınırlarını aşmayı nasıl sağladıysa; bilişim dünyasında da araçlar, insan zihninin ve yapay zekâ algoritmalarının salt teorik kapasitelerini gerçek dünya eylemlerine dönüştürmesini sağlar.

## 1. Geliştirici Araçları (Developer Tools & DevTools)
Yazılım mühendisliği, modern geliştirici araçlarının sağladığı soyutlama katmanları üzerinde yükselir:
- **Unix Felsefesi ve CLI Araçları:** Doug McIlroy ve Ken Thompson tarafından temelleri atılan Unix felsefesinin kalbinde araç tasarımı yatar: *"Tek bir iş yap, onu mükemmel yap ve diğer araçlarla birlikte çalışabilecek metin akışları üret."* `grep`, `sed`, `awk`, `curl` ve `jq` gibi komut satırı araçları, boru hatları (`|`) ile birleşerek karmaşık veri işleme operasyonlarını saniyeler içinde tamamlar.
- **Entegre Geliştirme Ortamları (IDE) ve Linter'lar:** VS Code, JetBrains ve Neovim gibi ortamlar; derleyiciler, dil sunucuları (LSP), statik kod analizcileri ve hata ayıklayıcıları (debugger) tek bir çatı altında birleştirir.
- **Tarayıcı DevTools:** Chrome, Firefox ve Safari'nin geliştirici araçları; DOM inceleme, ağ trafiği (Network tab), bellek sızıntısı yakalama (Heap Snapshot) ve JavaScript işlemci profilleme (CPU Profiler) imkânı sunar.

## 2. Yapay Zekâda Dönüm Noktası: Tool Use ve Function Calling
Geleneksel büyük dil modelleri (LLM) yalnızca olasılıksal metin üreteçleridir (Next-token prediction). Bu durum modelleri dört ölümcül kısıtlamaya hapseder:
1. **Bilgi Kesintisi (Knowledge Cutoff):** Model yalnızca eğitildiği tarihe kadar olan dünyayı bilir.
2. **Matematik ve Mantık Hataları:** Basit bir çarpma işlemini bile olasılıksal olarak tahmin etmeye çalıştığı için halüsinasyon görebilir.
3. **Gerçek Dünya Eylemsizliği:** Bir dosyayı değiştiremez, e-posta gönderemez veya canlı hisse senedi fiyatını bilemez.
4. **Özel Veriye Erişememe:** Şirket içi SQL veritabanından habersizdir.

İşte **Tool Use (Araç Kullanımı)** ve **Function Calling** mekanizması bu kısıtlamaları yıkar:
- **JSON Schema ile Tanımlama:** Geliştirici, modele kullanabileceği araçları tanıtır (`arama_yap`, `sql_sorgula`, `hava_durumu_getir`). Aracın adı, açıklaması ve alacağı parametreler katı bir JSON şemasıyla modele iletilir.
- **Karar ve Eylem Ayrımı:** Model kodu doğrudan kendi çalıştırmaz (zaten işletim sistemi çekirdeği yoktur). Kullanıcının niyetini analiz ederek metin üretmeyi durdurur ve bir `tool_calls` JSON nesnesi üretir.
- **Çalışma Ortamı (Runtime) Yürütmesi:** Uygulama katmanı bu çağrıyı yakalar, gerçek fonksiyonu çalıştırır (örneğin hava durumu API'sine gider) ve sonucu modele bir "gözlem" (observation) mesajı olarak geri besler.
- **Nihai Sentez:** Model gelen gerçek veriyi kullanarak kullanıcıya doğru, kanıtlanmış ve halüsinasyondan arınmış nihai cevabı üretir.

## 3. Model Context Protocol (MCP) ile Evrensel Standart
Yapay zekâ araçlarının yaygınlaşmasıyla birlikte her platform kendi özel araç formatını geliştirmiş, bu da $M \times N$ entegrasyon krizine yol açmıştır. Anthropic tarafından açık kaynak olarak duyurulan **Model Context Protocol (MCP)**, araç ekosistemini standartlaştırmıştır:
- Her veri kaynağı veya araç birer "MCP Sunucusu" (MCP Server) olarak paketlenir.
- Yapay zekâ istemcileri (Claude, Cursor, Antigravity) tek bir standart JSON-RPC protokolü üzerinden yüzlerce farklı araca anında bağlanabilir.
- Güvenlik ve İzin Modeli: Araçların dosya silme veya terminal komutu çalıştırma yetkileri, insan onayına (human-in-the-loop) bağlanarak güvenli sandbox ortamlarında izole edilir.

## 4. Siber Güvenlikte Çift Kullanımlı Araçlar (Dual-Use)
Siber güvenlik dünyasında "tool" kavramı iki ucu keskin bir kılıçtır:
- **Pentest ve Analiz:** Nmap (port tarama), Wireshark (paket analizi), Burp Suite (web güvenlik testi) ve Metasploit gibi araçlar; sistem yöneticileri tarafından açıkları kapatmak için kullanılırken, saldırganlar tarafından hedef ağlara sızmak için kullanılır.
- Araçların kendisi nötrdür; kullanım niyeti ve yetkilendirme sınırları güvenliğin ahlaki çerçevesini belirler.

## Sıkça Sorulanlar

**Tools ne demek ve Türkçe karşılığı nedir?**  
İngilizce kökenli bir kelime olup Türkçede 'araçlar' veya 'gereçler' anlamına gelir. Yazılımda geliştirici üretkenliğini artıran programları; yapay zekâda ise modellerin harici veritabanı veya API'leri çağırmasını sağlayan fonksiyonel yetenekleri ifade eder.

**Yapay zekâ modellerinde Tool Use (araç kullanımı) neden devrimseldir?**  
Yapay zekâyı pasif bir metin yazarından, gerçek dünyada iş bitiren otonom bir ajana (AI Agent) dönüştürür. Model bu sayede güncel veriye ulaşır, matematiksel hesaplamaları hatasız yapar ve harici sistemlerle entegre çalışır.

**Model Context Protocol (MCP) araç kullanımını nasıl değiştirdi?**  
Her yapay zekâ modeli için ayrı ayrı entegrasyon yazma gereğini ortadan kaldırdı. Araçların tek bir açık protokolle tüm yapay zekâ sistemlerine tak-çalıştır şeklinde bağlanmasını sağladı.

**Tool ile Plugin arasındaki fark nedir?**  
Bir tool (araç) genellikle tek bir amaca hizmet eden yalın bir fonksiyon çağrısıdır (örneğin SQL sorgulama); plugin (eklenti) ise birden fazla aracı, ayar panelini ve kullanıcı arayüzünü bir arada barındıran daha kapsamlı bir yazılım modülüdür.

## İlgili terimler
- [MCP](/dictionary/mcp/)
- [AI Agent](/dictionary/ai-agent/)
- [Plugin](/dictionary/plugin/)
- [SDK](/dictionary/sdk/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/tools/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
