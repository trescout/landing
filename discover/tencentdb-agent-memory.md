# Yapay zekâ ajanları için katmanlı bellek

TencentDB Agent Memory, yapay zekâ ajanları için dört aşamalı bir süreçle tamamen yerel uzun süreli bellek (long-term memory) çözümü sunuyor. Dış kaynaklı uygulama programlama arayüzlerine (API) ihtiyaç duymadan veri saklama ve geri çağırma işlemlerini gerçekleştiriyor.

- ★ 20.021
- TypeScript
- GitHub Trending · 2026-07-09

## Güncelleme
- 12 Ağustos 2026: Yıldız 18.953 → 20.021, son sürüm v2.0.0 (3 Ağustos 2026).
- 10 Ağustos 2026: Yıldız 17.887 → 18.953, son sürüm v2.0.0 (3 Ağustos 2026).
- 8 Ağustos 2026: Yıldız 16.699 → 17.887, son sürüm v2.0.0 (3 Ağustos 2026).
- 7 Ağustos 2026: Yıldız 15.363 → 16.699, son sürüm v2.0.0 (3 Ağustos 2026).

## Ne kazandırır?
- Token kullanımını %61'e varan oranda düşürür
- Karmaşık görevlerde başarı oranını artırır
- Verileri sembolik ve katmanlı yapıda saklar

## Kurulum

**Paket kurulumu**

```
mkdir -p ~/.memory-tencentdb
TEMP_DIR=$(mktemp -d)
cd "$TEMP_DIR"
npm init -y --silent
npm install @tencentdb-agent-memory/memory-tencentdb@latest --omit=dev
cp -r node_modules/@tencentdb-agent-memory/memory-tencentdb \
~/.memory-tencentdb/tdai-memory-openclaw-plugin
rm -rf "$TEMP_DIR"
```

**Bağımlılıkları yükleme**

```
cd ~/.memory-tencentdb/tdai-memory-openclaw-plugin
npm install --omit=dev
npm install tsx
```

## Çalıştırma

**Sunucuyu başlatma**

```
cd ~/.memory-tencentdb/tdai-memory-openclaw-plugin
npx tsx src/gateway/server.ts
```

**Bağlantıyı doğrulama**

```
curl http://127.0.0.1:8420/health
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
TencentDB Agent Memory kullanarak yapay zekâ ajanımın uzun süreli hafızasını yapılandır. Verileri düz bir vektör yığını yerine, kısa süreli görevler için sembolik Mermaid grafiklerini ve uzun süreli deneyimler için L0-L3 arası katmanlı bellek piramidini kullan. Ajanın geçmiş konuşmaları, atomik gerçekleri ve kullanıcı tercihlerini bu hiyerarşik yapıda saklamasını ve ihtiyaç anında node_id üzerinden tam izlenebilirlik ile geri çağırmasını sağla.

- **Kimin için:** Yapay zekâ ajanlarının bağlamı unutmasını istemeyen ve token maliyetlerini düşürerek daha tutarlı sonuçlar almayı hedefleyen geliştiriciler içindir. 

## Bağlantılar
- [GitHub deposu →](https://github.com/TencentCloud/TencentDB-Agent-Memory)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-07-09 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Long-term Memory Memory Token Agent API Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/tencentdb-agent-memory/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
