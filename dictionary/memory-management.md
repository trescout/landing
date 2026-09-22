# Memory Management nedir, ne demek ve nasıl çalışır?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

Memory Management (bellek yönetimi), bilgisayarın fiziksel ve sanal rastgele erişimli belleğinin (RAM) çalışan yazılımlar arasında tahsis edilmesi, korunması ve kullanım bittiğinde sisteme iade edilmesi sürecidir.

## 1. Bellek anatomisi: Stack (Yığın) ve Heap (Öbek) ayrımı

Bir program çalıştırıldığında işletim sistemi o sürece özel bir sanal bellek uzayı (Virtual Address Space) tahsis eder. Bu uzayın en kritik iki bileşeni Stack ve Heap'tir:

```
+------------------------------------+ Yüksek Bellek Adresleri (0xFFFFFFFF)
|           İşletim Sistemi / Kernel |
+------------------------------------+
|  STACK (Aşağıya doğru büyür ↓)     | <-- Yerel değişkenler, fonksiyon çerçeveleri
|                 ↓                  |
|                                    |
|                 ↑                  |
|  HEAP (Yukarıya doğru büyür ↑)     | <-- Dinamik nesneler (malloc, new)
+------------------------------------+
|  BSS (İlklendirilmemiş Global)     |
+------------------------------------+
|  DATA (İlklendirilmiş Statik Veri) |
+------------------------------------+
|  TEXT (Makine Kodu / Talimatlar)   |
+------------------------------------+ Düşük Bellek Adresleri (0x00000000)
```

| Özellik | Stack (Yığın) | Heap (Öbek) |
| :--- | :--- | :--- |
| **Yönetim** | CPU mimarisi tarafından otomatik yönetilir (LIFO). | Yazılımcı veya dilin çalışma ortamı (Runtime) yönetir. |
| **Hız** | Son derece hızlıdır (yalnızca stack pointer register kaydırılır). | Görece yavaştır (uygun boş bellek bloğunun aranması gerekir). |
| **Boyut** | Sınırlı ve sabittir (genellikle 1MB - 8MB arası). | Fiziksel RAM ve takas (swap) alanı kadar genişleyebilir. |
| **Ömür** | Fonksiyon çalıştığı sürece yaşar, fonksiyon dönünce yok edilir. | Açıkça serbest bırakılana veya çöp toplayıcı silene kadar yaşar. |
| **Hata Riski** | Sonsuz özyinelemede (recursion) **Stack Overflow** oluşur. | Temizlenmezse **Memory Leak** ve parçalanma (fragmentation) oluşur. |

## 2. Üç temel bellek yönetimi paradigması

Yazılım dünyasında belleğin ne zaman tahsis edilip ne zaman serbest bırakılacağına dair üç farklı felsefe uygulanır:

### A. Manuel Bellek Yönetimi (C, C++)
Yazılımcı, belleği işletim sisteminden `malloc()`, `calloc()` veya `new` ile bizzat ister ve işi bittiğinde `free()` veya `delete` ile sisteme geri verir.
- **Avantajı:** Sıfır gecikme, tam donanım kontrolü ve maksimum performans.
- **Tehlikeleri:** Yazılım tarihindeki siber güvenlik açıklarının %70'inden fazlası manuel bellek yönetim hatalarından kaynaklanır:
  - **Memory Leak (Bellek Sızıntısı):** `free` edilmeyen bloklar nedeniyle RAM'in dolması.
  - **Dangling Pointer (Sarkan İşaretçi):** Silinmiş bir bellek adresine işaret eden gösterici.
  - **Use-After-Free & Double Free:** Serbest bırakılan alanın tekrar okunması ya da iki kez silinmesi sonucu oluşan uzaktan kod yürütme (RCE) açıkları.

### B. Otomatik Çöp Toplama (Garbage Collection - Java, Go, Python, JavaScript)
Programcı bellek tahsis eder, ancak silme işlemini düşünmez. Arka planda çalışan bir çöp toplayıcı (GC motoru), artık ulaşılamayan nesneleri tespit edip temizler.
- **İşaretle ve Süpür (Mark-and-Sweep):** Kök referanslardan başlanarak erişilebilen tüm nesneler taranır, ulaşılamayanlar süpürülür.
- **Referans Sayımı (Reference Counting):** Python ve Swift'te her nesnenin kaç işaretçi tarafından tutulduğu sayılır; sayaç sıfıra düştüğünde nesne anında silinir.
- **Maliyeti:** Periyodik olarak çalışan GC taramaları işlemciyi meşgul eder ve oyunlarda veya yüksek frekanslı alım-satım (HFT) sistemlerinde mikro gecikmelere ("Stop-The-World" duraklamaları) yol açar.

### C. Sahiplik ve Ömür Modeli (Ownership & Borrowing - Rust)
Rust derleyicisi, her bellek bloğunun tek bir sahibi olduğunu ve bu sahibin kapsamından (scope) çıkıldığı an belleğin otomatik serbest bırakılacağını derleme anında doğrular.
- **Sonuç:** Çalışma zamanında ağır bir çöp toplayıcı çalıştırmadan, C hızında %100 bellek güvenliği (Memory Safety).

## 3. İşletim sistemi seviyesinde bellek: Sanal bellek ve OOM Killer

Fiziksel RAM tek bir havuzdur, ancak modern işletim sistemleri programların birbirinin belleğini okumasını engellemek için **Sanal Bellek (Virtual Memory)** ve **Sayfalama (Paging)** mimarisi kullanır.

- **Page Table ve TLB:** CPU'daki Bellek Yönetim Birimi (MMU), sanal adresleri donanımdaki fiziksel adreslere mikrosaniyeler içinde dönüştürür.
- **OOM Killer (Out of Memory Killer):** Fiziksel RAM ve sanal takas (swap) alanı tamamen tükendiğinde, Linux çekirdeği işletim sisteminin çökmesini engellemek için en çok bellek tüketen süreci tespit ederek acımasızca sonlandırır (`SIGKILL - Signal 9`).

## Bir benzetmeyle

Stack, masanızdaki kâğıt evrak kulesidir; gelen evrakı en üste koyarsınız ve işiniz bitince en üsttekini anında alırsınız, yerleştirme süresi sıfırdır. Heap ise büyük bir depo gibidir; depocuya gidip kutu için boş bir raf istersiniz, depocu uygun yeri arar, anahtarı size verir ve işiniz bittiğinde rafı depocuya teslim etmeyi unutursanız depo kısa sürede kullanılamaz hale gelir.

## Sıkça sorulanlar

**Memory management ne demek, Türkçe karşılığı nedir?**  
Memory Management Türkçede "bellek yönetimi" anlamına gelir. Bir bilgisayar programının çalışması esnasında RAM kaynaklarının tahsis edilmesi, izlenmesi ve serbest bırakılması süreçlerinin tümüdür.

**Stack ile Heap arasındaki en temel fark nedir?**  
Stack boyutu derleme anında bilinen yerel değişkenleri son derece hızlı şekilde LIFO mantığıyla yönetir; Heap ise çalışma anında dinamik olarak büyüyen nesneler için ayrılan, yönetimi daha karmaşık olan esnek bellek havuzudur.

**Garbage Collection (Çöp Toplayıcı) nasıl çalışır?**  
Yazılımcının manuel silme yapmadığı dillerde (Java, Go, JS vb.) arka planda çalışan motor, kök değişkenlerden ulaşılamayan yetim nesneleri tespit eder ve RAM'i temizler.

**Bellek sızıntısı (Memory Leak) nasıl engellenir?**  
Manuel dillerde her `malloc` için bir `free` yazılarak veya RAII desenleri kurularak; çöp toplayıcılı dillerde ise global dizi referansları ve kapatılmayan olay dinleyicileri (event listeners) temizlenerek engellenir.

## İlgili terimler

- [Runtime](/dictionary/runtime/)
- [State Management](/dictionary/state-management/)
- [Serialization](/dictionary/serialization/)
- [Network Stack](/dictionary/network-stack/)
- [Assembly](/dictionary/assembly/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/memory-management/  
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
