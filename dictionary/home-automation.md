# Home Automation nedir, ne demek?

**Kategori:** Yapay Zekâ  
**Son güncelleme:** 2026-09-19

Home Automation (akıllı ev otomasyonu), konut içerisindeki aydınlatma, iklimlendirme, güvenlik ve enerji sistemlerinin sensörler, ağ protokolleri ve yazılımsal kurallarla insan müdahalesine gerek kalmadan otomatik yönetilmesidir.

## 1. Etimolojik köken ve temel tanım: Home automation ne demek?

Home Automation terimi, İngilizce "home" (ev, yuva) sözcüğü ile Grekçe "kendi kendine hareket eden, kendi iradesiyle çalışan" anlamına gelen **"automatos"** (*autos* [kendi] + *matos* [isteyen/düşünen]) kelimesinin birleşiminden doğmuştur. Fransızca ve Latin dillerinde ise "ev" anlamına gelen *domus* ile *robotique* kelimelerinin sentezi olan **"domotique"** (domotik) kavramıyla karşılanır.

Günümüz Türkçesinde home automation; **akıllı ev otomasyonu**, **bina yönetim sistemleri** veya **konut otomasyonu** olarak adlandırılır.

Kavramın merkezinde, evdeki donanımların birbirinden kopuk aletler olmaktan çıkıp birbiriyle konuşan ve ortam koşullarına göre otonom kararlar alan tek bir yaşayan organizmaya dönüşmesi yatar.

## 2. Gündelik yaşamda akıllı ev: Uzaktan kumanda yanılgısı

Tüketici elektroniğinde en sık düşülen yanılgı, telefon uygulamasıyla bir lambayı açıp kapamayı "otomasyon" sanmaktır:

- **Uzaktan Kumanda vs Gerçek Otomasyon:** Akıllı telefon ekranındaki bir butona basarak ışığı açmak yalnızca pahalı bir uzaktan kumandadır. Gerçek otomasyon; siz odaya girdiğinizde hareket sensörünün tetiklenmesi, saatin gün batımından sonra olduğunu kontrol etmesi, ortam ışığı yetersizse lambayı %40 parlaklıkta yakması ve hareket kesildikten 3 dakika sonra kendi kendine kapatmasıdır.
- **Senaryolar ve Rutinler:** "Evden Ayrılış" senaryosu devreye girdiğinde açık kalan tüm prizlerin elektriğini kesen, robot süpürgeyi başlatan, güvenlik kameralarını aktif edip kombiyi tasarruf moduna alan zincirleme kurallar bütünüdür.
- **Tüketici Platformları:** Apple Home (HomeKit), Google Home, Amazon Alexa ve Tuya gibi ekosistemler, son kullanıcıya görsel arayüzlerle bu otomasyonları tasarlama imkânı sunar.

## 3. Bilgisayar mühendisliği, IoT protokolleri ve sistem mimarisi

Ev otomasyonu, arka planda dağıtık sistemler, gömülü yazılımlar ve özel ağ protokolleri üzerinde yükselir:

- **Örgü Ağ Protokolleri (Zigbee & Z-Wave):** Evdeki onlarca sensörün Wi-Fi ağını ve yönlendiriciyi tıkamaması için düşük güçlü, düşük frekanslı özel radyo dalgaları kullanılır. Şebekeye bağlı her priz veya anahtar, aynı zamanda bir tekrarlayıcı (mesh router) görevi görerek ağın menzilini evin en uzak köşesine kadar genişletir.
- **Matter ve Thread Devrimi (IPv6 / 6LoWPAN):** Apple, Google, Amazon ve yüzlerce üreticinin bir araya gelerek geliştirdiği Matter, tescilli duvarları yıkan açık standarttır. Alt katmanda çalışan Thread protokolü ise her akıllı cihaza yerel bir IPv6 adresi atayarak buluta ihtiyaç duymadan cihazların doğrudan birbiriyle haberleşmesini sağlar.
- **Hafif Mesajlaşma (MQTT Protokolü):** IoT aygıtları arasında durum ve telemetri verilerini taşımak için Publish/Subscribe (Yayınla/Abone Ol) modeline dayanan MQTT broker'ları kullanılır. Kilobaytlarca hafif JSON paketleriyle milisaniyeler içinde durum güncellenir.
- **Yerel Öncelikli Mimari (Local-First Architecture):** Açık kaynaklı **Home Assistant** gibi yerel işletim sistemleri, tüm veriyi evdeki mikro bilgisayarda (Raspberry Pi vb.) saklar. Şirketlerin sunucuları kapansa veya internet bağlantısı kopsa dahi yerel otomasyonlar kusursuz biçimde çalışmayı sürdürür.

## 4. Güvenlik, mahremiyet ve sosyolojik boyut

Ev, insanın en mahrem sığınağıdır; bu sığınağın internete bağlanması kritik etik ve teknik sorumluluklar doğurur:

- **Saldırı Yüzeyi ve Botnet Tehdidi:** Güvenliği zayıf, varsayılan şifreleri değiştirilmemiş IP kameralar ve akıllı prizler, Mirai botnet vakasında görüldüğü gibi tüm dünyayı hedef alan siber saldırı ordularına dönüştürülebilir. Bu nedenle akıllı cihazların ana ev ağından izole edilmiş ayrı bir sanal yerel ağda (IoT VLAN) tutulması güvenlik standartıdır.
- **Ev İçi Mahremiyet Paradoksu:** Salonunuzda sürekli dinlemede kalan akıllı hoparlörler ve yatak odasını tarayan akıllı süpürgelerin buluta ses ve harita verisi göndermesi, mahremiyet endişelerine yol açar. Bu yüzden teknoloji meraklıları tamamen yerel ses modellerine (Local Voice Assistants) yönelmektedir.
- **Enerji Optimizasyonu (Yeşil IoT):** Dinamik elektrik tarifelerini takip eden akıllı prizler; çamaşır ve bulaşık makinelerini elektriğin en ucuz olduğu saatlerde çalıştırarak, güneş panellerinden gelen fazla enerjiyi ev bataryalarına depolayarak enerji tüketimini ve karbon ayak izini minimize eder.

## Bir benzetmeyle

Evinizin görünmez, evin tüm alışkanlıklarını ezbere bilen dikkatli bir dijital kâhyaya sahip olması gibidir. Dışarıda fırtına çıktığında pencereleri ve panjurları kapatır, siz uyurken evin sıcaklığını rüya evresine göre ayarlar ve tehlike anında ana vanaları saniyeler içinde kilitler.

## Sık karıştırılanlar

- **Uzaktan Kumanda vs Otomasyon:** Telefondaki bir tuşa basarak aydınlatmayı açmak otomasyon değildir; sistemin çevresel sensör verilerini yorumlayıp kararı kendi kendine alması otomasyondur.
- **Bulut Bağımlı vs Yerel Kontrol:** Bulut tabanlı cihazlar internet kesildiğinde işlevsiz kalabilir ve üretici şirket kapandığında çöp olabilir; yerel kontrollü (Matter/Zigbee/Home Assistant) sistemler internetten bağımsız sonsuza kadar çalışır.

## Sıkça sorulanlar

**Home automation ne demek ve Türkçe karşılığı nedir?**  
Home Automation Türkçede "akıllı ev otomasyonu" veya "konut otomasyonu" olarak adlandırılır. Aydınlatma, iklimlendirme, priz ve güvenlik cihazlarının sensör kurallarıyla otonom çalışmasını niteler.

**Akıllı ev ile ev otomasyonu arasındaki fark nedir?**  
Akıllı ev genellikle internete bağlı cihazların genel adıyken, ev otomasyonu bu cihazların insan müdahalesine ihtiyaç duymadan önceden belirlenmiş mantıksal senaryolarla (Trigger-Action) kendi kendine hareket etmesidir.

**Home Assistant neden bu kadar popülerdir ve local-first neden önemlidir?**  
Home Assistant açık kaynaklıdır ve tüm verileri buluta göndermeden yerel ağda işler. Bu sayede hem kişisel mahremiyet korunur hem de internet kesintilerinde ev sistemi aksamadan çalışmaya devam eder.

**Matter ve Thread protokolleri ev otomasyonunda neleri değiştirdi?**  
Matter, farklı markaların (Apple, Google, Amazon vb.) cihazlarının tek bir standartta konuşmasını sağladı. Thread ise cihazlara düşük güçle doğrudan yerel IPv6 ağı kurarak bulut köprülerine olan bağımlılığı bitirdi.

## İlgili terimler

- [Digital Privacy](/dictionary/digital-privacy/)
- [Physical AI](/dictionary/physical-ai/)
- [AI Agent](/dictionary/ai-agent/)
- [End-to-End Privacy](/dictionary/end-to-end-privacy/)
- [Self-Hosted](/dictionary/self-hosted/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/home-automation/  
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
