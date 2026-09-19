# Apple Silicon nedir ve nasıl çalışır?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

Apple Silicon, Apple'ın Mac ve iPad cihazları için kendi bünyesinde tasarladığı; CPU, GPU, Neural Engine ve birleşik belleği (Unified Memory) tek bir silikon plaka üzerinde buluşturan ARM tabanlı yüksek performanslı SoC (System on a Chip) işlemci ailesidir.

## Kavramsal doğuş, tarihçe ve x86'dan ARM'a büyük göç
"Silicon" (silisyum), yarı iletken mikroçiplerin üretiminde kullanılan temel kimyasal elementtir. Apple Silicon ise Apple'ın üçüncü taraf çip üreticilerine (Intel, Motorola, IBM) olan bağımlılığını sonlandırarak kendi donanım ve yazılımını dikey olarak entegre ettiği özel mikroişlemci tasarımını temsil eder.

Apple, bilgisayar mimarisi tarihinde benzersiz bir mirasa sahiptir; şirket platform mimarisini tam üç kez radikal biçimde değiştirmiştir:
1. **1994:** Motorola 68000 serisinden PowerPC RISC mimarisine geçiş.
2. **2006:** PowerPC'den x86 mimarisini kullanan Intel Core işlemcilere geçiş.
3. **2020 (Büyük Dönüm Noktası):** Intel x86 mimarisi tamamen terk edilerek, iPhone'lardaki A serisi çiplerden edinilen 10 yıllık ARM deneyimiyle tasarlanan **Apple Silicon M serisi (M1, M2, M3, M4)** duyuruldu.

Bu dönüşüm, bilgisayar endüstrisindeki geleneksel CISC (karmaşık komut kümesi) egemenliğini kırarak, modern 64-bit ARM RISC (indirgenmiş komut kümesi) mimarisinin yüksek performanslı kişisel bilgisayarlarda da zirveye oturabileceğini tüm dünyaya kanıtladı.

## Çip üzerinde sistem (SoC) ve Birleşik Bellek Mimarisi (UMA)
Geleneksel bir masaüstü veya dizüstü bilgisayarda donanım parçalıdır: Anakart üzerinde ayrı bir CPU soketi, PCIe yuvasına takılan devasa bir harici ekran kartı (GPU), ayrı RAM modülleri ve anakart köprüleri bulunur. CPU'nun işlediği bir görüntüyü ekrana basmak için veri anakart veri yolu (bus) üzerinden RAM'den GPU'nun kendi VRAM belleğine kopyalanmak zorundadır. Bu durum gecikme (latency) ve yüksek güç tüketimi yaratır.

Apple Silicon ise bu paradigmayı kökten yıkar:
- **SoC (System on a Chip):** CPU, GPU, yapay zekâ hızlandırıcısı (NPU), görüntü sinyal işlemcisi (ISP) ve güvenlik donanımı (Secure Enclave) tek bir silikon kalıp üzerinde birleştirilmiştir.
- **Birleşik Bellek Mimarisi (UMA - Unified Memory Architecture):** Yüksek hızlı LPDDR5X bellekler doğrudan işlemci paketinin hemen yanına entegre edilmiştir. CPU, GPU ve Neural Engine aynı bellek havuzunu sıfır kopyalama (Zero-Copy) ile paylaşır. 800 GB/s'ye varan devasa bellek bant genişliği sayesinde veriyi bir birimden diğerine aktarma masrafı tamamen ortadan kalkar.

### Yerel Yapay Zekâ ve LLM Çıkarımında Bir Numara
Birleşik Bellek Mimarisi, üretken yapay zekâ çağında Mac bilgisayarları geliştiriciler için adeta bir AI iş istasyonuna dönüştürmüştür. Standart bir PC'de 70 milyar parametreli bir açık kaynaklı yapay zekâ modelini (Llama 3 70B) çalıştırmak için en az 48-64 GB VRAM'e sahip on binlerce dolarlık profesyonel sunucu GPU'ları gerekir. Oysa 128 GB Birleşik Belleğe sahip bir Apple Silicon Mac Studio, bu RAM'in neredeyse tamamını GPU'ya tek bir havuz olarak tahsis edebilir. Apple'ın geliştirdiği açık kaynaklı **MLX** kütüphanesi sayesinde dev dil modelleri yerel olarak sessizce ve düşük güçle koşturulabilir.

## Çekirdek anatomisi, hızlandırıcılar ve Rosetta 2
Apple Silicon'ın saf performans ve verimlilik dengesi üç temel mühendislik bileşenine dayanır:

1. **Heterojen Çekirdek Mimarisi (big.LITTLE):** İşlemci iki farklı çekirdek tipini bir arada barındırır. **Performans Çekirdekleri (P-Cores)** devasa komut yürütme genişliğiyle derleme ve video işleme gibi ağır işleri üstlenirken; **Verimlilik Çekirdekleri (E-Cores)** arka plan görevlerini ve metin yazımını neredeyse hiç pil harcamadan yürütür.
2. **Özel Donanım Hızlandırıcıları:** Genel CPU'yu yormamak için özel görev birimleri bulunur: Yapay zekâ tensör hesaplamaları için **Neural Engine**, matris çarpımları için dahili **AMX (Apple Matrix Coprocessor)** ve 8K video işleme için donanımsal **Media Engine** (ProRes/AV1 decoder).
3. **Rosetta 2 İkili Çevirisi (Binary Translation):** Intel (x86_64) için derlenmiş eski Mac uygulamaları, Rosetta 2 sayesinde kullanıcı uygulamayı ilk açtığı anda (AOT - Ahead-of-Time) otomatik olarak ARM64 koduna çevrilir. Apple Silicon çipleri, donanım seviyesinde x86'nın bellek modeli olan **TSO (Total Store Ordering)** desteği barındırdığı için bu çeviri neredeyse yerel hızda çalışır.

## Bir benzetmeyle
Geleneksel bilgisayarlar, şehrin farklı semtlerine dağılmış ofisler gibidir (CPU bir mahallede, ekran kartı başka bir ilçede, RAM ise şehirlerarası depodadır); departmanlar birbirine evrak göndermek için kurye beklemek zorundadır. Apple Silicon ise tüm uzman mühendislerin, grafikerlerin ve analistlerin aynı yuvarlak masada oturduğu ultra modern bir tasarım odası gibidir; masanın ortasındaki devasa beyaz tahta (Birleşik Bellek) herkese açıktır, hiç kimse evrak fotokopisiyle vakit kaybetmez.

## Sıkça sorulanlar

**Apple Silicon ne demek ve hangi işlemcileri kapsar?**  
Apple'ın kendi tasarladığı ARM tabanlı Çip Üzerinde Sistem (SoC) işlemci ailesidir. iPhone ve iPad'lerdeki A serisi yongalar ile Mac bilgisayarlara güç veren M serisi (M1, M2, M3, M4 ve bunların Pro, Max, Ultra varyantları) işlemcileri kapsar.

**Birleşik Bellek Mimarisi (UMA) geleneksel RAM ve VRAM'den neden farklıdır?**  
Geleneksel sistemlerde CPU ayrı bir sistem RAM'ine, ekran kartı ise ayrı bir VRAM'e sahiptir ve veri bu ikisi arasında kopyalanır. UMA'da ise bellek doğrudan işlemci paketindedir; CPU, GPU ve yapay zekâ motoru aynı bellek havuzuna kopyalama gecikmesi olmadan sıfır maliyetle erişir.

**Apple Silicon işlemcili bir Mac'te eski Intel uygulamaları çalışır mı?**  
Evet, macOS işletim sistemine entegre gelen Rosetta 2 çeviri motoru sayesinde Intel (x86_64) için yazılmış uygulamaların büyük çoğunluğu kullanıcı fark etmeden yüksek hızda çalıştırılır.

**Apple Silicon yerel yapay zekâ (LLM) geliştirmede neden bu kadar popülerdir?**  
Çünkü Birleşik Bellek Mimarisi sayesinde 64 GB, 96 GB veya 128 GB gibi devasa bellek havuzları doğrudan GPU tarafından VRAM olarak kullanılabilir. Bu da pahalı sunucu GPU'ları olmadan 70B+ parametreli dev dil modellerinin yerel olarak çalıştırılmasını sağlar.

## İlgili terimler
- [Runtime](/dictionary/runtime/)
- [Computer Science](/dictionary/computer-science/)
- [Assembly](/dictionary/assembly/)
- [Memory Management](/dictionary/memory-management/)
- [Emulator](/dictionary/emulator/)
- [Cloud Computing](/dictionary/cloud-computing/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/apple-silicon/  
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
