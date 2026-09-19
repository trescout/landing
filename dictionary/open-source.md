# Open Source nedir, ne demek?

> Açık Kaynak

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

Open Source (açık kaynak), bir yazılımın kaynak kodlarının telif hakkı sahibi tarafından herkesin incelemesine, değiştirmesine, geliştirmesine ve yasal lisanslar altında özgürce yeniden dağıtmasına izin verildiği merkeziyetsiz iş birliği modelidir.

## Etimoloji ve Felsefi Köken
Açık kaynak felsefesi, 1980'li yıllarda Richard Stallman tarafından başlatılan Özgür Yazılım Hareketi (Free Software) ve GNU Projesi'ne dayanır. Stallman'ın "Free as in speech, not as in beer" (bedava bira gibi değil, ifade özgürlüğü gibi özgür) ilkesi, kullanıcıların yazılımı çalıştırma, inceleme, değiştirme ve kopyalarını dağıtma hakkını savundu. 1998 yılında ise Eric S. Raymond ve Bruce Perens öncülüğünde Open Source Initiative (OSI) kurularak, bu felsefe kurumsal iş dünyasının benimseyebileceği pragmatik bir mühendislik standardına dönüştürüldü. Raymond'ın "Katedral ve Çarşı" (The Cathedral and the Bazaar) eserinde anlattığı gibi, yazılım geliştirme kapalı kapılar ardındaki loncalardan çıkıp küresel bir açık çarşıya evrildi.

## Bir Benzetmeyle: Açık Tarif Ansiklopedisi
Şöyle düşünün: Bir restoranın ünlü tatlısının tarifini kasada saklayıp gizlediğini hayal edin; kapalı kaynak yazılım tam olarak budur. Müşteriler içindeki katkı maddelerini bilemez, tarifi geliştiremez. Açık kaynak ise bir şefin tarifini, tüm ölçülerini ve pişirme tekniklerini açık bir gastronomi ansiklopedisinde yayınlaması gibidir. Dünyanın her yerindeki aşçılar bu tarifi inceler, yerel baharatlar katar, eksikleri tamamlar ve yeni lezzetler türetir. Tarif kamuya aittir; dileyen evinde yapar, dileyen lokantasında geliştirilmiş haliyle servis eder.

## Açık Kaynak Lisans Mimarisi ve Ekosistem
Açık kaynak ekosisteminin işleyişi hukuki lisanslar, dağıtık sürüm kontrolü ve topluluk dinamikleriyle şekillenir:

1. **Açık Kaynak Lisans Türleri:** Her açık kaynak proje telif hakkı hukukuyla korunur ve lisanslar iki ana sınıfa ayrılır:
- **İzin Verici (Permissive) Lisanslar:** MIT, Apache 2.0 ve BSD lisansları geliştiricilere azami esneklik tanır. Kod alınıp kaynak kodu açma zorunluluğu olmadan kapalı kaynaklı ticari ürünlere dahil edilebilir. Apache 2.0 ayrıca açık patent hibesi sağlar.
- **Telifli (Copyleft) Lisanslar:** GPL (General Public License) ailesi ve AGPL, yazılımın özgür kalmasını güvence altına alır. Bu kod kullanılarak geliştirilen türev ürünlerin de aynı lisansla kamuya açılması zorunludur. AGPLv3, bulut sunucuları üzerinden servis sunan şirketlerin de kodu paylaşmasını şart koşar.

2. **Modern Teknolojinin Omurgası:** Bugün internetin ve küresel altyapının yüzde 90'ından fazlası açık kaynak bileşenlerle ayakta durur. Akıllı telefonlarda çalışan Android ve sunucuları yöneten Linux çekirdeği, Git sürüm kontrol mekanizması, Kubernetes konteyner orkestrasyonu, PostgreSQL veritabanları ve Chromium web motoru açık kaynak topluluklarının ortak mirasıdır. Yapay zekâ devriminde ise PyTorch, Hugging Face ekosistemi ve Llama tabanlı modeller inovasyonu açık kaynak üzerinden hızlandırmaktadır.

3. **Güvenlik, Linus Yasası ve Tedarik Zinciri:** "Yeterince göz olursa tüm hatalar yüzeyseldir" (Linus Yasası) prensibi uyarınca, açık kaynak kodları binlerce bağımsız araştırmacı tarafından denetlenebilir. Bu şeffaflık arka kapıların gizlenmesini engeller. Ancak Heartbleed veya XZ Utils vakalarında görüldüğü gibi, küresel altyapıları sırtlayan gönüllü geliştiricilerin yalnız bırakılması tedarik zinciri riskleri doğurabilir; bu nedenle modern kurumsal yapılar SBOM (Software Bill of Materials) süreçleriyle bağımlılıkları sıkı denetime tabi tutar.

## Sosyolojik Boyut: Dijital Müşterekler ve Bilginin Paylaşımı
Açık kaynak, bilişim tarihinin en başarılı küresel imece ve dijital müşterekler (digital commons) hareketidir. Milyarlarca dolarlık bütçelere sahip dev teknoloji tekelleri dahi artık tüm araştırma-geliştirme süreçlerini tek başlarına yürütememekte; açık kaynak konsorsiyumlarına fon sağlamaktadır.

Bunun ötesinde açık kaynak, yazılım bilgisini demokratikleştirir. Gelişmekte olan ülkelerdeki genç bir mühendis ile Silikon Vadisi'ndeki bir kıdemli mimar aynı kod tabanını okuyabilir, aynı araçlarla yetkinlik kazanabilir. Açık kaynak, bilginin özel mülkiyet altına alınarak tekelleştirilmesine karşı insanlığın ortak zihinsel sermayesini savunan evrensel bir kültürdür.

## Sık Yapılan Hatalar ve Yanılgılar
Açık kaynakla ilgili sektörde en sık yapılan yanılgılar şunlardır:
- **Ücretsiz Yazılımla (Freeware) Karıştırmak:** Açık kaynak kodun özgürlüğünü ifade eder; geliştiriciler yazılımları satabilir, barındırma veya danışmanlık hizmetlerinden (Red Hat örneğinde olduğu gibi) milyarlarca dolar gelir elde edebilir.
- **Güvensiz Olduğunu Düşünmek:** Kodu gizleyerek güvenlik sağlama yanılgısı (security through obscurity) siber güvenlikte geçersizdir; kodu açık olan yazılımlar bağımsız denetimlerden geçtiği için çok daha sağlamdır.
- **Open Weights ile Karıştırmak:** Yapay zekâda sadece model ağırlıklarının paylaşılması tam açık kaynak değildir; eğitim verisi, kodları ve mimarisi paylaşılmayan sistemler açık kaynak tanımını tam karşılamaz.

## Sıkça Sorulanlar

**Açık kaynak (Open Source) ile özgür yazılım (Free Software) arasındaki temel fark nedir?**  
Özgür yazılım hareketi etik, felsefi ve kullanıcı haklarını temel alarak kodun sonsuza dek özgür kalmasını (copyleft) savunurken; açık kaynak hareketi daha pragmatik, metodolojik ve kurumsal iş dünyasının adaptasyonuna odaklanan bir yaklaşımı benimser.

**Açık kaynak kodlu bir yazılımı ticari projelerimde kullanıp satabilir miyim?**  
Evet, ancak bu durum kullanılan lisansa bağlıdır; MIT veya Apache gibi izin verici lisanslar kapalı kaynak ticari satışa izin verirken, GPL gibi katı copyleft lisanslar projenizin kaynak kodunu da aynı şekilde açmanızı zorunlu kılar.

**Açık kaynak yazılımlar kapalı kaynak yazılımlara göre daha mı güvenlidir?**  
Açık kaynakta kod kamuya açık olduğu için güvenlik açıkları küresel topluluk ve bağımsız güvenlik araştırmacıları tarafından çok daha hızlı tespit edilip yamalanır; gizliliğe dayalı güvenlik zaaflarından arındırılmıştır.

**Açık kaynak projeleri geliştiren şirketler ve topluluklar nasıl gelir elde eder?**  
Şirketler açık kaynak yazılımlar etrafında kurumsal teknik destek, SLA garantisi, yönetilen bulut barındırma (SaaS), kurumsal ek eklentiler (open-core) ve danışmanlık hizmetleri sunarak sürdürülebilir iş modelleri kurarlar.

## İlgili terimler
- [Self-hosted](/dictionary/self-hosted/)
- [Open Weights](/dictionary/open-weights/)
- [Offline](/dictionary/offline/)
- [Local](/dictionary/local/)
- [Artificial Intelligence](/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/open-source/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
