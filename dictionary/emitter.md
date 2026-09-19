# Emitter ne demek, nedir?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

Emitter (yayıcı), yazılım mühendisliğinde iki temel alanda karşımıza çıkan kritik bir terimdir: Olay güdümlü mimarilerde (Event-Driven Architecture) durum değişikliklerini dinleyicilere duyuran mekanizma (Event Emitter) ve derleyici teknolojisinde (Compiler) analiz edilen kodu hedef makine diline veya baytkoda dönüştüren kod üretim modülü (Code Emitter).

## Kavramsal köken: Fizikten yazılım mimarisine
"Emitter" sözcüğü, Latince "dışarı fırlatmak, salıvermek" anlamına gelen *emittere* fiilinden türemiştir. Elektronikte elektron yayan katotlara veya telekomünikasyonda sinyal basan radyo vericilerine emitter denir. Yazılım dünyası bu terimi, "kendisinde oluşan bir durumu ya da ürettiği bir çıktıyı dış dünyaya aktaran kaynak" anlamında ödünç almıştır.

Yazılımda "emitter" tek bir yapı değil, kullanıldığı bağlama göre iki devasa disiplini temsil eder: Olay akışları ve derleyici tasarımı.

## 1. Olay güdümlü mimari ve Event Emitter
Olay tabanlı programlamada Emitter, **Observer (Gözlemci) ve Publish-Subscribe (Yayınla-Abone Ol)** tasarım desenlerinin kalbidir. Sistemdeki bileşenlerin birbirini doğrudan tanıması yerine (tight coupling), olaylar üzerinden haberleşmesini (loose coupling) sağlar.

### Node.js ve JavaScript dünyasında EventEmitter
Node.js'in reaktif ve asenkron I/O yapısı `events` modülü içindeki `EventEmitter` sınıfına dayanır:
- **`emit(event, [...args])`:** Belirtilen isimdeki olayı tetikler ve kayıtlı tüm dinleyicileri uyarır.
- **`on(event, listener)`:** Belirtilen olay gerçekleştiğinde çalışacak geri çağırım (callback) fonksiyonunu kaydeder.
- **`once(event, listener)`:** Olayı yalnızca ilk gerçekleştiğinde bir kez yakalar ve ardından kaydı otomatik siler.

> **Önemli Teknik Detay:** Node.js `EventEmitter`, yaygın inanışın aksine olay dinleyicilerini varsayılan olarak **senkron** çalıştırır. Bir dinleyici bloke olursa sonraki dinleyiciler bekler. Asenkron yürütme için `setImmediate()` veya `process.nextTick()` kullanılır.

### Bellek Sızıntısı (Memory Leak) riski
Event Emitter mimarisinde en sık yapılan hata, yaşam döngüsü biten nesnelerin dinleyicilerinin (`removeListener` veya `off`) kaldırılmamasıdır. Bu durum nesnelerin Garbage Collector tarafından temizlenmesini engeller ve Node.js'te `MaxListenersExceededWarning` uyarısına neden olur.

## 2. Derleyici mimarisinde Code Emitter (Kod Üretici)
Bir derleyicinin (compiler) veya dönüştürücünün (transpiler) en son ve en can alıcı aşaması **Emitter** (Code Generator) katmanıdır. Derleme zinciri şu sırayla işler:
`Kaynak Kod` → `Lexer (Token'lar)` → `Parser (Sözdizim Ağacı - AST)` → `Semantik Analiz` → `Optimizasyon` → **`Emitter`** → `Hedef Kod`

- Emitter, optimize edilmiş Soyut Sözdizim Ağacını (AST) veya Ara Temsili (IR - Intermediate Representation) baştan sona dolaşır (genellikle Visitor Pattern ile).
- Her bir düğümü hedef platformun anlayacağı talimatlara döker: Bu çıktı ham makine dili (x86/ARM Assembly), sanal makine baytkodu (JVM, V8 Bytecode) veya başka bir yüksek seviyeli dil (TypeScript'ten JavaScript'e derleme gibi) olabilir.

## Bir benzetmeyle
- **Event Emitter:** Yangın alarm butonudur. Butona basıldığında (emit), buton binadaki kaç kişinin ve hangi sirenlerin çaldığını bilmez; yalnızca sinyal yayar ve bağlı tüm alarm sistemleri (listeners) devreye girer.
- **Code Emitter:** Bir mimarın çizdiği ayrıntılı teknik planları (AST) alıp şantiye ustalarının doğrudan uygulayabileceği kalıp ve demir donatı talimatlarına döken başmühendistir.

## Sıkça sorulanlar

**Emitter ne demek ve Türkçesi nedir?**  
Emitter, İngilizcede "yayıcı" veya "verici" anlamına gelir. Yazılımda genellikle "olay yayıcı" (event emitter) veya derleyicilerde "kod üretici / yayıcı" (code emitter) olarak kullanılır.

**Event Emitter kullanmanın en büyük avantajı nedir?**  
Bileşenler arasındaki bağımlılığı (coupling) sıfıra indirir. Bir modül bir olayı fırlatır; olayı kimin, ne zaman ve nasıl işlediğiyle ilgilenmez. Bu da modülerliği ve test edilebilirliği artırır.

**Derleyicilerde Emitter hangi görevi üstlenir?**  
Kaynak kodun ayrıştırılıp optimize edilmiş ağaç yapısını (AST) alarak hedef çıktıyı (Assembly, makine kodu, baytkod veya dönüştürülmüş kaynak kod) üreten son bileşendir.

**RxJS Observable ile Event Emitter arasındaki fark nedir?**  
Event Emitter genellikle çoklu yayın (multicast) yapar ve anlık olay bildirimleri için kullanılır. RxJS Observable ise zaman içindeki zengin veri akışlarını (streams), filtreleme, haritalama ve geciktirme gibi fonksiyonel operatörlerle dönüştürme gücü sunar.

## İlgili terimler
- [Parser](/dictionary/parser/)
- [Compiler](/dictionary/compiler/)
- [Runtime](/dictionary/runtime/)
- [Assembly](/dictionary/assembly/)
- [API](/dictionary/api/)
- [Bundler](/dictionary/bundler/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/emitter/  
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
