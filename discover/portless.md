# Yerel geliştirme ortamına kalıcı URL

Vercel Labs tarafından geliştirilen Portless, yerel geliştirme ortamlarında kullanılan port numaralarını kalıcı ve isimlendirilmiş URL adreslerine dönüştürüyor. Bu araç, hem yazılımcıların hem de otonom yapay zekâ ajanlarının yerel servislerle daha kolay etkileşime girmesini sağlıyor.

- ★ 11.949
- TypeScript
- GitHub Trending · 2026-09-03

## Güncelleme
- 3 Eylül 2026: Yıldız 11.944 → 11.949, son sürüm v0.15.6 (24 Ağustos 2026).

## Ne kazandırır?
- Değişken port numaralarını hatırlanabilir isimli adreslere dönüştürür
- HTTPS ve HTTP/2 desteğini otomatik olarak sağlar
- Monorepo yapılarında her paket için ayrı URL oluşturur

## Kurulum

**Genel kurulum**

```
npm install -g portless
```

**Proje bazlı kurulum**

```
npm install -D portless
```

## Çalıştırma

**Uygulamayı isimlendirilmiş URL ile başla**

```
portless myapp next dev
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Yerel geliştirme ortamımda çalışan servislerimin port numaraları yerine .localhost uzantılı kalıcı adresler kullanmasını istiyorum. Portless aracını kullanarak projemi çalıştır ve servislerime https://myapp.localhost gibi tanımlanabilir adresler üzerinden erişebilmemi sağla.

- **Kimin için:** Yerel geliştirme süreçlerinde port karmaşasından kurtulmak isteyen yazılımcılar ve otonom yapay zekâ ajanları içindir. 
- **Lisans:** Apache-2.0 

## Bağlantılar
- [GitHub deposu →](https://github.com/vercel-labs/portless)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-09-03 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Monorepo Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/portless/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
