# Mermaid nedir, ne demek?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-22

Mermaid, metin yazarak diyagram çizen açık kaynak JavaScript kütüphanesidir.

## Tanım ve Kelime Kökeni
Çizim aracında kutu sürüklemek yerine şema metinle yazılır, araç görsele çevirir. Metin sürümlenebilir olduğu için dokümantasyonla birlikte yaşar ve incelemeden geçer. Adını denizkızı mitinden alır, tekniklikle ilgisi yoktur.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Dokümantasyon:** README içinde mimari şeması.
- **Planlama:** Gantt ile takvim görünümü.
- **Rapor:** Akış ve sıra şemaları.

## Teknik Derinlik ve Mimari
Başlıca türler:
- **Flowchart:** Karar ve akış kutuları.
- **Sequence:** Zaman eksenli etkileşim.
- **Gantt:** Görev takvimi.
- **ER:** Varlık ilişki şeması.

Basit akış örneği:

```
flowchart LR
    A[İstek] --> B[Sunucu]
    B --> C[Yanıt]
```

GitHub ve GitLab bu blokları doğrudan çizer, eklenti gerekmez. Canlı önizleme için resmi editör kullanılır.

## Sık Karıştırılanlar
Çizim araçları sanılır. Oysa Mermaid metin tabanlıdır, sürükle-bırak içermez. Görsel hassasiyette çizim gerekirse grafik editörü gerekir.

## Farklı Disiplinlerde Kullanımı
- **Müzik:** Notalama ile sesin yazıya dökülmesi.
- **Stenografi:** Konuşmanın kısayolla yazılması.
- **Matematik:** Formülle şeklin anlatılması.

## Bir benzetmeyle
Bir mimarın çizim yapmak yerine binanın özelliklerini yazarak şemayı anında elde etmesi gibidir.

## Sıkça sorulanlar

**Mermaid ile hangi grafikler çizilir?**  
Akış, sıra, Gantt, pasta, ER ve zihin haritası gibi teknik şemalar çizilir.

**GitHub destekler mi?**  
Evet. Markdown içindeki mermaid blokları doğrudan çizilir.

**Ücretsiz mi?**  
Çekirdek kütüphane açık kaynak ve ücretsizdir. Barındırılan editörlerde ücretli katman olabilir.

**Ne zaman yetersiz kalır?**  
Piksel hassasiyeti ve serbest çizim gerektiğinde. O iş grafik editörünündür.

## İlgili terimler
- [Markdown](/dictionary/markdown/)
- [Diagrams](/dictionary/diagrams/)
- [Architecture Diagrams](/dictionary/architecture-diagrams/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/mermaid/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
