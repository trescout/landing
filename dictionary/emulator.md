# Emülatör nedir ve nasıl çalışır?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

Emülatör (öykünücü), bir bilgisayarın, mobil cihazın veya oyun konsolunun fiziksel donanım mimarisini yazılımsal olarak taklit ederek, yabancı platformlara ait yazılımları kendi cihazınızda çalıştırmanızı sağlayan bir sistem katmanıdır.

## Kavramsal çerçeve, etimoloji ve simülatör farkı
Emülatör terimi Latince **"aemulari"** (öykünmek, yarışmak, eşit olmaya çalışmak) fiilinden türemiştir. Türkçede teknik olarak **"öykünücü"** veya **"donanım taklitçisi"** olarak adlandırılır. 

Bilişim dünyasında kavram karmaşasını önlemek için üç terimi birbirinden ayırmak gerekir:
- **Simülatör (Simulator):** Bir sistemin yalnızca dış davranışını, fizik kurallarını veya API çağrılarını modeller; alt donanımı taklit etmez. Örneğin Apple Xcode içindeki iOS Simulator, iOS kodunu doğrudan bilgisayarınızın x86 veya Apple Silicon işlemcisinde yerel olarak koşturur; donanım çiplerini taklit etmez.
- **Emülatör (Emulator):** Hedef sistemin işlemcisini (CPU), grafik çipini (GPU), bellek veri yollarını ve donanım kayıtçılarını (registers) buyruk seviyesinde (instruction-level) birebir kopyalar. Yabancı bir mimari için derlenmiş ikili makine kodunu (binary) satır satır kendi diline çevirir.
- **Sanallaştırıcı (Virtualizer):** Ana makineyle aynı işlemci mimarisine sahip sistemleri doğrudan donanım üzerinde izole bölümler halinde koşturur (KVM, VMware ESXi). Komut çevirisi yapmadığı için emülatörlere göre katbekat hızlıdır.

## Bilgisayar mimarisi ve çekirdek döngü: Fetch-Decode-Execute
Bir emülatörün kalbinde, yazılımsal olarak modellenmiş bir sanal CPU bulunur. Bu sanal işlemci her saat döngüsünde üç adımı işletir:
1. **Getir (Fetch):** Sanal program sayacının (Program Counter - PC) işaret ettiği sanal bellek adresinden bir sonraki makine komutunu okur.
2. **Çöz (Decode):** Komutun işlem kodunu (opcode) ve parametrelerini ayrıştırır (örneğin `MOV RAX, 0x1` veya `ADD R1, R2`).
3. **Yürüt (Execute):** Hedef donanımın mantığını ana bilgisayar üzerinde simüle ederek sanal kayıtçıları (registers) ve bayrakları (flags) günceller.

### Buyruk Çevrim Yöntemleri
- **Yorumlayıcı (Interpreter):** Her makine komutu bir `switch-case` döngüsü içinde tek tek okunur ve karşılığı olan C/Rust kodu çağrılır. Geliştirmesi kolaydır ve saat döngüsü hassastır ancak CPU'yu aşırı yorar (yavaştır).
- **Dinamik Yeniden Derleme (JIT - Just-In-Time Recompiler):** Modern emülatörlerin (Dolphin, RPCS3, QEMU) yüksek performans sırrıdır. Yabancı makine kod blokları çalışma anında analiz edilir, tek seferde ana işlemcinin (host CPU) yerel makine koduna dönüştürülür ve bellek önbelleğinde saklanır. Böylece aynı döngü tekrar çalıştığında çeviri maliyeti sıfıra iner.
- **Saat Hassasiyeti (Cycle Accuracy):** Bazı retro konsollarda (Game Boy, SNES) oyun geliştiricileri ses çipi ile raster tarama çizgisini nanosaniye seviyesinde donanım saatine senkronize etmiştir. Bu cihazları hatasız emüle etmek için her komutun tükettiği CPU saat döngüsü (cycles) gecikmesiz hesaplanmak zorundadır.

## Geliştirici, güvenlik ve kurumsal kullanım alanları
Emülatörler yalnızca retro konsol oyunlarını modern ekranlara taşımakla kalmaz; modern yazılım mühendisliğinin de kritik araçlarındandır:
- **Mobil Uygulama Geliştirme:** Android Studio Emulator, arka planda QEMU hipervizörünü kullanarak geliştiricilerin kodlarını gerçek bir telefon satın almadan yüzlerce farklı donanım ve ekran konfigürasyonunda test etmesini sağlar.
- **Çapraz Mimari Geçişleri (Binary Translation):** Apple'ın Intel işlemcilerden ARM mimarisine geçerken sunduğu Rosetta 2, aslında sofistike bir AOT (Ahead-of-Time) ve JIT ikili çeviri motorudur. Intel için yazılmış x86_64 uygulamalarını Apple Silicon üzerinde neredeyse kayıpsız hızda koşturur.
- **Siber Güvenlik ve Zararlı Yazılım Analizi (Sandbox Emulation):** Güvenlik analistleri, şüpheli bir fidye yazılımını doğrudan fiziksel bilgisayarda açmak yerine emüle edilmiş bir sanal CPU üzerinde çalıştırır. Bellek yazma hareketleri ve sistem çağrıları (syscalls) adım adım izlenir.
- **Kurumsal Miras Sistemler (Legacy Modernization):** Bankacılık, savunma ve kamu altyapılarında 1980'lerden kalma IBM Mainframe veya DEC VAX sistemleri, modern Linux sunucular üzerinde emülatörler aracılığıyla sıfır kesintiyle çalıştırılmaya devam eder.

## Bir benzetmeyle
Yabancı bir dilde yazılmış teknik bir el kitabını okumaya benzer. Simülatör, kitabın ne anlattığını özetleyen bir rehberdir; Yorumlayıcı emülatör, eline sözlük alıp her cümleyi kelime kelime ağır ağır çeviren bir öğrencidir; JIT emülatör ise kitabın bölümlerini profesyonelce kendi diline baştan çevirip not alan ve sonraki okumalarında doğrudan bu Türkçe metni akıcı biçimde okuyan simültane tercümandır.

## Hukuki boyut ve telif hakları
Emülatör geliştirmenin yasallığı dünya çapında emsal davalarla tescillenmiştir:
- **Sony v. Connectix (2000) ve Sony v. Bleem! Davaları:** Mahkemeler, bir donanımın çalışma prensiplerini temiz oda (clean-room reverse engineering) yöntemiyle tersine mühendislik yaparak yazılıma dökmenin yasal olduğuna ve adil kullanım (fair use) kapsamına girdiğine hükmetmiştir.
- **Telif Sınırı:** Emülatör yazılımının kendisi yasaldır. Ancak hedef cihazın telif hakkı içeren tescilli BIOS yazılımlarını veya telifli oyun/yazılım ROM dosyalarını izinsiz kopyalayıp internetten indirmek telif hakkı ihlali oluşturur.

## Sıkça sorulanlar

**Emülatör ne demek ve Türkçe karşılığı nedir?**  
İngilizce 'emulator' kelimesinden türeyen terim, Türkçede öykünücü veya donanım taklitçisi anlamına gelir. Bir cihazın donanım bileşenlerini yazılımla taklit ederek yabancı platform yazılımlarını çalıştıran sistemdir.

**Emülatör ile simülatör arasındaki temel fark nedir?**  
Simülatör yalnızca sistemin davranışını ve mantığını taklit ederken; emülatör hedef donanımın işlemcisini, bellek veri yolunu ve makine kodlarını buyruk seviyesinde birebir yazılımsal olarak kopyalar.

**JIT (Just-In-Time) dinamik derleyici emülasyonda nasıl çalışır?**  
Yabancı işlemcinin makine kod bloklarını çalışma anında bilgisayarınızın kendi işlemcisinin yerel makine koduna çevirir ve önbelleğe alır. Böylece kod ikinci kez çalıştırıldığında yerel hızda yürütülür.

**Emülatör geliştirmek ve kullanmak yasal mıdır?**  
Evet, temiz oda tersine mühendislik prensipleriyle yazılan emülatör yazılımları tamamen yasaldır. Ancak cihazın tescilli BIOS dosyalarını veya oyunların telifli ROM kopyalarını izinsiz dağıtmak telif ihlali oluşturur.

## İlgili terimler
- [ROM](/dictionary/rom/)
- [Sandbox](/dictionary/sandbox/)
- [Virtual Machines](/dictionary/virtual-machines/)
- [Assembly](/dictionary/assembly/)
- [Runtime](/dictionary/runtime/)
- [Apple Silicon](/dictionary/apple-silicon/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/emulator/  
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
