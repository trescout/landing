#!/usr/bin/env python3
"""
Ana sayfa (v3) · altı dilde, son raporun verisinden.

    python3 scripts/ana-sayfa.py            # index.html + <dil>/index.html
    python3 scripts/ana-sayfa.py --tarih=2026-10-09

Neden üretiliyor (2026-10-10): eski ana sayfa elle yazılan bir tanıtım
sayfasıydı (ortalanmış başlık, sahte e-posta penceresi, kart ızgarası) ve
yaygın "yapay zekâ ile yapılmış site" görüntüsüne benziyordu. Yeni sayfanın
kendine özgü öğeleri ürünün kendi verisi: son raporun tarihi ve madde sayısı,
ilk rapordan bugüne gün şeridi (rapor çıkmayan günler boş), her maddenin son
7 rapordaki varlığı. Bu yüzden sayfa her rapordan sonra yeniden basılır
(dict-sync.yml · rapor arşivi sayfalarından sonra).

Yalnız <main> yazılır. <head> (başlık, hreflang, şema), nav, footer,
aydınlatma penceresi ve betikler her dilin kendi dosyasından korunur; onların
kanonik kaynakları ayrı (fix-all-headers-and-footers.js, dil-kabuk-tazele.py).

Tarih: TÜM dillerde raporu ve rapor sayfası olan en son gün. Diller farklı
günleri gösterirse kaynak bölümleri (h2) farklılaşır ve check-sayfa-paritesi.py
kırılır; ayrıca altı dilin aynı raporu göstermesi daha dürüst.

Vaat yok: erken erişim metni hangi özelliğin ne zaman geleceğini söylemez.
"""
import datetime
import glob
import html
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diller import DILLER  # noqa: E402
from riza_formu import blok as riza_blok  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAPOR = os.path.join(ROOT, "reports")
DILLER_SIRA = ["tr"] + list(DILLER)

# Ana sayfada kaynak başına gösterilen madde · raporun tamamı rapor sayfasında
GOSTER = {"github": 3, "hackernews": 2, "huggingface": 2, "hfpapers": 1, "lobsters": 1}
SERIT_GENIS, SERIT_DAR = 140, 60   # gün · masaüstü ve dar ekran şeridi
ADIM = 5                           # px · bir gün (3 px çizgi + 2 px boşluk)

M = {
    "tr": {
        "son_rapor": "Son rapor",
        "gunler": ["Pazar", "Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi"],
        "aylar": ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos",
                  "Eylül", "Ekim", "Kasım", "Aralık"],
        "kisa_aylar": ["Oca", "Şub", "Mar", "Nis", "May", "Haz", "Tem", "Ağu", "Eyl", "Eki", "Kas", "Ara"],
        "tarih": "{gun} {ay} {yil}", "gun_ay": "{gun} {ay}", "aralik": "{bas}-{son} {ay}",
        "binlik": ".",
        "ozet": "Bu raporda {n} madde var. Bunların {y} tanesi son 30 günün raporlarında yer almıyordu.",
        "ozet_hepsi_eski": "Bu raporda {n} madde var. Hepsi son 30 günün raporlarında da yer alıyordu.",
        "oku": "Raporu okuyun", "pdf": "PDF olarak indirin",
        "serit_ozet": "Bugüne kadar {sayi} rapor yayımlandı, ilki {ilk} tarihinde.",
        "serit_bosluk": "Rapor yayımlanmayan günler: {liste}.",
        "serit_bosluk_cok": "Rapor yayımlanmayan {sayi} gün var. Sonuncusu {son}.",
        "serit_etiket": "Gün şeridi: Her çizgi bir günü gösterir. Kısa çizgi o gün rapor yayımlanmadığı anlamına gelir. En sağdaki pembe çizgi bu rapordur.",
        "h1": "Teknoloji takibi artık bir iş yükü değil.",
        "giris": "GitHub, Hacker News ve Hugging Face'te öne çıkanları kısa Türkçe özetlerle her gün tek bir raporda bir araya getiriyoruz. Raporlar herkese açıktır, okumak için kayıt olmanız gerekmez.",
        "kaynaklar": {"github": "GitHub", "hackernews": "Hacker News", "huggingface": "Hugging Face modelleri",
                      "hfpapers": "Hugging Face makaleleri", "lobsters": "Lobsters"},
        "kaynak_sayi": ("bu raporda {n} madde", "bu raporda {n} madde"),
        "yeni": "yeni", "yeni_aciklama": "Son 30 günün raporlarında yer almıyordu",
        "son7": "son 7 rapor", "son7_aria": "Son 7 raporun {k} tanesinde yer alıyor",
        "birim": {"yildiz": ("yıldız", "yıldız"), "oy": ("oy", "oy"), "yorum": ("yorum", "yorum"),
                  "begeni": ("beğeni", "beğeni"), "indirme": ("indirme", "indirme")},
        "bugun": "+{n} bugün",
        "tamami": "Raporun tamamını okuyun ({n} madde)",
        "yz": ("Özetler yapay zekâ ile hazırlanır. Önemli bir karar vermeden önce her maddedeki "
               "bağlantıdan kaynağı kontrol etmenizi öneririz."),
        "yan_kaynak": "Bu raporda", "yan_terim": "Raporda geçen terimler", "sozluk": "Sözlükte {n} terim",
        "kesif_h2": "Keşif",
        "kesif_metin": ("Rapora giren her açık kaynak projesinin kendi sayfası var: ne işe yaradığı, nasıl "
                        "kurulduğu ve raporlardaki geçmişi. Şu anda {n} proje bulunuyor."),
        "kesif_bu": "Bu rapordan:", "kesif_git": "Keşfe gidin",
        "erken_h2": "Erken erişim listesi",
        "erken_metin": "Erken erişim başladığında haberdar olmak için listeye katılabilirsiniz. Hangi özelliklerin geleceği ve ne zaman geleceği henüz belli değil.",
        "eposta": "E-posta adresi", "eposta_yer": "E-posta adresiniz", "katil": "Listeye katılın",
    },
    "en": {
        "son_rapor": "Latest report",
        "kisa_aylar": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "tarih": "{ay} {gun}, {yil}", "gun_ay": "{ay} {gun}", "aralik": "{ay} {bas}-{son}",
        "ozet": "This report has {n} items. Of these, {y} were not in any report in the last 30 days.",
        "ozet_hepsi_eski": "This report has {n} items. All of them were also in reports in the last 30 days.",
        "oku": "Read the report", "pdf": "Download the PDF",
        "serit_ozet": "So far {sayi} reports have been published, the first on {ilk}.",
        "serit_bosluk": "Days without a report: {liste}.",
        "serit_bosluk_cok": "There were {sayi} days without a report. The latest was {son}.",
        "serit_etiket": "Day strip: Each line is a day. A short line means no report that day. The pink line on the right is this report.",
        "h1": "Tech monitoring is no longer a burden.",
        "giris": "Every day we collect the highlights from GitHub, Hacker News and Hugging Face in one report, with short summaries in English. Reports are public, and you don't need an account to read them.",
        "kaynaklar": {"github": "GitHub", "hackernews": "Hacker News", "huggingface": "Hugging Face models",
                      "hfpapers": "Hugging Face papers", "lobsters": "Lobsters"},
        "kaynak_sayi": ("{n} item in this report", "{n} items in this report"),
        "yeni": "new", "yeni_aciklama": "Not in any report in the last 30 days",
        "son7": "last 7 reports", "son7_aria": "Listed in {k} of the last 7 reports",
        "birim": {"yildiz": ("star", "stars"), "oy": ("point", "points"), "yorum": ("comment", "comments"),
                  "begeni": ("like", "likes"), "indirme": ("download", "downloads")},
        "bugun": "+{n} today",
        "tamami": "Read the full report ({n} items)",
        "yz": ("Summaries are prepared with AI. Before making an important decision, please check the "
               "source through the link in each item."),
        "yan_kaynak": "In this report", "yan_terim": "Terms in this report", "sozluk": "{n} terms in the dictionary",
        "kesif_h2": "Discover",
        "kesif_metin": ("Every open-source project that makes it into a report gets its own page: what it "
                        "does, how to set it up, and its history in our reports. {n} projects so far."),
        "kesif_bu": "From this report:", "kesif_git": "Go to Discover",
        "erken_h2": "Early access list",
        "erken_metin": "Join the list to hear when early access opens. Which features will come, and when, is not decided yet.",
        "eposta": "Email address", "eposta_yer": "Your email address", "katil": "Join the list",
    },
    "fr": {
        "son_rapor": "Dernier rapport",
        "kisa_aylar": ["janv.", "févr.", "mars", "avr.", "mai", "juin", "juil.", "août", "sept.", "oct.", "nov.", "déc."],
        "tarih": "{gun} {ay} {yil}", "gun_ay": "{gun} {ay}", "aralik": "{bas}-{son} {ay}",
        "ozet": "Ce rapport compte {n} éléments. Parmi eux, {y} ne figuraient dans aucun rapport des 30 derniers jours.",
        "ozet_hepsi_eski": "Ce rapport compte {n} éléments. Tous figuraient déjà dans les rapports des 30 derniers jours.",
        "oku": "Lire le rapport", "pdf": "Télécharger le PDF",
        "serit_ozet": "Jusqu'ici, {sayi} rapports ont été publiés, le premier le {ilk}.",
        "serit_bosluk": "Jours sans rapport : {liste}.",
        "serit_bosluk_cok": "Il y a eu {sayi} jours sans rapport. Le dernier\u00a0: {son}.",
        "serit_etiket": "Frise des jours\u00a0: Chaque trait est un jour. Un trait court signale un jour sans rapport. Le trait rose à droite est ce rapport.",
        "h1": "La veille technique n'est plus une corvée.",
        "giris": "Chaque jour, nous réunissons dans un seul rapport ce qui se démarque sur GitHub, Hacker News et Hugging Face, avec de courts résumés en français. Les rapports sont publics, aucune inscription n'est nécessaire pour les lire.",
        "kaynaklar": {"github": "GitHub", "hackernews": "Hacker News", "huggingface": "Modèles Hugging Face",
                      "hfpapers": "Articles Hugging Face", "lobsters": "Lobsters"},
        "kaynak_sayi": ("{n} élément dans ce rapport", "{n} éléments dans ce rapport"),
        "yeni": "nouveau", "yeni_aciklama": "Absent des rapports des 30 derniers jours",
        "son7": "7 derniers rapports", "son7_aria": "Présent dans {k} des 7 derniers rapports",
        "birim": {"yildiz": ("étoile", "étoiles"), "oy": ("point", "points"), "yorum": ("commentaire", "commentaires"),
                  "begeni": ("j'aime", "j'aime"), "indirme": ("téléchargement", "téléchargements")},
        "bugun": "+{n} aujourd'hui",
        "tamami": "Lire le rapport complet ({n} éléments)",
        "yz": ("Les résumés sont rédigés avec l'IA. Avant toute décision importante, vérifiez la source "
               "grâce au lien de chaque élément."),
        "yan_kaynak": "Dans ce rapport", "yan_terim": "Termes du rapport", "sozluk": "{n} termes dans le glossaire",
        "kesif_h2": "Découvrir",
        "kesif_metin": ("Chaque projet open source retenu dans un rapport a sa propre page : à quoi il sert, "
                        "comment l'installer et son historique dans nos rapports. {n} projets à ce jour."),
        "kesif_bu": "Dans ce rapport :", "kesif_git": "Aller à Découvrir",
        "erken_h2": "Liste d'accès anticipé",
        "erken_metin": "Inscrivez-vous pour être averti de l'ouverture de l'accès anticipé. Les fonctionnalités et leur calendrier ne sont pas encore décidés.",
        "eposta": "Adresse e-mail", "eposta_yer": "Votre adresse e-mail", "katil": "Rejoindre la liste",
    },
    "pt": {
        "son_rapor": "Último relatório",
        "kisa_aylar": ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"],
        "tarih": "{gun} de {ay} de {yil}", "gun_ay": "{gun} de {ay}", "aralik": "{bas}-{son} de {ay}",
        "ozet": "Este relatório tem {n} itens. Destes, {y} não estavam em nenhum relatório dos últimos 30 dias.",
        "ozet_hepsi_eski": "Este relatório tem {n} itens. Todos já estavam em relatórios dos últimos 30 dias.",
        "oku": "Ler o relatório", "pdf": "Baixar o PDF",
        "serit_ozet": "Até agora foram publicados {sayi} relatórios, o primeiro em {ilk}.",
        "serit_bosluk": "Dias sem relatório: {liste}.",
        "serit_bosluk_cok": "Houve {sayi} dias sem relatório. O mais recente foi {son}.",
        "serit_etiket": "Faixa de dias: Cada traço é um dia. Um traço curto indica um dia sem relatório. O traço rosa à direita é este relatório.",
        "h1": "Acompanhar tecnologia não é mais um fardo.",
        "giris": "Todos os dias reunimos em um único relatório os destaques do GitHub, do Hacker News e do Hugging Face, com resumos curtos em português. Os relatórios são públicos, não é preciso cadastro para ler.",
        "kaynaklar": {"github": "GitHub", "hackernews": "Hacker News", "huggingface": "Modelos do Hugging Face",
                      "hfpapers": "Artigos do Hugging Face", "lobsters": "Lobsters"},
        "kaynak_sayi": ("{n} item neste relatório", "{n} itens neste relatório"),
        "yeni": "novo", "yeni_aciklama": "Não estava nos relatórios dos últimos 30 dias",
        "son7": "últimos 7 relatórios", "son7_aria": "Presente em {k} dos últimos 7 relatórios",
        "birim": {"yildiz": ("estrela", "estrelas"), "oy": ("ponto", "pontos"), "yorum": ("comentário", "comentários"),
                  "begeni": ("curtida", "curtidas"), "indirme": ("download", "downloads")},
        "bugun": "+{n} hoje",
        "tamami": "Ler o relatório completo ({n} itens)",
        "yz": ("Os resumos são preparados com IA. Antes de tomar uma decisão importante, confira a fonte "
               "pelo link de cada item."),
        "yan_kaynak": "Neste relatório", "yan_terim": "Termos do relatório", "sozluk": "{n} termos no glossário",
        "kesif_h2": "Descobrir",
        "kesif_metin": ("Cada projeto de código aberto que entra em um relatório tem sua própria página: para "
                        "que serve, como instalar e seu histórico nos relatórios. {n} projetos até agora."),
        "kesif_bu": "Deste relatório:", "kesif_git": "Ir para Descobrir",
        "erken_h2": "Lista de acesso antecipado",
        "erken_metin": "Entre na lista para saber quando o acesso antecipado abrir. Ainda não está definido quais recursos virão nem quando.",
        "eposta": "Endereço de e-mail", "eposta_yer": "Seu e-mail", "katil": "Entrar na lista",
    },
    "es": {
        "son_rapor": "Último informe",
        "kisa_aylar": ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sept", "oct", "nov", "dic"],
        "tarih": "{gun} de {ay} de {yil}", "gun_ay": "{gun} de {ay}", "aralik": "{bas}-{son} de {ay}",
        "ozet": "Este informe tiene {n} elementos. De ellos, {y} no estaban en ningún informe de los últimos 30 días.",
        "ozet_hepsi_eski": "Este informe tiene {n} elementos. Todos estaban ya en informes de los últimos 30 días.",
        "oku": "Leer el informe", "pdf": "Descargar el PDF",
        "serit_ozet": "Hasta ahora se han publicado {sayi} informes, el primero el {ilk}.",
        "serit_bosluk": "Días sin informe: {liste}.",
        "serit_bosluk_cok": "Hubo {sayi} días sin informe. El más reciente fue el {son}.",
        "serit_etiket": "Franja de días: Cada trazo es un día. Un trazo corto indica un día sin informe. El trazo rosa de la derecha es este informe.",
        "h1": "Seguir la tecnología ya no es una carga.",
        "giris": "Cada día reunimos en un solo informe lo más destacado de GitHub, Hacker News y Hugging Face, con resúmenes breves en español. Los informes son públicos, no necesita registrarse para leerlos.",
        "kaynaklar": {"github": "GitHub", "hackernews": "Hacker News", "huggingface": "Modelos de Hugging Face",
                      "hfpapers": "Artículos de Hugging Face", "lobsters": "Lobsters"},
        "kaynak_sayi": ("{n} elemento en este informe", "{n} elementos en este informe"),
        "yeni": "nuevo", "yeni_aciklama": "No estaba en los informes de los últimos 30 días",
        "son7": "últimos 7 informes", "son7_aria": "Presente en {k} de los últimos 7 informes",
        "birim": {"yildiz": ("estrella", "estrellas"), "oy": ("punto", "puntos"), "yorum": ("comentario", "comentarios"),
                  "begeni": ("me gusta", "me gusta"), "indirme": ("descarga", "descargas")},
        "bugun": "+{n} hoy",
        "tamami": "Leer el informe completo ({n} elementos)",
        "yz": ("Los resúmenes se elaboran con IA. Antes de tomar una decisión importante, compruebe la "
               "fuente con el enlace de cada elemento."),
        "yan_kaynak": "En este informe", "yan_terim": "Términos del informe", "sozluk": "{n} términos en el glosario",
        "kesif_h2": "Descubrir",
        "kesif_metin": ("Cada proyecto de código abierto que entra en un informe tiene su propia página: para "
                        "qué sirve, cómo instalarlo y su historial en los informes. {n} proyectos hasta ahora."),
        "kesif_bu": "De este informe:", "kesif_git": "Ir a Descubrir",
        "erken_h2": "Lista de acceso anticipado",
        "erken_metin": "Únase a la lista para saber cuándo se abre el acceso anticipado. Todavía no está decidido qué funciones llegarán ni cuándo.",
        "eposta": "Correo electrónico", "eposta_yer": "Su correo electrónico", "katil": "Unirse a la lista",
    },
    "de": {
        "son_rapor": "Neuester Bericht",
        "kisa_aylar": ["Jan.", "Feb.", "März", "Apr.", "Mai", "Juni", "Juli", "Aug.", "Sept.", "Okt.", "Nov.", "Dez."],
        "tarih": "{gun}. {ay} {yil}", "gun_ay": "{gun}. {ay}", "aralik": "{bas}.-{son}. {ay}",
        "ozet": "Dieser Bericht enthält {n} Einträge. Davon standen {y} in keinem Bericht der letzten 30 Tage.",
        "ozet_hepsi_eski": "Dieser Bericht enthält {n} Einträge. Alle standen bereits in Berichten der letzten 30 Tage.",
        "oku": "Bericht lesen", "pdf": "PDF herunterladen",
        "serit_ozet": "Bisher sind {sayi} Berichte erschienen, der erste am {ilk}.",
        "serit_bosluk": "Tage ohne Bericht: {liste}.",
        "serit_bosluk_cok": "Es gab {sayi} Tage ohne Bericht. Zuletzt am {son}.",
        "serit_etiket": "Tagesleiste: Jeder Strich ist ein Tag. Ein kurzer Strich steht für einen Tag ohne Bericht. Der rosa Strich rechts ist dieser Bericht.",
        "h1": "Technik zu verfolgen ist keine Last mehr.",
        "giris": "Jeden Tag bündeln wir die Höhepunkte von GitHub, Hacker News und Hugging Face in einem Bericht, mit kurzen Zusammenfassungen auf Deutsch. Die Berichte sind öffentlich, zum Lesen ist keine Anmeldung nötig.",
        "kaynaklar": {"github": "GitHub", "hackernews": "Hacker News", "huggingface": "Hugging-Face-Modelle",
                      "hfpapers": "Hugging-Face-Papers", "lobsters": "Lobsters"},
        "kaynak_sayi": ("{n} Eintrag in diesem Bericht", "{n} Einträge in diesem Bericht"),
        "yeni": "neu", "yeni_aciklama": "In keinem Bericht der letzten 30 Tage",
        "son7": "letzte 7 Berichte", "son7_aria": "In {k} der letzten 7 Berichte",
        "birim": {"yildiz": ("Stern", "Sterne"), "oy": ("Punkt", "Punkte"), "yorum": ("Kommentar", "Kommentare"),
                  "begeni": ("Like", "Likes"), "indirme": ("Download", "Downloads")},
        "bugun": "+{n} heute",
        "tamami": "Den ganzen Bericht lesen ({n} Einträge)",
        "yz": ("Die Zusammenfassungen werden mit KI erstellt. Prüfen Sie vor wichtigen Entscheidungen die "
               "Quelle über den Link im jeweiligen Eintrag."),
        "yan_kaynak": "In diesem Bericht", "yan_terim": "Begriffe im Bericht", "sozluk": "{n} Begriffe im Glossar",
        "kesif_h2": "Entdecken",
        "kesif_metin": ("Jedes Open-Source-Projekt, das in einen Bericht aufgenommen wird, hat eine eigene "
                        "Seite: wofür es gut ist, wie man es einrichtet und seine Geschichte in unseren "
                        "Berichten. Bisher {n} Projekte."),
        "kesif_bu": "Aus diesem Bericht:", "kesif_git": "Zu Entdecken",
        "erken_h2": "Vorabzugangsliste",
        "erken_metin": "Tragen Sie sich ein, um zu erfahren, wann der Vorabzugang öffnet. Welche Funktionen wann kommen, steht noch nicht fest.",
        "eposta": "E-Mail-Adresse", "eposta_yer": "Ihre E-Mail-Adresse", "katil": "Eintragen",
    },
}
# Ay ve gün adları, binlik ayırıcı diller.py'den (Türkçe burada)
for _kod, _d in DILLER.items():
    M[_kod].setdefault("aylar", _d["aylar"])
    M[_kod].setdefault("gunler", _d["rapor_gunler"])
    M[_kod].setdefault("binlik", _d["binlik"])


def e(s):
    return html.escape(str(s), quote=True)


def onek(dil):
    return "" if dil == "tr" else f"/{dil}"


def json_yolu(dil, t):
    return os.path.join(RAPOR, f"trescout-rapor-{t}.json" if dil == "tr" else f"trescout-report-{t}-{dil}.json")


def pdf_yolu(dil, t):
    return f"/reports/trescout-rapor-{t}.pdf" if dil == "tr" else f"/reports/trescout-report-{t}-{dil}.pdf"


def sayfa_var(yol):
    return os.path.exists(os.path.join(ROOT, yol.strip("/"), "index.html"))


def sayi(n, m):
    s = f"{int(n):,}"
    return s.replace(",", m["binlik"])


def cogul(cift, n):
    return cift[0] if n == 1 else cift[1]


def tarih(t, m, kisa=False):
    d = datetime.date.fromisoformat(t)
    return m["gun_ay" if kisa else "tarih"].format(gun=d.day, ay=m["aylar"][d.month - 1], yil=d.year)


def bosluk_listesi(gunler, m):
    """Ardışık boş günleri aralık olarak yaz: 29-30 Ağustos, 17 Eylül."""
    gruplar = []
    for g in gunler:
        d = datetime.date.fromisoformat(g)
        if gruplar and (d - gruplar[-1][-1]).days == 1 and d.month == gruplar[-1][-1].month:
            gruplar[-1].append(d)
        else:
            gruplar.append([d])
    out = []
    for gr in gruplar:
        ay = m["aylar"][gr[0].month - 1]
        out.append(m["gun_ay"].format(gun=gr[0].day, ay=ay) if len(gr) == 1
                   else m["aralik"].format(bas=gr[0].day, son=gr[-1].day, ay=ay))
    # Aralık tireden satıra bölünmesin ("29-" / "30 Ağustos"): tirenin iki yanına
    # sözcük birleştirici (U+2060), gün ile ay arasına bölünmez boşluk
    return ", ".join(x.replace("-", "\u2060-\u2060").replace(" ", "\u00a0", 1) for x in out)


# ── veri ─────────────────────────────────────────────────────────────────────
def tarihler(dil):
    kalip = "trescout-rapor-2*.json" if dil == "tr" else f"trescout-report-2*-{dil}.json"
    out = []
    for f in glob.glob(os.path.join(RAPOR, kalip)):
        m = re.search(r"(\d{4}-\d{2}-\d{2})", os.path.basename(f))
        if m and sayfa_var(f"{onek(dil)}/reports/{m.group(1)}/"):
            out.append(m.group(1))
    return set(out)


def yukle(dil, t):
    return json.load(open(json_yolu(dil, t), encoding="utf-8"))


_URL_ONBELLEK = {}


def urller(t):
    """Bir raporun madde bağlantıları · seçim Türkçe raporla aynı, diller arası ortak."""
    if t not in _URL_ONBELLEK:
        d = yukle("tr", t)
        _URL_ONBELLEK[t] = {it["url"] for s in d["sections"] for it in s["items"]}
    return _URL_ONBELLEK[t]


def ilk_cumle(metin, azami=230):
    parca = re.split(r"(?<=[.!?])\s+(?=[A-ZÇĞİÖŞÜÂÉÈÀ0-9])", metin.strip())
    s = parca[0] if parca else metin
    if len(s) > azami:
        s = s[: s.rfind(" ", 0, azami)].rstrip(",;:") + "…"
    return s


def madde_sayilari(kaynak, it, m):
    md = (it.get("snapshot") or {}).get("metadata") or {}
    p, e_ = md.get("popularity"), md.get("engagementCount")
    b = m["birim"]
    out = []
    if kaynak == "github":
        if p is not None:
            out.append(f"{sayi(p, m)} {cogul(b['yildiz'], p)}")
        if e_:
            out.append(m["bugun"].format(n=sayi(e_, m)))
    elif kaynak in ("hackernews", "lobsters"):
        if p is not None:
            out.append(f"{sayi(p, m)} {cogul(b['oy'], p)}")
        if e_ is not None:
            out.append(f"{sayi(e_, m)} {cogul(b['yorum'], e_)}")
    elif kaynak == "huggingface":
        if p is not None:
            out.append(f"{sayi(p, m)} {cogul(b['begeni'], p)}")
        if e_ is not None:
            out.append(f"{sayi(e_, m)} {cogul(b['indirme'], e_)}")
    elif kaynak == "hfpapers":
        if p is not None:
            out.append(f"{sayi(p, m)} {cogul(b['begeni'], p)}")
        if e_ is not None:
            out.append(f"{sayi(e_, m)} {cogul(b['yorum'], e_)}")
    return out, md.get("language")


def slug_terim(t):
    t = t.lower().strip()
    for a, b in [("ç", "c"), ("ğ", "g"), ("ı", "i"), ("ş", "s"), ("ö", "o"), ("ü", "u")]:
        t = t.replace(a, b)
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")


def slug_depo(s):
    return re.sub(r"[^a-z0-9]+", "-", s.split("/")[-1].lower()).strip("-")


def sayfa_sayisi(dil, bolum):
    return len(glob.glob(os.path.join(ROOT, onek(dil).strip("/"), bolum, "*", "index.html")))


# ── çizimler (SVG öznitelikleri · CSP'de satır içi stil yasak) ─────────────────
def serit(gunler, rapor_gunleri, son, m, sinif, etiket=None):
    """Her gün bir çizgi. Rapor günü uzun çizgi, raporsuz gün taban çizgisinde kısa. Son gün pembe."""
    h, son_h, alt = 34, 44, 18
    gen = len(gunler) * ADIM
    parca = []
    for i, g in enumerate(gunler):
        x = i * ADIM
        if g == son:
            parca.append(f'<rect class="s-son" x="{x}" y="0" width="3" height="{son_h}"/>')
        elif g in rapor_gunleri:
            parca.append(f'<rect class="s-var" x="{x}" y="{son_h - h}" width="3" height="{h}"/>')
        else:
            parca.append(f'<rect class="s-yok" x="{x}" y="{son_h - 3}" width="3" height="3"/>')
    for i, g in enumerate(gunler):
        d = datetime.date.fromisoformat(g)
        if d.day == 1 or i == 0:
            if i > 0 or d.day <= 20:   # ilk gün ayın sonuna yakınsa etiket bir sonrakiyle çakışmasın
                parca.append(f'<text x="{i * ADIM}" y="{son_h + alt - 2}">{e(m["kisa_aylar"][d.month - 1])}</text>')
    nitelik = (f'role="img" aria-label="{e(etiket)}"' if etiket else 'aria-hidden="true"')
    return (f'<svg class="ana-serit {sinif}" width="{gen}" height="{son_h + alt}" '
            f'viewBox="0 0 {gen} {son_h + alt}" {nitelik}>{"".join(parca)}</svg>')


def noktalar(varlik, m):
    k = sum(varlik)
    parca = []
    for i, var in enumerate(varlik):
        cx = 5 + i * 12
        sinif = "n-son" if i == len(varlik) - 1 else ("n-var" if var else "n-yok")
        parca.append(f'<circle class="{sinif}" cx="{cx}" cy="6" r="4.25"/>')
    return (f'<svg class="ana-nokta" width="{len(varlik) * 12}" height="12" viewBox="0 0 {len(varlik) * 12} 12" '
            f'role="img" aria-label="{e(m["son7_aria"].format(k=k))}">{"".join(parca)}</svg>')


def cubuk(oran):
    return (f'<svg class="ana-cubuk" viewBox="0 0 100 6" preserveAspectRatio="none" aria-hidden="true">'
            f'<rect class="c-zemin" x="0" y="0" width="100" height="6"/>'
            f'<rect class="c-dolu" x="0" y="0" width="{oran:.1f}" height="6"/></svg>')


# ── sayfa ────────────────────────────────────────────────────────────────────
def main_html(dil, t, butun_tarihler, ortak_tarihler):
    m = M[dil]
    o = onek(dil)
    r = yukle(dil, t)
    d = datetime.date.fromisoformat(t)
    son7 = sorted(x for x in butun_tarihler if x <= t)[-7:]

    onceki = set()
    for x in butun_tarihler:
        fark = (d - datetime.date.fromisoformat(x)).days
        if 0 < fark <= 30:
            onceki |= urller(x)

    maddeler = [(s["sourceName"], it) for s in r["sections"] for it in s["items"]]
    n = len(maddeler)
    y = sum(1 for _, it in maddeler if it["url"] not in onceki)
    ozet = (m["ozet"] if y else m["ozet_hepsi_eski"]).format(n=n, y=y)

    # gün şeridi
    ilk = min(butun_tarihler)
    gunler = []
    g = datetime.date.fromisoformat(ilk)
    while g <= d:
        gunler.append(g.isoformat())
        g += datetime.timedelta(days=1)
    rapor_gunleri = {x for x in butun_tarihler if x <= t}
    bos = [x for x in gunler if x not in rapor_gunleri]
    serit_metni = m["serit_ozet"].format(ilk=tarih(ilk, m), sayi=sayi(len(rapor_gunleri), m))
    if bos:
        serit_metni += " " + (m["serit_bosluk"].format(liste=bosluk_listesi(bos, m)) if len(bos) <= 4
                              else m["serit_bosluk_cok"].format(sayi=len(bos), son=tarih(bos[-1], m)))

    rapor_url = f"{o}/reports/{t}/"
    bant = (
        f'<section class="ana-bant" id="son-rapor" aria-labelledby="ana-tarih">'
        f'<div class="container ana-bant-ic"><div class="ana-bant-sol">'
        f'<p class="ana-gun">{e(m["son_rapor"])}</p>'
        f'<p class="ana-tarih" id="ana-tarih"><time datetime="{t}">{e(tarih(t, m))}</time></p>'
        f'<p class="ana-ozet">{e(ozet)}</p>'
        f'<div class="ana-eylem"><a class="btn btn-primary ana-dugme" href="{rapor_url}">{e(m["oku"])}</a>'
        f'<a class="ana-bant-baglanti" href="{pdf_yolu(dil, t)}">{e(m["pdf"])}</a></div>'
        f'</div><div class="ana-bant-sag"><p class="ana-serit-metni">{e(serit_metni)}</p>'
        f'{serit(gunler[-SERIT_GENIS:], rapor_gunleri, t, m, "ana-serit-genis", m["serit_etiket"])}'
        f'{serit(gunler[-SERIT_DAR:], rapor_gunleri, t, m, "ana-serit-dar")}'
        f'</div></div></section>'
    )

    # kaynak bölümleri
    bolumler = []
    ilk_madde = True
    for s in r["sections"]:
        k = s["sourceName"]
        if not s["items"] or k not in m["kaynaklar"]:
            continue
        lis = []
        for it in s["items"][: GOSTER.get(k, 1)]:
            varlik = [it["url"] in urller(x) for x in son7]
            sayilar, prog_dili = madde_sayilari(k, it, m)
            yeni = (f' <span class="ana-yeni" title="{e(m["yeni_aciklama"])}">{e(m["yeni"])}</span>'
                    if it["url"] not in onceki else "")
            etiket = f'<span class="ana-iz-etiket">{e(m["son7"])}</span>' if ilk_madde else ""
            ilk_madde = False
            dil_satiri = f'<p class="ana-madde-dil">{e(prog_dili)}</p>' if prog_dili else ""
            lis.append(
                f'<li class="ana-madde"><div class="ana-iz">{noktalar(varlik, m)}{etiket}</div>'
                f'<div class="ana-madde-govde"><p class="ana-madde-baslik"><a href="{e(it["url"])}" '
                f'rel="noopener" target="_blank">{e(it["title"])}</a>{yeni}</p>'
                f'<p class="ana-madde-ozet">{e(ilk_cumle(it["summary"]))}</p>{dil_satiri}</div>'
                f'<p class="ana-madde-sayi">{"".join(f"<span>{e(x)}</span>" for x in sayilar)}</p></li>'
            )
        adet = len(s["items"])
        bolumler.append(
            f'<section class="ana-kaynak" id="kaynak-{e(k)}"><h2>{e(m["kaynaklar"][k])} '
            f'<span class="ana-kaynak-sayi">{e(cogul(m["kaynak_sayi"], adet).format(n=adet))}</span></h2>'
            f'<ol class="ana-maddeler">{"".join(lis)}</ol></section>'
        )

    # yan sütun · kaynak dağılımı + terimler
    sayimlar = [(s["sourceName"], len(s["items"])) for s in r["sections"]
                if s["items"] and s["sourceName"] in m["kaynaklar"]]
    en_cok = max(c for _, c in sayimlar)
    dagilim = "".join(
        f'<li><span class="ana-dagilim-ad">{e(m["kaynaklar"][k])}</span><span class="num">{c}</span>{cubuk(100 * c / en_cok)}</li>'
        for k, c in sayimlar)
    terimler = []
    for gl in r.get("glossary", [])[:3]:
        yol = f"{o}/dictionary/{slug_terim(gl['term'])}/"
        ad = (f'<a href="{yol}">{e(gl["term"])}</a>' if sayfa_var(yol) else e(gl["term"]))
        terimler.append(f'<li><p class="ana-terim">{ad}</p><p class="ana-terim-aciklama">{e(ilk_cumle(gl["explanation"], 140))}</p></li>')
    yan = (
        f'<aside class="ana-yan"><h2>{e(m["yan_kaynak"])}</h2><ul class="ana-dagilim">{dagilim}</ul>'
        + (f'<h2>{e(m["yan_terim"])}</h2><ul class="ana-terimler">{"".join(terimler)}</ul>' if terimler else "")
        + f'<p class="ana-yan-baglanti"><a href="{o}/dictionary/">{e(m["sozluk"].format(n=sayi(sayfa_sayisi(dil, "dictionary"), m)))}</a></p>'
        f'</aside>'
    )

    # keşif · bu rapordaki projelerin sayfaları
    projeler = []
    for k, it in maddeler:
        if k != "github":
            continue
        yol = f"{o}/discover/{slug_depo(it['title'])}/"
        if sayfa_var(yol):
            projeler.append(f'<a href="{yol}">{e(it["title"].split("/")[-1])}</a>')
    kesif = (
        f'<section class="ana-kesif" id="kesif"><h2>{e(m["kesif_h2"])}</h2>'
        f'<p>{e(m["kesif_metin"].format(n=sayi(sayfa_sayisi(dil, "discover"), m)))}</p>'
        + (f'<p class="ana-kesif-bu">{e(m["kesif_bu"])} {", ".join(projeler)}</p>' if projeler else "")
        + f'<p><a class="ana-git" href="{o}/discover/">{e(m["kesif_git"])}</a></p></section>'
    )

    form_id = f"email-final-{dil}"
    erken = (
        f'<section class="ana-erken" id="cta"><span id="top" aria-hidden="true"></span>'
        f'<h2>{e(m["erken_h2"])}</h2><p>{e(m["erken_metin"])}</p>'
        f'<form class="cta-form final-cta-form js-subscribe" data-source="final-cta" action="/api/subscribe" method="post">'
        f'<div class="form-row"><label class="visually-hidden" for="{form_id}">{e(m["eposta"])}</label>'
        f'<input class="input" type="email" name="email" id="{form_id}" placeholder="{e(m["eposta_yer"])}" '
        f'autocomplete="email" required>'
        f'<button class="btn btn-primary" type="submit">{e(m["katil"])}</button></div>'
        f'{riza_blok(dil, modal=True)}'
        f'<input type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true" class="hp-field">'
        f'</form></section>'
    )

    tamami = (f'<p class="ana-tamami"><a class="btn ana-dugme-koyu" href="{rapor_url}">'
              f'{e(m["tamami"].format(n=n))}</a></p><p class="ana-yz">{e(m["yz"])}</p>')
    govde = (
        f'<div class="container ana-govde"><div class="ana-icerik"><h1>{e(m["h1"])}</h1>'
        f'<p class="ana-giris">{e(m["giris"])}</p>{"".join(bolumler)}{tamami}</div>{yan}</div>'
        f'<div class="container ana-alt">{kesif}{erken}</div>'
    )
    return f'<main id="main">\n{bant}\n{govde}\n  </main>'


def yaz(dil, t, butun, ortak):
    yol = os.path.join(ROOT, onek(dil).strip("/"), "index.html")
    s = open(yol, encoding="utf-8").read()
    yeni = main_html(dil, t, butun, ortak)
    s, adet = re.subn(r"<main id=\"main\">[\s\S]*?</main>", lambda _: yeni, s, count=1)
    if adet != 1:
        raise SystemExit(f"✗ {yol}: <main id=\"main\"> bulunamadı")
    # Ana sayfa artık index.css'i (eski ana sayfa + nasıl çalışır) değil home.css'i yüklüyor
    s = re.sub(r'<link rel="stylesheet" href="/assets/(?:index|home)\.css">',
               '<link rel="stylesheet" href="/assets/home.css">', s)
    # Eski ana sayfanın radar/sekme betiği gerekmiyor
    s = re.sub(r'\s*<script src="/assets/home-interactions\.js" defer></script>', "", s)
    s = re.sub(r"\s*<!-- Inter typography[^>]*-->", "", s)
    s = re.sub(r"\s*<!-- =+ (?:DISCOVERY RADAR|DAILY FLOW PREVIEW|FINAL CTA|HERO|TABS[^=]*|SCROLL REVEAL[^=]*) =+ -->", "", s)
    open(yol, "w", encoding="utf-8").write(s)
    return yol


def main():
    istenen = next((a.split("=", 1)[1] for a in sys.argv if a.startswith("--tarih=")), None)
    kumeler = {dil: tarihler(dil) for dil in DILLER_SIRA}
    ortak = set.intersection(*kumeler.values())
    if not ortak:
        raise SystemExit("✗ Bütün dillerde ortak rapor günü yok.")
    t = istenen or max(ortak)
    if t not in ortak:
        raise SystemExit(f"✗ {t}: her dilde raporu ve rapor sayfası yok.")
    butun = {x for x in kumeler["tr"] if x <= t}
    for dil in DILLER_SIRA:
        yol = yaz(dil, t, butun, ortak)
        print(f"✓ {os.path.relpath(yol, ROOT)} · {t}")


if __name__ == "__main__":
    main()
