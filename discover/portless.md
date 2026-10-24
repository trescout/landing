# Yerel geliştirme ortamına kalıcı URL

Vercel Labs tarafından geliştirilen Portless, yerel geliştirme ortamlarında kullanılan port numaralarını kalıcı ve isimlendirilmiş URL adreslerine dönüştürüyor. Bu araç, hem yazılımcıların hem de otonom yapay zekâ ajanlarının yerel servislerle daha kolay etkileşime girmesini sağlıyor.

- ★ 12.739
- TypeScript
- GitHub Trending · 2026-09-03

## Güncelleme

- **24 Ekim 2026:** Yıldız 12.732 → 12.739, son sürüm v0.15.11 (24 Ekim 2026).
- **23 Ekim 2026:** Yıldız 12.695 → 12.732, son sürüm v0.15.9 (22 Ekim 2026).
- **14 Ekim 2026:** Yıldız 12.632 → 12.695, son sürüm v0.15.8 (13 Ekim 2026).
- **2 Ekim 2026:** Yıldız 11.949 → 12.632, son sürüm v0.15.7 (2 Ekim 2026).

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

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Yerel geliştirme ortamımda çalışan servislerimin port numaraları yerine .localhost uzantılı kalıcı adresler kullanmasını istiyorum. Portless aracını kullanarak projemi çalıştır ve servislerime https://myapp.localhost gibi tanımlanabilir adresler üzerinden erişebilmemi sağla.

Depo: https://github.com/vercel-labs/portless. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Yerel geliştirme süreçlerinde port karmaşasından kurtulmak isteyen yazılımcılar ve otonom yapay zekâ ajanları içindir.
- **Lisans:** Apache-2.0

## Bağlantılar

- [GitHub deposu →](https://github.com/vercel-labs/portless)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-09-03 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Monorepo](https://trescout.com/dictionary/monorepo/)
- [Localhost](https://trescout.com/dictionary/localhost/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/portless/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
