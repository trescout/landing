#!/usr/bin/env python3
"""
"Nasıl çalışır" sayfası (v3) · altı dilde.

    python3 scripts/nasil-calisir.py

Neden üretiliyor (2026-10-10): eski sayfa altı dilde elle yazılıydı ve gelecek
özellikleri vaat ediyordu ("E-posta teslimi açıldığında rapor seçtiğiniz saatte
gelen kutunuza ulaşır", "teslim saati seçimi ve konu filtreleri erken erişimle
sunulacak"). Burhan'ın kuralı: hiçbir özellik erken erişimle bile garanti
edilmez. Yeni sayfa yalnız bugün olanı anlatır ve sınırlarını söyler.

Yalnız <main> yazılır; <head>, nav, footer ve betikler her dilin dosyasından
korunur (ana-sayfa.py ile aynı yöntem). Örnek kayıt sabit bir rapordan
(ORNEK_TARIH) okunur: sayfa her rapordan sonra değişmesin.

Sayfa okuma sayfası: discover.css'in okuma sütununu (disc-*) kullanır.
"""
import html
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diller import DILLER  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORNEK_TARIH = "2026-10-09"
ORNEK_REPO = "morluto/rea"
ORNEK_TERIM = "reverse engineering"

M = {
    "tr": {
        "aciklama": "TreScout'un kaynakları nasıl taradığını, raporu nasıl hazırlayıp yayımladığını ve sınırlarını öğrenin.",
        "h1": "TreScout nasıl çalışır?",
        "giris": ("TreScout her gün kaynak akışlarını tarar, öne çıkanları yapay zekâ ile özetler ve tek bir "
                  "raporda bir araya getirir. Raporlar herkese açıktır, okumak için kayıt olmanız gerekmez."),
        "tarama": ("Tarama", "Her gün GitHub Trending, Hacker News ile Hugging Face'in model ve günlük "
                   "makale akışları taranır ve her kaynaktan o günün öne çıkan kayıtları alınır. Yıldız, oy, beğeni "
                   "ve indirme sayıları tarama anındaki değerleri yansıtır. Rapor sayfasında taramanın saati belirtilir."),
        "ozet": ("Özetleme", "Seçilen her kayıt, yapay zekâ ile bir veya iki cümlelik kısa bir özete dönüştürülür. "
                 "Teknik terimler özgün hâliyle parantez içinde korunur. Anlamları raporun sonundaki sözlük "
                 "bölümünde açıklanır."),
        "ornek": "Örnek olarak 9 Ekim 2026 raporundan bir kayıt:",
        "ornek_etiket": ("Kaynak kaydı", "TreScout özeti", "Sözlük açıklaması"),
        "tekrar": ("Tekrar filtresi", "Her rapor, son 30 günün raporlarıyla karşılaştırılır. Bu süre içinde "
                   "listede yer almayan maddeler \u201cyeni\u201d olarak işaretlenir. Tekrarsız raporda yalnızca bu "
                   "maddeler yer alır."),
        "tekrarsiz": "Tekrarsız raporlar",
        "yayin": ("Yayın", "Rapor her gün Türkçe, İngilizce, Fransızca, Portekizce, İspanyolca ve Almanca "
                  "dillerinde, web sayfası ve PDF olarak yayımlanır. Geçmiş raporlar arşivde kalır. Raporda yer "
                  "alan açık kaynak projelerinin keşif sayfaları, raporda geçen terimlerin ise sözlük sayfaları bulunur."),
        "sinir_h2": "Sınırlar",
        "sinirlar": [
            "Özetler yapay zekâ ile hazırlanır ve hata içerebilir. Önemli bir karar vermeden önce maddedeki "
            "bağlantıdan kaynağı kontrol etmenizi öneririz.",
            "Sayılar tarama anına aittir. Kaynak sayfası sonradan değişmiş olabilir.",
            "TreScout raporda geçen araçları geliştirmez, yalnızca seçer ve tanıtır.",
            "Diğer dillerdeki raporlar, Türkçe rapordan makine çevirisiyle hazırlanır.",
        ],
        "erken": ("Erken erişim", "Raporlar şu anda herkese açıktır. E-postayla gönderim gibi özellikler üzerinde "
                  "çalışıyoruz ancak bunlar için bir tarih ya da garanti vermiyoruz. Erken erişim başladığında "
                  "haberdar olmak için listeye katılabilirsiniz."),
        "erken_git": "Erken erişim listesine katılın",
    },
    "en": {
        "aciklama": 'How TreScout scans its sources, how the report is prepared and published, and its limits.',
        "h1": "How does TreScout work?",
        "giris": ("Every day TreScout scans source feeds, summarizes the highlights with AI and collects them in "
                  "one report. Reports are public. You don't need an account to read them."),
        "tarama": ("Scanning", "Every day we scan GitHub Trending, Hacker News, and Hugging Face's model "
                   "and daily paper feeds, and take the day's highlights from each source. Star, point, like and "
                   "download counts are the values at scan time. The report page shows when the scan happened."),
        "ozet": ("Summarizing", "Each selected record is turned into a one or two sentence summary with AI. "
                 "Technical terms keep their original form in parentheses, and the glossary at the end of the "
                 "report explains them."),
        "ornek": "A record from the October 9, 2026 report:",
        "ornek_etiket": ("Source record", "TreScout summary", "Glossary entry"),
        "tekrar": ("Repeat filter", "Each report is compared with the reports of the last 30 days. Items that "
                   "were not listed in that period are marked \u201cnew\u201d. The fresh-only report contains only those items."),
        "tekrarsiz": "Fresh-only reports",
        "yayin": ("Publishing", "The report is published every day as a web page and a PDF, in Turkish, English, "
                  "French, Portuguese, Spanish and German. Past reports stay in the archive. Open-source projects "
                  "from the reports have Discover pages, and terms from the reports have dictionary pages."),
        "sinir_h2": "Limits",
        "sinirlar": [
            "Summaries are prepared with AI and may contain mistakes. Before making an important decision, "
            "check the source through the link in each item.",
            "Counts belong to the moment of the scan. The source page may have changed since.",
            "TreScout does not build the tools in the reports. It only selects and describes them.",
            "Reports in other languages are machine-translated from the Turkish report.",
        ],
        "erken": ("Early access", "Reports are public today. We are working on features such as email delivery, "
                  "but we give no date or guarantee for them. Join the list to hear when early access opens."),
        "erken_git": "Join the early access list",
    },
    "fr": {
        "aciklama": 'Comment TreScout parcourt ses sources, comment le rapport est préparé et publié, et ses limites.',
        "h1": "Comment fonctionne TreScout ?",
        "giris": ("Chaque jour, TreScout parcourt les flux sources, résume l'essentiel avec l'IA et le réunit dans "
                  "un seul rapport. Les rapports sont publics . Aucune inscription n'est nécessaire pour les lire."),
        "tarama": ("Collecte", "Chaque jour, nous parcourons GitHub Trending, Hacker News ainsi que les "
                   "flux de modèles et d'articles du jour de Hugging Face, et retenons ce qui se démarque dans "
                   "chaque source. Les nombres d'étoiles, de points, de j'aime et de téléchargements sont ceux du "
                   "moment de la collecte . La page du rapport en indique l'heure."),
        "ozet": ("Résumé", "Chaque élément retenu est résumé en une ou deux phrases avec l'IA. Les termes "
                 "techniques gardent leur forme d'origine entre parenthèses . Le glossaire à la fin du rapport "
                 "les explique."),
        "ornek": "Un élément du rapport du 9 octobre 2026 :",
        "ornek_etiket": ("Élément source", "Résumé TreScout", "Entrée du glossaire"),
        "tekrar": ("Filtre des répétitions", "Chaque rapport est comparé aux rapports des 30 derniers jours. Les "
                   "éléments absents sur cette période sont marqués « nouveau ». Le rapport "
                   "« nouveautés seulement » ne contient que ces éléments."),
        "tekrarsiz": "Rapports nouveautés seulement",
        "yayin": ("Publication", "Le rapport est publié chaque jour sous forme de page web et de PDF, en turc, "
                  "anglais, français, portugais, espagnol et allemand. Les anciens rapports restent dans "
                  "l'archive. Les projets open source cités ont leur page Découvrir, et les termes leur page de "
                  "glossaire."),
        "sinir_h2": "Limites",
        "sinirlar": [
            "Les résumés sont rédigés avec l'IA et peuvent contenir des erreurs. Avant toute décision "
            "importante, vérifiez la source grâce au lien de chaque élément.",
            "Les chiffres correspondent au moment de la collecte . La page source a pu changer depuis.",
            "TreScout ne développe pas les outils cités . Il se contente de les sélectionner et de les présenter.",
            "Les rapports dans les autres langues sont traduits automatiquement à partir du rapport turc.",
        ],
        "erken": ("Accès anticipé", "Les rapports sont publics dès aujourd'hui. Nous travaillons sur des "
                  "fonctionnalités comme l'envoi par e-mail, sans date ni garantie. Inscrivez-vous pour être averti "
                  "de l'ouverture de l'accès anticipé."),
        "erken_git": "Rejoindre la liste d'accès anticipé",
    },
    "pt": {
        "aciklama": 'Como o TreScout percorre suas fontes, como o relatório é preparado e publicado, e seus limites.',
        "h1": "Como o TreScout funciona?",
        "giris": ("Todos os dias o TreScout percorre os fluxos das fontes, resume os destaques com IA e reúne tudo "
                  "em um único relatório. Os relatórios são públicos. Não é preciso cadastro para ler."),
        "tarama": ("Coleta", "Todos os dias percorremos o GitHub Trending, o Hacker News e os fluxos "
                   "de modelos e de artigos do dia do Hugging Face, e selecionamos os destaques de cada fonte. "
                   "Estrelas, pontos, curtidas e downloads são os valores do momento da coleta. A página do "
                   "relatório mostra o horário."),
        "ozet": ("Resumo", "Cada item selecionado vira um resumo de uma ou duas frases feito com IA. Os termos "
                 "técnicos ficam na forma original entre parênteses, e o glossário no fim do relatório os explica."),
        "ornek": "Um item do relatório de 9 de outubro de 2026:",
        "ornek_etiket": ("Item da fonte", "Resumo do TreScout", "Verbete do glossário"),
        "tekrar": ("Filtro de repetição", "Cada relatório é comparado com os relatórios dos últimos 30 dias. Itens "
                   "que não apareceram nesse período recebem a marca “novo”. O relatório “somente "
                   "novidades” traz apenas esses itens."),
        "tekrarsiz": "Relatórios somente novidades",
        "yayin": ("Publicação", "O relatório é publicado todos os dias como página web e PDF, em turco, inglês, "
                  "francês, português, espanhol e alemão. Os relatórios anteriores ficam no arquivo. Os projetos "
                  "de código aberto citados têm páginas em Descobrir, e os termos têm páginas no glossário."),
        "sinir_h2": "Limites",
        "sinirlar": [
            "Os resumos são feitos com IA e podem conter erros. Antes de uma decisão importante, confira a "
            "fonte pelo link de cada item.",
            "Os números são do momento da coleta. A página da fonte pode ter mudado depois.",
            "O TreScout não desenvolve as ferramentas citadas. Apenas as seleciona e apresenta.",
            "Os relatórios em outros idiomas são traduzidos automaticamente a partir do relatório em turco.",
        ],
        "erken": ("Acesso antecipado", "Os relatórios já são públicos. Estamos trabalhando em recursos como o "
                  "envio por e-mail, mas não damos data nem garantia para eles. Entre na lista para saber quando o "
                  "acesso antecipado abrir."),
        "erken_git": "Entrar na lista de acesso antecipado",
    },
    "es": {
        "aciklama": 'Cómo TreScout recorre sus fuentes, cómo se prepara y publica el informe, y sus límites.',
        "h1": "¿Cómo funciona TreScout?",
        "giris": ("Cada día TreScout recorre los flujos de fuentes, resume lo más destacado con IA y lo reúne en un "
                  "solo informe. Los informes son públicos. No necesita registrarse para leerlos."),
        "tarama": ("Recopilación", "Cada día recorremos GitHub Trending, Hacker News y los flujos de "
                   "modelos y artículos del día de Hugging Face, y tomamos lo más destacado de cada fuente. Las "
                   "estrellas, puntos, me gusta y descargas son los valores del momento de la recopilación. La "
                   "página del informe indica la hora."),
        "ozet": ("Resumen", "Cada elemento seleccionado se convierte en un resumen de una o dos frases hecho con "
                 "IA. Los términos técnicos se mantienen en su forma original entre paréntesis, y el glosario al "
                 "final del informe los explica."),
        "ornek": "Un elemento del informe del 9 de octubre de 2026:",
        "ornek_etiket": ("Elemento de la fuente", "Resumen de TreScout", "Entrada del glosario"),
        "tekrar": ("Filtro de repeticiones", "Cada informe se compara con los informes de los últimos 30 días. "
                   "Los elementos que no aparecieron en ese periodo se marcan como «nuevo». El informe «solo "
                   "novedades» contiene únicamente esos elementos."),
        "tekrarsiz": "Informes solo novedades",
        "yayin": ("Publicación", "El informe se publica cada día como página web y PDF, en turco, inglés, francés, "
                  "portugués, español y alemán. Los informes anteriores quedan en el archivo. Los proyectos de "
                  "código abierto citados tienen su página en Descubrir, y los términos su página en el glosario."),
        "sinir_h2": "Límites",
        "sinirlar": [
            "Los resúmenes se elaboran con IA y pueden contener errores. Antes de tomar una decisión "
            "importante, compruebe la fuente con el enlace de cada elemento.",
            "Las cifras corresponden al momento de la recopilación. La página de origen puede haber cambiado.",
            "TreScout no desarrolla las herramientas citadas. Solo las selecciona y las presenta.",
            "Los informes en otros idiomas se traducen automáticamente a partir del informe en turco.",
        ],
        "erken": ("Acceso anticipado", "Los informes ya son públicos. Trabajamos en funciones como el envío por "
                  "correo, pero no damos fecha ni garantía para ellas. Únase a la lista para saber cuándo se abre el "
                  "acceso anticipado."),
        "erken_git": "Unirse a la lista de acceso anticipado",
    },
    "de": {
        "aciklama": 'Wie TreScout seine Quellen durchsucht, wie der Bericht entsteht und erscheint, und wo seine Grenzen liegen.',
        "h1": "Wie funktioniert TreScout?",
        "giris": ("TreScout prüft jeden Tag Quellen-Feeds, fasst die Höhepunkte mit KI zusammen und bündelt sie in "
                  "einem Bericht. Die Berichte sind öffentlich. Zum Lesen ist keine Anmeldung nötig."),
        "tarama": ("Erfassung", "Jeden Tag prüfen wir GitHub Trending, Hacker News sowie die Modell- und "
                   "Tagespaper-Feeds von Hugging Face und übernehmen die Höhepunkte jeder Quelle. Sterne, Punkte, "
                   "Likes und Downloads sind die Werte zum Zeitpunkt der Erfassung. Die Berichtsseite nennt die "
                   "Uhrzeit."),
        "ozet": ("Zusammenfassung", "Jeder ausgewählte Eintrag wird mit KI in ein bis zwei Sätzen zusammengefasst. "
                 "Fachbegriffe bleiben in Klammern in ihrer ursprünglichen Form. Das Glossar am Ende des Berichts "
                 "erklärt sie."),
        "ornek": "Ein Eintrag aus dem Bericht vom 9. Oktober 2026:",
        "ornek_etiket": ("Quelleneintrag", "TreScout-Zusammenfassung", "Glossareintrag"),
        "tekrar": ("Wiederholungsfilter", "Jeder Bericht wird mit den Berichten der letzten 30 Tage verglichen. "
                   "Einträge, die in diesem Zeitraum nicht vorkamen, werden als „neu“ markiert. Der "
                   "Bericht „Nur Neues“ enthält nur diese Einträge."),
        "tekrarsiz": "Berichte „Nur Neues“",
        "yayin": ("Veröffentlichung", "Der Bericht erscheint jeden Tag als Webseite und als PDF, auf Türkisch, "
                  "Englisch, Französisch, Portugiesisch, Spanisch und Deutsch. Frühere Berichte bleiben im Archiv. "
                  "Open-Source-Projekte aus den Berichten haben eine Seite unter Entdecken, Begriffe eine Seite "
                  "im Glossar."),
        "sinir_h2": "Grenzen",
        "sinirlar": [
            "Die Zusammenfassungen werden mit KI erstellt und können Fehler enthalten. Prüfen Sie vor "
            "wichtigen Entscheidungen die Quelle über den Link im jeweiligen Eintrag.",
            "Die Zahlen gelten für den Zeitpunkt der Erfassung. Die Quellseite kann sich seitdem geändert haben.",
            "TreScout entwickelt die genannten Werkzeuge nicht. Es wählt sie nur aus und stellt sie vor.",
            "Berichte in anderen Sprachen werden maschinell aus dem türkischen Bericht übersetzt.",
        ],
        "erken": ("Vorabzugang", "Die Berichte sind schon heute öffentlich. Wir arbeiten an Funktionen wie dem "
                  "Versand per E-Mail, nennen dafür aber weder Termin noch Garantie. Tragen Sie sich ein, um zu "
                  "erfahren, wann der Vorabzugang öffnet."),
        "erken_git": "In die Vorabzugangsliste eintragen",
    },
}


def e(s):
    return html.escape(str(s), quote=True)


def onek(dil):
    return "" if dil == "tr" else f"/{dil}"


def ornek(dil):
    yol = os.path.join(ROOT, "reports", f"trescout-rapor-{ORNEK_TARIH}.json" if dil == "tr"
                       else f"trescout-report-{ORNEK_TARIH}-{dil}.json")
    r = json.load(open(yol, encoding="utf-8"))
    it = next(i for s in r["sections"] for i in s["items"] if i["title"] == ORNEK_REPO)
    gl = next(g for g in r["glossary"] if g["term"] == ORNEK_TERIM)
    return it, gl


def main_html(dil):
    m = M[dil]
    o = onek(dil)
    nav = DILLER[dil]["nav"] if dil in DILLER else ["Keşif", "Sözlük", "Raporlar", "Karşılaştır"]
    it, gl = ornek(dil)
    tekrarsiz_yol = "/reports/tekrarsiz/" if dil == "tr" else f"{o}/reports/fresh/"
    et = m["ornek_etiket"]

    def bolum(kimlik, baslik, govde):
        return f'<section class="disc-sec" id="{kimlik}"><h2>{e(baslik)}</h2>{govde}</section>'

    ornek_html = (
        f'<p>{e(m["ornek"])}</p><dl class="hiw-ornek">'
        f'<dt>{e(et[0])}</dt><dd><a href="{e(it["url"])}" rel="noopener" target="_blank">{e(it["title"])}</a></dd>'
        f'<dt>{e(et[1])}</dt><dd>{e(it["summary"])}</dd>'
        f'<dt>{e(et[2])}</dt><dd><strong>{e(gl["term"])}</strong>: {e(gl["explanation"])}</dd></dl>'
    )
    yayin_baglanti = (
        f'<ul class="hiw-baglantilar"><li><a href="{o}/reports/">{e(nav[2])}</a></li>'
        f'<li><a href="{o}/discover/">{e(nav[0])}</a></li><li><a href="{o}/dictionary/">{e(nav[1])}</a></li></ul>'
    )
    govde = (
        f'<article class="disc hiw">'
        f'<h1 class="disc-title">{e(m["h1"])}</h1><p class="disc-lead">{e(m["giris"])}</p>'
        + bolum("tarama", m["tarama"][0], f'<p>{e(m["tarama"][1])}</p>')
        + bolum("ozetleme", m["ozet"][0], f'<p>{e(m["ozet"][1])}</p>{ornek_html}')
        + bolum("tekrar-filtresi", m["tekrar"][0],
                f'<p>{e(m["tekrar"][1])}</p><p><a href="{tekrarsiz_yol}">{e(m["tekrarsiz"])}</a></p>')
        + bolum("yayin", m["yayin"][0], f'<p>{e(m["yayin"][1])}</p>{yayin_baglanti}')
        + bolum("sinirlar", m["sinir_h2"],
                '<ul class="disc-wins">' + "".join(f"<li>{e(x)}</li>" for x in m["sinirlar"]) + "</ul>")
        + bolum("erken-erisim", m["erken"][0],
                f'<p>{e(m["erken"][1])}</p><p><a class="btn btn-primary" href="{o}/#top">{e(m["erken_git"])}</a></p>')
        + "</article>"
    )
    return f'<main id="main">\n{govde}\n  </main>'


def yaz(dil):
    yol = os.path.join(ROOT, onek(dil).strip("/"), "how-it-works", "index.html")
    s = open(yol, encoding="utf-8").read()
    yeni = main_html(dil)
    s, adet = re.subn(r"<main id=\"main\">[\s\S]*?</main>", lambda _: yeni, s, count=1)
    if adet != 1:
        raise SystemExit(f"✗ {yol}: <main id=\"main\"> bulunamadı")
    # Okuma sütunu discover.css'te; eski ana sayfa stili (index.css) artık yok
    # Açıklama (meta, og, twitter) · eskisi "erken erişimle sunulacak yenilikler" diyordu (vaat)
    acik = e(M[dil]["aciklama"])
    s = re.sub(r'(<meta (?:name="description"|property="og:description"|name="twitter:description") content=")[^"]*(")',
               lambda mm: mm.group(1) + acik + mm.group(2), s)
    s = re.sub(r'<link rel="stylesheet" href="/assets/(?:index|discover)\.css">',
               '<link rel="stylesheet" href="/assets/discover.css">', s)
    s = re.sub(r'\s*<script src="/assets/home-interactions\.js" defer></script>', "", s)
    s = re.sub(r"\s*<!-- Inter typography[^>]*-->", "", s)
    s = re.sub(r"\s*<!-- =+ (?:EARLY-ACCESS FORM[^=]*|NAV SCROLL STATE|AYDINLATMA METNİ MODAL · scroll-to-bottom gate|"
               r"TABS[^=]*|SCROLL REVEAL[^=]*) =+ -->", "", s)
    open(yol, "w", encoding="utf-8").write(s)
    return yol


if __name__ == "__main__":
    for dil in ["tr"] + list(DILLER):
        print("✓", os.path.relpath(yaz(dil), ROOT))
