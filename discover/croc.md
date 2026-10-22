# Güvenli ve kolay dosya transferi

Croc, iki bilgisayar arasında uçtan uca şifreleme (end-to-end encryption) kullanarak güvenli dosya ve veri aktarımı sağlayan bir araçtır. Go programlama diliyle geliştirilen bu yazılım, aktarım sürecini kolaylaştırmak için geçici bir röle (relay) mekanizması kullanır.

- ★ 40.679
- Go
- GitHub Trending · 2026-07-22

## Güncelleme

- **20 Ekim 2026:** Yıldız 40.451 → 40.679, son sürüm v11.5.5 (19 Ekim 2026).
- **27 Eylül 2026:** Yıldız 40.324 → 40.451, son sürüm v11.5.4 (26 Eylül 2026).
- **14 Eylül 2026:** Yıldız 40.287 → 40.324, son sürüm v11.5.3 (13 Eylül 2026).
- **10 Eylül 2026:** Yıldız 40.279 → 40.287, son sürüm v11.5.2 (9 Eylül 2026).

## Ne kazandırır?

- Uçtan uca şifreli veri gönderimi
- Farklı işletim sistemleri arası uyum
- Kesilen aktarımları kaldığı yerden sürdürme

## Kurulum

**Genel kurulum**

```
curl https://getcroc.schollz.com | bash
```

**macOS üzerinde kurulum**

```
brew install croc
```

## Çalıştırma

**Dosya gönderme**

```
croc send [file(s)-or-folder]
```

**Dosya alma**

```
croc code-phrase
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Croc aracını kullanarak iki bilgisayar arasında güvenli bir şekilde dosya transferi yapmak istiyorum. Gönderici tarafında 'croc send [dosya_adı]' komutunu çalıştırdığımda bana verilen kod ifadesini, alıcı tarafta 'croc [kod_ifadesi]' komutuyla nasıl eşleştirip aktarımı başlatabilirim? Aktarım sırasında uçtan uca şifrelemenin sağlandığından ve sürecin güvenli ilerlediğinden emin olmak için dikkat etmem gereken özel bir ayar var mı?

Depo: https://github.com/schollz/croc. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** İki cihaz arasında aracı sunucuya ihtiyaç duymadan, şifreli ve hızlı dosya paylaşımı yapmak isteyen herkes için uygundur.
- **Lisans:** MIT

## Bağlantılar

- [GitHub deposu →](https://github.com/schollz/croc)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-07-22 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [End-to-End Encryption](https://trescout.com/dictionary/end-to-end-encryption/)
- [Relay](https://trescout.com/dictionary/relay/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/croc/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
