# Compositor nedir?

*Geliştirme · Son güncelleme: 3 Kasım 2026*

Ekranda pencerelerin nerede görüneceğini ve birbirleriyle görsel etkileşimini yöneten yazılım katmanıdır.

## Tanım

İşletim sisteminde pencerelerin çizilmesi, şeffaflık efektleri, gölgeler ve pencerelerin üst üste bindiği durumlardaki görünürlük hesaplamalarından sorumludur. Geleneksel pencere yöneticilerinin yerini alan modern yapılar hem görsel kaliteyi artırır hem de grafik kartının gücünü kullanarak pencerelerin akıcı hareket etmesini sağlar. Yazılım pencerelerden gelen görüntüleri birleştirerek monitöre son piksel halini gönderir.

*Tiyatro sahnesinde hangi dekorun önde hangi oyuncunun arkada duracağını, ışığın kime vuracağını ayarlayan sahne yönetmeni gibidir.*

## Nasıl çalışır?

Uygulamalardan gelen grafik verilerini toplar, pencerelerin konumunu ve görsel efektlerini işleyerek ekran kartına nihai resmi çizdirir.

## Nerede kullanılır?

Linux grafik sunucularında, Wayland protokolünde ve modern masaüstü işletim sistemlerinin çekirdek grafik mimarisinde yer alır.

## Sık karıştırılanlar

Doğrudan ekran kartı sürücüsüyle karıştırılır ama sürücü donanımı yönetirken compositor görsel katmanları düzenler.

## Sorular ve yanıtlar

**Ekran kartını yorar mı?**

Modern donanımlarda hayli hafiftir ve yükü ekran kartına vererek işlemciyi rahatlatır.

**Neden önemlidir?**

Pencereler taşınırken oluşan titremeleri önler ve modern görsel efektlerin sorunsuz çalışmasını sağlar.

## İlgili terimler

- [Dynamic Tiling](https://trescout.com/dictionary/dynamic-tiling/)
- [TUI](https://trescout.com/dictionary/tui/)
- [User Interface](https://trescout.com/dictionary/user-interface/)

## İlgili araçlar

- [Hyprland](https://trescout.com/discover/hyprland/)

Bu açıklama TreScout için yapay zekâ ile sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/compositor/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
