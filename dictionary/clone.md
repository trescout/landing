# Clone nedir, ne demek?

*Sözlük · Geliştirme · Son güncelleme: 22 Eylül 2026*

Clone (Türkçe karşılığıyla **klonlama**), uzak bir Git deposunun tüm geçmişiyle birlikte yerel kopyasını oluşturma işlemidir.

## Tanım ve Kelime Kökeni

"Clone" İngilizcede **birebir kopya** anlamına gelir. Git dünyasında `git clone` komutuyla kullanılır: Yalnızca güncel dosyaları değil, projenin tüm commit geçmişini, dallarını ve etiketlerini de indirirsiniz.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?

Açık kaynak bir projeyi incelemek veya katkı yapmak istediğinizde ilk adım genellikle klonlamaktır:

```
git clone https://github.com/kullanici/proje.git
```

Komut çalışınca bulunduğunuz dizinde `proje` klasörü oluşur. Depo çok büyükse geçmişin bir kısmını almak için sığ klon kullanılır:

```
git clone --depth 1 https://github.com/kullanici/proje.git
```

## Teknik Derinlik ve Mimari

Klonlanan klasörün içindeki `.git` dizini, deponun hafızasıdır: Tüm commit nesneleri, dal işaretçileri ve uzak adres burada durur. Klondan sonra:

`git fetch` uzak değişiklikleri indirir, dosyalarınıza dokunmaz.
`git pull` indirir ve mevcut dalınıza birleştirir.
`git push` sizin commitlerinizi uzağa gönderir (yetkiniz varsa).
`fork` ise sunucu tarafında kopya oluşturur. Klon, o kopyayı veya asıl depoyu bilgisayarınıza indirir. İkisi farklı kavramlardır.

## Farklı Disiplinlerde Kullanımı

**Biyoloji:** Canlının genetik kopyası. Yazılımdaki klon ise verinin kopyasıdır, canlıyla ilgisi yoktur.
**Medya:** Aslı dururken çalışılacak yedek kostümler.
**Sanallaştırma:** Hazır kalıptan yeni makine üretme.

*Kütüphanedeki kitabın yalnızca bir sayfasının fotoğrafını çekmek değil, kitabın tüm kopyasını kendi rafınıza almak gibidir.*

## Sıkça Sorulanlar

**Klonlayınca projeyi değiştirebilir miyim?**

Evet. Kendi kopyanızda dilediğiniz değişikliği yaparsınız. Orijinal depo etkilenmez. Değişikliğinizi projeye önermek isterseniz pull request açarsınız.

**Fork ile clone arasındaki fark nedir?**

Fork sunucuda kopya oluşturur (sizin hesabınızda), clone o kopyayı bilgisayarınıza indirir. Katkı akışı genellikle fork, ardından clone biçimindedir.

**Depo çok büyükse ne yapmalıyım?**

--depth 1 ile sığ klon alın veya yalnızca tek dalı (--single-branch) indirin. Geçmişe ihtiyaç duyarsanız sonra derinleştirebilirsiniz.

**Klonu güncel tutar mıyım?**

Evet. Klasör içinde git pull çalıştırmanız yeterlidir. Değişikliğiniz varsa önce onları commitlemeniz veya saklamanız (git stash) gerekir.

## İlgili terimler

- [CLI](https://trescout.com/dictionary/cli/)
- [Open Source](https://trescout.com/dictionary/open-source/)
- [Self-Hosting](https://trescout.com/dictionary/self-hosting/)

## İlgili araçlar

- [MoneyPrinterTurbo](https://trescout.com/discover/moneyprinterturbo/)
- [VoxCPM](https://trescout.com/discover/voxcpm/)
- [Clone-Wars](https://trescout.com/discover/clone-wars/)
- [Univer](https://trescout.com/discover/univer/)
- [OpenStock](https://trescout.com/discover/openstock/)
- [Hermes WebUI](https://trescout.com/discover/hermes-webui/)
- [Production Agentic RAG Course](https://trescout.com/discover/production-agentic-rag-course/)
- [Flowsint](https://trescout.com/discover/flowsint/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/clone/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
