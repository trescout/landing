# PowerPoint nedir, ne demek?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-22

PowerPoint, Microsoft'un slayt tabanlı sunum hazırlama uygulamasıdır.

## Tanım ve Kelime Kökeni
Program 1987 yılında Forethought şirketinden doğdu, kısa süre sonra Microsoft bünyesine katıldı. Fikirlerinizi, verilerinizi veya projenizi bir izleyici kitlesine anlatırken kullandığınız dijital sahnedir: Metinleri, görselleri ve grafikleri düzenli slaytlar halinde birleştirirsiniz. Dosya biçimi `.pptx`, aslında sıkıştırılmış bir XML paketidir.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **İş toplantıları:** Çeyrek raporları ve proje durum sunumları.
- **Okul:** Ödev ve tez savunmaları.
- **Konferanslar:** Açılış konuşmaları ve paneller.
- **Eğitim:** Ders anlatım setleri.

## Teknik Derinlik ve Mimari
Etkili sunumun parçaları:
- **Slayt-asıl (Slide Master):** Yazı tipi, renk ve logonun tek yerden yönetildiği şablon. Her slaytı ayrı biçimlendirmek yerine aslı düzenlersiniz.
- **Sunucu görünümü:** Siz notlarınızı görürsünüz, izleyiciyalnızca slaytı görür.
- **Dışa aktarma:** Sunum PDF veya video olarak kaydedilebilir.
- **Otomasyon:** Tekrarlanan sunumlar kodla üretilebilir. Python ile boş bir sunum açmak şöyledir:

```
from pptx import Presentation
sunum = Presentation()
slayt = sunum.slides.add_slide(sunum.slide_layouts[5])
slayt.shapes.title.text = "Merhaba"
sunum.save("ornek.pptx")
```

Kural olarak slayt başına tek fikir düşer. Yazıyı resimle desteklemek, duvar metni yazmaktan daha etkilidir.

## Farklı Disiplinlerde Kullanımı
- **Ders tahtası:** Konuyu adım adım açan tahta düzeni.
- **Fotoğraf albümü:** Anlatıyı sıraya dizen görsel akış.
- **Tiyatro:** Perde perde ilerleyen sahne planı.

## Bir benzetmeyle
Bir hikaye anlatıcısının, anlattıklarını desteklemek için elinde tuttuğu resimli kartlar destesi gibidir.

## Sıkça sorulanlar

**Sunum yaparken not alabilir miyim?**  
Evet. Sunucu görünümünde notlarınızı görürsünüz, izleyiciler yalnızca slaytı görür.

**Başka formatlara çevrilebilir mi?**  
Evet. Sunumunuzu PDF veya video olarak kaydedebilirsiniz.

**Ücretsiz alternatif var mı?**  
Evet. LibreOffice Impress ve web tabanlı Google Slides benzer işleri görür. Geçişte yazı tipi ve animasyon farklarına dikkat edin.

**Dosya çok büyüdüyse ne yapılır?**  
Görselleri sıkıştırın, videoyu bağlayın (gömmeyin) ve kullanılmayan asılları temizleyin. Tek dosya yerine bölüm bölüm kaydetmek de işe yarar.

## İlgili terimler
- [Design Tool](/dictionary/design-tool/)
- [User Interface](/dictionary/user-interface/)
- [Dashboard](/dictionary/dashboard/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/powerpoint/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
