# PDF Inspector nedir?

**Kategori:** Veri & Altyapı  
**Son güncelleme:** 2026-09-19

**PDF Inspector** (PDF denetim ve inceleme aracı), PDF belgelerinin iç yapısını, nesne hiyerarşisini (Object Tree), gömülü fontlarını, renk uzaylarını, meta verilerini ve potansiyel güvenlik risklerini kod ve bayt düzeyinde inceleyen teknik analiz yazılımıdır.

PDF dosyaları son kullanıcıya görsel bir dijital sayfa gibi görünse de arka planda PostScript tabanlı karmaşık bir komut dizisi ve hiyerarşik nesne veritabanı barındırır. PDF Inspector, bu derin katmanları görünür kılarak doğrulama ve hata ayıklama olanağı sağlar.

---

## 1. Bir PDF Dosyasının İç Mimarisi

Bir PDF belgesini derinlemesine inceleyen bir inspector, dosyanın 4 ana bileşenini analiz eder:

- **Header (Başlık):** Belgenin uyumlu olduğu PDF sürümünü belirtir (örn. `%PDF-1.7`, `%PDF-2.0`).
- **Body (Gövde / Nesneler):** Sayfaların, metinlerin, vektör çizimlerin ve görsellerin bulunduğu temel veri bloklarıdır (Sözlükler, Diziler, Akışlar/Streams).
- **Xref Table (Çapraz Referans Tablosu):** Dosyadaki her bir nesnenin (indirect object) dosya başından itibaren kaçıncı baytta başladığını tutan fihristtir. Hızlı rastgele erişim bu tablo sayesinde gerçekleşir.
- **Trailer:** Belgenin kök dizinini (Catalog/Root) ve şifreleme parametrelerini işaret eder.

---

## 2. PDF Inspector Neleri Denetler?

Bir PDF Inspector aracı sadece metin okumaz; belgenin teknik sağlığını şu boyutlarda inceler:

### A. Font ve Tipografi Doğrulaması
- **Gömülü Fontlar (Font Embedding):** Belgedeki fontların (TrueType, OpenType, Type 1) tam olarak mı yoksa yalnızca kullanılan harflerle mi (Subsetting) gömüldüğünü tespit eder. Gömülmemiş fontlar farklı cihazlarda tasarımın bozulmasına neden olur.
- **ToUnicode CMap:** Sayfadaki harf gliflerinin doğru Unicode karakterlerine eşlenip eşlenmediğini kontrol eder. Bu eşleme bozuksa, metin ekranda doğru görünse bile kopyalandığında veya arandığında anlamsız sembollere dönüşür.

### B. Baskı ve Renk Standartları (Prepress)
- **Renk Uzayları:** RGB, CMYK ve Spot (Pantone) renk ayrımlarını denetler.
- **Baskı Kutuları (Page Boxes):** Kesim payı (BleedBox), kırpma alanı (TrimBox) ve görsel sınırları (MediaBox) milimetrik hassasiyetle kontrol edilir.

### C. Standart Uyumluluğu (PDF/A ve PDF/UA)
- **Arşivleme Uyumluluğu (PDF/A):** Yıllar sonra bile belgenin aynı şekilde görüntülenebilmesi için dış bağlantıların, şifrelemenin ve gömülmemiş fontların yasaklandığı kuralları denetler (ISO 19005).
- **Erişilebilirlik (PDF/UA):** Görme engelli kullanıcılar ve ekran okuyucular için etiketleme hiyerarşisinin (Tagged PDF) ve alternatif görsel açıklamalarının (Alt Text) mevcudiyetini inceler.

### D. Güvenlik ve Zararlı Yazılım Analizi
- **Zararlı Kod Enjeksiyonu:** PDF içine gizlenmiş şüpheli JavaScript (`/JS`, `/JavaScript`), harici program çalıştırma komutları (`/Launch`) veya istismar amaçlı tampon taşması tetikleyen bozuk akışları (malicious streams) tespit eder.
- **Gizli Meta Veriler:** Yazar bilgileri, revizyon geçmişi, GPS konumları ve silindiği sanılan gizli katmanları ortaya çıkarır.

---

## 3. PDF Inspector vs PDF Parser vs PDF Viewer

| Özellik | PDF Viewer (Görüntüleyici) | PDF Parser (Ayrıştırıcı) | PDF Inspector (Denetçi) |
| :--- | :--- | :--- | :--- |
| **Amaç** | Belgeyi ekrana çizmek | Metin ve tabloları çekmek | Yapısal bütünlüğü ve güvenliği denetlemek |
| **Hedef Kitle** | Son kullanıcılar | Veri analistleri, LLM/RAG geliştiricileri | Güvenlik araştırmacıları, yayıncılar, mühendisler |
| **Çıktı** | Pikseller / Görsel çıktı | JSON, CSV, ham metin | Nesne ağacı, hata raporu, güvenlik skoru |
| **Tipik Araçlar** | Adobe Acrobat Reader, Chrome | PyPDF, pdfplumber, Tika | veraPDF, qpdf, pdf-parser |

---

## 4. Geliştiriciler ve Sistem Yöneticileri İçin Popüler Araçlar

- **`qpdf`:** Komut satırından PDF şifrelemelerini çözebilen, nesne yapılarını düzleştiren ve hatalı dosyaları onaran güçlü bir C++ aracıdır.
- **`veraPDF`:** Avrupa Komisyonu ve PDF Association tarafından desteklenen, PDF/A arşiv standartlarına uyumluluğu tescilleyen açık kaynaklı referans doğrulayıcıdır.
- **`pdf-parser.py` (Didier Stevens):** Siber güvenlik uzmanlarının zararlı ve şüpheli PDF dosyalarını deşifre etmek için kullandığı standart analiz aracıdır.
- **`pdfcpu`:** Go diliyle yazılmış, PDF optimizasyonu ve yapısal doğrulama yapan modern bir kütüphanedir.

---

## Sıkça Sorulan Sorular

### PDF Inspector nedir ve neden ihtiyaç duyulur?
PDF Inspector, PDF dosyalarının arkasındaki nesne kodlarını, font tablolarını ve meta verileri analiz eden bir araçtır. Dosya bozulmalarını, baskı hatalarını ve gömülü siber güvenlik tehditlerini tespit etmek için kullanılır.

### PDF belgesinden kopyalanan metin neden anlamsız karakterlere dönüşür?
Bu durum, PDF içindeki yazı tipinin "ToUnicode CMap" eşleme tablosunun eksik veya bozuk olmasından kaynaklanır. Harf şekli (glif) doğru çizilse de harfin metin karşılığı bilinmez. PDF Inspector bu tür eksiklikleri tespit edebilir.

### PDF/A uyumluluğu neden denetlenmelidir?
Resmi kurumlar ve arşivler, belgelerin 20-30 yıl sonra da birebir aynı görünmesini ister. PDF/A standardı ses/video, şifreleme ve dış font bağlantılarını yasaklar. Inspector araçları bu kriterleri denetler.

### Bir PDF dosyası siber saldırı aracı olabilir mi?
Evet; PDF formatı JavaScript kodlarını, harici bağlantıları ve gömülü ikili dosyaları çalıştırabilir. Siber saldırganlar bu özellikleri kullanarak kullanıcı fark etmeden zararlı yazılım indirebilir.

### PDF Parser ile PDF Inspector aynı şey midir?
Hayır; parser belgenin içeriğindeki metin ve veriyi çıkarmaya odaklanırken, inspector belgenin teknik standartlara, font kurallarına ve güvenlik ilkelerine uygunluğunu denetler.

## İlgili terimler
- [PDF Parser](/dictionary/pdf-parser/)
- [Document Parsing](/dictionary/document-parsing/)
- [PDF](/dictionary/pdf/)
- [Security Scanner](/dictionary/security-scanner/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/pdf-inspector/  
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
