# Runtime ne demek, nedir ve nasıl çalışır?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

Runtime (çalışma zamanı), bir programın derleme evresinden sonra bilgisayar işlemcisinde ve belleğinde fiilen çalıştırıldığı zaman dilimini ve bu yürütmeyi mümkün kılan yazılımsal altyapıyı (Runtime Environment) ifade eder.

## 1. Runtime kavramının iki temel anlamı

Yazılım mühendisliğinde "Runtime" sözcüğü bağlama göre iki farklı kavrama işaret eder:

1. **Bir Zaman Evresi Olarak (Runtime / Çalışma Zamanı):** Kodun yazıldığı (authoring) ve derleyiciden geçirildiği (compile-time) aşamanın ardından, son kullanıcının programı başlattığı andan kapandığı ana kadar geçen süredir.
2. **Bir Yürütme Katmanı Olarak (Runtime Environment / Çalışma Ortamı):** Yazılan kodun işletim sistemi ve donanım üzerinde doğrudan koşabilmesi için gereken kütüphaneler, bellek yöneticileri, çöp toplayıcılar ve sanal makineler bütünüdür. Örneğin Node.js, JVM (Java Virtual Machine) veya Go Runtime birer yürütme ortamıdır.

## 2. Compile-Time vs Runtime farkı

| Aşama | Ne Zaman Gerçekleşir? | Neler Yapılır? | Karşılaşılan Hatalar |
| :--- | :--- | :--- | :--- |
| **Compile-Time** (Derleme Zamanı) | Kod çalıştırılmadan önce, geliştirici ortamında veya CI hattında. | Sözdizimi analizi, statik tip denetimleri, kod optimizasyonu ve makine koduna / bayt koduna çevrim. | **Syntax Error**, **Type Mismatch**, Eksik kütüphane bağımlılığı. |
| **Runtime** (Çalışma Zamanı) | Kullanıcı veya sunucu programı fiilen yürütürken. | Bellek tahsisi (Stack/Heap), dinamik bağlama (dynamic linking), sistem çağrıları (I/O), olay döngüsü yönetimi. | **NullPointerException**, **Segmentation Fault (SIGSEGV)**, **Stack Overflow**, **OOM (Bellek Yetersizliği)**. |

## 3. Yönetilen (Managed) vs Yönetilmeyen (Unmanaged) Runtime Mimarileri

Farklı dillerin çalışma ortamları donanımla nasıl haberleştiğine göre ikiye ayrılır:

### A. Yönetilmeyen Runtime (C, C++, Rust, Zig)
Bu diller derlendiğinde doğrudan işletim sisteminin yerel makine koduna dönüşür. Arka planda ağır bir sanal makine veya çöp toplayıcı çalışmaz; program yalnızca hafif bir C standart kütüphanesine (`libc`, `crt0.o`) ihtiyaç duyar. Sıfır gecikme ve doğrudan donanım erişimi sunar.

### B. Yönetilen Runtime (Java, C#, Go, JavaScript, Python)
Program bir sanal makinenin veya özel bir çalışma ortamının koruması altında yürütülür:
- **JVM (.jar) & .NET CLR (.dll):** Kod önce platformdan bağımsız bir bayt koduna (bytecode) derlenir; çalışma anında JIT (Just-In-Time) derleyicisi bu kodu yerel makine diline çevirir.
- **Go Runtime:** Go kodu derlendiğinde tek bir ikili dosya üretilir; ancak Go, her binary dosyasının içine hafif bir çalışma ortamı gömer. Bu dahili runtime; goroutine'leri işletim sistemi iş parçacıklarına dağıtan $M:N$ Scheduler (zamanlayıcı) ve eş zamanlı çöp toplayıcıyı (Concurrent GC) yönetir.

## 4. Modern JavaScript Runtime Savaşları: Node.js vs Deno vs Bun

Tarayıcı dışındaki modern JavaScript dünyasında üç büyük mimari yarışmaktadır:

- **Node.js (2009):** Google'ın C++ ile yazılmış **V8** motorunu, asenkron I/O ve olay döngüsünü (Event Loop) yöneten **libuv** kütüphanesiyle birleştirmiştir. Endüstri standardı ve en geniş paket ekosistemidir (`npm`).
- **Deno (2018):** Node.js'in yaratıcısı Ryan Dahl tarafından geliştirilmiştir. V8 motorunu **Rust** ve **Tokio** asenkron altyapısıyla harmanlar. Varsayılan olarak TypeScript desteği ve dosya/ağ erişimini kısıtlayan güvenli izin mimarisi (sandbox) sunar.
- **Bun (2023):** V8 yerine Apple WebKit'in **JavaScriptCore** motorunu kullanır. Tamamen **Zig** diliyle sıfırdan yazılmıştır; bellek tahsislerini ve sistem çağrılarını mikrosaniyeler seviyesine indirerek dosya okuma, paket yükleme ve HTTP sunucusu hızında Node.js'ten 3-4 kat daha yüksek performans vadeder.
- **Edge Runtimes (Cloudflare Workers, Vercel Edge):** Tam teşekküllü bir Node süreci yerine saniyeler değil mikrosaniyeler içinde uyanan ultra hafif V8 Isolate sanal ortamlarıdır.

## Bir benzetmeyle

Compile-time bir binanın mimari çizimlerinin ve statik hesaplarının mühendis tarafından masada kontrol edilmesidir; bir hata varsa kâğıt üzerindeyken düzeltilir. Runtime ise o binanın inşa edilip içine insanların yerleştiği andır; deprem, su baskını veya aşırı yük gibi öngörülemeyen olaylar ancak bu aşamada binayı sınar.

## Sıkça sorulanlar

**Runtime ne demek, Türkçe karşılığı nedir?**  
Türkçede "çalışma zamanı" veya "yürütme ortamı" olarak adlandırılır. Bir programın kaynak kod halinden çıkıp bilgisayar donanımında fiilen çalıştığı zaman aralığını ve bu çalışmayı destekleyen yazılım katmanını niteler.

**Runtime Error (Çalışma Zamanı Hatası) nedir?**  
Derleme aşamasını başarıyla geçen ancak program çalışırken beklenmeyen bir durum (sıfıra bölme, boş bir nesneye erişim, RAM yetersizliği) nedeniyle uygulamanın aniden çökmesine yol açan hatadır.

**Node.js bir programlama dili midir, runtime mıdır?**  
Node.js bir dil değil; JavaScript kodunun tarayıcıya ihtiyaç duymadan sunucularda ve bilgisayarlarda çalışmasını sağlayan açık kaynaklı bir JavaScript çalışma ortamıdır (runtime).

**JIT (Just-In-Time) derleme runtime aşamasında nasıl çalışır?**  
JIT derleyici, program çalışırken sık kullanılan kod bloklarını ("hot paths") anında tespit eder ve bu blokları çalışma anında yerel makine koduna çevirerek uygulamanın performansını katlar.

## İlgili terimler

- [Memory Management](/dictionary/memory-management/)
- [Assembly](/dictionary/assembly/)
- [Compilation](/dictionary/compilation/)
- [Bundler](/dictionary/bundler/)
- [Tech Stack](/dictionary/tech-stack/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/runtime/  
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
