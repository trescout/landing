# Bilgisayarlı görü projelerinizi yapay zekâ ile hızlandırın

Roboflow tarafından geliştirilen Supervision, bilgisayarlı görü (computer vision) projeleri için yeniden kullanılabilir yardımcı araçlar ve fonksiyonlar sunuyor. Python tabanlı bu kütüphane, nesne tespiti ve takibi gibi süreçlerdeki standart işlemleri kolaylaştırarak geliştirme iş akışlarını hızlandırıyor.

- ★ 42.546
- Python
- GitHub Trending · 2026-06-09

## Ne kazandırır?
- Bilgisayarlı görü projelerinde veri yükleme ve işleme süreçlerini hızlandırır.
- Nesne tespiti ve takibi gibi işlemleri standartlaştırarak uygulama geliştirmeyi kolaylaştırır.
- Farklı model kütüphaneleriyle uyumlu çalışarak görselleştirme ve veri seti yönetimi sağlar.

## Kurulum

**Paket Kurulumu**

```
pip install supervision
```

## Çalıştırma

**Görsel Üzerinde Nesne İşaretleme**

```
import cv2
import supervision as sv

image = cv2.imread(...)
detections = sv.Detections(...)

box_annotator = sv.BoxAnnotator()
annotated_frame = box_annotator.annotate(scene=image.copy(), detections=detections)
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Python 3.9 veya üzeri bir ortamda pip install supervision komutuyla kütüphaneyi kurdum. Bilgisayarlı görü projemde nesne tespiti sonuçlarını görselleştirmek ve veri setimi yönetmek istiyorum. Supervision kütüphanesini kullanarak nesne tespiti sonuçlarını bir görüntü üzerine nasıl işaretleyebilirim ve farklı formatlardaki (COCO, YOLO vb.) veri setlerini nasıl yükleyip dönüştürebilirim? Lütfen kütüphanenin sunduğu annotator ve dataset yardımcı araçlarını kullanarak örnek bir iş akışı oluşturmama yardımcı ol.

- **Kimin için:** Bilgisayarlı görü projelerinde nesne tespiti ve takibi süreçlerini standartlaştırmak isteyen Python geliştiricileri için uygundur. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/roboflow/supervision)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-06-09 tarihindeki hâlini anlatır: yıldız, sayılar ve metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Computer Vision Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/supervision/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
