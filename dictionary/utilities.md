# Utilities ne demek?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

Utilities (yardımcı araçlar veya yardımcı fonksiyonlar), işletim sistemlerinde bakım ve yönetimi üstlenen, yazılım projelerinde ise sık tekrarlanan rutin görevleri yerine getiren bağımsız, pratik ve tek amaçlı modül paketleridir.

## Kavramsal köken ve günlük hayatta "Utility"
İngilizce "utility" sözcüğü, Latince "yararlı, elverişli olmak" anlamına gelen *utilis* kökünden ve *utilitas* (fayda, amaca uygunluk) kavramından türemiştir. Günlük İngilizcede ve iş dünyasında bu kelime birkaç farklı bağlamda karşımıza çıkar:
- **Kamu Hizmetleri (Public Utilities):** Elektrik, su, doğal gaz ve kanalizasyon gibi bir kentin altyapısını ayakta tutan temel şebeke hizmetleri.
- **Spor ve Yönetim (Utility Player):** Tek bir mevkide uzmanlaşmak yerine sahanın her yerinde görev alabilen, çok yönlü yedek sporcu veya çalışan.
- **Felsefi Faydacılık (Utilitarianism):** Jeremy Bentham ve John Stuart Mill tarafından temellenen, bir eylemin ahlaki değerini sağladığı pratik fayda ve toplam refahla ölçen felsefi yaklaşım.

Bilişim dünyasındaki "utility" kavramı da bu faydacı mirasın doğrudan bir uzantısıdır: Gösterişli veya karmaşık bir ürün sunmak yerine, tek bir amaca odaklanan ve kullanıcının veya geliştiricinin yükünü hafifleten pratik araçtır.

## İşletim sistemleri seviyesinde: Unix felsefesi ve GNU Coreutils
Bilgisayar biliminde modern utility kavramının temeli Bell Laboratuvarları'nda atılan Unix felsefesine dayanır. Doug McIlroy'un formüle ettiği temel kural şudur: *"Her program tek bir işi yapsın ve onu mükemmel yapsın. Programlar birlikte çalışabilecek şekilde tasarlansın."*

Bu yaklaşım, tek parça (monolitik) dev programlar yerine boru hatları (pipes - `|`) ile birbirine bağlanan küçük utility araçlarını doğurmuştur:
- **GNU Coreutils:** `ls`, `cat`, `grep`, `awk`, `sed`, `sort`, `find`, `chmod` gibi araçlar dosya ve metin manipülasyonunun omurgasını oluşturur.
- **Gömülü Sistemler (BusyBox):** Kaynak kısıtlı yönlendirici ve IoT cihazlarında onlarca standart utility aracını tek bir çalıştırılabilir dosya altında birleştirir.
- **Sistem Tanılama ve İzleme:** `top`, `htop`, `ps`, `netstat`, `curl`, `tcpdump` ve Windows dünyasındaki Mark Russinovich imzalı *Sysinternals* (Process Explorer, Autoruns) paketleri işletim sisteminin röntgenini çeker.

## Yazılım mimarisinde `utils` klasörü ve "Çöp Çekmecesi" anti-pattern'i
Yazılım geliştiriciler projelerinde tarih formatlama, dize (string) temizleme, para birimi yuvarlama veya kriptografik özet (hash) çıkarma gibi görevleri genellikle `utils/`, `helpers/` veya `common/` dizinlerinde toplar.

Bir utility fonksiyonunun ideal özellikleri şunlardır:
1. **Saf Fonksiyon (Pure Function):** Dış dünyaya (veritabanı, ağ, global değişkenler) yan etkisi (side-effect) bulunmaz. Aynı girdiye her zaman aynı çıktıyı üretir.
2. **Durumsuzluk (Statelessness):** Kendi içinde dahili durum saklamaz.
3. **Yüksek Yeniden Kullanılabilirlik (High Reusability):** Projenin herhangi bir katmanından bağımsızca çağrılabilir.

### Tehlike: Çöp Çekmecesi (Junk Drawer) anti-pattern'i
Projeler büyüdükçe `utils/` klasörü genellikle geliştiricilerin nereye koyacağını bilemediği kodların boca edildiği bir "çöp çekmecesine" dönüşür. `utils.ts` veya `helpers.py` dosyasının binlerce satıra ulaşması; döngüsel bağımlılıklara (circular dependencies), zayıf test kapsamına ve belirsiz alan sınırlarına (domain boundaries) yol açar.

Modern yazılım mimarisinde bu sorunu aşmak için:
- **Alana Dayalı Tasarım (DDD):** Fonksiyonlar genel bir torbaya değil, ait oldukları iş alanının (örneğin `billing/`, `auth/`) içine yerleştirilir.
- **Spesifik Ad Alanları:** `utils` yerine `string-utils`, `date-utils`, `crypto` gibi net odaklı modüller oluşturulur.
- **Dil Standartlarının Benimsenmesi:** Geçmişte Lodash veya Underscore gibi kütüphanelerin doldurduğu boşluklar günümüzde modern ECMAScript (`Array.prototype.map`, `flatMap`, `Optional Chaining`, `Nullish Coalescing`) ve Python standart kütüphanesi (`itertools`, `functools`) tarafından doğrudan karşılanmaktadır.

## Bir benzetmeyle
Bir mutfak düşünün: Fırın ve ocak uygulamanın ana mimarisidir (framework). Mutfak çekmecesindeki tirbüşon, sarımsak ezici veya soyacak ise utility araçlarıdır. Tek başlarına bir ziyafet hazırlayamazlar; ancak onlar olmadan aşçının işi katbekat zorlaşır ve zaman kaybedilir.

## Yapay zeka ve oyun geliştirmede: Utility AI
Oyun geliştirme ve yapay zeka alanında "Utility AI", karar verme mekanizmalarında kullanılan matematiksel bir modeldir. Klasik sonlu durum makineleri (FSM) veya davranış ağaçları (Behavior Trees) yerine; her olası eyleme mevcut durum parametrelerine göre bir fayda puanı (utility score) atanır ve karakter en yüksek faydayı sağlayan eylemi seçer (örneğin canı %20'nin altındaysa "kaçma" eyleminin fayda puanı fırlar).

## Sıkça sorulanlar

**Utilities ne demek ve Türkçesi nedir?**  
Utilities, İngilizcede "yararlı araçlar" anlamına gelir. Bilişimde Türkçeye "yardımcı programlar", "yardımcı araçlar" veya kod seviyesinde "yardımcı fonksiyonlar" olarak çevrilir.

**Yazılım projelerinde `utils` klasörü neden zamanla teknik borca dönüşür?**  
Geliştiriciler belirli bir modüle ait olmayan her kodu `utils` içine attığında, bu klasör binlerce satırlık denetimsiz bir çöp çekmecesine dönüşür; döngüsel bağımlılık ve yüksek kod karmaşıklığı yaratır.

**Unix felsefesi ile utility araçları arasındaki ilişki nedir?**  
Unix felsefesi, her utility aracının yalnızca tek bir işi mükemmel yapmasını ve girdi/çıktı boru hatları (pipes) aracılığıyla diğer araçlarla zincirlenerek devasa problemleri çözmesini öğütler.

**Lodash gibi utility kütüphaneleri hala gerekli midir?**  
Modern JavaScript sürümleri (ES6+) birçok temel dizi ve nesne manipülasyonunu yerleşik olarak sunduğu için eski popülaritesini yitirmiştir; ancak derin klonlama ve gelişmiş fonksiyonel işlemler için hala kullanılmaktadır.

## İlgili terimler
- [CLI](/dictionary/cli/)
- [API](/dictionary/api/)
- [Framework](/dictionary/framework/)
- [Runtime](/dictionary/runtime/)
- [Production Pipeline](/dictionary/production-pipeline/)
- [Bundler](/dictionary/bundler/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/utilities/  
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
