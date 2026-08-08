#!/usr/bin/env python3
"""
TreScout · dil tabloları · çok dilli sayfa üreticilerinin tek kaynağı.

Neden ayrı dosya: 2026-08-07'ye kadar İngilizce metinler `discover-en.py` ve
`dictionary-en.py` içine serpiliydi. Üçüncü dil eklemek her iki dosyayı da
baştan okumayı gerektiriyordu. Artık dil eklemek = buraya bir sözlük eklemek.

Kaynak dil DAİMA Türkçe · sayfalar Türkçesinden üretilir, buradaki tablolar
yalnız arayüz metinlerini (başlık, düğme, uyarı) taşır. İçerik metinleri
çeviri uç noktasından geçer.

Yeni dil eklerken:
  1. DILLER'e kodu ve tabloyu ekleyin
  2. scripts/fix-all-headers-and-footers.js'e o dilin nav/footer'ını ekleyin
  3. check-nav-consistency.py ve check-footer-consistency.py'ye kanonik seti ekleyin
  4. assets/subscribe.js · index.js · discover.js sözlüklerine dalı ekleyin
  5. trescout-app/lib/report/template.ts I18N paketine ekleyin (rapor PDF'i)
"""

import re

DILLER = {
    "en": {
        "kod": "en",
        "html_lang": "en",
        "onek": "/en",                      # URL öneki · Türkçe için ""
        "og_locale": "en_US",
        "tagline_alan": "tagline_en",       # katalogdaki çeviri alanı
        "kisa_alan": "kisa_en",             # sözlük manifestindeki çeviri alanı
        # ── chrome (nav + footer) · KANONİK KAYNAK fix-all-headers-and-footers.js
        # Buradaki set yalnız YENİ dilin ilk üretiminde kullanılır (o dilde
        # kopyalanacak sayfa henüz yokken). Sonra normalize edici devralır.
        "nav": ["Discover", "Dictionary", "Reports Archive", "Compare"],
        "nav_yollar": ["discover", "dictionary", "reports", "compare/rss-vs-ai"],
        "nav_cta": "Early Access",
        # Dil değiştirme düğmeleri · (etiket, o dilin URL öneki). Sıra menüde
        # göründüğü sıra. Hedef sayfa yoksa o dilin ana sayfasına düşer.
        "dil_dugmeleri": [("TR", ""), ("FR", "/fr")],
        # Footer "Ürün" sütunu nav'dan bir fazla: ana sayfadaki "nasıl çalışır"
        # bölümü. O bölüm çevrilmemiş dillerde None olur.
        "footer_nasil": "How It Works",
        "footer_urun": "Product",
        "footer_iletisim": "Contact",
        "footer_sosyal": "Social",
        "footer_gizlilik": "Privacy Notice",
        "footer_tagline": "TreScout scans, summarizes, and delivers. You just read.",
        "footer_alt": "© 2026 TreScout · All rights reserved.",
        "atla": "Skip to main content",
        # ── keşif sayfası
        "kesif": "Discover",
        "kesif_geri": "← Discover",
        "kesif_tumu": "All discoveries →",
        "baglantilar": "Links",
        "depo": "GitHub repository →",
        "turkce_oku": "Read in Turkish →",
        "resmi_kaynak": "Official source →",
        "kopyala_komut": "Copy command",
        "kopyala_istem": "Copy prompt",
        "kopyala": "Copy",
        "ajan_istem": "🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)",
        "guncellemeler": "Updates",
        "yildiz": "Stars",
        "son_surum": "latest release",
        "tasindi": "repository moved, new address",
        "arsiv": "repository archived, development stopped",
        "kimin_icin": "Who it is for",
        "lisans": "License",
        "bugun": "today",
        "cta_baslik": "TreScout catches tools like this every day.",
        "cta_metin": "GitHub, Hacker News and HuggingFace are scanned, the highlights are summarized for you.",
        "sorumluluk": ("TreScout did not build this tool · we found it in GitHub trends and wrote it up. "
                       "This page describes the repository as of {date}: The star count and our text belong "
                       "to that day, the repository may have changed since. Check the repository link for "
                       "the current state."),
        "trescout_notu": "TreScout note:",
        # ── sözlük sayfası
        "sozluk": "Dictionary",
        "sozluk_geri": "← Dictionary",
        "sozluk_tumu": "All terms →",
        "nedir": "What is {terim}?",
        "son_guncelleme": "Last updated: {tarih}",
        "analoji": "Analogy:",
        "sozluk_cta_baslik": "New tech terms in your inbox every morning.",
        "sozluk_cta_metin": "Join TreScout early access for the daily digest.",
        # ── bölüm başlıkları (Türkçe → hedef dil)
        "bolumler": {
            "Ne kazandırır?": "What you get",
            "Kurulum": "Installation",
            "Çalıştırma": "Running it",
            "Nasıl başlanır?": "Getting started",
            "Kod bilmiyorsanız": "If you don't write code",
            "İlgili sözlük terimleri": "Related dictionary terms",
            "Bağlantılar": "Links",
            "Tanım": "Overview",
            "Nasıl çalışır?": "How it works",
            "Nerede kullanılır?": "Where it is used",
            "Sık karıştırılanlar": "Commonly confused with",
            "Sıkça sorulanlar": "Frequently asked questions",
            "İlgili terimler": "Related terms",
            "İlgili araçlar": "Related tools",
        },
        # ── kayıt formu
        "form_yer_tutucu": "Enter your email",
        "form_dugme": "Join early access",
        "form_onay": ('I have read the <a href="{gizlilik}" target="_blank" rel="noopener">Privacy Notice</a> '
                      "and consent to my email being processed for this purpose."),
        "gizlilik_yolu": "/en/privacy.html",
        # ── markdown
        "md_kaynak_kesif": "Source: TreScout Discover · {url}",
        "md_kaynak_sozluk": "Source: TreScout Dictionary · {url}",
        # ── tarih
        "aylar": ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December"],
        "tarih_bicimi": "{ay} {gun}, {yil}",
        "binlik": ",",                      # 186.094 → 186,094
        # ── dizin sayfaları (build-en.js) ──────────────────────────────
        # ── rapor arşivi (build-reports-en.js) ────────────────────────────
        "rapor_gunler": ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
        "rapor_tarih": "{ay} {gun}, {yil} ({gunad})",
        "rapor_arsiv_esigi": "2026-08-05",   # bu tarihe kadar "çevrilmiş arşiv" rozeti
        "rapor_rozet": "Translated Archive",
        "rapor_sayfa_baslik": "{tarih} · TreScout Daily Report",
        "rapor_sayfa_aciklama": ("TreScout Daily Technology Intelligence Report for {tarih}. Curated "
                                 "open-source tools, Hacker News discussions, and AI papers."),
        "rapor_sayfa_og": "TreScout Daily Technology Intelligence Report for {tarih}.",
        "rapor_eyebrow": "Daily Technology Report",
        "rapor_eyebrow_arsiv": "· Translated Archive Edition",
        "rapor_arsiv": "Archive",
        "rapor_ac": "Open {dil} PDF →",
        "rapor_indir": "Download PDF",
        "rapor_oku": "Read →",
        "rapor_dil_adi": "English",
        "rapor_not": ("Full report PDF: every item with its summary, source links and the glossary of "
                      "terms. Translated from the original Turkish edition."),
        "rapor_cta": ("<strong>Get daily technology reports in your inbox.</strong> TreScout scans, "
                      "summarizes, and delivers. You just read."),
        "rapor_cta_dugme": "Join Early Access List →",
        "rapor_banner_baslik": "Historical Translated Archive Notice",
        "rapor_banner": ("These English pages and report PDFs are translated from the original Turkish "
                         "daily reports. Item selection, metrics and links are identical to the Turkish "
                         "edition."),
        "rapor_cipler": {
            "Günün Modelleri": "Daily Models",
            "Günün Makaleleri": "Daily Papers",
            "öne çıkan": "highlights",
        },
        "rapor_varyant": {
            "normal": {
                "geri": "All Reports",
                "baslik": "Daily Technology Reports",
                "intro": ("Daily AI-curated summaries of GitHub Trending, Hacker News, HuggingFace and "
                          "Lobsters. Read online in English or download the English PDF."),
                "dizin_baslik": "Daily Technology Reports Archive · TreScout",
                "dizin_aciklama": ("TreScout daily technology reports archive · Curated AI summaries of "
                                   "GitHub, Hacker News, and HuggingFace trends every day."),
            },
            "fresh": {
                "geri": "Fresh Only",
                "baslik": "Fresh Only Reports",
                "intro": ("Only what is new today. Repositories already covered in the last 30 days are "
                          "filtered out, so nothing repeats."),
                "dizin_baslik": "Fresh Only Reports Archive · TreScout",
                "dizin_aciklama": "TreScout fresh-only daily reports · nothing that was already covered.",
            },
        },
        "etiketler": {                       # katalog etiketi TR → hedef dil
            "Yapay zekâ araçları": "AI Tools",
            "Geliştirici aracı": "Developer Tool",
            "Kod bilmeyenler için": "No-Code",
            "Öğrenme": "Learning",
            "Üretkenlik": "Productivity",
        },
        "sozluk_dizin_baslik": "Tech Dictionary · AI & Software Terms · TreScout",
        "sozluk_dizin_aciklama": "Plain-language definitions of AI and software terms including RAG, Fine-tuning, LLM, MCP, and more.",
        "sozluk_dizin_h1": "Modern AI & Software Glossary",
        "sozluk_dizin_lead": "Plain-language definitions for modern technical terms. TreScout scans daily trends and expands this glossary continuously.",
        "sozluk_dizin_ara": "Search term: RAG, embedding, fine-tuning…",
        "sozluk_dizin_ara_etiket": "Search term",
        "sozluk_dizin_cipler": [("", "All"), ("ai", "Artificial Intelligence"),
                                ("dev", "Development"), ("data", "Data & Infra")],
        "sozluk_dizin_birim": "terms",
        "sozluk_dizin_bos": "No matching terms. Try adjusting your search.",
        "kesif_dizin_baslik": "Discover Open Source Projects · TreScout",
        "kesif_dizin_aciklama": "Daily curated highlights of open-source developer tools, AI projects, and trending GitHub repositories.",
        "kesif_dizin_h1": "Discover Trending Developer Tools",
        "kesif_dizin_lead": ("Handpicked open-source projects, AI tools, and frameworks captured daily by "
                             "TreScout: overview, star growth, and <strong>how to use with AI agents.</strong>"),
        "kesif_dizin_ara": "Search tool name or description…",
        "kesif_dizin_ara_etiket": "Search tools",
        "kesif_dizin_sirala": "Sort",
        "kesif_dizin_siralar": [("stars", "Most stars"), ("date", "Newest"), ("title", "A–Z")],
        "kesif_dizin_birim": "projects",
        "kesif_dizin_bos": "No matching tools. Try adjusting your search.",
        "kesif_dizin_kategori": "Categories",
        # ── aydınlatma modal'ı · ana sayfada onay kutusu bunu açar
        "onay_ipucu": "Please read the Privacy Notice to give consent.",
        "modal_baslik": "Privacy Notice",
        "modal_kapat": "Close",
        "modal_kaydir": "Scroll to the end of the text to give consent",
        "modal_onayla": "I have read it, I consent",
        # ── dil ana sayfası (yalnız Türkçe ana sayfası çevrilmemiş dillerde)
        "ana_h1": None,
    },
    "fr": {
        "kod": "fr",
        "html_lang": "fr",
        "onek": "/fr",
        "og_locale": "fr_FR",
        "tagline_alan": "tagline_fr",
        "kisa_alan": "kisa_fr",
        # Karşılaştırma sayfası henüz çevrilmedi · menüde olmayan bölüme
        # bağlantı vermek kırık sayfa demek, geldiğinde buraya eklenecek.
        "nav": ["Découvrir", "Glossaire", "Archive des rapports"],
        "nav_yollar": ["discover", "dictionary", "reports"],
        "nav_cta": "Accès anticipé",
        "dil_dugmeleri": [("TR", ""), ("EN", "/en")],
        "footer_nasil": None,      # Türkçe ana sayfanın "nasıl çalışır" bölümü çevrilmedi
        "footer_urun": "Produit",
        "footer_iletisim": "Contact",
        "footer_sosyal": "Réseaux",
        "footer_gizlilik": "Notice de confidentialité",
        "footer_tagline": "TreScout analyse, résume et livre. Vous n'avez qu'à lire.",
        "footer_alt": "© 2026 TreScout · Tous droits réservés.",
        "atla": "Aller au contenu principal",
        "kesif": "Découvrir",
        "kesif_geri": "← Découvrir",
        "kesif_tumu": "Toutes les découvertes →",
        "baglantilar": "Liens",
        "depo": "Dépôt GitHub →",
        "turkce_oku": "Lire en turc →",
        "resmi_kaynak": "Source officielle →",
        "kopyala_komut": "Copier la commande",
        "kopyala_istem": "Copier l'invite",
        "kopyala": "Copier",
        "ajan_istem": "🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)",
        "guncellemeler": "Mises à jour",
        "yildiz": "Étoiles",
        "son_surum": "dernière version",
        "tasindi": "dépôt déplacé, nouvelle adresse",
        "arsiv": "dépôt archivé, développement arrêté",
        "kimin_icin": "Pour qui",
        "lisans": "Licence",
        "bugun": "aujourd'hui",
        "cta_baslik": "TreScout repère des outils comme celui-ci chaque jour.",
        "cta_metin": "GitHub, Hacker News et HuggingFace sont analysés, l'essentiel vous est résumé.",
        "sorumluluk": ("TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub "
                       "et présenté. Cette page décrit le dépôt tel qu'il était le {date} : Le nombre d'étoiles "
                       "et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du "
                       "dépôt pour l'état actuel."),
        "trescout_notu": "Note TreScout :",
        "sozluk": "Glossaire",
        "sozluk_geri": "← Glossaire",
        "sozluk_tumu": "Tous les termes →",
        "nedir": "Qu'est-ce que {terim} ?",
        "son_guncelleme": "Dernière mise à jour : {tarih}",
        "analoji": "Analogie :",
        "sozluk_cta_baslik": "De nouveaux termes techniques chaque matin.",
        "sozluk_cta_metin": "Rejoignez l'accès anticipé de TreScout pour le résumé quotidien.",
        "bolumler": {
            "Ne kazandırır?": "Ce que ça vous apporte",
            "Kurulum": "Installation",
            "Çalıştırma": "Exécution",
            "Nasıl başlanır?": "Pour commencer",
            "Kod bilmiyorsanız": "Si vous ne codez pas",
            "İlgili sözlük terimleri": "Termes liés du glossaire",
            "Bağlantılar": "Liens",
            "Tanım": "Définition",
            "Nasıl çalışır?": "Comment ça marche",
            "Nerede kullanılır?": "Où est-ce utilisé",
            "Sık karıştırılanlar": "Souvent confondu avec",
            "Sıkça sorulanlar": "Questions fréquentes",
            "İlgili terimler": "Termes liés",
            "İlgili araçlar": "Outils liés",
        },
        "form_yer_tutucu": "Votre adresse e-mail",
        "form_dugme": "Accès anticipé",
        "form_onay": ('J\'ai lu <a href="{gizlilik}" target="_blank" rel="noopener">la notice de confidentialité</a> '
                      "et je consens au traitement de mon adresse e-mail à cette fin."),
        "gizlilik_yolu": "/fr/privacy.html",
        "md_kaynak_kesif": "Source : TreScout Découvrir · {url}",
        "md_kaynak_sozluk": "Source : TreScout Glossaire · {url}",
        "aylar": ["janvier", "février", "mars", "avril", "mai", "juin",
                  "juillet", "août", "septembre", "octobre", "novembre", "décembre"],
        "tarih_bicimi": "{gun} {ay} {yil}",
        # Fransızca binlik ayırıcı boşluk: 186 094 · bölünmez boşlukla yazılır
        "binlik": "\u00a0",
        "rapor_gunler": ["dimanche", "lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi"],
        "rapor_tarih": "{gun} {ay} {yil} ({gunad})",
        "rapor_arsiv_esigi": "2026-08-07",
        "rapor_rozet": "Archive traduite",
        "rapor_sayfa_baslik": "{tarih} · rapport quotidien TreScout",
        "rapor_sayfa_aciklama": ("Le rapport technologique quotidien de TreScout du {tarih} : outils open "
                                 "source, discussions Hacker News et articles sur l'IA, sélectionnés et résumés."),
        "rapor_sayfa_og": "Le rapport technologique quotidien de TreScout du {tarih}.",
        "rapor_eyebrow": "Rapport technologique quotidien",
        "rapor_eyebrow_arsiv": "· édition traduite",
        "rapor_arsiv": "Archive",
        "rapor_ac": "Ouvrir le PDF en {dil} →",
        "rapor_indir": "Télécharger le PDF",
        "rapor_oku": "Lire →",
        "rapor_dil_adi": "français",
        "rapor_not": ("Le PDF complet : chaque élément avec son résumé, ses liens sources et le glossaire "
                      "des termes. Traduit de l'édition turque originale."),
        "rapor_cta": ("<strong>Recevez le rapport quotidien dans votre boîte mail.</strong> TreScout "
                      "analyse, résume et livre. Vous n'avez qu'à lire."),
        "rapor_cta_dugme": "Rejoindre l'accès anticipé →",
        "rapor_banner_baslik": "À propos de cette archive traduite",
        "rapor_banner": ("Ces pages et les PDF sont traduits des rapports quotidiens turcs originaux. La "
                         "sélection des éléments, les mesures et les liens sont identiques à l'édition turque."),
        "rapor_cipler": {
            "Günün Modelleri": "modèles du jour",
            "Günün Makaleleri": "articles du jour",
            "öne çıkan": "à retenir",
        },
        "rapor_varyant": {
            "normal": {
                "geri": "Tous les rapports",
                "baslik": "Rapports technologiques quotidiens",
                "intro": ("Chaque jour, un résumé des tendances de GitHub Trending, Hacker News, "
                          "HuggingFace et Lobsters. À lire en ligne ou en PDF."),
                "dizin_baslik": "Archive des rapports quotidiens · TreScout",
                "dizin_aciklama": ("L'archive des rapports technologiques quotidiens de TreScout · les "
                                   "tendances de GitHub, Hacker News et HuggingFace, résumées chaque jour."),
            },
            "fresh": {
                "geri": "Nouveautés",
                "baslik": "Rapports · nouveautés seulement",
                "intro": ("Uniquement ce qui est nouveau aujourd'hui. Les dépôts déjà traités ces 30 "
                          "derniers jours sont écartés, rien ne se répète."),
                "dizin_baslik": "Archive des rapports · nouveautés seulement · TreScout",
                "dizin_aciklama": "Les rapports quotidiens de TreScout, sans rien de déjà traité.",
            },
        },
        "etiketler": {
            "Yapay zekâ araçları": "Outils IA",
            "Geliştirici aracı": "Outil développeur",
            "Kod bilmeyenler için": "Sans code",
            "Öğrenme": "Apprentissage",
            "Üretkenlik": "Productivité",
        },
        "sozluk_dizin_baslik": "Glossaire tech · termes IA et logiciel · TreScout",
        "sozluk_dizin_aciklama": "Définitions en langage clair des termes de l'IA et du logiciel : RAG, fine-tuning, LLM, MCP et bien d'autres.",
        "sozluk_dizin_h1": "Glossaire de l'IA et du logiciel",
        "sozluk_dizin_lead": "Des définitions en langage clair pour les termes techniques d'aujourd'hui. TreScout suit les tendances chaque jour et enrichit ce glossaire en continu.",
        "sozluk_dizin_ara": "Rechercher un terme : RAG, embedding, fine-tuning…",
        "sozluk_dizin_ara_etiket": "Rechercher un terme",
        "sozluk_dizin_cipler": [("", "Tous"), ("ai", "Intelligence artificielle"),
                                ("dev", "Développement"), ("data", "Données et infra")],
        "sozluk_dizin_birim": "termes",
        "sozluk_dizin_bos": "Aucun terme ne correspond. Essayez une autre recherche.",
        "kesif_dizin_baslik": "Découvrir des projets open source · TreScout",
        "kesif_dizin_aciklama": "Une sélection quotidienne d'outils open source, de projets d'IA et de dépôts GitHub en vogue.",
        "kesif_dizin_h1": "Découvrez les outils qui montent",
        "kesif_dizin_lead": ("Projets open source, outils d'IA et frameworks repérés chaque jour par TreScout : "
                             "présentation, progression des étoiles et <strong>comment les utiliser avec un "
                             "agent.</strong>"),
        "kesif_dizin_ara": "Rechercher un outil ou une description…",
        "kesif_dizin_ara_etiket": "Rechercher un outil",
        "kesif_dizin_sirala": "Trier",
        "kesif_dizin_siralar": [("stars", "Les plus étoilés"), ("date", "Les plus récents"), ("title", "A–Z")],
        "kesif_dizin_birim": "projets",
        "kesif_dizin_bos": "Aucun outil ne correspond. Essayez une autre recherche.",
        "kesif_dizin_kategori": "Catégories",
        "onay_ipucu": "Veuillez lire la notice de confidentialité pour donner votre consentement.",
        "modal_baslik": "Notice de confidentialité",
        "modal_kapat": "Fermer",
        "modal_kaydir": "Faites défiler jusqu'à la fin du texte pour donner votre consentement",
        "modal_onayla": "J'ai lu, je consens",
        "ana_h1": "TreScout analyse, résume et livre. Vous n'avez qu'à lire.",
        "ana_lead": ("Chaque jour, TreScout parcourt GitHub, Hacker News, HuggingFace et Lobsters, "
                     "retient ce qui compte et le rassemble dans un seul rapport."),
        "ana_bolum": "Ce que vous trouverez ici",
        "ana_kartlar": [
            ("Découvrir", "/fr/discover/", "Les outils open source repérés chaque jour, expliqués simplement."),
            ("Glossaire", "/fr/dictionary/", "Les termes techniques d'aujourd'hui, définis en langage clair."),
        ],
        "ana_kayit": "Recevez le rapport quotidien dès l'ouverture.",
        # Ana sayfadaki onay cümlesi · bağlantı modal'ı açar (İngilizce ana
        # sayfayla aynı kurgu). {gizlilik} yolu form_onay ile aynı.
        "ana_onay": ('J\'ai lu <a href="{gizlilik}" data-privacy-modal>la notice de confidentialité</a> '
                     "et je consens au traitement de mon adresse e-mail à cette fin."),
        "ana_not": ("Les pages françaises sont traduites automatiquement à partir de l'original turc · "
                    "en cas de doute, la version turque fait foi."),
    },
}


def nav_etiketleri(d):
    """Sayfada görünen nav etiketleri · guard'lar bunu bekler."""
    return tuple(d["nav"]) + tuple(e for e, _ in d["dil_dugmeleri"])


def footer_etiketleri(d):
    """Footer 'Ürün' sütununda görünen etiketler · guard'lar bunu bekler."""
    bas = (d["footer_nasil"],) if d.get("footer_nasil") else ()
    return bas + tuple(d["nav"]) + (d["nav_cta"],)


def dil(kod):
    """Dil tablosunu getir · bilinmeyen kodda anlaşılır hata ver."""
    if kod not in DILLER:
        raise SystemExit(f"✗ Bilinmeyen dil: {kod!r} · tanımlı diller: {', '.join(DILLER)}")
    return DILLER[kod]


def chrome(d, logo_svg):
    """Yeni dilin İLK üretimi için nav + footer · sonra normalize edici devralır.

    Kanonik kaynak `scripts/fix-all-headers-and-footers.js` · orada o dilin seti
    yoksa hattaki normalize adımı sayfayı düzeltemez, guard da kırılır. Yeni dil
    eklerken ikisini de güncelleyin.
    """
    o = d["onek"]
    nav_link = "".join(
        f'<a href="{o}/{yol}/" class="btn btn-ghost">{ad}</a>'
        for ad, yol in zip(d["nav"], d["nav_yollar"])
    )
    # Nav'da erken erişim düğmesi YOK · İngilizce kabuk da böyle (kanonik kaynak
    # fix-all-headers-and-footers.js). Diller arasında desen aynı kalsın diye.
    diller = "".join(
        f'<a href="{onek}/" class="btn btn-ghost" aria-label="{etiket}">{etiket}</a>'
        for etiket, onek in d["dil_dugmeleri"]
    )
    nav = (f'<nav><div class="container nav-inner"><a class="logo-link" href="{o}/" aria-label="TreScout">'
           f'{logo_svg}<span>TreScout</span></a><div class="nav-actions">{nav_link}'
           f'{diller}</div></div></nav>')

    nasil = (f'<li><a href="{o}/#how-it-works">{d["footer_nasil"]}</a></li>' if d.get("footer_nasil") else "")
    urun = nasil + "".join(f'<li><a href="{o}/{yol}/">{ad}</a></li>'
                           for ad, yol in zip(d["nav"], d["nav_yollar"]))
    footer = (f'<footer><div class="container"><div class="footer-grid">'
              f'<div class="footer-brand-block"><div class="footer-logo">{logo_svg}<span>TreScout</span></div>'
              f'<p class="footer-tagline">{d["footer_tagline"]}</p></div>'
              f'<div class="footer-col"><div class="footer-col-title">{d["footer_urun"]}</div><ul>{urun}'
              f'<li><a href="{o}/#top">{d["nav_cta"]}</a></li></ul></div>'
              f'<div class="footer-col"><div class="footer-col-title">{d["footer_iletisim"]}</div><ul>'
              f'<li><a href="mailto:hello@trescout.com">hello@trescout.com</a></li>'
              f'<li><a href="{d["gizlilik_yolu"]}" target="_blank" rel="noopener">{d["footer_gizlilik"]}</a></li>'
              f'</ul></div>'
              f'<div class="footer-col"><div class="footer-col-title">{d["footer_sosyal"]}</div><ul>'
              f'<li><a href="https://x.com/GetTreScout" target="_blank" rel="noopener noreferrer">X / Twitter</a></li>'
              f'</ul></div></div>'
              f'<div class="footer-bottom"><span>{d["footer_alt"]}</span></div></div></footer>')
    return nav, footer


DIL_ONEK = {"TR": "", "EN": "/en", "FR": "/fr"}
_DUGME = re.compile(r'<a href="[^"]*" class="btn btn-ghost" aria-label="[^"]*">(TR|EN|FR)</a>')


def dil_dugmeleri_yaz(nav, hedefler):
    """Nav'daki dil düğmelerini SAYFAYA ÖZEL yap.

    hedefler: {"TR": "/dictionary/rag/", "EN": "/en/dictionary/rag/"} · sözlükte
    olmayan etiket olduğu gibi bırakılır. 2026-08-07'ye kadar 885 İngilizce sayfa
    kabuğun kopyalandığı örnek sayfanın bağlantısını taşıyordu
    (/dictionary/action/) · düğme sayfaya özel olmalı.
    """
    def degis(m):
        etiket = m.group(1)
        hedef = hedefler.get(etiket)
        if not hedef:
            return m.group(0)
        return f'<a href="{hedef}" class="btn btn-ghost" aria-label="{etiket}">{etiket}</a>'
    return _DUGME.sub(degis, nav)


def dil_hedefleri(bolum, slug, kok, atla=None):
    """Bir sayfanın diğer dillerdeki karşılıkları · yoksa o dilin ana sayfası.

    bolum: "dictionary" · "discover" · "reports" · "reports/fresh"
    slug : terim/araç slug'ı ya da rapor tarihi · dizin sayfasında None
    """
    import os
    TR_YOL = {"dictionary": "/dictionary", "discover": "/discover",
              "reports": "/reports", "reports/fresh": "/reports/tekrarsiz"}
    out = {}
    for etiket, onek in DIL_ONEK.items():
        if atla and etiket in atla:
            continue
        taban = TR_YOL[bolum] if onek == "" else f"{onek}/{bolum}"
        yol = f"{taban}/{slug}/" if slug else f"{taban}/"
        out[etiket] = yol if os.path.exists(os.path.join(kok, yol.strip("/"), "index.html")) \
            else (f"{onek}/" if onek else "/")
    return out


def tarih_yaz(iso, d):
    """ISO tarihi hedef dilin biçiminde yaz."""
    try:
        yil, ay, gun = iso.split("-")
        return d["tarih_bicimi"].format(ay=d["aylar"][int(ay) - 1], gun=int(gun), yil=yil)
    except Exception:
        return iso


# ── JS tarafı için köprü ──────────────────────────────────────────────────────
# `scripts/build-en.js` dizin sayfalarını basarken metinleri buradan okur ·
# tabloyu JS'e ikinci kez yazmamak için. Kullanım:
#     python3 scripts/diller.py --json fr
if __name__ == "__main__":
    import sys, json
    if "--json" in sys.argv:
        kod = sys.argv[sys.argv.index("--json") + 1]
        print(json.dumps(dil(kod), ensure_ascii=False))
    else:
        print("Kullanım: diller.py --json <dil kodu>  ·  diller:", ", ".join(DILLER))
