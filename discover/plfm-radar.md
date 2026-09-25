# Açık kaynaklı faz dizili radar sistemi

PLFM RADAR, 10.5 GHz (X-bandı) frekansında çalışan, elektronik huzme yönlendirme (electronic beam steering) ve FPGA tabanlı sayısal sinyal işleme yeteneklerine sahip açık kaynaklı bir faz dizili radar sistemidir. Mekanik hareketli parça kullanmaksızın hava ve yer hedeflerini yüksek hassasiyetle tespit edip izler.

- ★ 24.168
- C++
- GitHub Trending · 2026-08-18

## Güncelleme
- 18 Ağustos 2026: Yıldız 24.168, son kararlı sürüm v2.0.2-p0-audit (FPGA sinyal filtreleme ve menzil kalibrasyonu güncellemesi).

## Ne kazandırır?
- Elektronik huzme yönlendirme: Mekanik motor veya döner antene ihtiyaç duymadan milisaniyeler içinde faz kaydırıcılarla 90 derecelik sektörü tarama.
- Çift menzil çalışma modu: Kısa menzilde 3 km (İHA/Drone tespiti), uzun menzilde 20 km (çevre gözetleme ve uçak takibi) operasyon kabiliyeti.
- FPGA tabanlı gerçek zamanlı sinyal işleme: Ham radar yankılarını yüksek hızlı FFT ve CFAR algoritmalarıyla FPGA üzerinde donanımsal işleme.
- Düşük maliyetli erişilebilir donanım: Ticari ve askeri radarların yüz binlerce dolarlık maliyetini açık kaynak PCB tasarımlarıyla bin doların altına düşürme.
- Python ve SDR entegrasyonu: Sayısal radar verilerini açık kaynak SDR donanımları ve Python arayüzü üzerinden canlı izleme.

## Donanım bileşenleri ve radar mimarisi

PLFM RADAR sistemi RF ön uç (front-end), anten dizisi ve sayısal işleme katmanlarından meydana gelir:
- 10.5 GHz X-Band mikroşerit anten dizisi: Düşük kayıplı Rogers/FR4 tabakaları üzerine tasarlanmış çoklu yama (patch) anten elemanları.
- Sayısal kontrollü faz kaydırıcılar: Her anten elemanının sinyal fazını 5.6 derecelik hassasiyetle geciktirerek huzmeyi uzayda yönlendiren RF entegreleri.
- FMCW frekans sentezleyici: Doğrusal frekans modülasyonlu sürekli dalga üreten yüksek kararlılıklı yerel osilatör (VCO/PLL).

## Sinyal işleme ve kontrol yazılımı

Radar yankıları donanım düzeyinde işlenerek kullanıcı arayüzüne hedeflerin menzil, hız ve açı verileri aktarılır:
- Menzil-Doppler FFT (2D FFT): Gelen sinyale önce menzil sonra Doppler FFT uygulayarak hedefin mesafesini ve radyal hızını eşzamanlı hesaplama.
- CFAR (Sabit Yanlış Alarm Oranı) detektörü: Arka plan gürültüsü ve yer yankıları (clutter) arasından gerçek hareketli hedefleri dinamik eşikle ayıklama.
- Python GUI ve PPI ekranı: Hedef izlerini (track) geleneksel dairesel radar ekranında (PPI) canlı harita üzerinde görselleştirme.

## Teknik çalışma prensibi: FMCW ve faz dizilimi

PLFM RADAR, geleneksel darbeli (pulse) radarlar yerine frekans modülasyonlu sürekli dalga (FMCW) tekniğini kullanır:
- Frekans farkından mesafe ölçümü: Gönderilen cıvıltı (chirp) sinyali ile hedeften dönen sinyal karıştırılarak vuru frekansı (beat frequency) elde edilir. Bu frekans mesafeyle doğrudan orantılıdır.
- Yapıcı girişimle huzme odaklama: Dizideki her anten elemanına belirli bir faz gecikmesi verilerek sinyalin istenen yönde yapıcı, diğer yönlerde yıkıcı girişim yapması sağlanır.

## Kullanım senaryoları ve saha testleri

Açık kaynak faz dizili radar altyapısı geniş bir uygulama yelpazesine sahiptir:
- Düşük irtifa İHA ve Drone savunması: Optik kameraların yetersiz kaldığı sisli veya gece koşullarında küçük insansız hava araçlarını tespit etme.
- Kritik tesis çevre güvenliği: Havalimanları, veri merkezleri ve endüstriyel sahalarda 3 km çapında yetkisiz insan veya araç yaklaşmasını izleme.
- Meteorolojik ve atmosferik araştırmalar: Bulut hareketleri ve yağış yoğunluğunu yerel ölçekte mikro-Doppler yöntemleriyle analiz etme.

## Kod bilmiyorsanız
🤖 Kod bilmiyorsanız
PLFM RADAR projesinin 10.5 GHz faz dizili donanım şemalarını ve FPGA sinyal işleme bloklarını incelemek istiyorum. FMCW cıvıltı sinyali üretimini, Menzil-Doppler 2D FFT hesaplamasını ve Python tabanlı PPI radar ekranına veri aktarımını açıklayan bir simülasyon Python betiği hazırlar mısın? Yapay bir hedef için mesafe ve hız tespit algoritmasını adım adım gösterir misin?

- **Kimin için:** Radar araştırmacıları, savunma sanayii mühendisleri, drone geliştiricileri ve RF/SDR meraklıları.
- **Lisans:** Açık kaynak donanım ve yazılım lisansı
- **Frekans Bandı:** 10.5 GHz (X-Band) FMCW
- **Hedef Menzili:** 3 km (Drone/Taktik) - 20 km (Geniş alan gözetleme)

## Sıkça sorulan sorular
- Sistemi evde veya laboratuvarda üretmek mümkün mü? Evet. Projenin tüm PCB şemaları, Gerber üretim dosyaları ve FPGA Verilog/VHDL kodları GitHub deposunda açık kaynak olarak sunulmuştur. Standart PCB üreticilerinden kartlar sipariş edilip laboratuvar ortamında lehimlenebilir.
- Elektronik huzme yönlendirmenin mekanik radarlara üstünlüğü nedir? Mekanik radarlar saniyede 1-2 tur dönerken, faz dizili radarlar mikrosaniyeler içinde huzmenin yönünü değiştirebilir. Aşınan mekanik parça bulunmaz ve anlık olarak birden fazla hedefe kilitlenebilir.
- Çalıştırmak için özel bir radyo frekans izni gerekir mi? 10.5 GHz bandı birçok ülkede amatör telsiz veya endüstriyel/bilimsel (ISM) frekans tahsislerine tabidir. Düşük çıkış güçlerinde laboratuvar içi testler serbest olmakla birlikte, açık hava uzun menzil yayınlarında yerel regülasyonlara uyulmalıdır.
- Hangi FPGA geliştirme kartlarıyla uyumludur? Xilinx Zynq-7000 serisi veya modern AMD UltraScale+ RFSoC kartları doğrudan desteklenir; yüksek hızlı ADC/DAC arayüzleri FMC konektörü üzerinden bağlanır.

## Bağlantılar
- [GitHub →](https://github.com/NawfalMotii79/PLFM_RADAR)

## İlgili sözlük terimleri
Edge Computing Open Source Local Offline

---
Source: TreScout Discover · https://trescout.com/discover/plfm-radar/
