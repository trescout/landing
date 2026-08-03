# Özyinelemeli yapay zekâ modelleri için altyapı

Özyinelemeli dil modelleri (Recursive Language Models) için geliştirilen rlm, farklı çalışma ortamlarını (sandboxes) destekleyen tak-çalıştır bir çıkarım kütüphanesidir. Python tabanlı bu araç, karmaşık dil modeli süreçlerini standartlaştırarak farklı sistemlere entegre edilmesini kolaylaştırır.

- ★ 5.343
- Python
- GitHub Trending · 2026-06-18

## Güncelleme
- 2 Ağustos 2026: Yıldız 4.987 → 5.343, son sürüm v0.1.3 (26 Haziran 2026).

## Ne kazandırır?
- Sonsuz uzunlukta bağlam yönetimi
- Kod ortamında çalışan tak-çalıştır mimari
- Farklı sandbox ortamları ile güvenli entegrasyon

## Kurulum

**Hızlı kurulum**

```
pip install rlms
```

**Manuel kurulum**

```
curl -LsSf https://astral.sh/uv/install.sh | sh
uv init && uv venv --python 3.12 # change version as needed
uv pip install -e .
```

## Çalıştırma

**Hızlı test çalıştırma**

```
make quickstart
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
RLM kütüphanesini kullanarak dil modelinin girdiyi parçalara ayırmasını, analiz etmesini ve kendi içinde özyinelemeli çağrılar yapmasını sağlayan bir yapı kur. RLM sınıfını başlatırken backend olarak kullandığın modelin yapılandırmasını tanımla ve karmaşık görevlerin çözümünde modelin kod ortamıyla etkileşime geçmesine izin ver.

- **Kimin için:** Karmaşık dil modeli süreçlerini standartlaştırmak ve özyinelemeli model çağrıları ile çalışmak isteyen geliştiriciler içindir. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/alexzhang13/rlm)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-06-18 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Sandbox Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/rlm/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
