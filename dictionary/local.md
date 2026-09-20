# Local ne demek, nedir?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

Local (yerel), bilişim ve yazılım dünyasında işlemlerin, verilerin veya hesaplama döngülerinin uzak bir bulut sunucusu yerine doğrudan kullanıcının kendi fiziksel cihazında, işletim sistemi çekirdeğinde veya fonksiyonel bellek kapsamında çalıştırılmasıdır.

## Etimoloji ve Bilişimde 4 Temel Katman
İngilizce kökenli *local* kelimesi Türkçede **yerel** anlamına gelir. Günlük hayatta belirli bir yöreye veya mekâna ait olanı tanımlayan bu sözcük, bilişim ekosisteminde dört kritik mühendislik katmanında temel bir kavramdır:
1. **Ağ ve İşletim Sistemi:** Bilgisayarın harici bir ağa çıkmadan kendi kendine konuşmasını sağlayan `localhost` ve geri döngü (loopback) arabirimi.
2. **Programlama Dilleri ve Bellek:** Bir fonksiyon veya blok içinde tanımlanan, yaşam döngüsü çağrı yığını (call stack) ile sınırlı olan yerel değişkenler (local variables).
3. **Yazılım Mimarisi (Local-First):** Verinin asıl sahibinin kullanıcının kendi cihazı olduğu, bulutun ise yalnızca senkronizasyon için ikincil bir katman olarak kullanıldığı modern mimari paradigma.
4. **Yapay Zekâ ve Uç Bilişim (Local AI):** Büyük dil modellerinin (LLM) harici API'lere bağımlı kalmaksızın doğrudan yerel GPU/NPU donanımı üzerinde çalıştırılması.

## 1. Ağ Boyutu: Localhost ve Loopback Arayüzü
Geliştiricilerin her gün kullandığı `localhost`, bilgisayarın ağ üzerindeki kendi kimliğidir:
- **Loopback Arayüzü:** Standart olarak `127.0.0.1` (IPv4) veya `::1` (IPv6) IP adresine atanmıştır. Bu adrese gönderilen ağ paketleri fiziksel ağ kartına (NIC) veya kabloya gitmez; işletim sistemi çekirdeği (kernel) içinde anında geri döndürülür.
- **Unix Domain Sockets:** Yerel makinede çalışan iki süreç (örneğin bir web sunucusu ile PostgreSQL veritabanı) ağ protokollerinin (TCP/IP checksum, paketleme) getirdiği ek yükten kaçınmak için doğrudan dosya sistemi tabanlı yerel soketler (`.sock`) üzerinden ışık hızında haberleşir.

## 2. Programlama Dilleri ve Bellek Yönetimi: Local Scope
Yazılım dillerinde bir değişkenin "local" (yerel) olması, bellek güvenliği ve performans için hayati önem taşır:
- **Çağrı Yığını (Call Stack) Ayrımı:** Bir fonksiyon çağrıldığında o fonksiyona ait yerel değişkenler stack frame içine yazılır. Fonksiyon tamamlandığında ise stack pointer geriye çekilir ve bu bellek anında, sıfır çöp toplama (GC) maliyetiyle sisteme geri kazandırılır.
- **Kapsam (Lexical Scoping) ve Gizleme:** Yerel değişkenler global isim alanını kirletmez ve yan etkileri (side effects) sınırlandırır. Fonksiyonel programlamada kapanışlar (closures), yerel değişkenlerin fonksiyon bittikten sonra da güvenli bir bağlamda yaşamasını sağlar.

## 3. Mimari Devrim: Local-First Yazılım Yaklaşımı
Geleneksel SaaS (Bulut) modelinde kullanıcının verileri uzak şirket sunucularında tutulur ve internet bağlantısı koptuğunda uygulama felç olur. **Local-First** hareketi (Ink & Switch araştırmacılarının öncülüğünde) bu paradigmayı tersine çevirir:
- **Veri Mülkiyeti:** Dosyalarınız ve veritabanınız doğrudan kendi sabit diskinizde (SQLite, Markdown veya yerel IndexedDB) saklanır.
- **Sıfır Gecikmeli Arayüz:** Kullanıcı bir tuşa bastığında yanıt uzak sunucudan beklenmez; arayüz yerel disk hızında mikrosaniyeler içinde güncellenir.
- **Çakışmasız Çoğaltılan Veri Tipleri (CRDT):** İnternet bağlantısı kesildiğinde birden fazla kullanıcı aynı belge üzerinde çalışsa bile, ağ yeniden kurulduğunda Automerge veya Yjs gibi algoritmalar sayesinde veriler insan müdahalesine gerek kalmadan matematiksel olarak pürüzsüzce birleşir (conflict-free merge).
- **Popüler Örnekler:** Obsidian not sistemi, Linear proje yönetimi ve yerel önbellek destekli modern geliştirici araçları.

## 4. Yapay Zekâda Yerel Devrim: Local AI
Yapay zekânın yükselişiyle birlikte "local" kavramı kurumsal güvenlik ve gizlilik için en kritik terim haline gelmiştir:
- **Veri Mahremiyeti (Sıfır Sızıntı):** Hassas şirket kodları, mali tablolar veya sağlık verileri OpenAI ya da Anthropic sunucularına iletilmez; Ollama, llama.cpp veya vLLM gibi açık kaynaklı çalışma ortamlarıyla yerel donanımda işlenir.
- **Maliyet ve Kota Bağımsızlığı:** Token başına API ücreti veya hız sınırlaması (rate limit) olmadan modeller sınırsızca çalıştırılır.
- **Apple Silicon ve Birleşik Bellek Avantajı:** CPU ve GPU'nun aynı yüksek hızlı bellek havuzunu (UMA) paylaşması, tüketici dizüstü bilgisayarlarında bile 70B parametreli modellerin yerel olarak yürütülmesini mümkün kılmıştır.

## Karşılaştırma: Local vs Self-Hosted vs Cloud
- **Local (Yerel):** Yazılım ve veri doğrudan kullanıcının kendi kişisel makinesindedir. İnternet gerekmez, maksimum gizlilik ve sıfır ağ gecikmesi sunar.
- **Self-Hosted (Kendi Sunucunda):** Kullanıcının ofisinde veya evinde bir sunucuda barındırılır; yerel ağ üzerinden bağlanılır, bakım yükü kullanıcıdadır.
- **Cloud (Bulut / SaaS):** Tüm donanım ve veri üçüncü taraf bir şirketin veri merkezindedir; yüksek erişilebilirlik sunar ancak sürekli internet ve gizlilik tavizi gerektirir.

## Sıkça Sorulanlar

**Local ne demek ve bilişimdeki karşılığı nedir?**  
İngilizce kökenli bir kelime olup Türkçede "yerel" anlamına gelir. Bilişimde verilerin ve programların internetteki uzak bir sunucu yerine kullanıcının kendi fiziksel cihazında bulunmasını ifade eder.

**Localhost (127.0.0.1) tam olarak nasıl çalışır?**  
Bilgisayarın harici bir ağ kartına veya internete ihtiyaç duymadan, işletim sistemi çekirdeği içerisinde kendi kendine paket gönderip almasını sağlayan özel geri döngü (loopback) mekanizmasıdır.

**Local-first yazılım yaklaşımının bulut sistemlerinden farkı nedir?**  
Bulut sistemlerinde ana veri sunucuda tutulurken, local-first yaklaşımında verinin asıl sahibi yerel cihazdır. İnternet olmasa dahi uygulama tam performansla çalışır ve ağ bağlandığında CRDT protokolleriyle bulutla eşitlenir.

**Yapay zekâ modellerini local (yerel) çalıştırmanın en büyük avantajı nedir?**  
Tam veri gizliliğidir. Kodlar, belgeler ve kullanıcı soruları harici bir bulut şirketine gönderilmez, internet kesintilerinden etkilenmez ve sürekli token API ücreti ödenmez.

## İlgili terimler
- [Self-hosted](/dictionary/self-hosted/)
- [Offline](/dictionary/offline/)
- [Runtime](/dictionary/runtime/)
- [Network Stack](/dictionary/network-stack/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/local/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
