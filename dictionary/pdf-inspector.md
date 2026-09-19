# PDF Inspector nedir?

**Kategori:** Veri & Altyapı  
**Son güncelleme:** 2026-09-19

PDF Inspector, PDF belgelerinin içindeki metin akışları, gömülü yazı tipleri, vektör katmanları, meta veriler ve nesne hiyerarşisini detaylıca inceleyerek yapısal hataları ve uyumluluk sorunlarını tespit eden teknik denetim aracıdır.

## Tanım
PDF dosyaları kullanıcıya basit bir dijital sayfa gibi görünse de arka planda karmaşık bir nesne ağacı (DOM), akışlar (streams) ve gömülü varlıklar barındırır. PDF Inspector, dosyanın içindeki verilerin nasıl dizildiğini, hangi yazı tipi alt kümelerinin (font subsets) kullanıldığını, renk uzaylarını ve metinlerin doğru kodlanıp kodlanmadığını röntgen gibi inceler.

## PDF Inspector ne demek?
İngilizce "inspector" (denetçi / müfettiş) kelimesinden gelen bu terim, bir PDF dosyasını salt görsel olarak açmak yerine, dosyanın mimarisini ve nesne tablosunu kod seviyesinde denetleyen yazılımları ifade eder. Belgelerin yayın, baskı veya uzun vadeli arşivleme öncesinde teknik bütünlüğe sahip olduğunu garanti eder.

## Hangi alanlarda ve neden kullanılır?
- **Baskı ve Prepress:** Baskı öncesinde renk profilleri (CMYK), taşma payları ve gömülü fontların doğrulanması.
- **PDF/A Arşiv Uyumluluğu:** Kurumsal arşivleme standartlarına (PDF/A-1b, PDF/A-2b) uygunluğun denetlenmesi.
- **OCR ve Veri Çıkarma Doğrulaması:** Metin katmanlarının taranmış bir resim mi yoksa seçilebilir saf metin mi olduğunun kontrolü.
- **Güvenlik ve Gizlilik:** Belge içine gömülmüş şüpheli JavaScript kodları, gizli form alanları ve temizlenmemiş meta verilerin ayıklanması.

## Bir benzetmeyle
Bir kitabın sadece kapağına ve sayfalarına uzaktan bakmak yerine, cildin dikişlerini, kağıdın gramajını, mürekkep türünü ve sayfaların sırasını inceleyen bir uzman büyüteci gibidir.

## Nasıl çalışır?
Belgeyi araca yüklediğinizde, inspector dosyanın XObject, Font, Annotations ve Catalog gibi temel sözlük yapılarını ağaç görünümü şeklinde önünüze serer. Böylece eksik fontlar, bozuk akışlar veya standart dışı etiketler hızla ayıklanır.

## Sık karıştırılanlar: PDF Parser ile farkı nedir?
PDF Parser (ayrıştırıcı), belgenin içindeki saf metin veya tablo verilerini çıkarıp başka bir veritabanına aktarmaya odaklanır. PDF Inspector ise verinin çıkarılmasından ziyade dosyanın teknik yapısını, standartlara uyumunu ve kalitesini denetler.

## Sıkça sorulanlar

**Sadece metinleri mi inceler?**  
Hayır; gömülü yazı tiplerinin çözünürlüğünü, renk profillerini, katmanları, form alanlarını ve dosyanın meta veri etiketlerini de kapsamlı şekilde denetler.

**Geliştiriciler için popüler PDF denetim araçları nelerdir?**  
Açık kaynak dünyasında `qpdf`, `pdfminer`, `veraPDF` (PDF/A için resmi doğrulayıcı) ve ticari alanda Adobe Acrobat Preflight en yaygın araçlardır.

## İlgili terimler
- [PDF Parser](/dictionary/pdf-parser/)
- [Document Parsing](/dictionary/document-parsing/)
- [PDF](/dictionary/pdf/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/pdf-inspector/  
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
