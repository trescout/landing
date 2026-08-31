# Terminalde yapay zekâ destekli kodlama

Codex CLI, yerel bilgisayarınızda terminalde çalışan bir kodlama ajanıdır. Kodları inceleyebilir, dosyalarda değişiklik yapabilir ve komut çalıştırabilir.

- ★ 120.409
- GitHub Trending · 2026-08-23

## Kurulum

**macOS veya Linux**

```
curl -fsSL https://chatgpt.com/codex/install.sh | sh
```

**Windows PowerShell**

```
powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"
```

## Çalıştırma

**Codex CLI başlatma**

```
codex
```

Kaynak: OpenAI’nin Codex CLI belgeleri ve openai/codex README’si, 24 Ağustos 2026’da kontrol edildi.

## Güncelleme
- 31 Ağustos 2026: Yıldız 119.077 → 120.409, son sürüm rust-v0.151.0 (29 Ağustos 2026).
- 27 Ağustos 2026: Yıldız 115.876 → 119.077, son sürüm rust-v0.150.1 (27 Ağustos 2026).

## Bu araç ne yapar?

Codex CLI, yerel bilgisayarınızda terminalde çalışan bir kodlama ajanıdır. Bir proje dizinindeki kodu inceleyebilir, dosyalarda değişiklik yapabilir, komut çalıştırabilir ve tekrarlanan işleri otomatikleştirmeye yardımcı olabilir.

## Kimin için?

Terminalde çalışan, kod tabanını incelemek, dosyaları düzenlemek ve tekrarlanan geliştirme işlerini otomatikleştirmek isteyen geliştiriciler.

## Ne beklememeli?

Terminal kullanmak istemeyenler için uygun olmayabilir.

## Öne çıkanlar
- Kodları inceleyebilir ve dosyalarda değişiklik yapabilir.
- Komut çalıştırabilir ve tekrarlanan işleri otomatikleştirebilir.
- Model, reasoning effort, izinler ve komut onayları kullanıcı tarafından yönetilebilir.
- GitHub deposu Apache-2.0 lisanslıdır.

## İlk kullanım akışı
- İşletim sisteminize uygun resmî kurulum yöntemini seçin.
- Kurulumdan sonra Codex CLI’ı terminalden başlatın.
- ChatGPT ile veya mevcut başka bir oturum açma yöntemiyle giriş yapın.
- Proje dizininden başlayın. Değişikliklerden önce ve sonra Git checkpoint oluşturun.

## Güvenli başlangıç

Değişikliklerden önce ve sonra Git checkpoint oluşturmanız önerilir. İzinleri /permissions ile, mevcut durumu /status ile inceleyebilirsiniz.

## İlk görev istemi
İlk adım için hazır istem 
İlk kullanımda, projenin amacını ve dosya yapısını açıklayan bir inceleme talebiyle başlayabilirsiniz.

## Bağlantılar
- [GitHub deposu →](https://github.com/openai/codex)
- [Codex CLI resmî belgeleri →](https://learn.chatgpt.com/docs/codex/cli)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-08-23 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Terminal CLI Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/codex/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
