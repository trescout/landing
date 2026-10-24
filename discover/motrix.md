# Modern ve kapsamlı indirme yöneticisi

Motrix, TypeScript ile geliştirilen ve tüm dosya indirme ihtiyaçlarını karşılayan kapsamlı bir indirme yöneticisi (download manager). Kullanıcılara HTTP, FTP ve BitTorrent gibi farklı protokolleri tek bir arayüz üzerinden yönetme imkânı sunuyor.

- ★ 57.305
- TypeScript
- GitHub Trending · 2026-08-18

## Güncelleme

- **24 Ekim 2026:** Yıldız 56.101 → 57.305, son sürüm v2.0.0 (23 Ekim 2026).
- **5 Ekim 2026:** Yıldız 53.428 → 56.101, son sürüm v1.8.19 (3 Mayıs 2023).
- **18 Ağustos 2026:** Yıldız 53.422 → 53.428, son sürüm v1.8.19 (3 Mayıs 2023).

## Ne kazandırır?

- HTTP, FTP ve BitTorrent protokollerini tek arayüzden yönetir
- İndirme hızlarını sınırlar ve gelişmiş oturum yönetimi sunar
- Tarayıcı eklentileriyle tek tıkla indirme başlatır

## Kurulum

**Komut satırı arayüzünü yükleme**

```
npm install -g @motrix/cli
```

## Çalıştırma

**Dosya indirme işlemini başlatma**

```
motrix add https://example.com/file.iso --save-dir ~/Downloads
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Motrix komut satırı arayüzünü kullanarak indirme görevlerini yönetmeme yardımcı ol. İndirme listesini görüntülemek için 'motrix list', yeni bir dosya eklemek için 'motrix add [URL] --save-dir [DİZİN]' ve indirme ilerlemesini canlı takip etmek için 'motrix watch --stats' komutlarını kullan. Uzak bir sunucuya bağlanmam gerekirse 'motrix pair' komutunu devreye al.

Depo: https://github.com/agalwood/Motrix. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** İnternet üzerindeki farklı kaynaklardan dosya indirme süreçlerini tek bir merkezden kontrol etmek isteyen kullanıcılar içindir.

## Bağlantılar

- [GitHub deposu →](https://github.com/agalwood/Motrix)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-08-18 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Download Manager](https://trescout.com/dictionary/download-manager/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/motrix/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
