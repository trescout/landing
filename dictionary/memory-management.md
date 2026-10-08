# Memory Management nedir, ne demek ve nasıl çalışır?

*Sözlük · Geliştirme · Son güncelleme: 19 Eylül 2026*

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

- **Stack (Yığın):** CPU mimarisi tarafından otomatik yönetilir (LIFO). Son derece hızlıdır (yalnızca stack pointer register kaydırılır). Ancak boyutu sabittir (1MB - 8MB) ve sonsuz özyinelemede **Stack Overflow** verir.
- **Heap (Öbek):** Yazılımcı veya dilin çalışma ortamı (Runtime) yönetir. Dinamik nesneler için ayrılır; fiziksel RAM ve takas (swap) kadar büyüyebilir. Temizlenmezse **Memory Leak** ve parçalanma (fragmentation) yaratır.

## 2. Üç temel bellek yönetimi paradigması

- **Manuel Bellek Yönetimi (C, C++):** Yazılımcı `malloc()` ve `free()` ile belleği bizzat yönetir. Maksimum hız ve sıfır gecikme sunar; ancak yazılım dünyasındaki güvenlik açıklarının %70'inden fazlasına sebep olan sızıntı, sarkan işaretçi (dangling pointer) ve Use-After-Free risklerini taşır.
- **Otomatik Çöp Toplama (Garbage Collection - Java, Go, Python, JS):** Programcı silme yapmaz; arka planda çalışan GC motoru kök referanslardan ulaşılamayan yetim nesneleri Mark-and-Sweep veya Reference Counting algoritmalarıyla temizler. Ancak periyodik taramalar mikro duraklamalara (Stop-The-World) yol açabilir.
- **Sahiplik ve Ömür Modeli (Ownership & Borrowing - Rust):** Rust derleyicisi her bellek bloğunun tek bir sahibi olduğunu derleme anında doğrular. Çöp toplayıcı çalıştırmadan, C hızında %100 bellek güvenliği (Memory Safety) sağlar.

## 3. İşletim sistemi seviyesinde bellek: Sanal bellek ve OOM Killer

Modern işletim sistemleri programların birbirinin belleğini okumasını engellemek için **Sanal Bellek (Virtual Memory)** ve **Sayfalama (Paging)** mimarisi kullanır. CPU'daki Bellek Yönetim Birimi (MMU), sanal adresleri donanımdaki fiziksel adreslere TLB önbelleği yardımıyla dönüştürür. Fiziksel RAM ve swap tamamen tükendiğinde ise Linux çekirdeğinin **OOM Killer (Out of Memory Killer)** mekanizması sistemi kurtarmak için en agresif süreci `SIGKILL` ile sonlandırır.

*Stack, masanızdaki kâğıt evrak kulesidir; gelen evrakı en üste koyarsınız ve işiniz bitince en üsttekini anında alırsınız, yerleştirme süresi sıfırdır. Heap ise büyük bir depo gibidir; depocuya gidip kutu için boş bir raf istersiniz, depocu uygun yeri arar, anahtarı size verir ve işiniz bittiğinde rafı depocuya teslim etmeyi unutursanız depo kısa sürede kullanılamaz hale gelir.*

## Sıkça sorulanlar

**Memory management ne demek, Türkçe karşılığı nedir?**

Memory Management Türkçede "bellek yönetimi" anlamına gelir. Bir bilgisayar programının çalışması esnasında RAM kaynaklarının tahsis edilmesi, izlenmesi ve serbest bırakılması süreçlerinin tümüdür.

**Stack ile Heap arasındaki en temel fark nedir?**

Stack boyutu derleme anında bilinen yerel değişkenleri son derece hızlı şekilde LIFO mantığıyla yönetir; Heap ise çalışma anında dinamik olarak büyüyen nesneler için ayrılan, yönetimi daha karmaşık olan esnek bellek havuzudur.

**Garbage Collection (Çöp Toplayıcı) nasıl çalışır?**

Yazılımcının manuel silme yapmadığı dillerde (Java, Go, JS vb.) arka planda çalışan motor, kök değişkenlerden ulaşılamayan yetim nesneleri tespit eder ve RAM'i temizler.

**Bellek sızıntısı (Memory Leak) nasıl engellenir?**

Manuel dillerde her malloc için bir free yazılarak veya RAII desenleri kurularak; çöp toplayıcılı dillerde ise global dizi referansları ve kapatılmayan olay dinleyicileri (event listeners) temizlenerek engellenir.

## İlgili terimler

- [Runtime](https://trescout.com/dictionary/runtime/)
- [State Management](https://trescout.com/dictionary/state-management/)
- [Serialization](https://trescout.com/dictionary/serialization/)
- [Network Stack](https://trescout.com/dictionary/network-stack/)
- [Assembly](https://trescout.com/dictionary/assembly/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/memory-management/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
