# Bundler nedir, ne işe yarar?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

Bundler (modül paketleyici), modern web ve yazılım geliştirme ekosisteminde yüzlerce bağımsız parçaya bölünmüş kaynak kodları (JavaScript, TypeScript, CSS, HTML, grafik ve yazı tipi varlıkları) ile harici kütüphane bağımlılıklarını analiz eden, bu varlıkları tarayıcıların en hızlı ve verimli biçimde çalıştırabileceği optimize dosya paketlerine (bundle) dönüştüren geliştirme aracıdır.

## Bundler Ne Demek ve Neden Ortaya Çıktı?

Web'in ilk yıllarında siteler, HTML içine sırayla eklenen birkaç `<script>` etiketinden ibaretti. Ancak web uygulamaları masaüstü yazılımları kadar karmaşık hale geldikçe ve binlerce modülden oluşan devasa kod tabanlarına dönüştükçe ciddi yapısal engeller belirdi:

1. **Global Kapsam (Global Scope) Çakışmaları:** Klasik komut dosyaları ortak bir global nesneyi (`window`) paylaştığı için farklı kütüphanelerin aynı değişken adını kullanması çakışmalara ve kestirilemeyen hatalara yol açıyordu.
2. **HTTP/1.1 Ağ Sınırlamaları:** Tarayıcılar aynı alan adına aynı anda yalnızca sınırlı sayıda (genellikle 6 adet) eşzamanlı TCP bağlantısı açabiliyordu. Birbirine bağımlı 300 farklı JavaScript dosyasını tek tek istemek, aşırı yüksek ağ gecikmesine ve kilitlenmelere neden oluyordu.
3. **Modül Standartları Ayrımı:** Node.js tarafında `require()` ve `module.exports` tabanlı CommonJS standardı kullanılırken, tarayıcılar uzun yıllar boyunca yerel bir modül sistemi barındırmadı.

Bundler'lar, geliştiricilerin kodlarını küçük, sürdürülebilir, izole modüllere bölerek yazmalarını sağlarken; bu modülleri derleyip birleştirerek tarayıcının hızlıca yükleyebileceği optimize paketler üretme görevini üstlendi.

## Bir Benzetmeyle Bundler

Bir otomobil fabrikasını düşünün: Yüzlerce farklı atölyede motor parçaları, vidalar, elektrik kabloları ve göstergeler ayrı ayrı üretilir. Müşteriye binlerce demonte parçayı kutu kutu yollamak yerine, fabrika montaj hattı tüm parçaları birbirine entegre eder, test eder, gereksiz fazlalıkları ayıklar ve anahtarı çevirdiğinizde çalışan tek parça bir araç olarak teslim eder. Bundler, web projeleri için bu yüksek teknolojili montaj hattıdır.

## Bundler Nasıl Çalışır? Derinlemesine Mimari

Modern bir paketleyicinin işleyişi temelde üç aşamadan meydana gelir:

### 1. Çözümleme ve Bağımlılık Grafiği (Dependency Graph) Oluşturma
Süreç bir veya birden çok giriş noktasından (entry point, örn. `src/main.ts`) başlar:
- Paketleyici bu dosyayı okur ve içerisindeki `import`, `export` veya `require` ifadelerini tarar.
- Düğüm çözümleme algoritması (Node module resolution) veya `package.json` tanımları doğrultusunda çağrılan dosyaların diskteki yerini bulur.
- Her kaynak dosyayı bir **düğüm (node)**, import ilişkilerini ise **kenar (edge)** olarak modellediği bir Yönlü Çevrimsiz Çizge (Directed Acyclic Graph - DAG) oluşturur.

### 2. Dönüştürme ve AST Ayrıştırma
- Her modül bir derleyiciye (Babel, SWC, esbuild gibi) aktarılarak Soyut Sözdizimi Ağacına (AST - Abstract Syntax Tree) çevrilir.
- TypeScript kodları JavaScript'e dönüştürülür, JSX sözdizimi derlenir, CSS modülleri çözümlenir ve modern ECMAScript özellikleri hedeflenen tarayıcı sürümleriyle uyumlu hale getirilir.

### 3. Paketleme, Ağaç Sallama ve Çıktı Üretimi (Packaging & Emit)
- **Tree-Shaking (Ölü Kod Ayıklama):** ECMAScript Modüllerinin (ESM) statik sözdiziminden yararlanılarak, kütüphanelerden içe aktarılan ancak projede asla çağrılmayan ölü kodlar AST üzerinden elenir.
- **Minifikasyon ve Karartma:** Değişken isimleri kısaltılır (mangling), boşluklar ve yorum satırları silinerek dosya boyutu minimize edilir.
- **İçerik Damgası (Content Hashing):** Üretilen dosyalara içeriklerine dayalı hash kodları eklenir (örn. `app.d83f12a.js`), böylece tarayıcı önbelleklemesi (caching) kusursuz yönetilir.

## Kritik Optimizasyon Teknikleri

- **Kod Bölme (Code Splitting):** Tüm uygulamanın tek bir devasa dosyaya sıkıştırılması ilk sayfa açılışını (FCP - First Contentful Paint) yavaşlatır. Dinamik `import()` çağrıları sayesinde uygulama mantıksal parçalara (chunks) ayrılır; örneğin kullanıcı profil sayfasına tıklayana kadar o sayfanın kodu tarayıcıya indirilmez.
- **Sıcak Modül Değişimi (Hot Module Replacement - HMR):** Geliştirme sırasında kodda bir değişiklik yapıldığında, tarayıcı sayfasını tamamen yenilemeden ve mevcut uygulama durumunu (state) kaybetmeden yalnızca değişen modülün canlı olarak güncellenmesini sağlar.

## Paketleyici Ekosisteminin Karşılaştırması

Web ekosisteminde farklı ihtiyaçlara yanıt veren öne çıkan araçlar şunlardır:

| Araç | Yazıldığı Dil | Geliştirme Deneyimi | Üretim Motoru | Güçlü Yönü |
| :--- | :--- | :--- | :--- | :--- |
| **Webpack** | JavaScript / Node.js | Bundled (Bellek içi paketleme) | Webpack | Muazzam eklenti ekosistemi, kurumsal olgunluk |
| **Vite** | JS + Go (esbuild) | Unbundled (Yerel ESM) | Rollup / Rolldown | Anında dev server başlangıcı, yüksek geliştirici konforu |
| **Rollup** | JavaScript / Node.js | Bundled | Rollup | Kütüphane / SDK paketlemede kusursuz tree-shaking |
| **esbuild** | Go | Bundled | esbuild | İnanılmaz ham derleme hızı (Node.js araçlarından 10-100x hızlı) |
| **Turbopack / Rspack** | Rust | Bundled / Hibrid | Rust motoru | Webpack ekosistemiyle uyumlu, devasa projeler için performans |

## Sıkça Sorulan Sorular

### Bundler nedir ve modern web geliştirmede neden zorunludur?
Bundler; geliştiricinin yazdığı yüzlerce modüler kaynak dosyayı, görseli ve stil dosyasını tarayıcının tek ve optimize şekilde işleyebileceği paketlere dönüştüren araçtır. Dosya boyutu optimizasyonu, ağ isteği azaltımı ve tarayıcı uyumluluğu için modern projelerde zorunlu kabul edilir.

### Webpack ile Vite arasındaki temel fark nedir?
Webpack, geliştirme ortamında da tüm projeyi derleyip bellek içinde tek bir paket oluşturur; proje büyüdükçe başlatma süresi uzar. Vite ise geliştirme ortamında tarayıcının yerel ES Modül (Native ESM) desteğini kullanır ve dosyaları yalnızca tarayıcı talep ettiğinde anlık derler, böylece proje büyüklüğünden bağımsız olarak anında açılır.

### Tree-shaking nedir ve neden sadece ES Modüllerinde çalışır?
Tree-shaking, projede hiç kullanılmayan fonksiyon ve kod bloklarının son paketten temizlenmesidir. Bu işlem yalnızca `import` ve `export` gibi statik sözdizimine sahip ESM formatında güvenle yapılabilir; dinamik çağrılabilen CommonJS (`require()`) kodlarının derleme aşamasında tam analizi mümkün değildir.

### Transpiler (Babel, SWC) ile Bundler arasındaki fark nedir?
Transpiler sadece kodun sözdizimini dönüştürür (örneğin modern TypeScript veya ES6+ kodunu ES5'e çevirir). Bundler ise bu dönüştürülen bağımsız dosyaları, aralarındaki bağımlılık ilişkilerini çözerek birleştirir ve tek çatı altında paketler.

### Code splitting (kod bölme) ne işe yarar?
Uygulama kodunun tek bir büyük dosya yerine parçalı dosyalara bölünmesini sağlar. Kullanıcı sadece o an görüntülediği sayfanın kodunu indirir, bu da ilk yükleme süresini ciddi biçimde kısaltır ve kullanıcı deneyimini iyileştirir.

## İlgili terimler
- [Bundling](/dictionary/bundling/)
- [Compilation](/dictionary/compilation/)
- [Frontend Stack](/dictionary/frontend-stack/)
- [Runtime](/dictionary/runtime/)
- [DOM](/dictionary/dom/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/bundler/  
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
