# Kendi sunucunuzda çalışan spor takip yazılımı

OpenGym, antrenman rutinlerini planlamaya ve vücut ağırlığı egzersizlerini takip etmeye yarayan açık kaynaklı bir spor salonu yönetim aracıdır. Kullanıcıların verilerini kendi sunucularında barındırmalarına olanak tanıyan bu yazılım, popüler fitness uygulamalarından (Strong, Hevy) veri aktarımını destekler.

- ★ 13.304
- JavaScript
- GitHub Trending · 2026-10-05

## Güncelleme

- **18 Ekim 2026:** Yıldız 12.021 → 13.304, son sürüm v1.4.1 (10 Ekim 2026).
- **15 Ekim 2026:** Yıldız 10.912 → 12.021, son sürüm v1.4.1 (10 Ekim 2026).
- **13 Ekim 2026:** Yıldız 9.501 → 10.912, son sürüm v1.4.1 (10 Ekim 2026).
- **11 Ekim 2026:** Yıldız 8.392 → 9.501, son sürüm v1.4.1 (10 Ekim 2026).

## Ne kazandırır?

- Antrenman verilerinizi üçüncü taraf şirketlerin sunucuları yerine kendi kontrol ettiğiniz güvenli bir alanda saklayabilirsiniz.
- Strong ve Hevy gibi popüler fitness uygulamalarından geçmiş egzersiz verilerinizi kolayca aktarabilirsiniz.
- İnternet bağlantınız olmasa bile telefonunuzdan veya bilgisayarınızdan antrenmanlarınızı planlayıp takip edebilirsiniz.

## Kurulum

**Docker konteyner yönetim platformu ile k**

```
git clone https://github.com/DuarteSantos8/openGym
cd openGym
cp .env.example .env
docker compose pull      # prebuilt images, amd64 + arm64 (skip this to build from source)
docker compose up -d
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

openGym spor takip yazılımını Docker konteyner yönetim platformu üzerinde kurmak istiyorum. Bana 'git clone https://github.com/DuarteSantos8/openGym' komutuyla başlayan kurulum adımlarını, '.env' çevre değişkenleri dosyasının nasıl yapılandırılacağını ve kurulum tamamlandıktan sonra tarayıcıdan uygulamaya nasıl erişeceğimi adım adım açıklar mısın?

Depo: https://github.com/DuarteSantos8/openGym. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Bir API anahtarı gerekirse onu sohbete yazmamı isteme. .env dosyasına nasıl ekleyeceğimi göster ve bu dosyanın Git'e gönderilmediğinden emin ol.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Antrenman verilerinin gizliliğine önem veren ve spor salonu rutinlerini kendi sunucusunda ücretsizce takip etmek isteyen spor tutkunları içindir.
- **Lisans:** AGPL-3.0

## Bağlantılar

- [GitHub deposu →](https://github.com/DuarteSantos8/openGym)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-10-05 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Clone](https://trescout.com/dictionary/clone/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/opengym/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
