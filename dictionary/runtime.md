# Runtime ne demek, nedir ve nasıl çalışır?

*Sözlük · Geliştirme · Son güncelleme: 19 Eylül 2026*

Runtime (çalışma zamanı), bir programın derleme evresinden sonra bilgisayar işlemcisinde ve belleğinde fiilen çalıştırıldığı zaman dilimini ve bu yürütmeyi mümkün kılan yazılımsal altyapıyı (Runtime Environment) ifade eder.

## 1. Runtime kavramının iki temel anlamı

Yazılım mühendisliğinde "Runtime" sözcüğü bağlama göre iki farklı kavrama işaret eder:

1. **Bir Zaman Evresi Olarak (Runtime / Çalışma Zamanı):** Kodun yazıldığı (authoring) ve derleyiciden geçirildiği (compile-time) aşamanın ardından, son kullanıcının programı başlattığı andan kapandığı ana kadar geçen süredir.
2. **Bir Yürütme Katmanı Olarak (Runtime Environment / Çalışma Ortamı):** Yazılan kodun işletim sistemi ve donanım üzerinde doğrudan koşabilmesi için gereken kütüphaneler, bellek yöneticileri, çöp toplayıcılar ve sanal makineler bütünüdür. Örneğin Node.js, JVM (Java Virtual Machine) veya Go Runtime birer yürütme ortamıdır.

## 2. Compile-Time vs Runtime farkı

- **Compile-Time (Derleme Zamanı):** Kod çalıştırılmadan önce sözdizimi analizi, statik tip denetimleri ve makine koduna çevrim yapılır. *Syntax Error* ve *Type Mismatch* hataları bu evrede yakalanır.
- **Runtime (Çalışma Zamanı):** Kullanıcı programı fiilen çalıştırırken bellek tahsisi, sistem çağrıları ve olay döngüsü yönetilir. *NullPointerException*, *Segmentation Fault (SIGSEGV)* ve *Stack Overflow* hataları bu evrede patlak verir.

## 3. Yönetilen (Managed) vs Yönetilmeyen (Unmanaged) Runtimelar

- **Yönetilmeyen (C, C++, Rust, Zig):** Doğrudan yerel makine koduna dönüşür; arka planda ağır bir sanal makine veya çöp toplayıcı çalışmaz, yalnızca hafif bir C standart kütüphanesi (`libc`) yeterlidir. Maksimum hız ve sıfır gecikme sunar.
- **Yönetilen (Java, C#, Go, JavaScript, Python):** Bir sanal makine (JVM, CLR) veya çalışma ortamı korumasında çalışır. JIT derleyicileri, otomatik çöp toplayıcıları ve Go örneğindeki gibi goroutine'leri yöneten dahili bir Scheduler barındırır.

## 4. Modern JavaScript Runtime Savaşları: Node.js vs Deno vs Bun

- **Node.js (2009):** Google V8 motoru ile C++ tabanlı `libuv` asenkron I/O olay döngüsünü birleştiren sektör standardıdır.
- **Deno (2018):** V8 motorunu Rust ve Tokio altyapısıyla harmanlayan, yerleşik TypeScript ve güvenli izin sandbox'ına sahip modern platformdur.
- **Bun (2023):** Apple WebKit'in `JavaScriptCore` motorunu kullanan ve tamamen Zig diliyle sıfırdan yazılmış, Node.js'e kıyasla kat kat hızlı dosya/ağ I/O'su sunan yeni nesil çalışma ortamıdır.

*Compile-time bir binanın mimari çizimlerinin ve statik hesaplarının mühendis tarafından masada kontrol edilmesidir; bir hata varsa kâğıt üzerindeyken düzeltilir. Runtime ise o binanın inşa edilip içine insanların yerleştiği andır; deprem, su baskını veya aşırı yük gibi öngörülemeyen olaylar ancak bu aşamada binayı sınar.*

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

- [Memory Management](https://trescout.com/dictionary/memory-management/)
- [Assembly](https://trescout.com/dictionary/assembly/)
- [Compilation](https://trescout.com/dictionary/compilation/)
- [Bundler](https://trescout.com/dictionary/bundler/)
- [Tech Stack](https://trescout.com/dictionary/tech-stack/)

## İlgili araçlar

- [Andrej Karpathy Skills](https://trescout.com/discover/andrej-karpathy-skills/)
- [Node](https://trescout.com/discover/node/)
- [Deno](https://trescout.com/discover/deno/)
- [BUN](https://trescout.com/discover/bun/)
- [Svelte](https://trescout.com/discover/svelte/)
- [Wand-Enhancer](https://trescout.com/discover/wand-enhancer/)
- [Univer](https://trescout.com/discover/univer/)
- [Onnxruntime](https://trescout.com/discover/onnxruntime/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/runtime/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
