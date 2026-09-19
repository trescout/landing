# Assembly nedir, ne demek?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

Assembly, bilişimde iki temel kavrama karşılık gelir: Birincisi donanım işlemcisine doğrudan hükmeden en düşük seviyeli sembolik programlama dili; ikincisi ise farklı yazılım bileşenlerinin, modüllerinin veya kütüphanelerinin tek bir çalışabilir bütün halinde montajlanması (birleştirilmesi) sürecidir.

## Tanım ve İki Temel Anlamı
- **1. Düşük Seviyeli Programlama Dili (Assembly Language):** Bilgisayar işlemcisinin (CPU) anladığı 0 ve 1'lerden oluşan ikili makine kodlarının, insan tarafından okunabilir sembolik komutlara (`MOV`, `ADD`, `PUSH`, `JMP`) dönüştürülmüş halidir. Yazılan kodlar **Assembler** adı verilen dönüştürücülerle doğrudan makine koduna çevrilir.
- **2. Yazılım Bileşen Montajı (.NET / Software Assembly):** Yazılım mühendisliğinde farklı kaynak dosyalarının, bağımlılıkların ve kütüphanelerin bir araya getirilerek tek bir yürütülebilir veya dağıtılabilir paket (.dll, .exe, .jar) haline getirilmesi sürecidir.

## Bir benzetmeyle
Assembly dili, bir saatin içindeki çarkları, yayları ve milleri mikroskop altında cımbızla tek tek yerleştirmeye benzer; en yüksek hassasiyet ve performansı sağlar ama büyük dikkat ister. Yazılım montajı ise üretilen bu hassas mekanizmayı kasanın içine oturtup çalışır bir kol saati olarak kutulamaktır.

## Nerede ve Hangi Alanlarda Kullanılır?
- **Tersine Mühendislik ve Güvenlik:** Zararlı yazılım (malware) analizi, güvenlik açığı tespiti ve ikili kod (binary) denetimleri.
- **İşletim Sistemi ve Sürücü Geliştirme:** Çekirdek (Kernel) önyükleyicileri (bootloader), donanım aygıt sürücüleri ve doğrudan CPU register yönetimi.
- **Gömülü Sistemler ve IoT:** Donanım ve bellek kaynaklarının son derece sınırlı olduğu mikrodenetleyiciler (ARM, RISC-V, AVR).
- **Yüksek Başarımlı Hesaplama:** Grafik motorları, kriptografi algoritmaları ve anlık gecikme toleransı olmayan sistemler.

## Sık karıştırılanlar
Üst seviye diller (Python, C#, JavaScript) ile Assembly dili karıştırılmamalıdır. Üst seviye diller donanımdan tamamen soyutlanmış taşınabilir kod üretirken, Assembly dili doğrudan kullanılan işlemcinin mimarisine (x86_64, ARM64) sıkı sıkıya bağlıdır. Ayrıca modern bir standart olan **WebAssembly (WASM)**, web tarayıcılarında çalışan güvenli bir sanal makine ikili kodudur; geleneksel işlemci assembly dilinden farklıdır.

## Sıkça sorulanlar

**Assembly nedir ve ne işe yarar?**  
Donanım işlemcisine en yakın sembolik programlama dilidir; doğrudan işlemci kayıtçılarını (register), yığın (stack) bellek alanını ve CPU komut setini yönetmek için kullanılır.

**Assembly dili öğrenmek zor mudur?**  
Evet, bellek tahsisinden işlemci döngülerine kadar her ayrıntıyı geliştiricinin yönetmesi gerektiğinden öğrenme eğrisi üst seviye dillere göre oldukça yüksektir.

**WebAssembly ile Assembly aynı şey midir?**  
Hayır; WebAssembly (WASM), C/C++ ve Rust gibi dillerin web tarayıcılarında neredeyse yerel hızda çalışmasını sağlayan taşınabilir bir ikili bayt kodu formatıdır.

**Yazılım geliştirmede "Assembly" dosya paketi ne anlama gelir?**  
Özellikle .NET dünyasında, derlenmiş C# kodlarını, tip meta verilerini ve manifestoyu barındıran dağıtılabilir mantıksal birimdir (.dll veya .exe).

## İlgili terimler
- [Compilation](/dictionary/compilation/)
- [Bundling](/dictionary/bundling/)
- [Deployment](/dictionary/deployment/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/assembly/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
