# Yapay zekâ ile tersine mühendislik

Rea, uygulama davranışlarından yerel ikili dosyalara (native binaries) kadar her şeyi analiz eden yapay zekâ ajanları tabanlı bir tersine mühendislik (reverse engineering) aracıdır. TypeScript ile geliştirilen bu yazılım, karmaşık sistemlerin çalışma mantığını otomatize edilmiş süreçlerle çözümlemeyi amaçlar.

- ★ 329.371
- TypeScript
- GitHub Trending · 2026-10-06

## Güncelleme

- **19 Ekim 2026:** Yıldız 313.106 → 329.371, son sürüm rea-agents-6.7.0 (18 Ekim 2026).
- **18 Ekim 2026:** Yıldız 296.420 → 313.106, son sürüm rea-agents-6.7.0 (18 Ekim 2026).
- **17 Ekim 2026:** Yıldız 280.503 → 296.420, son sürüm rea-agents-6.5.0 (14 Ekim 2026).
- **16 Ekim 2026:** Yıldız 255.025 → 280.503, son sürüm rea-agents-6.5.0 (14 Ekim 2026).

## Ne kazandırır?

- Kaynak koduna erişiminiz olmayan masaüstü veya web uygulamalarının iç mantığını yapay zekâ desteğiyle çözebilirsiniz.
- Tersine mühendislik yazılımları Hopper ve Ghidra ile entegre olarak ikili sistem dosyalarını yerel bilgisayarınızda güvenle incelersiniz.
- Beğendiğiniz bir yazılım özelliğinin nasıl çalıştığını adım adım kanıtlarıyla öğrenip kendi projenize uyarlayabilirsiniz.

## Kurulum

**Kurulum yardımcısını başlatma**

```
npx rea-agents setup
```

**Paket yöneticisi npm ile küresel kurulum**

```
npm install --global rea-agents
rea setup
```

## Çalıştırma

**Sistem kontrolü ve örnek uygulama analiz**

```
npx -y rea-agents@latest doctor
npx -y rea-agents@latest analyze /Applications/Notes.app
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Sistemimde tersine mühendislik aracı REA'yı yapılandırmak istiyorum. Öncelikle 'npx rea-agents setup' komutuyla gerekli kurulum adımlarını tamamla ve yapay zekâ arayüzüm için MCP (Model Context Protocol, yapay zekâ araç protokolü) bağlantısını kur. Ardından 'npx -y rea-agents@latest doctor' komutunu çalıştırarak bağımlılıkları denetle ve seçtiğim yerel bir uygulamayı inceleyip aradığım özelliğin nasıl çalıştığını kanıtlarıyla açıkla.

Depo: https://github.com/morluto/rea. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Mevcut uygulamaların çalışma mantığını kaynak koda ihtiyaç duymadan yapay zekâ yardımıyla incelemek ve benzer özellikleri kendi projelerine uyarlamak isteyen geliştiriciler içindir.
- **Lisans:** MIT

## Bağlantılar

- [GitHub deposu →](https://github.com/morluto/rea)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-10-06 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Native Binaries](https://trescout.com/dictionary/native-binaries/)
- [Reverse Engineering](https://trescout.com/dictionary/reverse-engineering/)
- [Native](https://trescout.com/dictionary/native/)
- [Model Context Protocol](https://trescout.com/dictionary/model-context-protocol/)
- [Model Context Protocol](https://trescout.com/dictionary/model-context-protocol-mcp/)
- [Context](https://trescout.com/dictionary/context/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/rea/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
