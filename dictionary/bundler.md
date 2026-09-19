# Bundler nedir, ne işe yarar?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

Bundler (modül paketleyici), modern web uygulamalarındaki yüzlerce bağımsız JavaScript dosyasını, stil şablonlarını ve medya varlıklarını analiz ederek tarayıcıların en hızlı şekilde yükleyebileceği optimize paketlere (bundle) dönüştüren geliştirme aracıdır.

## Tanım ve Temel Amacı
Modern web geliştirme süreçlerinde kodlar yüzlerce modüle, bileşene ve harici npm paketine bölünür. Ancak tarayıcıların yüzlerce ayrı HTTP isteğiyle bu dosyaları tek tek indirmesi ciddi performans kayıplarına yol açar. Bundler, projenin giriş noktasından (entry point) başlayarak tüm `import` ve `require` ilişkilerini tarar, bir **bağımlılık grafiği** (dependency graph) oluşturur ve tarayıcı dostu nihai dosyalara dönüştürür.

## Bir benzetmeyle
Büyük bir makine inşa ederken fabrikanın farklı atölyelerinden çıkan yüzlerce cıvata, dişli ve kabloyu müşteriye darmadağınık kargolamak yerine; montaj hattında parçaları birbirine bağlayıp tek ve çalışmaya hazır kompakt bir paket halinde teslim etmeye benzer.

## Temel Özellikleri ve Yetenekleri
- **Bağımlılık Grafiği Çıkarma:** Dosyaların birbirine nasıl bağlandığını belirler ve doğru yürütme sırasına göre paketler.
- **Tree-Shaking (Ölü Kod Ayıklama):** İçe aktarılan kütüphanelerde fiilen çağrılmayan fonksiyonları tespit ederek nihai paketten siler, dosya boyutunu büyük ölçüde düşürür.
- **Kod Bölme (Code Splitting):** Tüm uygulamayı tek bir devasa dosyaya hapsetmek yerine, rotalara (route) veya dinamik bileşenlere göre parçalayarak kullanıcının yalnızca ihtiyaç duyduğu kodu indirmesini sağlar (Lazy loading).
- **Varlık Yönetimi ve Minifikasyon:** CSS, SVG, resim gibi varlıkları modül olarak işler; JavaScript kodundaki boşlukları, yorum satırlarını ve değişken adlarını kısaltarak sıkıştırır.

## Popüler Modül Paketleyicileri
- **Vite:** Geliştirme sürecinde yerel ES modüllerini (Native ESM) ve arka planda esbuild'i kullanarak anında açılan ve ultra hızlı sıcak modül değişimi (HMR) sunan modern araç.
- **Webpack:** Ekosistemin en köklü ve en geniş eklenti desteğine sahip, kurumsal projelerin vazgeçilmezi olan yapılandırma standardı.
- **Rollup:** Özellikle JavaScript kütüphanesi ve SDK geliştiricileri için kusursuz tree-shaking yeteneği sağlayan paketleyici.
- **esbuild & Turbopack:** Go ve Rust dilleriyle yazılmış, geleneksel Node.js tabanlı paketleyicilere kıyasla 10-100 kat daha hızlı çalışan yeni nesil derleyiciler.

## Sık karıştırılanlar
Compiler (Transpiler) ile Bundler sıklıkla karıştırılır. Babel veya SWC gibi derleyiciler modern ECMAScript sözdizimini eski tarayıcıların anlayacağı JavaScript sürümüne dönüştürür. Bundler ise farklı dosyalardaki modülleri bir araya getirip birbirine bağlar. Günümüzde modern bundler'lar (Vite, Webpack) derleme işlemlerini de bünyelerinde barındırır.

## Sıkça sorulanlar

**What is a bundler (Bundler nedir)?**  
Yazılım projelerinde modüllere ayrılmış kodları, CSS dosyalarını ve harici paketleri analiz ederek tarayıcıların kolayca çalıştırabileceği optimize dosyalara dönüştüren araçtır.

**Vite ve Webpack arasındaki temel fark nedir?**  
Webpack tüm dosyaları bellek üzerinde paketleyip sunucu başlatırken; Vite, geliştirme aşamasında tarayıcının yerel ES modül yeteneğinden faydalanarak projeyi sıfır bekleme süresiyle ayağa kaldırır.

**Tree-shaking nedir?**  
Paketleyicinin, projenize dahil ettiğiniz kütüphanelerdeki kullanılmayan kod parçalarını otomatik olarak tespit edip dağıtım paketinin dışında bırakması tekniğidir.

**Neden her şeyi tek bir dosyada birleştirmiyoruz?**  
Tüm uygulamanın tek bir büyük dosyada olması ilk sayfa yükleme hızını (FCP) olumsuz etkiler; kod bölme sayesinde kullanıcı sadece ziyaret ettiği sayfanın kodlarını indirir.

## İlgili terimler
- [Bundling](/dictionary/bundling/)
- [Compilation](/dictionary/compilation/)
- [Frontend Stack](/dictionary/frontend-stack/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/bundler/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
