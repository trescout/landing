# Offline nedir, ne demek?

> Çevrimdışı

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

Offline (çevrimdışı), bir bilişim aygıtının veya yazılımın merkezi bir ağa ya da internete aktif bağlantı kurmaksızın temel işlevlerini yerel donanım kaynaklarıyla sürdürebilme durumudur.

## Etimoloji ve Çevrimdışı Mimarisi
Offline kavramı, telekomünikasyonun ilk yıllarında iletim hattına bağlı olmama durumunu belirten "off the line" tabirinden doğmuştur. Günümüz yazılım mühendisliğinde offline, yalnızca internet kablosunun çekilmesi durumunda sistemin donması anlamına gelmez. Modern disiplinde bu kavram, uygulamanın birincil çalışma alanı olarak yerel belleği (RAM), yerel diskleri (NVMe/SSD) ve istemci işlem gücünü (CPU/GPU/NPU) merkeze aldığı "Offline-First" mimarisini simgeler.

Geleneksel web ve bulut sistemleri, her kullanıcı etkileşimini uzaktaki sunucuya göndermek, orada işlemek ve yanıtı beklemek üzerine kuruludur; bu modelde ağ gecikmesi ve sunucu kesintileri deneyimi doğrudan kilitler. Offline sistemler ise veriyi doğrudan kullanıcının cihazında barındırır; ağ bağlantısını yalnızca isteğe bağlı ve asenkron bir eşitleme katmanı olarak konumlandırır. Bu mimari, veri güvenliğini zirveye taşırken ağ kopmalarına karşı tam dayanıklılık sağlar.

## Bir Benzetmeyle: Sahra Mühendisinin Çantası
Şöyle düşünün: İşlerini sürekli uzaktaki merkez ofise telefon açıp danışarak yürüten bir sahra mühendisi, telefon şebekesi çöktüğü anda hiçbir karar veremez ve işi tamamen durur. Buna karşın offline-first yaklaşım, aynı mühendisin yanındaki dayanıklı çantada projenin tüm planlarını, yönergelerini, teknik kütüphanesini ve hesap araçlarını taşıması gibidir. Mühendis dağ başında, internetin ve baz istasyonunun bulunmadığı en izole vadide bile notlarını alır, projelerini çizer ve hesaplarını tamamlar. Merkez ofisle bağlantı kurulduğu ilk anda ise yalnızca sahada aldığı yeni kayıtları merkeze ileterek iki tarafın verilerini eşitler. Offline yaklaşım, kullanıcıyı uzak bir sunucu sinyaline muhtaç olmaktan çıkarıp donanımının asıl sahibi yapar.

## Teknik Derinlik ve Sistem Mimarisi
Teknik düzeyde eksiksiz bir offline mimarisi, istemci tarafında yerel veri saklama, asenkron iletişim ve matematiksel uzlaşma protokollerinin uyumunu gerektirir:

1. **Yerel Depolama ve İstemci Veritabanları:** Web tarafında Service Workers ve Cache Storage API statik varlıkları saklarken, veri katmanında IndexedDB, SQLite, LibSQL veya WatermelonDB gibi yerel motorlar kullanılır. CRUD işlemleri milisaniyeler içinde yerel veritabanına işlenir; kullanıcı arabirimi sunucu yanıtı beklemeden anında güncellenir (iyimser güncelleme - optimistic update).

2. **Çatışmasız Çoğaltılmış Veri Tipleri (CRDT):** Çevrimdışı ortamda aynı veri kümesi üzerinde birden fazla istemcinin bağımsız değişiklikler yapması durumunda veri çakışması kaçınılmazdır. Modern sistemler, merkezi kilit mekanizmasına gerek duymadan dağıtık değişiklikleri matematiksel olarak birleştirebilen CRDT (Conflict-free Replicated Data Types) algoritmalarını kullanır. Yolda yazılan not internete bağlanıldığı anda sunucuyla kayıpsız birleşir.

3. **Hava Boşluğu (Air-Gapped) Güvenliği:** Yüksek güvenlik gerektiren askeri, tıbbi veya finansal sistemlerde çevrimdışı kalmak bilinçli bir mimari tercihtir. Dış ağlara fiziksel ve mantıksal olarak bağlanmayan hava boşluklu sistemler, uzaktan siber saldırı yüzeyini sıfıra indirir.

4. **Cihaz Üzerinde Yerel Yapay Zekâ (On-Device AI):** SLM (Small Language Model) ve kuantizasyon teknolojileri sayesinde derin öğrenme modelleri (Llama, Gemma vb.) WebGPU, NPU veya llama.cpp motorlarıyla internetten yalıtılmış olarak doğrudan dizüstü bilgisayarlarda çalıştırılabilmektedir.

## Sosyolojik Boyut: Ağ Bağımlılığı ve Veri Egemenliği
Offline sistemler, salt teknik bir mimari tercihi olmanın ötesinde, gözetim kapitalizmine ve dijital tekellere karşı güçlü bir politik ve felsefi duruşu ifade eder. Bulut bilişim şirketlerinin tüm kullanıcı hareketlerini, kişisel notlarını ve tüketim alışkanlıklarını merkezi sunucularında toplaması, bireyi sürekli gözetlenen bir veri kaynağına dönüştürür.

İnternet kesildiğinde çalışmayı reddeden akıllı ev cihazları veya not uygulamaları, kullanıcının gerçekte o cihazlara sahip olmadığını, yalnızca geçici bir hak kiraladığını gösterir. Offline-first ve yerel-merkezli (local-first) yazılımlar veri egemenliğini tekrar bireye devreder. Doğal afet, altyapı çöküşü veya sansür dönemlerinde toplumun işleyişini ayakta tutabilen yegane güç, çevrimdışı çalışabilen dayanıklı yazılımlardır.

## Sık Yapılan Hatalar ve Yanılgılar
Offline mimariler tasarlanırken en sık karşılaşılan yanılgılar şunlardır:
- **Sadece Hata Yönetimi Sanmak:** Offline olmayı yalnızca ağ hatası aldığında ekrana uyarı basmak sanmak; sistemin internet yokken de kesintisiz çalışması hedeflenmelidir.
- **Çakışma Çözümünü Basite İndirgemek:** Dağıtık veri değişikliklerinde en son yazanın kazanması mantığını körü körüne uygulamak, kritik veri kayıplarına yol açar.
- **Yerel Şifrelemeyi Unutmak:** Verilerin istemci cihazda saklanması fiziksel risk doğurur; yerel veritabanları mutlaka uçtan uca şifrelenmelidir (at-rest encryption).
- **Donanım Sınırlarını Yoksaymak:** Özellikle yerel yapay zekâ modelleri çalıştırılırken RAM, VRAM ve batarya bütçesi gözetilmeden optimizasyonsuz model yüklemek cihazı kilitleyebilir.

## Sıkça Sorulanlar

**Offline-first mimari ile geleneksel istemci-sunucu mimarisi arasındaki temel fark nedir?**  
Geleneksel mimari her istekte sunucuya ve aktif internete bağımlıyken, offline-first mimari yerel istemci veritabanını birincil kaynak kabul eder; internet bağlantısını yalnızca asenkron bir senkronizasyon aracı olarak kullanır.

**Çevrimdışı yapılan değişiklikler internete bağlanıldığında nasıl senkronize edilir?**  
İstemci ağ bağlantısını algıladığı anda yerel işlem günlüğünü sunucuya aktarır; CRDT veya Operasyonel Dönüştürme gibi algoritmalar sayesinde veri çakışmaları kayıpsız bir şekilde çözülerek merkezi veriyle eşitlenir.

**Hava boşluklu (air-gapped) sistem nedir ve ne zaman offline tutulmalıdır?**  
Fiziksel ve mantıksal olarak hiçbir dış ağa bağlı olmayan izole sistemlerdir; askeri donanımlar, nükleer santral kontrol üniteleri ve hassas tıbbi cihazlar gibi sıfır siber saldırı toleransı gerektiren senaryolarda tercih edilir.

**Cihaz üzerinde (offline) yapay zekâ çalıştırmak internet tabanlı modellere göre hangi avantajları sağlar?**  
İstemci tarafında çalışan yerel modeller sıfır ağ gecikmesi sunar, kullanıcı verileri asla üçüncü taraf sunuculara iletilmediği için mutlak veri mahremiyeti sağlar ve internet bağlantısı olmayan ortamlarda kesintisiz çalışır.

## İlgili terimler
- [Self-hosted](/dictionary/self-hosted/)
- [Local](/dictionary/local/)
- [Open Source](/dictionary/open-source/)
- [SLM](/dictionary/slm/)
- [Open Weights](/dictionary/open-weights/)
- [Quantization](/dictionary/quantization/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/offline/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
