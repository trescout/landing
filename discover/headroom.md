# Headroom

Headroom, büyük dil modellerine (LLM) gönderilen günlük dosyalarını, araç çıktılarını ve bağlamsal veri parçalarını (RAG chunks) sıkıştırarak jeton (token) kullanımını %60 ile %95 oranında azaltıyor. Python tabanlı bu araç, kütüphane, vekil sunucu (proxy) ve Model Bağlam Protokolü (MCP) sunucusu olarak farklı entegrasyon seçenekleri sunuyor.

- ★ 7.746
- GitHub Trending · 2026-06-03

## Ne kazandırır?
- Jeton kullanımını %60 ile %95 oranında azaltır.
- Verileri yerel olarak sıkıştırarak gizliliği korur.
- Orijinal verileri kaybetmeden geri çağrılabilir sıkıştırma sağlar.

## Kurulum

**Paket Kurulumu**

```
pip install "headroom-ai[all]" # Python
npm install headroom-ai # Node / TypeScript
```

## Çalıştırma

**Mod Seçimi ve Başlatma**

```
headroom wrap claude # wrap a coding agent
headroom proxy --port 8787 # drop-in proxy, zero code changes
```

**Performans Kontrolü**

```
headroom perf
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Headroom aracını kullanarak yapay zeka ajanımın bağlamsal veri ve günlük dosyası tüketimini optimize etmek istiyorum. Python ortamında "pip install "headroom-ai[all]"" komutuyla kurulumu tamamladım. Ajanımın kullandığı jeton miktarını düşürmek için "headroom wrap claude" veya "headroom proxy --port 8787" komutlarını nasıl yapılandırmalıyım? Ayrıca "headroom perf" komutu ile elde ettiğim tasarruf verilerini nasıl yorumlamalıyım?

- **Kimin için:** Günlük olarak yapay zeka kodlama ajanları kullanan ve jeton maliyetlerini düşürmek isteyen yazılımcılar için uygundur. 
- **Lisans:** Apache-2.0 

## Bağlantılar
- [GitHub deposu →](https://github.com/chopratejas/headroom)

## İlgili sözlük terimleri
RAG Chunks Proxy Token MCP RAG LLM 

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Yıldız ve sayılar keşif tarihindeki değerlerdir.

---
Kaynak: TreScout Keşif · https://trescout.com/discover/headroom/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
