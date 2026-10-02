# Yapay zekâ ajanları için güvenli ortam

NVIDIA tarafından geliştirilen OpenShell, otonom yapay zekâ ajanları için güvenli ve gizlilik odaklı bir çalışma zamanı (runtime) ortamı sunuyor. Rust diliyle yazılan bu altyapı, ajanların sistem kaynaklarına erişimini izole ederek güvenli bir yürütme alanı oluşturmayı amaçlıyor.

- ★ 14.197
- Rust
- GitHub Trending · 2026-09-29

## Güncelleme
- 2 Ekim 2026: Yıldız 12.978 → 14.197, son sürüm v0.1.2 (28 Eylül 2026).
- 1 Ekim 2026: Yıldız 11.092 → 12.978, son sürüm v0.1.2 (28 Eylül 2026).
- 30 Eylül 2026: Yıldız 9.876 → 11.092, son sürüm v0.1.2 (28 Eylül 2026).
- 29 Eylül 2026: Yıldız 9.860 → 9.876, son sürüm v0.1.2 (28 Eylül 2026).

## Ne kazandırır?
- Yapay zekâ ajanlarını izole sandbox çevresinde çalıştırır
- Dosya ve ağ erişimini kurallarla sınırlar
- Kimlik bilgilerini gizleyerek güvenliği artırır

## Kurulum

**Aracı Kur ve Demo Ortam Oluştur**

```
curl -LsSf https://raw.githubusercontent.com/NVIDIA/OpenShell/main/install.sh | sh
openshell sandbox create --name demo
```

## Çalıştırma

**Yetenekleri Ekle**

```
npx skills add NVIDIA/OpenShell
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
OpenShell aracını kurmak ve test etmek için şu komutları kullanabilirsin: curl -LsSf https://raw.githubusercontent.com/NVIDIA/OpenShell/main/install.sh | sh ve ardından openshell sandbox create --name demo komutunu çalıştırarak demo ortamı oluşturabilirsin.

- **Kimin için:** Yapay zekâ ajanlarını güvenli ve izole bir ortamda bütün sistem kaynaklarına tam yetki vermeden çalıştırmak isteyen geliştiriciler. 
- **Lisans:** Apache-2.0 

## Bağlantılar
- [GitHub deposu →](https://github.com/NVIDIA/OpenShell)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-09-29 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Sandbox Runtime Rust Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/openshell/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
