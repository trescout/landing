# Digital Privacy nedir, ne demek?

**Kategori:** Veri & Altyapı  
**Son güncelleme:** 2026-09-19

Digital Privacy (dijital gizlilik veya sayısal mahremiyet), bireylerin internette, akıllı cihazlarda ve dijital servislerde ürettiği kişisel verilerin kimler tarafından toplanabileceğini, saklanabileceğini ve işlenebileceğini denetleme ve sınırlama hakkıdır.

## 1. Etimolojik köken ve temel tanım: Digital privacy ne demek?

Gizlilik (privacy) kavramı, Latince "kamuya ait olmayan, topluluktan ayrılmış, kişiye özgü ve tecrit edilmiş" anlamına gelen **"privatus"** sözcüğünden türemiştir. Modern hukuk literatüründe ilk kez 1890 yılında Amerikalı hukukçular Samuel Warren ve Louis Brandeis tarafından kaleme alınan tarihi makalede **"The Right to be Let Alone"** (Yalnız Bırakılma / Rahatsız Edilmeme Hakkı) olarak formüle edilmiştir.

Günümüz Türkçesinde digital privacy; **dijital gizlilik**, **sayısal mahremiyet** veya **kişisel veri mahremiyeti** olarak adlandırılır.

Kavramın merkezinde "bireysel veri egemenliği" yatar. Web tarama geçmişinizden konum verilerinize, mesajlaşma içeriklerinizden parmak izi kayıtlarınıza kadar oluşturduğunuz her dijital ayak izi üzerinde karar verme yetkisinin size ait olması anlamına gelir.

## 2. Gündelik yaşamda ve AdTech ekosisteminde gözetim gerçekliği

Günümüz internet ekonomisinde "ücretsiz bir ürün kullanıyorsanız, asıl ürün sizsiniz" kuralı işler. Gündelik hayatta dijital gizliliği tehdit eden temel mekanizmalar şunlardır:

- **Davranışsal Reklamcılık ve İzleyiciler (Ad Trackers):** Web sitelerine yerleştirilen üçüncü taraf çerezler (cookies) ve pikseller, farklı sitelerdeki tüm gezinme alışkanlıklarınızı tek bir dijital profil altında birleştirir.
- **Tarayıcı Parmak İzi Alma (Browser Fingerprinting):** Çerezleri temizleseniz dahi ekran çözünürlüğünüz, yüklü sistem fontları, GPU sürücünüz ve tarayıcı eklentileriniz birleşerek cihazınıza %99 benzersiz bir dijital kimlik damgalar (Canvas & AudioContext fingerprinting).
- **Dinamik Fiyatlandırma ve Mikro-Hedefleme:** Bir uçak bileti ararken konumunuza, cihazınızın markasına ve geçmiş aramalarınıza göre fiyatın otomatik artırılması veya seçim dönemlerinde siyasi manipülasyon amaçlı duygu durumu hedeflemeleri yapılması doğrudan gizlilik ihlallerinin sonucudur.

## 3. Bilgisayar mühendisliği ve kriptografik gizlilik mimarisi

Bilgisayar bilimlerinde gizlilik, soyut bir arzu değil; matematiksel ve algoritmik bir mühendislik disiplinidir:

- **Uçtan Uca Şifreleme (Signal Protocol & Double Ratchet):** Klasik sistemlerde mesajlar sunucuda çözülüp depolanırken, modern E2EE altyapısında anahtarlar yalnızca uç cihazlarda bulunur. Her mesaj gönderiminde şifreleme anahtarı ileriye dönük olarak yenilenir (Forward Secrecy); böylece geçmiş bir anahtar ele geçirilse bile sonraki mesajlar okunamaz.
- **Sıfır Bilgi İspatları (Zero-Knowledge Proofs - ZKP):** Karşı tarafa bilginin içeriğini (örneğin doğum tarihinizi veya maaşınızı) göstermeden, sadece aranan koşulu (örneğin "18 yaşından büyüğüm" veya "krediye uygundur") matematiksel olarak ispatlama yöntemidir (zk-SNARKs).
- **Diferansiyel Gizlilik (Differential Privacy):** Büyük veri setleri analiz edilirken istatistiki sonuçlara kontrollü matematiksel gürültü (Laplace/Gauss) eklenir. Böylece araştırmacılar genel eğilimleri görürken, veri setindeki tek bir bireyin varlığı veya yokluğu asla ifşa edilemez ($\epsilon$-gizlilik bütçesi).
- **Soğan Yönlendirmesi (Onion Routing - Tor):** Veri paketleri çok katmanlı olarak şifrelenir ve rastgele üç düğüm üzerinden iletilir. Hiçbir düğüm hem göndericiyi hem de hedef sunucuyu aynı anda göremez.

## 4. Felsefe, sosyoloji ve siyaset bilimi: Panoptikon ve gözetim kapitalizmi

Dijital gizlilik salt bir teknik konu değil, özgür toplumların varoluşsal zeminidir:

- **Bentham ve Foucault: Panoptikon Etkisi:** 18. yüzyılda Jeremy Bentham tarafından tasarlanan ve Michel Foucault tarafından felsefeye taşınan Panoptikon hapishane modelinde mahkûmlar, her an gözetlenebileceklerini bildikleri için kendi davranışlarını disipline ederler. Dijital gözetim altında yaşayan bir toplumda bireyler, sansürlenmese bile cezalandırılma korkusuyla aykırı fikirleri araştırmaktan ve ifade etmekten vazgeçer (caydırıcı etki / chilling effect).
- **Shoshana Zuboff ve Gözetim Kapitalizmi:** Sosyolog Zuboff, teknoloji devlerinin insan deneyimini ücretsiz hammadde olarak sömürdüğünü, bu davranışsal artıklarla (behavioral surplus) gelecekteki eylemlerimizi tahmin eden ve yönlendiren piyasalar kurduğunu savunur.
- **"Saklayacak Bir Şeyim Yok" Yanılgısı:** Edward Snowden'ın veciz ifadesiyle: *"Saklayacak bir şeyim yok, bu yüzden gizliliği önemsemiyorum demek; söyleyecek bir şeyim yok, bu yüzden ifade özgürlüğünü önemsemiyorum demekle aynıdır."* Gizlilik suçluların değil, hür insanların özerklik alanıdır.

## Bir benzetmeyle

Evinizin perdelerini akşam olunca kapatmak gibidir. Perdeleri kapatmanız içeride yasa dışı bir iş çevirdiğiniz anlamına gelmez; yalnızca evinizdeki mahremiyetin sokaktan geçen herkes tarafından izlenmesini istemezsiniz.

## Siber güvenlik ile dijital gizlilik arasındaki fark

Siber güvenlik, verilerinizin yetkisiz saldırganlar (hacker'lar) tarafından çalınmasını önleyen zırhtır (evin çelik kapısı ve alarm sistemi). Dijital gizlilik ise, evinize yasal olarak giren misafirlerin (kullandığınız uygulamalar ve servis sağlayıcılar) çekmecelerinizi karıştırmamasını ve özel notlarınızı başkalarına satmamasını garanti eden haktır.

## Sıkça sorulanlar

**Digital Privacy ne demek, Türkçe karşılığı nedir?**  
Digital Privacy Türkçede "dijital gizlilik" veya "sayısal mahremiyet" olarak karşılanır. Bireylerin çevrimiçi ortamda ürettiği tüm verilerin kimler tarafından toplanacağını ve işleneceğini belirleme hakkını niteler.

**"Saklayacak hiçbir şeyim yok" argümanı neden hatalıdır?**  
Gizlilik suç örtbas etmekle ilgili değildir; bireysel özerklik, manipülasyondan ve dinamik fiyat ayrımcılığından korunma ve düşünce özgürlüğünü koruma temel insan hakkıdır.

**Siber güvenlik ile dijital gizlilik arasındaki temel fark nedir?**  
Siber güvenlik verinin yetkisiz üçüncü partilerce çalınmasını engeller (dışarıdan sızma koruması); dijital gizlilik ise verinizi teslim ettiğiniz yetkili platformların o veriyi rızanız dışında profillemesini ve satmasını engeller.

**Diferansiyel gizlilik (Differential Privacy) ve ZKP ne işe yarar?**  
Diferansiyel gizlilik, veri analizlerinde bireysel kimlikleri matematiksel gürültüyle gizlerken makro eğilimleri ölçer. Sıfır Bilgi İspatları (ZKP) ise bilginin kendisini paylaşmadan bir iddianın doğruluğunu kriptografik olarak kanıtlar.

## İlgili terimler

- [End-to-End Privacy](/dictionary/end-to-end-privacy/)
- [GDPR](/dictionary/gdpr/)
- [Data Residency](/dictionary/data-residency/)
- [Regulatory Restriction](/dictionary/regulatory-restriction/)
- [Home Automation](/dictionary/home-automation/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/digital-privacy/  
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
