# Yığınlı çekme isteklerini yönetin

GitHub tarafından geliştirilen gh-stack, yazılım geliştirme sürecinde yığınlı çekme istekleri (stacked pull requests) oluşturmayı ve yönetmeyi kolaylaştıran bir komut satırı aracıdır. Karmaşık kod değişikliklerini küçük ve bağımsız parçalara bölerek inceleme sürecini hızlandırmayı hedefler.

- ★ 911
- Go
- GitHub Trending · 2026-08-02

## Güncelleme
- 2 Ağustos 2026: Yıldız 860 → 911, son sürüm v0.1.0 (29 Temmuz 2026).

## Ne kazandırır?
- Büyük kod değişikliklerini küçük ve yönetilebilir parçalara böler
- Çekme istekleri arasındaki bağımlılıkları otomatik olarak düzenler
- Yığın içindeki dalları güncel tutmak için rebase işlemlerini kolaylaştırır

## Kurulum

**Aracı yükleme**

```
gh extension install github/gh-stack
```

**Yapay zekâ desteğini etkinleştirme**

```
gh skill install github/gh-stack
```

## Çalıştırma

**Yeni bir yığın başlatma**

```
gh stack init
```

**Yığına yeni katman ekleme**

```
gh stack add api-endpoints
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
GitHub üzerinde yığınlı çekme istekleri (stacked pull requests) oluşturmak için gh-stack aracını kullanıyorum. Mevcut çalışma dallarımı bir yığın yapısına dahil et, dallar arasındaki bağımlılıkları yönet ve kod inceleme sürecini hızlandırmak için yığını GitHub'a gönder.

- **Kimin için:** Karmaşık özelliklerini küçük ve bağımsız parçalar halinde geliştirerek kod inceleme süreçlerini hızlandırmak isteyen yazılım geliştiriciler için uygundur. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/github/gh-stack)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-08-02 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Stacked Pull Requests Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/gh-stack/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
