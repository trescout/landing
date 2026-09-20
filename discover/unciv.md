# Hafif ve açık kaynaklı strateji oyunu

Unciv, Civilization V oyununun açık kaynak kodlu, minimalist ve çapraz platformlu bir masaüstü ve Android uyarlamasıdır. Kotlin ve LibGDX altyapısıyla geliştirilen proje, orijinal 4X strateji mekaniklerini sıfır donanım yükü ve yüksek mod desteğiyle sunar.

- ★ 11.285
- Kotlin
- GitHub Trending · 2026-06-18

## Güncelleme
- 18 Eylül 2026: Yıldız 11.276 → 11.285, son sürüm 4.22.1 (17 Eylül 2026).
- 15 Eylül 2026: Yıldız 11.257 → 11.276, son sürüm 4.22.0 (14 Eylül 2026).
- 10 Eylül 2026: Yıldız 11.241 → 11.257, son sürüm 4.21.19 (9 Eylül 2026).
- 8 Eylül 2026: Yıldız 11.223 → 11.241, son sürüm 4.21.18 (7 Eylül 2026).

## Ne kazandırır?
- Düşük donanım ve batarya dostu mimari: Ağır 3D render motorları yerine 2D vektörel ve piksel grafikler kullanarak en temel mobil cihazlarda dahi sıfır ısınma ile çalışır.
- Orijinal Civilization V mekanikleri: Şehir planlaması, teknoloji ağacı, sosyal politikalar, diplomasi ve taktiksel altıgen (hex) savaş sistemi eksiksiz korunur.
- Çapraz platform kayıt ve çok oyunculu destek: Masaüstü ve Android arasında kayıt dosyalarını doğrudan taşıyabilir veya e-posta/sunucu tabanlı tur usulü çok oyunculu maçlar yapabilirsiniz.
- Topluluk odaklı zengin mod ekosistemi: Yeni medeniyetler, birimler, fantezi senaryoları ve grafik temaları oyun içi arayüzden tek tıkla yüklenip etkinleştirilebilir.
- Tamamen özgür ve reklamsız deneyim: MPL-2.0 lisansıyla dağıtılır; uygulama içi satın alma, reklam, izleme veya veri toplama içermez.

## Nasıl başlanır ve kurulum seçenekleri

Unciv projesini cihazınızda oynamak için platformunuza uygun dağıtım kanalını seçebilirsiniz. Mobil tarafta Android kullanıcıları Google Play Store veya gizlilik odaklı F-Droid deposu üzerinden kurulum yapabilir. Masaüstü tarafında ise Windows için doğrudan MSI veya taşınabilir ZIP dosyaları, Linux için Flatpak paketi veya itch.io dağıtımları tercih edilebilir.
- [Google Play Store Sayfası →](https://play.google.com/store/apps/details?id=com.unciv.app)
- [F-Droid Açık Kaynak Deposu →](https://f-droid.org/packages/com.unciv.app/)
- [itch.io Masaüstü Sürümleri →](https://yairm210.itch.io/unciv)

## Teknik mimari ve çalışma prensibi

Unciv, Java ekosisteminin güçlü 2D oyun geliştirme çatısı olan LibGDX ve modern Kotlin diliyle inşa edilmiştir. Projenin temel felsefesi, grafiksel karmaşayı soyutlayarak oyun mantığını deterministik ve hafif bir veri yapısı üzerine oturtmaktır:
- Durum odaklı oyun motoru: Oyun tahtasındaki her altıgen karo, birim, şehir ve diplomatik ilişki saf JSON nesneleri olarak saklanır. Bu yapı kayıt dosyası boyutlarını yalnızca birkaç yüz kilobaytta tutar.
- Deklaratif modlama motoru: Medeniyet özellikleri, teknoloji ağaçları ve bina maliyetleri kaynak koda dokunmadan JSON dosyaları üzerinden tanımlanır. Bu sayede mod geliştiricileri harici derleyiciye ihtiyaç duymaz.
- Deterministik tur hesaplaması: Yapay zekâ hamleleri ve savaş sonuçları öngörülebilir algoritmalarla hesaplanır. Bu durum asenkron çok oyunculu oyunlarda senkronizasyon kopmalarını engeller.
- Çok platformlu derleme: LibGDX sayesinde tek bir Kotlin kod tabanı masaüstü (JVM) ve mobil (Android runtime) için yerel performansla paketlenir.

## Oynanış stratejileri ve 4X dinamikleri

Unciv, klasik 4X türünün temel taşlarını kusursuz bir ritimle sunar: eXplore (Keşfet), eXpand (Genişle), eXploit (Sömür) ve eXterminate (Yok et). Başarılı bir sefer yönetmek için şu ilkelere dikkat edilmelidir:
- İlk turlarda harita keşfi: Savaşçı ve gözcü birimlerinizi erkenden haritaya dağıtarak antik kalıntıları toplayın, şehir devletleriyle ilk teması kurarak altın geliri elde edin.
- Mutluluk ve gıda dengesi: Yeni şehirler kurarken lüks kaynakların menzilinde olmaya özen gösterin. Mutluluk oranınız negatife düştüğünde nüfus büyümesi ve üretim ciddi oranda yavaşlar.
- Teknoloji yol haritası: Rastgele araştırma yapmak yerine medeniyetinizin güçlü yönlerine odaklanın; askeri zafer için demircilik ve barut, kültürel zafer için felsefe ve eğitim yollarını takip edin.
- Arazi avantajlarını kullanma: Nehir arkası savunma, tepe avantajı ve dar geçitler oluşturarak az sayıda birimle büyük orduları püskürtün.

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Unciv oyunu için geçerli bir JSON mod yapısı hazırlamak istiyorum. Lider yeteneği olarak bilim ve kültür üretimine bonus veren, özel bir süvari birimi ve özel bir kütüphane binası içeren örnek bir Unciv mod şablonu oluşturur musun? Hangi JSON dosyalarını hangi klasör yapısında kaydetmem gerektiğini ve oyun içi Mod Manager arayüzünden bunu nasıl test edebileceğimi adım adım açıklar mısın?

- **Kimin için:** Klasik 4X strateji oyunlarını hafif, reklamsız ve açık kaynaklı bir altyapıda deneyimlemek isteyen oyuncular ve bağımsız mod geliştiricileri içindir. 
- **Lisans:** MPL-2.0 (Mozilla Public License 2.0) 
- **Oyun Motoru:** LibGDX (Kotlin tabanlı çapraz platform) 
- **Platformlar:** Android, Windows, Linux, macOS 

## Sıkça sorulan sorular
- Unciv Civilization V ile ne kadar benzer? Oyun mekanikleri, birim istatistikleri, teknoloji ağacı ve zafer koşulları büyük oranda Civilization V Gods and Kings ve Brave New World eklentileriyle birebir uyumludur. Fark temel olarak 3D grafikler yerine sade 2D görsel tasarım kullanılmasıdır.
- Oynamak için internet bağlantısı gerekir mi? Hayır. Unciv tamamen çevrim dışı oynanabilir. Tek oyunculu modda yapay zekâ rakiplere karşı oynamak için hiçbir ağ bağlantısına ihtiyaç duyulmaz. Yalnızca mod indirme ve çok oyunculu maçlar için bağlantı gerekir.
- Unciv modları nasıl yüklenir? Ana menüdeki Modlar sekmesine giderek topluluk tarafından yüklenen yüzlerce modu listeleyebilir, tek tıkla cihazınıza indirebilirsiniz. Ayrıca GitHub üzerindeki herhangi bir mod deposunun bağlantısını ekleyerek doğrudan yükleme yapabilirsiniz.
- Masaüstü ve telefon arasında kayıt dosyası aktarılabilir mi? Evet. Oyun içi kayıt menüsünden kayıt dosyasını panoya kopyalayabilir, metin formatında e-posta veya mesaj yoluyla diğer cihazınıza gönderip oradaki panodan yükle seçeneğiyle kaldığınız yerden devam edebilirsiniz.

## Bağlantılar
- [GitHub deposu →](https://github.com/yairm210/Unciv)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-06-18 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Open Source Offline

---
Kaynak: TreScout Keşif · https://trescout.com/discover/unciv/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
