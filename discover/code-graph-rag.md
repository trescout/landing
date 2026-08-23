# Kod deponuzu yapay zekâ ile sorgulayın

Code-graph-rag, büyük kod depolarındaki (monorepo) karmaşık yapıları anlamak ve sorgulamak için bilgi grafikleri (knowledge graphs) ile getirme destekli üretim (RAG) yöntemini birleştiriyor. Geliştiricilerin farklı dillerdeki kod tabanlarını yapay zekâ yardımıyla analiz etmelerine ve düzenlemelerine olanak tanıyor.

- ★ 4.782
- Python
- GitHub Trending · 2026-08-10

## Güncelleme
- 23 Ağustos 2026: Yıldız 4.593 → 4.782, son sürüm v0.0.720 (22 Ağustos 2026).
- 18 Ağustos 2026: Yıldız 4.359 → 4.593, son sürüm v0.0.670 (18 Ağustos 2026).
- 15 Ağustos 2026: Yıldız 3.158 → 4.359, son sürüm v0.0.639 (14 Ağustos 2026).
- 10 Ağustos 2026: Yıldız 3.153 → 3.158, son sürüm v0.0.589 (10 Ağustos 2026).

## Ne kazandırır?
- Kod tabanını bilgi grafiğine dönüştürerek karmaşık ilişkileri görün
- Doğal dilde sorular sorarak kod yapısı hakkında yanıtlar alın
- Yapısal arama ve düzenleme araçlarıyla kod üzerinde hassas değişiklikler yapın

## Kurulum

**Paket yöneticisi ile kurulum**

```
uv tool install "code-graph-rag[treesitter-full,semantic]"
```

**Alternatif kurulum yöntemi**

```
pipx install "code-graph-rag[treesitter-full,semantic]"
```

## Çalıştırma

**Veritabanını başlatma**

```
cgr daemon up
```

**Depoyu analiz etme ve sorgulama**

```
cgr start --repo-path /path/to/repo --update-graph
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Code-Graph-RAG aracını kullanarak kod depomu analiz et. Kod tabanındaki fonksiyonlar, sınıflar ve modüller arasındaki ilişkileri kullanarak sorduğum sorulara yanıt ver. Kod üzerinde yapmam gereken değişiklikleri veya optimizasyonları, aracın sağladığı yapısal analiz yeteneklerini kullanarak öner.

- **Kimin için:** Büyük ve karmaşık kod depolarındaki yapısal ilişkileri anlamak, sorgulamak ve yapay zekâ yardımıyla güvenli değişiklikler yapmak isteyen yazılımcılar içindir. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/vitali87/code-graph-rag)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-08-10 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Monorepo RAG Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/code-graph-rag/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
