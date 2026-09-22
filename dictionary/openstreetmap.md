# OpenStreetMap nedir, ne demek?

**Kategori:** Veri & Altyapı  
**Son güncelleme:** 2026-09-22

OpenStreetMap (kısaca **OSM**), gönüllülerin birlikte çizdiği özgür ve açık dünya haritasıdır.

## Tanım ve Kelime Kökeni
Proje 2004 yılında başlatıldı. Ticari haritaların aksine veriyi bir şirket değil, **gönüllü topluluğu** üretir: Herkes yeni yol, bina veya önemli nokta ekleyebilir, hataları düzeltebilir. Veriler **ODbL** lisansıyla herkese açıktır. Bu, veriyi ücretsiz kullanabileceğiniz, ancak paylaşırken kaynağı belirtmeniz gerektiği anlamına gelir.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Navigasyon uygulamaları:** OsmAnd ve MAPS.ME gibi uygulamalar haritasını OSM verisinden alır.
- **Lojistik:** Dağıtım firmalarının rota planlaması.
- **Afet yardımı:** Gönüllülerin kriz bölgelerini hızla haritalaması (ör. HOT topluluğu).
- **Şehir planlama:** Bisiklet yolu ve yeşil alan analizleri.

## Teknik Derinlik ve Mimari
OSM verisi üç yapı taşından oluşur:
- **Düğüm (Node):** Tek bir nokta (ör. eczane konumu).
- **Yol (Way):** Düğümlerin birleşimi (cadde, bina çevresi).
- **İlişki (Relation):** Parçaların mantıksal grubu (otobüs hattı).

Her ögeye **etiket** yapışır: `highway=residential` gibi anahtar ve değer çiftleri. Düzenleme için tarayıcıdaki iD editörü veya gelişmiş JOSM uygulaması kullanılır.

Belirli veriyi çekmek için Overpass API sorgulanır. Örneğin çevredeki eczaneleri bulan küçük bir sorgu:

```
[out:json];
node["amenity"="pharmacy"](around:1000,41.0,29.0);
out;
```

Ham veri Planet.osm dosyasından indirilebilir. Harita görselleri ise karo (tile) sunucularından parça parça alınır.

## Farklı Disiplinlerde Kullanımı
- **Ansiklopedi:** Herkesin yazdığı ve düzelttiği Wikipedia modeli.
- **Açık kaynak yazılım:** Gönüllü katkıyla büyüyen Linux çekirdeği.
- **Vatandaş bilimi:** Kuş gözlem kayıtlarının ortak veritabanında toplanması.

## Bir benzetmeyle
Haritaların Wikipedia'sı gibidir; herkes bir şeyler ekleyebilir, hataları düzeltebilir ve topluluk sayesinde sürekli güncel kalır.

## Sıkça sorulanlar

**Gerçekten ücretsiz midir?**  
Veri ODbL lisansıyla ücretsizdir. Kendi sunucunuzda barındırırsanız ek ücret ödemezsiniz. Hazır karo hizmeti sunan firmalar ayrıca ücret isteyebilir.

**Google Haritalar ile farkı nedir?**  
Google veriyi şirket üretir ve API kotalarına bağlar. OSM verisini topluluk üretir, ham veriyi indirip sınırsız işleyebilirsiniz.

**Haritaya nasıl katkı yaparım?**  
Hesap açıp tarayıcıdaki iD editörüyle başlayabilirsiniz. Sokağınızdaki eksik dükkânı eklemek iyi bir ilk adımdır.

**Ticari ürünümde kullanabilir miyim?**  
Evet, ancak ODbL gereği OpenStreetMap atfını görünür şekilde vermeniz ve türetilmiş veriyi aynı lisansla paylaşmanız gerekir.

## İlgili terimler
- [Data Pipeline](/dictionary/data-pipeline/)
- [OSINT](/dictionary/osint/)
- [Graph-based Investigation](/dictionary/graph-based-investigation/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/openstreetmap/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
