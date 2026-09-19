# Memory Management nedir, ne demek?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

Memory Management (bellek yönetimi), bilgisayarın rastgele erişimli belleğinin (RAM) çalışan programlar arasında tahsis edilmesi ve temizlenmesi sürecidir.

## Tanım ve bellek mimarisi
Bellek Yönetimi (Memory Management), bir yazılımın veya işletim sisteminin geçici bellek (RAM) kaynaklarını kontrol etme metodolojisidir. Bir program başlatıldığında veya değişken tanımlandığında işletim sistemi bellekte yer ayırır (allocation). İlgili verilerle iş bittiğinde ise bu alanın sisteme iade edilmesi (deallocation) gerekir. Doğru yönetilmeyen bellek, sızıntılara (memory leak) ve uygulamanın çökmesine yol açar.

## Bir benzetmeyle
Büyük bir otoparkın vale görevlisi gibidir: Gelen her arabaya (çalışan fonksiyona veya değişkene) uygun boyutta bir park yeri tahsis eder; araba işini bitirip ayrıldığında ise o yeri temizleyip yeni gelen araçlara hazır hale getirir.

## Nasıl çalışır?
1. **Stack ve Heap Ayrımı:**
   - **Stack (Yığın):** Boyutu derleme anında bilinen yerel değişkenlerin tutulduğu, son giren ilk çıkar (LIFO) mantığıyla çalışan son derece hızlı bellek alanıdır.
   - **Heap (Öbek):** Dinamik olarak çalışma zamanında (runtime) tahsis edilen, daha büyük ancak yönetimi daha karmaşık olan bellek havuzudur.
2. **Otomatik Çöp Toplama (Garbage Collection):** JavaScript, Python, Go ve Java gibi modern dillerde artık referans verilmeyen nesneler arka plandaki GC motoru tarafından periyodik olarak taranır ve bellekten silinir.
3. **Manuel Bellek Yönetimi:** C ve C++ gibi sistem dillerinde geliştirici `malloc`/`free` ile belleği bizzat yönetirken; Rust, sahiplik (ownership) modeliyle derleme anında bellek güvenliğini sağlar.

## Nerede kullanılır?
İşletim sistemi çekirdeklerinde, oyun motorlarında (Unity, Unreal Engine), veritabanlarında ve yüksek performanslı arka uç mimarilerinde performansı belirleyen ana etkendir.

## Sık karıştırılanlar
Kalıcı depolama (SSD / Sabit Disk) ile karıştırılmamalıdır; bellek yönetimi yalnızca bilgisayar açıkken çalışan geçici RAM belleğin optimizasyonunu kapsar.

## Sıkça sorulanlar

**Memory management ne demek ve Türkçe karşılığı nedir?**  
Türkçede 'bellek yönetimi' olarak ifade edilir. Yazılımların RAM kaynaklarını verimli kullanması için geliştirilen kontrol mekanizmalarıdır.

**Bellek sızıntısı (Memory Leak) nedir ve nasıl önlenir?**  
Programın artık ihtiyaç duymadığı bellek alanlarını serbest bırakmaması sonucu RAM tüketiminin sürekli artması durumudur. Profiling araçları ve referans döngülerini temizleyerek önlenir.

**Rust dili neden Garbage Collector olmadan bellek güvenliği sunar?**  
Rust, 'Ownership ve Borrowing' (sahiplik ve ödünç alma) kurallarını derleme anında doğrular; böylece çalışma zamanında bir çöp toplayıcı çalıştırmadan bellek güvenliği ve maksimum hız sağlar.

## İlgili terimler
- [State Management](/dictionary/state-management/)
- [Memory Engine](/dictionary/memory-engine/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/memory-management/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
