#!/usr/bin/env python3
"""
TreScout Sözlük · per-term OG kart üreticisi (YEREL araç · Pillow + font gerektirir).
Manifest'teki kartı eksik her terim için 1200x630 marka kartı üretir ve o terimin
sayfasındaki og:image/twitter:image'ı og-default'tan kendi kartına çevirir.
Idempotent (var olan kartı atlar) · CI'da da güvenli (font yoksa 0 ile çıkar).
Kullanım: python3 scripts/dict-cards.py
Font: SF Pro (macOS) → yoksa DejaVu (Linux/CI) → yoksa atlar.
"""
import os, json, glob
from PIL import Image, ImageDraw, ImageFont
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OG=os.path.join(ROOT,"assets","dictionary","og"); os.makedirs(OG,exist_ok=True)
DICT=os.path.join(ROOT,"dictionary")
MAN=os.path.join(ROOT,"assets","dictionary","dictionary.json")
CAT_TR={"ai":"Yapay Zekâ","dev":"Geliştirme","data":"Veri & Altyapı"}
FONT=next((p for p in ["/System/Library/Fonts/SFNS.ttf","/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"] if os.path.exists(p)),None)
if not FONT: print("Font yok (SF Pro/DejaVu) · kart üretilemiyor."); raise SystemExit(0)
W,H=1200,630; PAD=76
NAVY=(27,73,101); YELLOW=(244,211,94); BLUE=(95,168,211); WHITE=(255,255,255); LIGHT=(205,218,229)
BG_TOP=(19,44,67); BG_BOT=(9,17,28)
def f(s,w=400):
    x=ImageFont.truetype(FONT,s)
    try: x.set_variation_by_axes([100,max(17,min(96,s)),400,w])
    except Exception: pass
    return x
def wrap(d,t,fn,mw,ml):
    ws=t.split(); ls=[]; c=""
    for w in ws:
        x=(c+" "+w).strip()
        if d.textlength(x,font=fn)<=mw: c=x
        else:
            if c: ls.append(c)
            c=w
            if len(ls)==ml: break
    if c and len(ls)<ml: ls.append(c)
    return ls
def card(e,out):
    img=Image.new("RGB",(W,H),BG_BOT); d=ImageDraw.Draw(img,"RGBA")
    for yy in range(H): d.line([(0,yy),(W,yy)],fill=tuple(int(BG_TOP[i]+(BG_BOT[i]-BG_TOP[i])*(yy/H)) for i in range(3)))
    for r in (520,400,280,160): d.arc([W-260-r,H-40-r,W-260+r,H-40+r],180,360,fill=(95,168,211,28),width=3)
    k=52/100.0; x=y=PAD
    d.rounded_rectangle([x,y,x+52,y+52],radius=int(22*k),fill=NAVY)
    for r in (30,20,10):
        rr=r*k; cx,cy=x+50*k,y+56*k; d.arc([cx-rr,cy-rr,cx+rr,cy+rr],180,360,fill=BLUE,width=2)
    d.rounded_rectangle([x+20*k,y+56*k,x+80*k,y+67*k],radius=2,fill=YELLOW)
    d.rounded_rectangle([x+44.5*k,y+56*k,x+55.5*k,y+84*k],radius=2,fill=YELLOW)
    d.text((PAD+68,PAD+8),"TreScout",font=f(30,700),fill=WHITE)
    d.text((PAD,PAD+78),("SÖZLÜK · "+CAT_TR.get(e["cat"],"")).upper(),font=f(20,700),fill=YELLOW)
    tf=f(66,800); tl=wrap(d,e["en"]+" nedir?",tf,W-2*PAD,2)
    for i,ln in enumerate(tl): d.text((PAD,PAD+128+i*76),ln,font=tf,fill=WHITE)
    gy=PAD+128+len(tl)*76+6
    for ln in wrap(d,e["kisa"],f(28,400),W-2*PAD,3): d.text((PAD,gy),ln,font=f(28,400),fill=LIGHT); gy+=40
    d.text((PAD,H-PAD-30),e["full"] if e.get("full") else "TreScout Teknoloji Sözlüğü",font=f(24,500),fill=BLUE)
    img.save(out,"WEBP",quality=86,method=6)

man=json.load(open(MAN,encoding="utf-8"))
n=0
for e in man:
    out=os.path.join(OG,e["slug"]+".webp")
    if os.path.exists(out): continue
    card(e,out)
    # sayfanın og/twitter görselini og-default'tan kendi kartına çevir
    p=os.path.join(DICT,e["slug"],"index.html")
    if os.path.exists(p):
        t=open(p,encoding="utf-8").read()
        t=t.replace("https://trescout.com/assets/dictionary/og-default.webp",f"https://trescout.com/assets/dictionary/og/{e['slug']}.webp")
        open(p,"w",encoding="utf-8").write(t)
    n+=1; print("  kart:",e["slug"])
print(f"✅ {n} yeni kart üretildi (font: {os.path.basename(FONT)})")
