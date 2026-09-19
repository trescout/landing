# Apple Silicon nedir?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

Apple Silicon, Apple'ın Mac ve iPad cihazları için kendi bünyesinde tasarladığı; CPU, GPU, Neural Engine ve birleşik belleği (Unified Memory) tek bir çip üzerinde birleştiren ARM tabanlı yüksek performanslı işlemci ailesidir.

## Tanım
Apple Silicon, Apple'ın 2020 yılında Intel x86 işlemcilerden ayrılarak başlattığı mimari dönüşümün kalbidir. M serisi (M1, M2, M3, M4) yongalar, bilgisayar donanımını geleneksel ayrık parçalar yerine **SoC (System on a Chip - Çip Üzerinde Sistem)** mimarisiyle tek bir silikon plaka üzerinde buluşturur.

## Apple Silicon ne demek?
İngilizce "silicon" (yarı iletken çip üretiminde kullanılan silisyum elementi) kelimesinden türeyen bu isim, Apple'ın kendi donanım ve yazılımını uçtan uca kontrol ettiği özel mikroişlemci tasarımını temsil eder. Hem akıllı telefonlardaki A serisi yongaları hem de bilgisayarlardaki M serisi işlemcileri kapsar.

## Temel mimari avantajları nelerdir?
- **Birleşik Bellek Mimarisi (Unified Memory - UMA):** RAM, doğrudan işlemci paketinin üzerine entegre edilmiştir. CPU, GPU ve yapay zekâ birimleri aynı bellek havuzuna kopyalama gecikmesi olmadan sıfır maliyetle erişir.
- **Yüksek Enerji Verimliliği (Performance per Watt):** ARM RISC mimarisi sayesinde prize takılı olmadan tam performans sunar, fan gürültüsünü ve ısınmayı neredeyse sıfıra indirir.
- **Neural Engine (Yapay Zekâ Hızlandırıcısı):** Makine öğrenimi, yerel LLM çalıştırma ve görsel işleme görevleri için özel nöral donanım çekirdekleri barındırır.
- **Rosetta 2 Uyumluluk Katmanı:** Intel (x86_64) mimarisi için yazılmış eski Mac uygulamalarını ARM komut setine otomatik çevirerek sorunsuz çalıştırır.

## Bir benzetmeyle
Geleneksel bir bilgisayarda işlemci, ekran kartı ve RAM birbirine otoyollarla bağlı farklı şehirler gibidir (veri aktarımı vakit alır). Apple Silicon'da ise tüm bu birimler aynı gökdelende çalışan uzman ekipler gibidir; asansörle saniyeler içinde doğrudan aynı masada buluşurlar.

## Sıkça sorulanlar

**Apple Silicon işlemcilerde x86 uygulamaları çalışır mı?**  
Evet, macOS içindeki Rosetta 2 çeviri motoru sayesinde Intel tabanlı uygulamaların büyük bölümü kullanıcı hiçbir şey fark etmeden yüksek hızda çalışır.

**Neden Mac bilgisayarlar çok daha az ısınıyor ve uzun pil ömrü sunuyor?**  
Çünkü ARM mimarisi watt başına işlem gücünde x86 mimarisine göre çok daha verimlidir; işlemci boştayken veya hafif işlerde minimum enerji harcar.

## İlgili terimler
- [Runtime](/dictionary/runtime/)
- [Computer Science](/dictionary/computer-science/)
- [Desktop App](/dictionary/desktop-app/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/apple-silicon/  
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
