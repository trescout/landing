# AGENTS.md · TreScout Org AI Çalışma Kuralları

> Bu dosya bu repoya kod, içerik veya doküman katkısı yapan **insanlar ve onların kullandığı AI ajanları** için kanonik kuraldır. Hangi araç kullanılırsa kullanılsın (Claude Code, Antigravity, Cursor, Continue, manual editing, ChatGPT yardımı), bu dosyadaki kurallar geçerli.
>
> Diğer AI araç-spesifik dosyalar (`CLAUDE.md`, `.cursorrules`, `.continue/config.json` vb.) bu dosyaya referans verir, içeriği tekrarlamaz.

**Versiyon:** 1.0  
**Son güncelleme:** 2026-05-09

---

## 1. Genel ilke

> **Her AI'ın güçlü olduğu iş farklı. TreScout'ta hangi işi hangi AI yapacağını yöneten bir router var. Bu kural sadece ürünün backend'i için değil; bu repoya katkı yapan herkesin AI kullanımı için geçerli.**

Tek bir LLM her şeyde iyi değil. Yaygın gözlem:
- **Kod yazımı, akıl yürütme, denetim:** Claude
- **Türkçe doğal dil, marketing copy, doküman üslubu:** Gemini
- **Hızlı sınıflandırma, structured output, veri etiketleme:** Cerebras

Bu projede üretilen her parça (kod, açıklama, marketing) bu üç başlıktan birine düşer. Dolayısıyla **görev başına model** seçimi standart pratik.

---

## 2. Türkçe içerik kuralı (KRİTİK)

**Türkçe doğal dil üretimi → her zaman Gemini'den geçer.**

Şuna dokunan her metin Gemini ile üretilir veya Gemini'den geçer:
- Marketing copy (landing page, e-postalar, tagline)
- Kullanıcı-yüzü içerik (rapor metinleri, "Birkaç Yudum" editöryel, terim tanımları)
- Türkçe dokümantasyon (README, blog yazıları, changelog Türkçe versiyonu)
- Kod yorumlarındaki Türkçe açıklamalar (uzun olanlar)

**Gerekçe:** Claude'un Türkçesi akademik, çevrilmiş hissi veriyor. Gemini'nin Türkçe akıcılığı belirgin şekilde önde (NotebookLM testlerinde de doğrulandı). Marka sesimiz "siz, sıcak ama profesyonel"; bunu en iyi taşıyan model Gemini.

**İstisnalar (Claude doğrudan yazabilir):**
- Kısa kod yorumu (`// kullanıcı saatini IANA formatında tutuyoruz`)
- Git commit mesajı
- Dahili teknik tartışma / brainstorm
- İngilizce çıktı (Claude İngilizcede güçlü)

---

## 3. AI rolleri (Plan / Skills / Denetim)

Tek bir LLM çağrısı her şeye uygun değil. Ne yaptığını **bilinçli adlandırınca** daha iyi sonuç çıkıyor. Bunlar ayrı LLM oturumu olmak zorunda değil · aynı Claude Code session'ında "şimdi planlıyoruz" / "şimdi uzmana soruyoruz" demek yetiyor.

### 3.a. Plan moment'i · "ne yapacağız, niye?"

Mimari, scope, kabul kriteri, sprint kararı.

Landing örnekleri:
- "Tally form'u nereye koyalım, hangi alanları soralım, başarı metriği ne?"
- "Bu sprint hero copy'yi mi değiştirsek yoksa form akışını mı?"
- "Sample report'u landing'e mi gömelim yoksa ayrı PDF mi?"

Çıktı: `AGENTS.md` / `README.md` güncellemesi, GitHub Issue açıklaması, sprint notu.

### 3.b. Skills moment'i · "şu spesifik şeyi uzman gibi nasıl yaparız?"

Uzmanlık gerektiren teknik konularda, "uzman yazılımcıya soruyormuş gibi" sor. Landing örnekleri:
- Tally form embed + spam koruması
- OG image kompozisyonu (1200×630)
- LCP / CLS performans optimizasyonu
- Erişilebilirlik audit (a11y)
- SEO meta tag stratejisi
- Vercel cache / security header'ları

Çıktı: somut kod / değişiklik, PR'a eklenir.

### 3.c. Claude · denetimci

Plan ve Skills çıktıları (ve Gemini Türkçe metni) Claude denetiminden geçer:

1. Gemini Türkçe metni üretir (Türkçe iş ise)
2. Claude marka kuralları (siz/sen, em dash, TreScout casing, TDK noktalama, mantık tutarlılığı) açısından kontrol eder
3. Gerekirse düzeltir veya Gemini'den / Skills'ten revize ister
4. İnsan reviewer (Burhan) merge'den önce son okur

**Sonuç:** Plan'ı bilinçli yapıyoruz, Skills'i uzman gibi sorabiliyoruz, Türkçe akıcılığını Gemini'den, marka tutarlılığını Claude'dan alıyoruz.

---

## 4. Pratik kullanım · geliştirici için

### 4.a. Claude Code kullanıyorsanız

Claude Code'a şöyle deyin:

> "Bu landing page'in hero metnini Türkçe yaz. Marka sesi 'siz, formal'. Gemini'den taslak istemek için MCP/tool varsa kullan; yoksa taslağı kendin yaz ama Türkçe akıcılık konusunda kritik kal; gerekirse 2-3 alternatif üret."

Claude Code (eğer Gemini MCP server bağlıysa) doğrudan Gemini'ye delegate eder. Yoksa Claude kendi yazar; siz çıktıyı Gemini'de revize edip geri yapıştırırsınız.

### 4.b. Antigravity / Cursor / başka AI kullanıyorsanız

Sıralama:
1. AI'ya Türkçe içerik yazdırın
2. **Çıktıyı Gemini'ye yapıştırın** ("Bu metni daha doğal Türkçeye çevir; marka sesi siz, formal, em dash kullanma")
3. Gemini'nin çıktısını PR'a koyun
4. Reviewer (Burhan) Claude ile son denetimden geçirir

### 4.c. AI kullanmıyorsanız

Düz yazıyorsanız zaten sorun yok. Sadece BRAND.md §5.5'teki Türkçe kurallarını izleyin.

---

## 5. Diğer AI araçlarının görmesi için

Bu repoya bağlanan AI araçları farklı dosyalar okuyor. Her birinde **bu AGENTS.md'ye yönlendirme** var:

| Araç | Dosya | İçerik |
|---|---|---|
| Claude Code | `CLAUDE.md` | "Tüm kurallar için → AGENTS.md" |
| Cursor | `.cursorrules` | "See AGENTS.md" |
| Continue.dev | `.continue/config.json` | systemMessage'da AGENTS.md referansı |
| Antigravity | (henüz standardı yok) | README'de manuel açıklama |

Yeni bir AI aracı ekleyen kişi, bu tabloya satır ekler ve o aracın config dosyasında AGENTS.md'ye referans bırakır.

---

## 6. Marka kuralları (özet)

Tam liste için `docs/BRAND.md`. Buradaki sadece en sık ihlal edilenler:

### Voice
- ✅ "Siz" formal Türkçe (her zaman)
- ❌ "sen" (informal, kullanılmaz)

### Noktalama
- ❌ Em dash (`—`) Türkçede yok. Yerine `,` `.` `:` `;` veya `·`
- ❌ ", ama" virgülü (Türkçede ama'dan önce virgül yok)
- ✅ "..." sonrası **büyük harf** ile devam
- ✅ ":" sonrası tam cümle gelirse **büyük harf**
- ✅ Tırnak içi tam cümle ise nokta **içeride**, ifade ise nokta **dışarıda**

### Marka adı
- ✅ **TreScout** (Title Case, T ve S büyük)
- ❌ Trescout, trescout, TRESCOUT, TreSout

### Tagline (kilitli; değiştirme!)
- Hero: "Teknoloji takibi artık bir iş yükü değil."
- Mid: "TreScout tarar, özetler, gönderir. Siz sadece okursunuz."
- Sub: "GitHub, Hacker News, HuggingFace ve daha fazlası. Kendi temponuzda, istediğiniz saatte."

### Renkler
Tek kaynak: `docs/BRAND.md §3`. Hardcoded yeni renk eklemeyin; mevcut palet veya türevi kullanın.

---

## 7. PR akışı

1. Branch açın (`feat/`, `fix/`, `docs/` öneki)
2. Kod + (gerekirse) doküman güncellemesi
   - Conventional commit mesajı: `feat(<scope>): ...`, `fix(<scope>): ...`, `docs(<scope>): ...`, `chore(<scope>): ...`
   - `<scope>` parantezinde **kullanılan AI aracı**: `claude-code`, `cursor`, `antigravity`, `manual`. Örnek: `feat(claude-code): add tally form to hero`
3. Türkçe içerik varsa Gemini'den geçirin (yukarıda §2-§4)
4. PR açın · template (`.github/pull_request_template.md`) otomatik gelir, tüm bölümleri doldurun
5. Burhan Claude ile son denetim yapar, merge eder

> Repo küçük, 3 kişilik. Issue template'i yok · ad-hoc issue'lar yeterli. AI_USAGE_LOG yok · git log + commit scope audit trail için yeterli. Bu yapı `trescout/app` açıldığında o repoya göre yeniden tartılır.

---

## 8. Soru / istisna durumları

Bu kurallarda olmayan bir durum çıktıysa:
- Issue açın, etiket: `discussion / agents-rule`
- Burhan ve ekiple konuşulup karar verilir
- Karar bu dosyaya eklenir, versiyon artırılır

> Bu doküman canlı. Her yeni karar buraya yazılır, başka yerde dağılmaz.
