# Teknik kitapları yapay zekâ yeteneğine dönüştürün

Book-to-skill projesi, teknik kitapların taşınabilir belge biçimlerini (PDF) Claude Code için kullanılabilir yetenek paketlerine (skills) dönüştürüyor. Bu araç, teknik kaynakların çalışma süreçlerinde doğrudan referans alınmasını ve uygulanmasını sağlıyor.

- ★ 11.802
- Python
- GitHub Trending · 2026-07-29

## Ne kazandırır?
- Kitapları ve belgeleri doğrudan yapay zekâ ajanınızın çalışma belleğine aktarır.
- Büyük dosyaları bölümlere ayırarak gereksiz token tüketimini engeller.
- PDF, EPUB ve Markdown gibi birçok formatı yapılandırılmış yetenek paketine çevirir.

## Kurulum

**Aracı kurma ve kontrol etme**

```
pip install "book-to-skill[pdf,epub,docx]" # engine + optional extractors
book-to-skill ~/path/to/book.pdf --mode text # or: python -m book_to_skill ...
book-to-skill --check # report which extractors are installed
```

## Çalıştırma

**Belgeyi yetenek paketine dönüştürme**

```
/book-to-skill 
... [skill-name-slug]
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın Bu teknik kaynağı bir yetenek paketi olarak kullanıyorum. Lütfen içeriği analiz ederken sadece dönüştürülen bölümlere ve yapılandırılmış dosyalara sadık kal. Bir soru sorduğumda ilgili bölümü referans alarak yanıt ver ve halüsinasyondan kaçınarak sadece belgedeki teknik bilgileri kullan.

- **Kimin için:** Teknik kitapları, dokümantasyonları veya araştırma notlarını yapay zekâ ajanları üzerinden hızlıca sorgulamak isteyen geliştiriciler ve araştırmacılar içindir. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/virgiliojr94/book-to-skill)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-07-29 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Markdown Token Skill AI Skills PDF Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/book-to-skill/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
