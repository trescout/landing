# Yapay zekâ ile tersine mühendislik

Rea, uygulama davranışlarından yerel ikili dosyalara (native binaries) kadar her şeyi analiz eden yapay zekâ ajanları tabanlı bir tersine mühendislik (reverse engineering) aracıdır. TypeScript ile geliştirilen bu yazılım, karmaşık sistemlerin çalışma mantığını otomatize edilmiş süreçlerle çözümlemeyi amaçlar.

- ★ 37.239
- TypeScript
- GitHub Trending · 2026-10-06

## Güncelleme

- **9 Ekim 2026:** Yıldız 34.379 → 37.239, son sürüm rea-agents-6.1.0 (9 Ekim 2026).
- **9 Ekim 2026:** Yıldız 24.429 → 34.379, son sürüm rea-agents-6.1.0 (9 Ekim 2026).
- **8 Ekim 2026:** Yıldız 20.955 → 24.429, son sürüm rea-agents-6.0.0 (8 Ekim 2026).
- **8 Ekim 2026:** Yıldız 19.417 → 20.955, son sürüm rea-agents-6.0.0 (8 Ekim 2026).

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

🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Sistemimde tersine mühendislik aracı REA'yı yapılandırmak istiyorum. Öncelikle 'npx rea-agents setup' komutuyla gerekli kurulum adımlarını tamamla ve yapay zekâ arayüzüm için MCP (Model Context Protocol, yapay zekâ araç protokolü) bağlantısını kur. Ardından 'npx -y rea-agents@latest doctor' komutunu çalıştırarak bağımlılıkları denetle ve seçtiğim yerel bir uygulamayı inceleyip aradığım özelliğin nasıl çalıştığını kanıtlarıyla açıkla.

- **Kimin için:** Mevcut uygulamaların çalışma mantığını kaynak koda ihtiyaç duymadan yapay zekâ yardımıyla incelemek ve benzer özellikleri kendi projelerine uyarlamak isteyen geliştiriciler içindir.
- **Lisans:** MIT

## Bağlantılar

- [GitHub deposu →](https://github.com/morluto/rea)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-10-06 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Native Binaries](https://trescout.com/dictionary/native-binaries/)
- [Reverse Engineering](https://trescout.com/dictionary/reverse-engineering/)
- [Native](https://trescout.com/dictionary/native/)
- [Model Context Protocol](https://trescout.com/dictionary/model-context-protocol/)
- [Model Context Protocol](https://trescout.com/dictionary/model-context-protocol-mcp/)
- [Context](https://trescout.com/dictionary/context/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/rea/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
