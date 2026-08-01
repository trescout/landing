# Yapay zekâ ajanları için bilgisayar kontrolü

CUA, bilgisayar kullanım yeteneğine sahip yapay zekâ ajanları için açık kaynaklı bir altyapı sunuyor. Masaüstü işletim sistemlerini kontrol edebilen ajanların eğitimi ve değerlendirilmesi amacıyla kum havuzu (sandbox), yazılım geliştirme kiti (SDK) ve kıyaslama (benchmark) araçlarını tek bir çatı altında topluyor.

- ★ 18.298
- HTML
- GitHub Trending · 2026-06-16

## Ne kazandırır?
- Masaüstü uygulamalarını arka planda kontrol etme
- Farklı işletim sistemleri için izole kum havuzları
- Ajan performansını ölçmek için kıyaslama araçları

## Kurulum

**Sürücü kurulumu (macOS/Linux)**

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/cua-driver/scripts/install.sh)"
```

**Sandbox SDK kurulumu**

```
pip install cua
```

## Çalıştırma

**macOS sanal makine başlatma**

```
# Install Lume
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/lume/scripts/install.sh)"

# Pull & start a macOS VM
lume run macos-sequoia-vanilla:latest
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
CUA altyapısını kullanarak bir bilgisayar kullanım ajanı geliştirmek istiyorum. Ajanımın masaüstü uygulamalarıyla arka planda etkileşime girmesini, fare tıklamaları yapmasını ve klavye girdileri göndermesini sağlayacak temel Python yapısını kurmama yardımcı ol. CUA Sandbox SDK kullanarak bir Linux ortamında komut çalıştıran ve ekran görüntüsü alan örnek bir kod taslağı oluştur.

- **Kimin için:** Bilgisayar üzerinde otonom görevler gerçekleştiren yapay zekâ ajanları geliştiren yazılımcılar ve araştırmacılar için uygundur. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/trycua/cua)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-06-16 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Benchmark Sandbox SDK Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/cua/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
