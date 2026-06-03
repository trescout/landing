#!/usr/bin/env python3
"""
Keşif ↔ Sözlük çapraz-link · REFRESH (yeniden örer)
===================================================
Her çalıştırmada mevcut çapraz-link bölümlerini kaldırıp GÜNCEL terim/repo listesiyle
yeniden ekler → oto-büyüme (dict-sync / discover-sync) sonrası graf bayatlamaz.

- Keşif entry'lerine: "İlgili sözlük terimleri" (içerikte geçen sözlük terimleri → /dictionary/)
- Sözlük sayfalarına: "İlgili araçlar" (o terimi kullanan keşif araçları → /discover/)

Action sırası: dict-sync → discover-sync → cross-link → guard → commit.
Kullanım: python3 scripts/cross-link.py
"""
import os, re, glob, json, html
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DISC=os.path.join(ROOT,"discover"); DICT=os.path.join(ROOT,"dictionary")
def esc(s): return html.escape(s,quote=True)

man=json.load(open(os.path.join(ROOT,"assets","dictionary","dictionary.json"),encoding="utf-8"))
EN={t["slug"]:t["en"] for t in man}
cat=json.load(open(os.path.join(ROOT,"assets","discover","catalog.json"),encoding="utf-8"))
DTITLE={c["slug"]:c["title"] for c in cat}; DSTARS={c["slug"]:c.get("stars",0) for c in cat}

ALIAS={"open-source":["açık kaynak"],"artificial-intelligence":["yapay zekâ","yapay zeka"],"llm":["büyük dil model"],
 "web-scraping":["web kazıma","veri kazıma"],"voice-cloning":["ses klonla"],"text-to-speech":["metinden konuşma","seslendirme"],
 "knowledge-graph":["bilgi grafiği"],"vector-database":["vektör veritabanı"],"self-hosting":["kendi sunucu","self-host"],
 "machine-learning":["makine öğren"],"jupyter-notebooks":["jupyter"]}
def pats(t):
    ps=[t["en"]]
    if t.get("full") and re.match(r'^[A-Za-z0-9 .\-]+$',t["full"]) and len(t["full"])>3: ps.append(t["full"])
    return ps+ALIAS.get(t["slug"],[])
def rx(p):
    acr=p.isupper() and len(p)<=5
    return re.compile(r'(?<![\w-])'+re.escape(p)+r'(?![\w-])', 0 if acr else re.I)
TERMS=[(t["slug"],[rx(p) for p in pats(t)]) for t in man]

# mevcut bölümleri kaldır (refresh)
RE_DICTTERMS=re.compile(r'<section class="disc-sec"><h2>İlgili sözlük terimleri</h2>.*?</section>\n?',re.S)
RE_TOOLS=re.compile(r'<section class="disc-sec"><h2>İlgili araçlar</h2>.*?</section>\n?',re.S)

def prose(t):
    t=re.sub(r'(?s)<(script|style|nav|footer|form)\b.*?</\1>',' ',t)
    t=re.sub(r'(?s)<aside class="disc-cta">.*?</aside>',' ',t)
    b=re.search(r'(?s)<article class="disc">(.*?)</article>',t); t=b.group(1) if b else t
    t=re.sub(r'(?s)<(code|pre)\b.*?</\1>',' ',t)
    return html.unescape(re.sub(r'<[^>]+>',' ',t))

# 1) keşif entry'leri: önce sözlük-terim bölümünü kaldır, sonra prose'dan eşleştir
ent_terms={}; term_ents={}
disc_files=glob.glob(DISC+"/*/index.html")
for f in disc_files:
    slug=f.split("/discover/")[1].split("/")[0]
    t=open(f,encoding="utf-8").read()
    t=RE_DICTTERMS.sub('',t)   # eski bölümü kaldır
    open(f,"w",encoding="utf-8").write(t)  # temiz hâli yaz (sonra ekleyeceğiz)
    hits=[ts for ts,rxs in TERMS if any(r.search(prose(t)) for r in rxs)]
    ent_terms[slug]=hits
    for h in hits: term_ents.setdefault(h,[]).append(slug)
freq={t:len(e) for t,e in term_ents.items()}

# yeni sözlük-terim bölümlerini ekle (özgül önce, cap 6)
n_disc=0
for slug,hits in ent_terms.items():
    if not hits: continue
    f=DISC+"/"+slug+"/index.html"; t=open(f,encoding="utf-8").read()
    ordered=sorted(hits,key=lambda h:freq.get(h,0))[:6]
    chips="".join(f'<a href="/dictionary/{h}/">{esc(EN[h])}</a>' for h in ordered if h in EN)
    sec=f'<section class="disc-sec"><h2>İlgili sözlük terimleri</h2><div class="disc-related">{chips}</div></section>\n      '
    if '<aside class="disc-cta">' in t:
        t=t.replace('<aside class="disc-cta">',sec+'<aside class="disc-cta">',1); open(f,"w",encoding="utf-8").write(t); n_disc+=1

# 2) sözlük sayfaları: eski "İlgili araçlar"ı kaldır, güncel listeyle ekle (yıldıza göre, cap 8)
n_dict=0
for tslug in EN:
    f=DICT+"/"+tslug+"/index.html"
    if not os.path.exists(f): continue
    t=open(f,encoding="utf-8").read()
    t=RE_TOOLS.sub('',t)
    ents=term_ents.get(tslug,[])
    if ents:
        ordered=sorted(set(ents),key=lambda e:-DSTARS.get(e,0))[:8]
        chips="".join(f'<a href="/discover/{e}/">{esc(DTITLE.get(e,e))}</a>' for e in ordered)
        sec=f'<section class="disc-sec"><h2>İlgili araçlar</h2><div class="dict-related">{chips}</div></section>\n'
        if '<aside class="disc-cta">' in t:
            t=t.replace('<aside class="disc-cta">',sec+'<aside class="disc-cta">',1); n_dict+=1
    open(f,"w",encoding="utf-8").write(t)

print(f"çapraz-link yenilendi · keşif→sözlük: {n_disc} entry · sözlük→araç: {n_dict} sayfa")
