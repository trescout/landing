# Güvenli ve kolay dosya transferi

Croc, iki bilgisayar arasında uçtan uca şifreleme (end-to-end encryption) kullanarak güvenli dosya ve veri aktarımı sağlayan bir araçtır. Go programlama diliyle geliştirilen bu yazılım, aktarım sürecini kolaylaştırmak için geçici bir röle (relay) mekanizması kullanır.

- ★ 39.942
- Go
- GitHub Trending · 2026-07-22

## Güncelleme
- 19 Ağustos 2026: Yıldız 39.923 → 39.942, son sürüm v11.2.2 (19 Ağustos 2026).
- 19 Ağustos 2026: Yıldız 39.880 → 39.923, son sürüm v11.2.1 (18 Ağustos 2026).
- 18 Ağustos 2026: Yıldız 39.809 → 39.880, son sürüm v11.2.0 (18 Ağustos 2026).
- 16 Ağustos 2026: Yıldız 39.672 → 39.809, son sürüm v11.1.1 (15 Ağustos 2026).

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
