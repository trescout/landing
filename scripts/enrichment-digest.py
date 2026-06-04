#!/usr/bin/env python3
"""
TreScout · Aylık elle-zenginleştirme kuyruğu
============================================
catalog'daki `needs_enrichment: true` (oto-zenginleştirilemeyen lite) entry'leri
TEK bir GitHub Issue'da toplar (varsa günceller, yoksa açar). Onay kutularıyla takip.

Çalışır: GitHub Actions (aylık cron) · ortam: GH_TOKEN (Actions otomatik verir).
Yerel/tokensiz: sadece gövdeyi yazdırır (issue açmaz). Kullanım: python3 scripts/enrichment-digest.py [--dry]
"""
import os, re, sys, json, subprocess
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOG=os.path.join(ROOT,"assets","discover","catalog.json")
TITLE="🧰 Elle zenginleştirme kuyruğu (lite → en iyi)"
DRY="--dry" in sys.argv or not os.environ.get("GH_TOKEN")

def missing(slug):
    """Sayfayı okuyup eksik parçaları döner: kurulum komutu / ekran görüntüsü."""
    f=os.path.join(ROOT,"discover",slug,"index.html")
    t=open(f,encoding="utf-8").read() if os.path.exists(f) else ""
    m=[]
    if "<pre><code>" not in t: m.append("kurulum komutu")
    if 'class="disc-shot"' not in t: m.append("ekran görüntüsü")
    return m

def repo_url(slug):
    f=os.path.join(ROOT,"discover",slug,"index.html")
    if not os.path.exists(f): return ""
    t=open(f,encoding="utf-8").read()
    m=re.search(r'"codeRepository":\s*"([^"]+)"',t) or re.search(r'href="(https://github\.com/[^"]+?)"',t)
    return m.group(1) if m else ""

def main():
    cat=json.load(open(CATALOG,encoding="utf-8"))
    q=[c for c in cat if c.get("needs_enrichment")]
    if not q:
        print("kuyruk boş · işaretli entry yok · issue açılmadı."); return
    lines=["Bu liste otomatik üretildi. Aşağıdaki keşif sayfaları henüz **en iyi** seviyede değil. "
           "Her birine eksik parçayı ekleyin: gerçek kurulum komutu bulunursa, lisansı temiz ekran görüntüsü. "
           "Uygun değilse (ör. masaüstü uygulaması, komutu yok) olduğu gibi bırakın. "
           "Bitince kutucuğu işaretleyin ve kuyruktan çıkarmak için "
           "`python3 scripts/discover-sync.py --done=SLUG` çalıştırın (ya da bana söyleyin).","",
           f"Toplam: **{len(q)}** entry.",""]
    for c in sorted(q,key=lambda x:-(x.get("stars") or 0)):
        ru=repo_url(c["slug"]); rl=f" · [repo]({ru})" if ru else ""
        miss=missing(c["slug"]); eksik=("eksik: "+", ".join(miss)) if miss else "elle gözden geçir"
        lines.append(f"- [ ] **{c['title']}** · {eksik} · [sayfa](https://trescout.com/discover/{c['slug']}/){rl}")
    body="\n".join(lines)
    if DRY:
        print("[dry / GH_TOKEN yok] açılacak/güncellenecek issue gövdesi:\n")
        print("BAŞLIK:",TITLE,"\n"); print(body); return
    # mevcut açık issue'yu bul (başlık birebir), varsa güncelle
    num=None
    try:
        out=subprocess.run(["gh","issue","list","--state","open","--search",TITLE,"--json","number,title"],
                           capture_output=True,text=True,cwd=ROOT,check=True)
        for it in json.loads(out.stdout or "[]"):
            if it.get("title")==TITLE: num=it["number"]; break
    except Exception as e:
        print("uyarı: mevcut issue aranamadı:",e)
    if num:
        subprocess.run(["gh","issue","edit",str(num),"--body",body],cwd=ROOT,check=True)
        print(f"issue #{num} güncellendi · {len(q)} entry")
    else:
        subprocess.run(["gh","issue","create","--title",TITLE,"--body",body],cwd=ROOT,check=True)
        print(f"yeni issue açıldı · {len(q)} entry")

if __name__=="__main__": main()
