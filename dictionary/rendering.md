# Rendering nedir, ne demek?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-22

Rendering (Türkçe karşılığıyla **oluşturma** veya **işleme**), ham veriyi ekranda gördüğünüz görüntüye dönüştürme sürecidir.

## Tanım ve Kelime Kökeni
"Render" İngilizcede **sunmak, çizmek** anlamlarına gelir. Bilgisayarlar veriyi sayılarla tutar. Rendering, bu sayısal verilerin ışık, renk ve şekil özelliklerini hesaplayarak görebileceğiniz görüntüye dönüştürür. Bu süreç yoğun matematiksel hesap gerektirir, bu yüzden genellikle ekran kartı (GPU) üstlenir.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Web sayfaları:** Tarayıcınızın HTML ve CSS kodunu piksel piksel ekrana çizmesi.
- **Oyunlar:** Saniyede 30 veya 60 kez yeni kare üretilmesi.
- **Video düzenleme:** Efektli zaman çizelgesinin izlenebilir videoya dönüştürülmesi (dışa aktarma).
- **Haritalar:** Yakınlaştırdıkça yeni detayların çizilmesi.

## Teknik Derinlik ve Mimari
Görüntü oluşturmanın iki ana yolu vardır:
- **Rasterleştirme (Rasterization):** Üç boyutlu sahne üçgenlere bölünür, her üçgen piksele çevrilir. Hızlıdır, oyunlarda standarttır.
- **Işın izleme (Ray Tracing):** Işık huzmelerinin sahnedeki yolu tersine takip edilir. Yansıma ve gölgeler gerçekçi olur, ancak çok daha pahalıdır.

Web tarafında da iki yaklaşım konuşulur:
- **Sunucuda oluşturma (SSR):** Sayfa sunucuda çizilip hazır HTML gönderilir. İlk açılış hızlı olur.
- **İstemcide oluşturma (CSR):** Boş sayfa gelir, içerik tarayıcıda JavaScript ile çizilir. Sonrası akıcıdır, ilk açılış yavaştır.

Kare hızı (FPS) deneyimi belirler: Değer düştükçe takılma hissedersiniz. Yavaşlığın nedeni genellikle işlenecek veri miktarının donanımı aşmasıdır.

## Farklı Disiplinlerde Kullanımı
- **Matbaa:** Sayfa tasarımının baskı kalıbına dönüştürülmesi.
- **Mimari:** Projenin gerçeğe yakın üç boyutlu görseli (vaziyet).
- **Sinema:** Çekim sonrası efektlerin karesel olarak hesaplanması.

## Bir benzetmeyle
Bir şefin elindeki ham malzemeleri (veriler) kullanarak sunuma hazır bir tabağa (görsel) dönüştürmesi gibidir.

## Sıkça sorulanlar

**Rendering neden yavaş olabilir?**  
İşlenecek veri miktarı donanımın kapasitesini aşarsa süreç yavaşlar. Çözüm genellikle detayı kısmak, donanımı güçlendirmek veya işi parçalara bölmektir.

**Ray tracing nedir?**  
Işık huzmelerinin sahnedeki yolunu takip ederek yansıma ve gölgeleri gerçekçi hesaplayan yöntemdir. Kalitelidir, ancak rasterleştirmeye göre çok daha fazla işlem gücü ister.

**SSR ile CSR arasındaki fark nedir?**  
SSR sayfayı sunucuda çizip hazır gönderir, ilk açılış hızlı olur. CSR çizimi tarayıcıya bırakır, ilk açılış yavaş olur ama sonrası akıcıdır.

**Rendering için güçlü ekran kartı şart mı?**  
Her zaman değil. Web sayfası ve ofis işleri için işlemci yeterlidir. Oyun, 3B tasarım ve video işleri ise güçlü ekran kartı ister.

## İlgili terimler
- [GUI](/dictionary/gui/)
- [User Interface](/dictionary/user-interface/)
- [Frontend Stack](/dictionary/frontend-stack/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/rendering/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
