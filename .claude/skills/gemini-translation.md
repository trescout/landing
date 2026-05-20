---
name: gemini-translation
description: Türkçe doğal dil üretimi her zaman Gemini'den geçer. Doğrudan Claude çıktısını kullanıcı-yüzü metin olarak yayınlama.
trigger: Marketing copy, e-posta, rapor metni, landing içeriği, kullanıcı-yüzü Türkçe metin üretiliyorken
applies-to:
  - "**/*.md"
  - "**/*.tsx"
  - "**/*.jsx"
  - "**/*.html"
  - "**/*.ts"
  - "**/*.js"
---

# Skill · Gemini Translation

## Ne zaman aktif

Kullanıcı-yüzü Türkçe metin üretiliyor: hero copy, e-posta, rapor içeriği, terim tanımları, landing copy, blog yazısı. `AGENTS.md §2` (KRİTİK) zorunluluğu.

## Procedure

1. **Taslakla** · Claude olarak Türkçe metni taslakla, ama bunun Gemini'den geçirileceğini biliyor ol
2. **Gemini'ye ilet** · MCP server bağlıysa `.mcp.json`'daki gemini server'ı kullan; yoksa geliştiriciye "Bu metni Gemini'den geçirin: 'Bu metni daha doğal Türkçeye çevir, marka sesi siz formal, em dash kullanma'" mesajı bırak
3. **Gemini çıktısını al**
4. **Claude denetimi** · marka kuralları kontrolü (`brand-voice-check` skill'ini çağır):
   - "siz" formal Türkçe
   - Em dash (—) yok
   - TreScout casing doğru
   - TDK noktalama
   - Mantık tutarlılığı
5. **PR'da işaretle** · AI Traceability bölümünde:
   - [ ] Gemini'den geçti
   - [ ] Claude denetiminden geçti

## İyi örnek

**Kötü (Claude doğrudan):** "Bugün dünya teknoloji konusunda büyük bir adım attı."

**İyi (Gemini'den geçmiş):** "Bugünün ekseni yapay zekâ ajanları (AI agents): hem yetenek paketleri (skills) hem de güvenli bellek mimarisi üzerine yoğun yayın var."

## İstisnalar · Claude doğrudan yazabilir

- Kısa kod yorumu (`// kullanıcı saatini IANA formatında tutuyoruz`)
- Git commit mesajı
- Dahili teknik tartışma / brainstorm
- TypeScript/Python tip tanımı, interface
- İngilizce çıktı (Claude İngilizcede güçlü)

## Anti-patterns

- ❌ Doğrudan Claude'dan Türkçe metin alıp commit etmek
- ❌ "TreScout olarak..." veya "Biz olarak..." cümle başlangıçları
- ❌ Em dash (—, –) kullanmak
- ❌ "sen" informal hitabı
- ❌ "Şekillendiren", "ayak izi bırakan", "yepyeni" gibi pazarlama dolgu

## Detay

- `AGENTS.md §2` · "Türkçe içerik kuralı (KRİTİK)"
- `AGENTS.md §4` · pratik kullanım rehberi (Claude Code / Cursor / Antigravity)
- Gerekçe: Claude'un Türkçesi akademik/çevrilmiş hissi veriyor, Gemini akıcılığı belirgin önde.
