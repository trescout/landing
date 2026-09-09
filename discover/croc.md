# Güvenli ve kolay dosya transferi

Croc, iki bilgisayar arasında uçtan uca şifreleme (end-to-end encryption) kullanarak güvenli dosya ve veri aktarımı sağlayan bir araçtır. Go programlama diliyle geliştirilen bu yazılım, aktarım sürecini kolaylaştırmak için geçici bir röle (relay) mekanizması kullanır.

- ★ 40.279
- Go
- GitHub Trending · 2026-07-22

## Güncelleme
- 9 Eylül 2026: Yıldız 40.262 → 40.279, son sürüm v11.5.1 (8 Eylül 2026).
- 7 Eylül 2026: Yıldız 40.219 → 40.262, son sürüm v11.5.0 (6 Eylül 2026).
- 4 Eylül 2026: Yıldız 40.177 → 40.219, son sürüm v11.4.0 (3 Eylül 2026).
- 31 Ağustos 2026: Yıldız 40.115 → 40.177, son sürüm v11.3.6 (30 Ağustos 2026).

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
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Croc aracını kullanarak iki bilgisayar arasında güvenli bir şekilde dosya transferi yapmak istiyorum. Gönderici tarafında 'croc send [dosya_adı]' komutunu çalıştırdığımda bana verilen kod ifadesini, alıcı tarafta 'croc [kod_ifadesi]' komutuyla nasıl eşleştirip aktarımı başlatabilirim? Aktarım sırasında uçtan uca şifrelemenin sağlandığından ve sürecin güvenli ilerlediğinden emin olmak için dikkat etmem gereken özel bir ayar var mı?

- **Kimin için:** İki cihaz arasında aracı sunucuya ihtiyaç duymadan, şifreli ve hızlı dosya paylaşımı yapmak isteyen herkes için uygundur. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/schollz/croc)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-07-22 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
End-to-End Encryption Relay Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/croc/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
