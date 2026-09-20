# Jupyter Notebooks nedir, ne işe yarar?

**Kategori:** Veri & Altyapı  
**Son güncelleme:** 2026-09-19

Jupyter Notebook (Jupyter Not Defteri), Python, R ve Julia gibi dillerde canlı kod çalıştırma, zengin metin, matematiksel formüller ve veri görselleştirmelerini tek bir etkileşimli web dokümanında birleştiren açık kaynaklı hesaplama ortamıdır.

## Doğuşu, felsefesi ve edebi programlama
Jupyter Notebooks, modern veri bilimi, makine öğrenimi ve akademik araştırmaların fiili çalışma alanıdır. 2001 yılında Fernando Perez tarafından başlatılan IPython (Interactive Python) projesinin evrilmesiyle 2014 yılında bağımsız bir çatı olan **Project Jupyter** doğmuştur.

İsmin kökeni iki anlamlı bir göndermedir:
1. Bilimsel hesaplamanın öncü üç açık kaynak dili olan **Ju**lia, **Pyt**hon ve **R** harflerinin birleşimi.
2. Astronom Galileo Galilei'nin 1610 yılında Jüpiter'in uydularını keşfederken tuttuğu gözlem defterlerine (notebook) duyulan saygı.

Felsefi olarak bilgisayar bilimcisi Donald Knuth'un ortaya attığı **"Literate Programming" (Edebi Programlama)** ilkesine dayanır: Programlar sadece makinelerin çalıştırması için değil, öncelikle insanların okuyup düşünce zincirini takip edebilmesi için yazılmalıdır. Jupyter; hipotezlerinizi, kodunuzu, görsel grafiklerinizi ve vardığınız sonuçları tek bir yaşayan belgede birleştirir.

## Bir benzetmeyle
Geleneksel bir Python scripti kapalı bir fabrikaya benzer; hammaddeyi verirsiniz ve içeride ne olduğunu görmeden sadece son ürünü alırsınız. Jupyter Notebook ise şeffaf bir mutfak ve adım adım fotoğraflı bir yemek tarifi defteri gibidir: Her malzemeyi tek tek ekler, anlık tadına bakar, fotoğrafını çeker ve notlarınızı hemen yanına iliştirirsiniz.

## Sistem mimarisi: İstemci, sunucu ve çekirdek (Kernel)
Jupyter altyapısı, gevşek bağlı (loosely coupled) üç katmanlı bir mimari üzerinde çalışır:

1. **İstemci (Web Arayüzü):** Tarayıcınızda çalışan, hücreleri düzenlemenize, çalıştırmanıza ve çıktıları görüntülemenize imkân tanıyan JavaScript/HTML5 ön yüzüdür (JupyterLab veya klasik arayüz).
2. **Jupyter Sunucusu (Tornado tabanlı Web Server):** Yerel makinenizde veya uzak bir sunucuda çalışan, dosya sistemini yöneten, oturumları koordine eden ve WebSocket bağlantılarını sağlayan arka uçtur.
3. **Çekirdek (Kernel):** Kodu fiilen çalıştıran izole dildir. Örneğin Python için `ipykernel`, R için `IRkernel`, Julia için `IJulia` kullanılır. Sunucu ile çekirdek arasındaki iletişim, endüstri standardı **ZeroMQ** mesajlaşma soketleri üzerinden JSON formatında gerçekleşir.

### .ipynb Dosyasının İç Yapısı
Jupyter belgeleri uzantısı `.ipynb` olsa da aslında hiyerarşik birer **JSON** dosyasıdır. Her hücrenin türü (`code`, `markdown`), çalıştırılma sırası (`execution_count`), kaynak kodu (`source`) ve üretilen çıktılar (`outputs` - metin, HTML, Base64 formatında PNG grafikleri) bu JSON nesnesinde saklanır.

## Veri bilimindeki gücü ve yazılım mühendisliği tuzakları
- **Keşifsel Veri Analizi (EDA):** Veri bilimciler devasa bir veri setini belleğe bir kez yükledikten sonra, saatlerce süren bellek yükleme aşamasını tekrarlamadan farklı hücrelerde veri temizleme, model eğitme ve Matplotlib/Seaborn/Plotly ile görselleştirme yapabilirler.
- **Gizli Durum (Hidden State) Riski:** Hücrelerin yukarıdan aşağıya sıralı yerine rastgele bir sırada çalıştırılabilmesi (out-of-order execution), hafızada görünmeyen değişken durumları bırakabilir. Bu durum, başkasının aynı not defterini çalıştırdığında farklı sonuçlar almasına veya hata vermesine yol açabilir ("reproducibility crisis").
- **Versiyon Kontrolü (Git) Zorlukları:** `.ipynb` dosyaları zengin çıktılar ve Base64 grafikler içerdiğinden, Git üzerinde satır farkı (diff) incelemek ve çakışmaları (merge conflict) çözmek zordur. Bu sorunu aşmak için `jupytext` (not defterini temiz Markdown veya Python script'iyle senkronize eden araç) ve `nbdime` gibi araçlar kullanılır.

## Sıkça sorulanlar

**Jupyter Notebook ne demek ve açılımı nereden gelir?**  
Jupyter adı; Julia, Python ve R programlama dillerinin ilk harflerinden ve astronom Galileo'nun Jüpiter gözlem notlarına yapılan atıftan türetilmiştir. Canlı kod ve zengin metin içeren interaktif not defteridir.

**Jupyter Notebook ile standart bir Python dosyası (.py) arasındaki fark nedir?**  
`.py` dosyaları baştan sona tek parça halinde derlenip çalıştırılan saf metin kodlarıdır. `.ipynb` ise kodu parçalı hücreler (cells) halinde çalıştırabilen, çıktıları, tabloları ve grafikleri doğrudan kodun altında saklayan bir JSON yapısıdır.

**Google Colab ile Jupyter Notebook arasındaki ilişki nedir?**  
Google Colab, Jupyter Notebook altyapısının Google bulutunda çalışan, ücretsiz GPU ve TPU donanım hızlandırması sunan, kurulum gerektirmeyen tescilli bir bulut türevidir.

**Jupyter Notebook'ta temiz kod ve sürüm kontrolü nasıl sağlanır?**  
Kodları depoya göndermeden önce hücre çıktılarını temizlemek (Clear All Outputs), hücreleri yukarıdan aşağıya sırayla yeniden çalıştırmak ve `jupytext` gibi araçlarla dosya formatını sürümlenebilir kılmak en iyi yaklaşımdır.

## İlgili terimler
- [Data Pipeline](/dictionary/data-pipeline/)
- [Markdown](/dictionary/markdown/)
- [Runtime](/dictionary/runtime/)
- [Apple Silicon](/dictionary/apple-silicon/)
- [Tech Stack](/dictionary/tech-stack/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/jupyter-notebooks/  
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
