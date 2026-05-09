# CLAUDE.md · TreScout Landing

Bu repoda Claude Code'un (ve Cursor / Antigravity'nin) **kodlama davranışı** için kurallar. Org-wide kurallar (Türkçe/Gemini protokolü, marka, AI rolleri) `AGENTS.md`'de · burada **nasıl kod yazılır.**

> **Köken:** Andrej Karpathy'nin LLM kodlama prensiplerine dayanır, TreScout için kısaltıp landing bağlamına uyarlandı. Hackathon `trescout/trescout` repo'sunda kullanıldı, burada landing'e göre tekrar yazıldı.

**Trade-off:** Bu kurallar hızdan çok dikkat tarafına eğilir. Trivial görevde sağduyu.

---

## 1) Kodlamadan Önce Düşün

Varsayma. Kafa karışıklığını gizleme.

- Birden fazla yorum varsa hepsini sun · sessizce seçme.
- Daha basit yaklaşım varsa belirt, gerekirse karşı çık.
- Net olmayan şey varsa **dur, sor.**

Landing örneği: "CTA'yı header'a taşı" → tek CTA mı kalacak yoksa iki noktada mı? Kararı sor önce, kodu değiştirme.

## 2) Önce Basitlik

Problemi çözen minimum kod. Spekülatif hiçbir şey yok.

- Tek kullanımlık kod için soyutlama yapma.
- İstenmemiş "esneklik" / "yapılandırılabilirlik" yok.
- 200 satır yazıp 50 olabilirken yeniden yaz.

Landing örneği: Yeni feature kartı eklenecekse mevcut `.feature-card` class'ını kullan, "yeni bir card system" tasarlama.

## 3) Cerrahi Değişiklikler

Sadece dokunman gerekene dokun.

- Komşu kodu, formatlamayı "iyileştirme" yapma.
- Bozuk olmayan şeyi refactor etme.
- Mevcut stile uy, kendi tercihini dayatma.

Landing örneği: Hero metnini değiştirirken altındaki `.hero-stats` div'in formatlamasını "düzeltmeye" çalışma.

## 4) Hedef Odaklı

Başarı kriterini önceden tanımla, ona ulaşana kadar git.

- "Bug'ı düzelt" → önce bug'ı tetikleyen senaryo (Safari iOS, hangi viewport), sonra fix, sonra tekrar test.
- "Layout düzelt" → önce mevcut görsel, sonra hedef görsel, sonra değişiklik.

Çok adımlı işte kısa plan ver:
```
1. [Adım] → doğrula: [check]
2. [Adım] → doğrula: [check]
```

---

## TreScout Landing · Özel Notlar

### A) Türkçe içerik
Kullanıcı-yüzü Türkçe metin **Gemini'den geçer.** Detay → `AGENTS.md §2`.

### B) Marka
TreScout (T+S büyük), em dash yasak, "siz" formal, hero/mid/sub tagline'lar **kilitli**. Detay → `AGENTS.md §6`. Renk paleti: `trescout-brand-kit/docs/BRAND.md §3` (ayrı repo).

### C) AI rolleri
Plan moment'i (ne yapacağız), Skills moment'i (uzman gibi nasıl yapacağız), Claude denetimi. Detay → `AGENTS.md §3`.

### D) Commit
`feat(<ai-tool>): ...`. Detay → `AGENTS.md §7`.

### E) Secret
`.env`, API key, token commit etme. Vercel env var'lar Vercel dashboard'da, repo'da değil.

---

**Bu kurallar işliyor olduğunun sinyali:**
- Diff'lerde gereksiz değişiklik az
- Karmaşıklık yüzünden yeniden yazma az
- Açıklayıcı sorular **uygulamadan önce** geliyor, hatadan sonra değil
