# Antigravity için otonom yapay zekâ kiti

Ag-kit, TypeScript tabanlı projelerde otonom yapay zekâ ajanları (AI agents) oluşturmak için gerekli araçları ve yapıları sunan bir geliştirme kütüphanesidir. Geliştiricilerin karmaşık iş akışlarını yönetebilen ajan sistemlerini (agentic systems) hızlıca tasarlamasına olanak tanır.

- ★ 8.084
- TypeScript
- GitHub Trending · 2026-07-28

## Güncelleme
- 2 Ağustos 2026: Yıldız 8.020 → 8.084, son sürüm v2026.7.27 (26 Temmuz 2026).

## Ne kazandırır?
- 20 farklı uzman yapay zekâ rolü
- Güvenli komut çalıştırma denetimi
- Kalıcı hafıza ve iş akışı yönetimi

## Kurulum

**Projeye kurulum**

```
npx @vudovn/ag-kit init
```

**Küresel kurulum**

```
npm install -g @vudovn/ag-kit
ag-kit init
```

## Çalıştırma

**Çalışma alanı doğrulaması**

```
npm run check:agents
npm run check:antigravity
npm run test:antigravity
```

**Güvenlik kancasını test etme**

```
printf '%s' '{"tool_args":{"CommandLine":"rm -rf /"}}' \
| node .agents/hooks/validate-tool-call.mjs
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Bu projede Antigravity çalışma alanı kurdum ve AG Kit araçlarını aktif ettim. Proje dizinindeki .agents/ klasöründe tanımlı kuralları, uzman ajan rollerini ve iş akışlarını kullanarak görevlerimi yönetmeni istiyorum. Güvenlik kancasının aktif olduğundan emin ol ve karmaşık iş akışlarını /coordinate veya /orchestrate komutlarıyla planlayarak ilerle.

- **Kimin için:** TypeScript tabanlı projelerinde Antigravity çalışma alanı kullanan ve otonom ajan sistemleri geliştirmek isteyen yazılımcılar içindir. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/vudovn/ag-kit)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-07-28 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Agentic Systems Agentic AI Agents Agents Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/ag-kit/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
