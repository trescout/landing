#!/usr/bin/env python3
"""
TreScout Keşif · .md endpoint üreteci (LLM/AI için temiz markdown)
=================================================================
Her discover/<slug>/index.html sayfasından discover/<slug>.md üretir (HTML'den
türetir → küratörlü + oto-eklenen TÜM entry'leri kapsar) ve sayfaya
rel="alternate" text/markdown linkini ekler. Sözlük .md'leriyle simetri sağlar
→ AI'a hizmet katmanı her keşif sayfasında tam.

Action'da cross-link'ten sonra çalışır · idempotent (içerik değişmezse .md değişmez).
Kullanım: python3 scripts/discover-md.py
"""
import os, re, glob, html as H
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DISC = os.path.join(ROOT, "discover")

def txt(s):
    return re.sub(r'[ \t]+', ' ', H.unescape(re.sub(r'<[^>]+>', ' ', s or ''))).strip()

def linktxt(s):
    # <a href>metin</a> → [metin](href), sonra kalan etiketleri at
    s = re.sub(r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', lambda m: f'[{txt(m.group(2))}]({m.group(1)})', s, flags=re.S)
    return txt(s)

def page_md(t, canon):
    m = re.search(r'<article class="disc">(.*?)</article>', t, re.S)
    if not m:
        return None
    s = m.group(1)
    # gürültüyü çıkar: geri linki, eyebrow, CTA/form, save şeridi
    for pat in [r'<a class="disc-back".*?</a>', r'<div class="disc-top">.*?</div>',
                r'<aside class="disc-cta">.*?</aside>', r'<aside class="disc-save">.*?</aside>']:
        s = re.sub(pat, '', s, flags=re.S)
    # ekran görüntüsü → figcaption'ı italik not olarak koru
    s = re.sub(r'<figure class="disc-shot">.*?<figcaption>(.*?)</figcaption>\s*</figure>',
               lambda x: f'\n_{txt(x.group(1))}_\n', s, flags=re.S)
    s = re.sub(r'<button[^>]*>.*?</button>', '', s, flags=re.S)
    # komut başlığı (disc-cmd-head span) → kalın satır
    s = re.sub(r'<div class="disc-cmd-head"><span>(.*?)</span>.*?</div>', lambda x: f'\n**{txt(x.group(1))}**\n', s, flags=re.S)
    # başlıklar
    s = re.sub(r'<h1[^>]*>(.*?)</h1>', lambda x: f'# {txt(x.group(1))}\n', s, flags=re.S)
    s = re.sub(r'<h2[^>]*>(.*?)</h2>', lambda x: f'\n## {txt(x.group(1))}\n', s, flags=re.S)
    # kod blokları (birebir)
    s = re.sub(r'<pre><code>(.*?)</code></pre>', lambda x: f'\n```\n{H.unescape(x.group(1)).strip()}\n```\n', s, flags=re.S)
    # facts (k:v)
    s = re.sub(r'<span class="disc-fact-k">(.*?)</span><span class="disc-fact-v">(.*?)</span>',
               lambda x: f'\n- **{txt(x.group(1))}:** {txt(x.group(2))}', s, flags=re.S)
    # liste + paragraf (linkleri koru)
    s = re.sub(r'<li>(.*?)</li>', lambda x: f'- {linktxt(x.group(1))}\n', s, flags=re.S)
    s = re.sub(r'<p[^>]*>(.*?)</p>', lambda x: f'\n{linktxt(x.group(1))}\n', s, flags=re.S)
    s = re.sub(r'<div class="disc-note">(.*?)</div>', lambda x: f'\n{linktxt(x.group(1))}\n', s, flags=re.S)
    # kalan tüm etiketleri temizle
    s = H.unescape(re.sub(r'<[^>]+>', ' ', s))
    s = re.sub(r'[ \t]+', ' ', s)
    s = re.sub(r'\n[ \t]+', '\n', s)
    s = re.sub(r'\n{3,}', '\n\n', s).strip()
    return s + f"\n\n---\nKaynak: TreScout Keşif · {canon}\nTreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.\n"

def main():
    n_md = n_link = 0
    for f in sorted(glob.glob(DISC + "/*/index.html")):
        slug = f.split("/discover/")[1].split("/")[0]
        t = open(f, encoding="utf-8").read()
        canon = f"https://trescout.com/discover/{slug}/"
        md = page_md(t, canon)
        if not md:
            continue
        mdpath = os.path.join(DISC, slug + ".md")
        old = open(mdpath, encoding="utf-8").read() if os.path.exists(mdpath) else None
        if md != old:
            open(mdpath, "w", encoding="utf-8").write(md); n_md += 1
        # sayfaya rel=alternate ekle (yoksa)
        if 'type="text/markdown"' not in t:
            link = f'<link rel="alternate" type="text/markdown" href="/discover/{slug}.md">\n'
            t = t.replace('<link rel="canonical"', link + '<link rel="canonical"', 1)
            open(f, "w", encoding="utf-8").write(t); n_link += 1
    print(f"discover .md: {n_md} yazıldı/güncellendi · rel=alternate: {n_link} sayfaya eklendi")

if __name__ == "__main__":
    main()
