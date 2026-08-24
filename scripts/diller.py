#!/usr/bin/env python3
"""
TreScout · dil tabloları · çok dilli sayfa üreticilerinin tek kaynağı.

Neden ayrı dosya: 2026-08-07'ye kadar İngilizce metinler `discover-en.py` ve
`dictionary-en.py` içine serpiliydi. Üçüncü dil eklemek her iki dosyayı da
baştan okumayı gerektiriyordu. Artık dil eklemek = buraya bir sözlük eklemek.

Kaynak dil DAİMA Türkçe · sayfalar Türkçesinden üretilir, buradaki tablolar
yalnız arayüz metinlerini (başlık, düğme, uyarı) taşır. İçerik metinleri
çeviri uç noktasından geçer.

YENİ DİL EKLEME · 2026-08-15'te Almanca eklenirken güncellendi. Liste her turda
kısalıyor: artık guard'lar, normalize edicilerin atlama listeleri, kabuk
düğmeleri, elle yazılan sayfa listeleri ve YAYIN HATTI bu tablodan türüyor.
Sırayı bozmayın · 3'ten önce 4 yaparsanız keşif sayfaları çapraz bağlantısız
çıkar.

  1. Buraya tabloyu ekleyin. Dizin adı ile hreflang FARKLI olabilir:
     Portekizce dizini "pt", hreflang'i "pt-BR" ("hreflang" alanı).
     Diğer dillerin "dil_dugmeleri" listesine de yeni dili ekleyin.

  2. İstemci sözlükleri · assets/index.js · subscribe.js · discover.js ·
     dictionary.js. DİKKAT: anahtarı sayfanın <html lang>'i ile eşleşmeli ya da
     _dilSec bölge kodunu kırpabilmeli. "pt-BR" anahtarı "pt" iken sözlük
     sessizce TÜRKÇEYE düşüyordu ve aydınlatma modal'ı Türkçe metni açıyordu.

  3. Çeviri alanları: node scripts/translate-i18n.js --lang=XX
     (katalog tagline_XX + sözlük kisa_XX)

  4. Sayfalar · SIRA ÖNEMLİ, önce sözlük:
        python3 scripts/dictionary-en.py --lang=XX
        python3 scripts/discover-en.py   --lang=XX
     Keşif sayfasındaki "İlgili sözlük terimleri" bölümü o dilde sözlük sayfası
     DİSKTE varsa basılıyor · ters sırada 400+ sayfa çapraz bağlantısız çıkar.

  5. Dizinler, kapaklar, elle yazılan sayfalar:
        node scripts/build-en.js --lang=XX
        python3 scripts/kapak-gorselleri.py --lang=XX
        python3 scripts/dil-anasayfa.py --lang=XX     (küçük giriş sayfası)
     Ana sayfayı tam çevirecekseniz dil-kabuk-tazele.py'ye ve
     check-sayfa-paritesi.py'ye o dili ekleyin · karşılaştırma ve aydınlatma
     metni de elle yazılır.

  6. Rapor · trescout-app: template.ts I18N + SOURCE_LABEL_XX + formatDate,
     build-lang-report.ts DILLER, publish-report.ts RAPOR_DILLERI.
     Arşivi geriye dönük basacaksanız: build-lang-report.ts <tarihler> --lang=XX
     Sonra landing'de: node scripts/build-reports-en.js --lang=XX

  7. Hat · dict-sync.yml'ye DOKUNMAYIN. Adımlar `diller.py --liste` üzerinden
     döngüyle çalışıyor (2026-08-15'e kadar dil adları beş ayrı yerde elle
     yazılıydı · biri unutulursa o dil hatta sessizce eksik kalıyordu).

  8a. SÖZLÜK + KEŞİF TURUNU İKİ KEZ DÖNDÜRÜN. Çapraz bağlantılar karşı bölümün
     o dilde DİSKTE olmasına bakıyor: keşif → sözlük, sözlük → keşif. Yeni bir
     dilde ilk turda hangisi önce çalışırsa diğerinin bağlantıları eksik kalır ·
     2026-08-15'te 353 Almanca sözlük sayfası "İlgili araçlar" bölümü olmadan
     çıktı (hat ertesi gün düzeltirdi, o yüzden yıllardır görülmemişti).

  8b. ESKİ dillerin kabuğunu da tazeleyin · yeni dilin düğmesi onlarda YOK.
     Üretilen dillerin (en/fr/pt/es…) nav'ı diller.py'den her ÜRETİMDE
     basılıyor · yalnız yeni dili üretmek yetmez, eskileri de bir tur döndürün:
        for d in $(python3 scripts/diller.py --liste); do
          python3 scripts/dictionary-en.py --lang=$d
          python3 scripts/discover-en.py   --lang=$d
          node    scripts/build-en.js      --lang=$d
        done
     (Çeviriler önbellekli, ikinci tur hızlı. Atlarsanız nav guard kırılır ·
     hat ertesi gün kendiliğinden düzeltirdi ama PR kırmızı gelir.)

  9. Kapanış: fix-all-headers-and-footers.js → hreflang-normalize.py →
     sitemap-sync.py → llms-txt.py, sonra on guard.

KENDİLİĞİNDEN OLANLAR (elle dokunmayın):
  · nav/footer guard'ları beklenen setleri buradan türetiyor
  · normalize edicinin atlayacağı diller listesi buradan
  · fix-all-headers-and-footers.js'teki dil düğmeleri + aria etiketleri buradan
  · hreflang normalize edici ve guard'ı buradan
  · yönlendirme üreticisi ve birleşme guard'ı dil öneklerini buradan
  · dil-kabuk-tazele.py ve check-sayfa-paritesi.py'nin sayfa listeleri buradan
  · dict-sync.yml adımları `--liste` çıktısı üzerinde döngü kuruyor

ELLE KALAN İKİ ŞEY · unutulursa guard yakalamaz:
  · Ana sayfa/karşılaştırma metinleri (çeviri makineden geçerse ÖZEL ADLARI
    bozuyor). 2026-08-15 denetimi: fr/pt/es sayfalarında RAG → "chiffon/pano/
    trapo" (bez), MCP → "PCM", fine-tuning → "réglage fin", Lobste.rs →
    "Homard.rs", hello@ → "bonjour@/olá@/hola@". Yeni dilde metni ELLE yazın ·
    özel adlar (GitHub · Hacker News · HuggingFace · Lobste.rs · RAG · MCP ·
    fine-tuning · CLI · TreScout) ve e-posta adresi çevrilmez.
  · Karşılaştırma sayfasındaki "rapor şu dillerde" satırı · beş sayfada birden
    güncellenmeli. 2026-08-15'e kadar Türkçesi hâlâ "Türkçe ve İngilizce"
    diyordu, üç dil eklendiği hâlde.
"""

import re

DILLER = {
    "en": {
        "kod": "en",
        "aria_gec": "Switch to English",     # dil düğmesinin aria-label'ı · KENDİ dilinde
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
        "dil_dugmeleri": [("TR", ""), ("FR", "/fr"), ("PT", "/pt"), ("ES", "/es"), ("DE", "/de")],
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
            "Bu araç ne yapar?": "What does this tool do?",
            "Kimin için?": "Who it is for",
            "Ne beklememeli?": "What not to expect",
            "Öne çıkanlar": "Highlights",
            "İlk kullanım akışı": "First-use flow",
            "Güvenli başlangıç": "Safe start",
            "İlk görev istemi": "First task prompt",
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
        "ceviri_notu_kisa": "This page was <strong>machine-translated</strong> from the Turkish original · the Turkish version prevails.",
        "ceviri_notu": ("This explanation was written in plain language for TreScout and <strong>machine-translated</strong> from the Turkish original · the Turkish version prevails. If something looks wrong or missing, write to "),
        "rapor_cekim": "Data captured {an}",
        "rapor_cekim_not": "Sources are snapshots · this report reflects the moment above, not the whole calendar day.",
        "rapor_snapshot_notu": "Report counts and item metadata are a snapshot from the capture time above. Discovery pages may show newer live source values.",
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
            "yeni": "new",
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
        "aria_gec": "Passer au français",     # dil düğmesinin aria-label'ı · KENDİ dilinde
        "html_lang": "fr",
        "onek": "/fr",
        "og_locale": "fr_FR",
        "tagline_alan": "tagline_fr",
        "kisa_alan": "kisa_fr",
        "nav": ["Découvrir", "Glossaire", "Archive des rapports", "Comparer"],
        "nav_yollar": ["discover", "dictionary", "reports", "compare/rss-vs-ai"],
        "nav_cta": "Accès anticipé",
        "dil_dugmeleri": [("TR", ""), ("EN", "/en"), ("PT", "/pt"), ("ES", "/es"), ("DE", "/de")],
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
            "Bu araç ne yapar?": "Que fait cet outil ?",
            "Kimin için?": "Pour qui ?",
            "Ne beklememeli?": "À quoi ne faut-il pas s’attendre ?",
            "Öne çıkanlar": "Points forts",
            "İlk kullanım akışı": "Premiers pas",
            "Güvenli başlangıç": "Démarrage prudent",
            "İlk görev istemi": "Premier prompt",
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
        "ceviri_notu_kisa": "Cette page a été <strong>traduite automatiquement</strong> depuis l’original turc · la version turque fait foi.",
        "ceviri_notu": ("Cette explication a été rédigée en langage clair pour TreScout puis <strong>traduite automatiquement</strong> depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à "),
        "rapor_cekim": "Données collectées le {an}",
        "rapor_cekim_not": "Les sources sont des instantanés · ce rapport reflète le moment ci-dessus, pas la journée entière.",
        "rapor_snapshot_notu": "Les nombres et métadonnées de ce rapport sont l’instantané du moment indiqué ci-dessus. Les pages Découverte peuvent afficher des valeurs sources en direct plus récentes.",
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
            "yeni": "nouveaux",
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
    "pt": {
        "kod": "pt",
        "aria_gec": "Mudar para português",     # dil düğmesinin aria-label'ı · KENDİ dilinde
        # Brezilya Portekizcesi · geliştirici kitlesinin ağırlığı orada.
        # Dizin adı "pt", hreflang "pt-BR" · ikisi ayrı alanlar.
        "html_lang": "pt-BR",
        "hreflang": "pt-BR",
        "onek": "/pt",
        "og_locale": "pt_BR",
        "tagline_alan": "tagline_pt",
        "kisa_alan": "kisa_pt",
        "nav": ["Descobrir", "Glossário", "Arquivo de relatórios", "Comparar"],
        "nav_yollar": ["discover", "dictionary", "reports", "compare/rss-vs-ai"],
        "nav_cta": "Acesso antecipado",
        "dil_dugmeleri": [("TR", ""), ("EN", "/en"), ("FR", "/fr"), ("ES", "/es"), ("DE", "/de")],
        "footer_nasil": None,
        "footer_urun": "Produto",
        "footer_iletisim": "Contato",
        "footer_sosyal": "Redes",
        "footer_gizlilik": "Aviso de privacidade",
        "footer_tagline": "A TreScout busca, resume e entrega. Você só precisa ler.",
        "footer_alt": "© 2026 TreScout · Todos os direitos reservados.",
        "atla": "Ir para o conteúdo principal",
        "kesif": "Descobrir",
        "kesif_geri": "← Descobrir",
        "kesif_tumu": "Todas as descobertas →",
        "baglantilar": "Links",
        "depo": "Repositório no GitHub →",
        "turkce_oku": "Ler em turco →",
        "resmi_kaynak": "Fonte oficial →",
        "kopyala_komut": "Copiar comando",
        "kopyala_istem": "Copiar prompt",
        "kopyala": "Copiar",
        "ajan_istem": "🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)",
        "guncellemeler": "Atualizações",
        "yildiz": "Estrelas",
        "son_surum": "versão mais recente",
        "tasindi": "repositório movido, novo endereço",
        "arsiv": "repositório arquivado, desenvolvimento encerrado",
        "kimin_icin": "Para quem é",
        "lisans": "Licença",
        "bugun": "hoje",
        "cta_baslik": "A TreScout encontra ferramentas assim todos os dias.",
        "cta_metin": "GitHub, Hacker News e HuggingFace são vasculhados e o essencial é resumido para você.",
        "sorumluluk": ("A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do "
                       "GitHub e a apresentamos. Esta página descreve o repositório em {date}: A contagem "
                       "de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde "
                       "então. Consulte o link do repositório para ver o estado atual."),
        "trescout_notu": "Nota da TreScout:",
        "sozluk": "Glossário",
        "sozluk_geri": "← Glossário",
        "sozluk_tumu": "Todos os termos →",
        "nedir": "O que é {terim}?",
        "son_guncelleme": "Última atualização: {tarih}",
        "analoji": "Analogia:",
        "sozluk_cta_baslik": "Novos termos técnicos na sua caixa de entrada toda manhã.",
        "sozluk_cta_metin": "Entre no acesso antecipado da TreScout para receber o resumo diário.",
        "bolumler": {
            "Ne kazandırır?": "O que você ganha",
            "Kurulum": "Instalação",
            "Çalıştırma": "Execução",
            "Nasıl başlanır?": "Como começar",
            "Kod bilmiyorsanız": "Se você não programa",
            "İlgili sözlük terimleri": "Termos relacionados do glossário",
            "Bağlantılar": "Links",
            "Tanım": "Definição",
            "Nasıl çalışır?": "Como funciona",
            "Nerede kullanılır?": "Onde é usado",
            "Sık karıştırılanlar": "Costuma ser confundido com",
            "Sıkça sorulanlar": "Perguntas frequentes",
            "İlgili terimler": "Termos relacionados",
            "İlgili araçlar": "Ferramentas relacionadas",
            "Bu araç ne yapar?": "O que esta ferramenta faz?",
            "Kimin için?": "Para quem é?",
            "Ne beklememeli?": "O que não esperar",
            "Öne çıkanlar": "Destaques",
            "İlk kullanım akışı": "Primeiro fluxo de uso",
            "Güvenli başlangıç": "Início seguro",
            "İlk görev istemi": "Primeiro prompt",
        },
        "form_yer_tutucu": "Seu e-mail",
        "form_dugme": "Acesso antecipado",
        "form_onay": ('Li o <a href="{gizlilik}" target="_blank" rel="noopener">aviso de privacidade</a> '
                      "e concordo com o tratamento do meu e-mail para esta finalidade."),
        "ana_onay": ('Li o <a href="{gizlilik}" data-privacy-modal>aviso de privacidade</a> '
                     "e concordo com o tratamento do meu e-mail para esta finalidade."),
        "gizlilik_yolu": "/pt/privacy.html",
        "md_kaynak_kesif": "Fonte: TreScout Descobrir · {url}",
        "md_kaynak_sozluk": "Fonte: TreScout Glossário · {url}",
        "aylar": ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
                  "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"],
        "tarih_bicimi": "{gun} de {ay} de {yil}",
        "binlik": ".",                      # pt-BR binlik ayırıcı nokta · Türkçeyle aynı
        "etiketler": {
            "Yapay zekâ araçları": "Ferramentas de IA",
            "Geliştirici aracı": "Ferramenta de desenvolvimento",
            "Kod bilmeyenler için": "Sem código",
            "Öğrenme": "Aprendizado",
            "Üretkenlik": "Produtividade",
        },
        "sozluk_dizin_baslik": "Glossário de tecnologia · termos de IA e software · TreScout",
        "sozluk_dizin_aciklama": "Definições em linguagem simples de termos de IA e software: RAG, fine-tuning, LLM, MCP e muito mais.",
        "sozluk_dizin_h1": "Glossário de IA e software",
        "sozluk_dizin_lead": "Definições em linguagem simples para os termos técnicos de hoje. A TreScout acompanha as tendências todos os dias e amplia este glossário continuamente.",
        "sozluk_dizin_ara": "Buscar termo: RAG, embedding, fine-tuning…",
        "sozluk_dizin_ara_etiket": "Buscar termo",
        "sozluk_dizin_cipler": [("", "Todos"), ("ai", "Inteligência artificial"),
                                ("dev", "Desenvolvimento"), ("data", "Dados e infraestrutura")],
        "sozluk_dizin_birim": "termos",
        "sozluk_dizin_bos": "Nenhum termo corresponde. Tente outra busca.",
        "kesif_dizin_baslik": "Descobrir projetos open source · TreScout",
        "kesif_dizin_aciklama": "Uma seleção diária de ferramentas open source, projetos de IA e repositórios em alta no GitHub.",
        "kesif_dizin_h1": "Descubra as ferramentas em alta",
        "kesif_dizin_lead": ("Projetos open source, ferramentas de IA e frameworks encontrados todos os dias "
                             "pela TreScout: visão geral, crescimento em estrelas e <strong>como usar com um "
                             "agente.</strong>"),
        "kesif_dizin_ara": "Buscar ferramenta ou descrição…",
        "kesif_dizin_ara_etiket": "Buscar ferramenta",
        "kesif_dizin_sirala": "Ordenar",
        "kesif_dizin_siralar": [("stars", "Mais estrelas"), ("date", "Mais recentes"), ("title", "A–Z")],
        "kesif_dizin_birim": "projetos",
        "kesif_dizin_bos": "Nenhuma ferramenta corresponde. Tente outra busca.",
        "kesif_dizin_kategori": "Categorias",
        "rapor_gunler": ["domingo", "segunda-feira", "terça-feira", "quarta-feira",
                         "quinta-feira", "sexta-feira", "sábado"],
        "rapor_tarih": "{gun} de {ay} de {yil} ({gunad})",
        "rapor_arsiv_esigi": "2026-08-13",
        "rapor_rozet": "Arquivo traduzido",
        "rapor_sayfa_baslik": "{tarih} · relatório diário TreScout",
        "rapor_sayfa_aciklama": ("O relatório diário de tecnologia da TreScout de {tarih}: ferramentas open "
                                 "source, discussões do Hacker News e artigos sobre IA, selecionados e resumidos."),
        "rapor_sayfa_og": "O relatório diário de tecnologia da TreScout de {tarih}.",
        "rapor_eyebrow": "Relatório diário de tecnologia",
        "rapor_eyebrow_arsiv": "· edição traduzida",
        "rapor_arsiv": "Arquivo",
        "rapor_ac": "Abrir o PDF em {dil} →",
        "rapor_indir": "Baixar o PDF",
        "rapor_oku": "Ler →",
        "ceviri_notu_kisa": "Esta página foi <strong>traduzida automaticamente</strong> do original em turco · a versão turca é a que vale.",
        "ceviri_notu": ("Esta explicação foi escrita em linguagem simples para a TreScout e <strong>traduzida automaticamente</strong> do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para "),
        "rapor_cekim": "Dados coletados em {an}",
        "rapor_cekim_not": "As fontes são instantâneos · este relatório reflete o momento acima, não o dia inteiro.",
        "rapor_snapshot_notu": "As contagens e os metadados dos itens deste relatório são o instantâneo do momento indicado acima. As páginas de Descoberta podem mostrar valores de fontes ao vivo mais recentes.",
        "rapor_dil_adi": "português",
        "rapor_not": ("PDF completo: cada item com seu resumo, os links das fontes e o glossário de termos. "
                      "Traduzido da edição original em turco."),
        "rapor_cta": ("<strong>Receba o relatório diário na sua caixa de entrada.</strong> A TreScout busca, "
                      "resume e entrega. Você só precisa ler."),
        "rapor_cta_dugme": "Entrar no acesso antecipado →",
        "rapor_banner_baslik": "Sobre este arquivo traduzido",
        "rapor_banner": ("Estas páginas e os PDFs são traduzidos dos relatórios diários originais em turco. "
                         "A seleção dos itens, as métricas e os links são idênticos à edição turca."),
        "rapor_cipler": {
            "Günün Modelleri": "modelos do dia",
            "Günün Makaleleri": "artigos do dia",
            "öne çıkan": "em destaque",
            "yeni": "novos",
        },
        "rapor_varyant": {
            "normal": {
                "geri": "Todos os relatórios",
                "baslik": "Relatórios diários de tecnologia",
                "intro": ("Todos os dias, um resumo das tendências do GitHub Trending, Hacker News, "
                          "HuggingFace e Lobsters. Leia online ou baixe o PDF."),
                "dizin_baslik": "Arquivo de relatórios diários · TreScout",
                "dizin_aciklama": ("O arquivo de relatórios diários de tecnologia da TreScout · as tendências "
                                   "do GitHub, Hacker News e HuggingFace, resumidas todos os dias."),
            },
            "fresh": {
                "geri": "Somente novidades",
                "baslik": "Relatórios · somente novidades",
                "intro": ("Apenas o que é novo hoje. Repositórios já cobertos nos últimos 30 dias ficam de "
                          "fora, nada se repete."),
                "dizin_baslik": "Arquivo de relatórios · somente novidades · TreScout",
                "dizin_aciklama": "Os relatórios diários da TreScout, sem nada que já tenha sido coberto.",
            },
        },
        "onay_ipucu": "Leia o aviso de privacidade para dar o seu consentimento.",
        "modal_baslik": "Aviso de privacidade",
        "modal_kapat": "Fechar",
        "modal_kaydir": "Role até o fim do texto para dar o seu consentimento",
        "modal_onayla": "Li e concordo",
        "ana_h1": "Acompanhar tecnologia não é mais um fardo.",
        "ana_lead": ("Todos os dias, a TreScout percorre GitHub, Hacker News, HuggingFace e Lobsters, "
                     "retém o que importa e reúne tudo em um único relatório."),
        "ana_bolum": "O que você encontra aqui",
        "ana_kartlar": [
            ("Descobrir", "/pt/discover/", "As ferramentas open source encontradas todos os dias, explicadas de forma simples."),
            ("Glossário", "/pt/dictionary/", "Os termos técnicos de hoje, definidos em linguagem simples."),
        ],
        "ana_kayit": "Receba o relatório diário assim que abrirmos.",
        "ana_not": ("As páginas em português são traduzidas automaticamente a partir do original em turco · "
                    "em caso de dúvida, a versão turca prevalece."),
    },
    "es": {
        "kod": "es",
        "aria_gec": "Cambiar a español",     # dil düğmesinin aria-label'ı · KENDİ dilinde
        # Nötr İspanyolca · İspanya ve Latin Amerika arasında Portekizcedeki
        # gibi net bir ağırlık yok, tek sürüm ikisine de hitap ediyor.
        "html_lang": "es",
        "hreflang": "es",
        "onek": "/es",
        "og_locale": "es_ES",
        "tagline_alan": "tagline_es",
        "kisa_alan": "kisa_es",
        "nav": ["Descubrir", "Glosario", "Archivo de informes", "Comparar"],
        "nav_yollar": ["discover", "dictionary", "reports", "compare/rss-vs-ai"],
        "nav_cta": "Acceso anticipado",
        "dil_dugmeleri": [("TR", ""), ("EN", "/en"), ("FR", "/fr"), ("PT", "/pt"), ("DE", "/de")],
        "footer_nasil": None,
        "footer_urun": "Producto",
        "footer_iletisim": "Contacto",
        "footer_sosyal": "Redes",
        "footer_gizlilik": "Aviso de privacidad",
        "footer_tagline": "TreScout rastrea, resume y entrega. Usted solo lee.",
        "footer_alt": "© 2026 TreScout · Todos los derechos reservados.",
        "atla": "Ir al contenido principal",
        "kesif": "Descubrir",
        "kesif_geri": "← Descubrir",
        "kesif_tumu": "Todos los descubrimientos →",
        "baglantilar": "Enlaces",
        "depo": "Repositorio en GitHub →",
        "turkce_oku": "Leer en turco →",
        "resmi_kaynak": "Fuente oficial →",
        "kopyala_komut": "Copiar comando",
        "kopyala_istem": "Copiar instrucción",
        "kopyala": "Copiar",
        "ajan_istem": "🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)",
        "guncellemeler": "Actualizaciones",
        "yildiz": "Estrellas",
        "son_surum": "última versión",
        "tasindi": "repositorio movido, nueva dirección",
        "arsiv": "repositorio archivado, desarrollo detenido",
        "kimin_icin": "Para quién es",
        "lisans": "Licencia",
        "bugun": "hoy",
        "cta_baslik": "TreScout encuentra herramientas como esta todos los días.",
        "cta_metin": "Rastreamos GitHub, Hacker News y HuggingFace, y le resumimos lo esencial.",
        "sorumluluk": ("TreScout no desarrolló esta herramienta · la encontramos en las tendencias de "
                       "GitHub y la presentamos. Esta página describe el repositorio tal como estaba el "
                       "{date}: El número de estrellas y nuestro texto son de ese día, el repositorio "
                       "puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver "
                       "el estado actual."),
        "trescout_notu": "Nota de TreScout:",
        "sozluk": "Glosario",
        "sozluk_geri": "← Glosario",
        "sozluk_tumu": "Todos los términos →",
        "nedir": "¿Qué es {terim}?",
        "son_guncelleme": "Última actualización: {tarih}",
        "analoji": "Analogía:",
        "sozluk_cta_baslik": "Nuevos términos técnicos en su bandeja de entrada cada mañana.",
        "sozluk_cta_metin": "Únase al acceso anticipado de TreScout para recibir el resumen diario.",
        "bolumler": {
            "Ne kazandırır?": "Qué aporta",
            "Kurulum": "Instalación",
            "Çalıştırma": "Ejecución",
            "Nasıl başlanır?": "Cómo empezar",
            "Kod bilmiyorsanız": "Si no programa",
            "İlgili sözlük terimleri": "Términos relacionados del glosario",
            "Bağlantılar": "Enlaces",
            "Tanım": "Definición",
            "Nasıl çalışır?": "Cómo funciona",
            "Nerede kullanılır?": "Dónde se usa",
            "Sık karıştırılanlar": "Suele confundirse con",
            "Sıkça sorulanlar": "Preguntas frecuentes",
            "İlgili terimler": "Términos relacionados",
            "İlgili araçlar": "Herramientas relacionadas",
            "Bu araç ne yapar?": "¿Qué hace esta herramienta?",
            "Kimin için?": "¿Para quién es?",
            "Ne beklememeli?": "Qué no esperar",
            "Öne çıkanlar": "Aspectos destacados",
            "İlk kullanım akışı": "Primer flujo de uso",
            "Güvenli başlangıç": "Inicio seguro",
            "İlk görev istemi": "Primer prompt",
        },
        "form_yer_tutucu": "Su correo electrónico",
        "form_dugme": "Acceso anticipado",
        "form_onay": ('He leído el <a href="{gizlilik}" target="_blank" rel="noopener">aviso de privacidad</a> '
                      "y acepto que mi correo se trate con esta finalidad."),
        "ana_onay": ('He leído el <a href="{gizlilik}" data-privacy-modal>aviso de privacidad</a> '
                     "y acepto que mi correo se trate con esta finalidad."),
        "gizlilik_yolu": "/es/privacy.html",
        "md_kaynak_kesif": "Fuente: TreScout Descubrir · {url}",
        "md_kaynak_sozluk": "Fuente: TreScout Glosario · {url}",
        "aylar": ["enero", "febrero", "marzo", "abril", "mayo", "junio",
                  "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"],
        "tarih_bicimi": "{gun} de {ay} de {yil}",
        "binlik": ".",                      # İspanyolcada binlik ayırıcı nokta
        "etiketler": {
            "Yapay zekâ araçları": "Herramientas de IA",
            "Geliştirici aracı": "Herramienta de desarrollo",
            "Kod bilmeyenler için": "Sin código",
            "Öğrenme": "Aprendizaje",
            "Üretkenlik": "Productividad",
        },
        "sozluk_dizin_baslik": "Glosario tecnológico · términos de IA y software · TreScout",
        "sozluk_dizin_aciklama": "Definiciones en lenguaje sencillo de términos de IA y software: RAG, fine-tuning, LLM, MCP y muchos más.",
        "sozluk_dizin_h1": "Glosario de IA y software",
        "sozluk_dizin_lead": "Definiciones en lenguaje sencillo para los términos técnicos de hoy. TreScout sigue las tendencias cada día y amplía este glosario de forma continua.",
        "sozluk_dizin_ara": "Buscar término: RAG, embedding, fine-tuning…",
        "sozluk_dizin_ara_etiket": "Buscar término",
        "sozluk_dizin_cipler": [("", "Todos"), ("ai", "Inteligencia artificial"),
                                ("dev", "Desarrollo"), ("data", "Datos e infraestructura")],
        "sozluk_dizin_birim": "términos",
        "sozluk_dizin_bos": "Ningún término coincide. Pruebe otra búsqueda.",
        "kesif_dizin_baslik": "Descubrir proyectos de código abierto · TreScout",
        "kesif_dizin_aciklama": "Una selección diaria de herramientas de código abierto, proyectos de IA y repositorios en tendencia en GitHub.",
        "kesif_dizin_h1": "Descubra las herramientas en tendencia",
        "kesif_dizin_lead": ("Proyectos de código abierto, herramientas de IA y frameworks que TreScout "
                             "encuentra cada día: presentación, crecimiento en estrellas y <strong>cómo "
                             "usarlos con un agente.</strong>"),
        "kesif_dizin_ara": "Buscar herramienta o descripción…",
        "kesif_dizin_ara_etiket": "Buscar herramienta",
        "kesif_dizin_sirala": "Ordenar",
        "kesif_dizin_siralar": [("stars", "Más estrellas"), ("date", "Más recientes"), ("title", "A–Z")],
        "kesif_dizin_birim": "proyectos",
        "kesif_dizin_bos": "Ninguna herramienta coincide. Pruebe otra búsqueda.",
        "kesif_dizin_kategori": "Categorías",
        "rapor_gunler": ["domingo", "lunes", "martes", "miércoles",
                         "jueves", "viernes", "sábado"],
        "rapor_tarih": "{gun} de {ay} de {yil} ({gunad})",
        "rapor_arsiv_esigi": "2026-08-14",
        "rapor_rozet": "Archivo traducido",
        "rapor_sayfa_baslik": "{tarih} · informe diario de TreScout",
        "rapor_sayfa_aciklama": ("El informe diario de tecnología de TreScout del {tarih}: herramientas de "
                                 "código abierto, discusiones de Hacker News y artículos sobre IA, "
                                 "seleccionados y resumidos."),
        "rapor_sayfa_og": "El informe diario de tecnología de TreScout del {tarih}.",
        "rapor_eyebrow": "Informe diario de tecnología",
        "rapor_eyebrow_arsiv": "· edición traducida",
        "rapor_arsiv": "Archivo",
        "rapor_ac": "Abrir el PDF en {dil} →",
        "rapor_indir": "Descargar el PDF",
        "rapor_oku": "Leer →",
        "ceviri_notu_kisa": "Esta página se <strong>tradujo automáticamente</strong> del original en turco · prevalece la versión turca.",
        "ceviri_notu": ("Esta explicación se redactó en lenguaje sencillo para TreScout y se <strong>tradujo automáticamente</strong> del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a "),
        "rapor_cekim": "Datos recogidos el {an}",
        "rapor_cekim_not": "Las fuentes son instantáneas · este informe refleja el momento indicado, no el día entero.",
        "rapor_snapshot_notu": "Los recuentos y metadatos de los elementos de este informe corresponden al instante indicado arriba. Las páginas de Descubrimiento pueden mostrar valores de fuentes en vivo más recientes.",
        "rapor_dil_adi": "español",
        "rapor_not": ("PDF completo: cada elemento con su resumen, los enlaces de las fuentes y el glosario "
                      "de términos. Traducido de la edición original en turco."),
        "rapor_cta": ("<strong>Reciba el informe diario en su bandeja de entrada.</strong> TreScout "
                      "rastrea, resume y entrega. Usted solo lee."),
        "rapor_cta_dugme": "Unirse al acceso anticipado →",
        "rapor_banner_baslik": "Sobre este archivo traducido",
        "rapor_banner": ("Estas páginas y los PDF están traducidos de los informes diarios originales en "
                         "turco. La selección de elementos, las métricas y los enlaces son idénticos a la "
                         "edición turca."),
        "rapor_cipler": {
            "Günün Modelleri": "modelos del día",
            "Günün Makaleleri": "artículos del día",
            "öne çıkan": "destacados",
            "yeni": "nuevos",
        },
        "rapor_varyant": {
            "normal": {
                "geri": "Todos los informes",
                "baslik": "Informes diarios de tecnología",
                "intro": ("Cada día, un resumen de las tendencias de GitHub Trending, Hacker News, "
                          "HuggingFace y Lobsters. Léalo en línea o descargue el PDF."),
                "dizin_baslik": "Archivo de informes diarios · TreScout",
                "dizin_aciklama": ("El archivo de informes diarios de tecnología de TreScout · las "
                                   "tendencias de GitHub, Hacker News y HuggingFace, resumidas cada día."),
            },
            "fresh": {
                "geri": "Solo novedades",
                "baslik": "Informes · solo novedades",
                "intro": ("Solo lo nuevo de hoy. Los repositorios ya tratados en los últimos 30 días "
                          "quedan fuera, nada se repite."),
                "dizin_baslik": "Archivo de informes · solo novedades · TreScout",
                "dizin_aciklama": "Los informes diarios de TreScout, sin nada que ya se haya tratado.",
            },
        },
        "onay_ipucu": "Lea el aviso de privacidad para dar su consentimiento.",
        "modal_baslik": "Aviso de privacidad",
        "modal_kapat": "Cerrar",
        "modal_kaydir": "Desplácese hasta el final del texto para dar su consentimiento",
        "modal_onayla": "Lo he leído y acepto",
        "ana_h1": "Seguir la tecnología ya no es una carga.",
        "ana_lead": ("Cada día, TreScout recorre GitHub, Hacker News, HuggingFace y Lobsters, se queda "
                     "con lo que importa y lo reúne en un solo informe."),
        "ana_bolum": "Lo que encontrará aquí",
        "ana_kartlar": [
            ("Descubrir", "/es/discover/", "Las herramientas de código abierto que encontramos cada día, explicadas con sencillez."),
            ("Glosario", "/es/dictionary/", "Los términos técnicos de hoy, definidos en lenguaje sencillo."),
        ],
        "ana_kayit": "Reciba el informe diario en cuanto abramos.",
        "ana_not": ("Las páginas en español se traducen automáticamente desde el original en turco · "
                    "en caso de duda, prevalece la versión turca."),
    },
    "de": {
        "kod": "de",
        "aria_gec": "Auf Deutsch wechseln",     # dil düğmesinin aria-label'ı · KENDİ dilinde
        # Standarddeutsch · Almanya, Avusturya ve İsviçre'yi birlikte kapsıyor.
        # "Sie" (formal) kullanılıyor · markanın Türkçedeki "siz" tonuyla birebir.
        "html_lang": "de",
        "hreflang": "de",
        "onek": "/de",
        "og_locale": "de_DE",
        "tagline_alan": "tagline_de",
        "kisa_alan": "kisa_de",
        "nav": ["Entdecken", "Glossar", "Berichtsarchiv", "Vergleich"],
        "nav_yollar": ["discover", "dictionary", "reports", "compare/rss-vs-ai"],
        "nav_cta": "Vorabzugang",
        "dil_dugmeleri": [("TR", ""), ("EN", "/en"), ("FR", "/fr"), ("PT", "/pt"), ("ES", "/es")],
        "footer_nasil": None,
        "footer_urun": "Produkt",
        "footer_iletisim": "Kontakt",
        "footer_sosyal": "Netzwerke",
        "footer_gizlilik": "Datenschutzhinweis",
        "footer_tagline": "TreScout durchsucht, fasst zusammen und liefert. Sie lesen nur.",
        "footer_alt": "© 2026 TreScout · Alle Rechte vorbehalten.",
        "atla": "Zum Hauptinhalt springen",
        "kesif": "Entdecken",
        "kesif_geri": "← Entdecken",
        "kesif_tumu": "Alle Entdeckungen →",
        "baglantilar": "Links",
        "depo": "GitHub-Repository →",
        "turkce_oku": "Auf Türkisch lesen →",
        "resmi_kaynak": "Offizielle Quelle →",
        "kopyala_komut": "Befehl kopieren",
        "kopyala_istem": "Anweisung kopieren",
        "kopyala": "Kopieren",
        "ajan_istem": "🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)",
        "guncellemeler": "Aktualisierungen",
        "yildiz": "Sterne",
        "son_surum": "neueste Version",
        "tasindi": "Repository verschoben, neue Adresse",
        "arsiv": "Repository archiviert, Entwicklung eingestellt",
        "kimin_icin": "Für wen es gedacht ist",
        "lisans": "Lizenz",
        "bugun": "heute",
        "cta_baslik": "TreScout findet jeden Tag Werkzeuge wie dieses.",
        "cta_metin": "Wir durchsuchen GitHub, Hacker News und HuggingFace und fassen das Wesentliche für Sie zusammen.",
        "sorumluluk": ("TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends "
                       "gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am "
                       "{date} war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das "
                       "Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über "
                       "den Link zum Repository."),
        "trescout_notu": "Hinweis von TreScout:",
        "sozluk": "Glossar",
        "sozluk_geri": "← Glossar",
        "sozluk_tumu": "Alle Begriffe →",
        "nedir": "Was ist {terim}?",
        "son_guncelleme": "Zuletzt aktualisiert: {tarih}",
        "analoji": "Analogie:",
        "sozluk_cta_baslik": "Jeden Morgen neue Fachbegriffe in Ihrem Postfach.",
        "sozluk_cta_metin": "Sichern Sie sich den Vorabzugang zu TreScout und erhalten Sie die tägliche Zusammenfassung.",
        "bolumler": {
            "Ne kazandırır?": "Was es bringt",
            "Kurulum": "Installation",
            "Çalıştırma": "Ausführung",
            "Nasıl başlanır?": "So fangen Sie an",
            "Kod bilmiyorsanız": "Wenn Sie nicht programmieren",
            "İlgili sözlük terimleri": "Verwandte Begriffe aus dem Glossar",
            "Bağlantılar": "Links",
            "Tanım": "Definition",
            "Nasıl çalışır?": "So funktioniert es",
            "Nerede kullanılır?": "Wo es eingesetzt wird",
            "Sık karıştırılanlar": "Häufig verwechselt mit",
            "Sıkça sorulanlar": "Häufige Fragen",
            "İlgili terimler": "Verwandte Begriffe",
            "İlgili araçlar": "Verwandte Werkzeuge",
            "Bu araç ne yapar?": "Was macht dieses Werkzeug?",
            "Kimin için?": "Für wen ist es?",
            "Ne beklememeli?": "Was Sie nicht erwarten sollten",
            "Öne çıkanlar": "Höhepunkte",
            "İlk kullanım akışı": "Ablauf für die erste Nutzung",
            "Güvenli başlangıç": "Sicherer Start",
            "İlk görev istemi": "Erster Prompt",
        },
        "form_yer_tutucu": "Ihre E-Mail-Adresse",
        "form_dugme": "Vorabzugang",
        "form_onay": ('Ich habe den <a href="{gizlilik}" target="_blank" rel="noopener">Datenschutzhinweis</a> '
                      "gelesen und bin damit einverstanden, dass meine E-Mail-Adresse zu diesem Zweck "
                      "verarbeitet wird."),
        "ana_onay": ('Ich habe den <a href="{gizlilik}" data-privacy-modal>Datenschutzhinweis</a> '
                     "gelesen und bin damit einverstanden, dass meine E-Mail-Adresse zu diesem Zweck "
                     "verarbeitet wird."),
        "gizlilik_yolu": "/de/privacy.html",
        "md_kaynak_kesif": "Quelle: TreScout Entdecken · {url}",
        "md_kaynak_sozluk": "Quelle: TreScout Glossar · {url}",
        "aylar": ["Januar", "Februar", "März", "April", "Mai", "Juni",
                  "Juli", "August", "September", "Oktober", "November", "Dezember"],
        "tarih_bicimi": "{gun}. {ay} {yil}",
        "binlik": ".",                      # Almancada binlik ayırıcı nokta
        "etiketler": {
            "Yapay zekâ araçları": "KI-Werkzeuge",
            "Geliştirici aracı": "Entwicklerwerkzeug",
            "Kod bilmeyenler için": "Ohne Programmieren",
            "Öğrenme": "Lernen",
            "Üretkenlik": "Produktivität",
        },
        "sozluk_dizin_baslik": "Technik-Glossar · KI- und Software-Begriffe · TreScout",
        "sozluk_dizin_aciklama": "Verständliche Definitionen für KI- und Software-Begriffe: RAG, Fine-Tuning, LLM, MCP und viele mehr.",
        "sozluk_dizin_h1": "Glossar für KI und Software",
        "sozluk_dizin_lead": "Verständliche Definitionen für die Fachbegriffe von heute. TreScout verfolgt die Trends jeden Tag und erweitert dieses Glossar fortlaufend.",
        "sozluk_dizin_ara": "Begriff suchen: RAG, Embedding, Fine-Tuning…",
        "sozluk_dizin_ara_etiket": "Begriff suchen",
        "sozluk_dizin_cipler": [("", "Alle"), ("ai", "Künstliche Intelligenz"),
                                ("dev", "Entwicklung"), ("data", "Daten und Infrastruktur")],
        "sozluk_dizin_birim": "Begriffe",
        "sozluk_dizin_bos": "Kein Begriff passt dazu. Versuchen Sie eine andere Suche.",
        "kesif_dizin_baslik": "Open-Source-Projekte entdecken · TreScout",
        "kesif_dizin_aciklama": "Eine tägliche Auswahl an Open-Source-Werkzeugen, KI-Projekten und Repositorys aus den GitHub-Trends.",
        "kesif_dizin_h1": "Entdecken Sie die Werkzeuge im Trend",
        "kesif_dizin_lead": ("Open-Source-Projekte, KI-Werkzeuge und Frameworks, die TreScout jeden Tag "
                             "findet: Vorstellung, Wachstum der Sterne und <strong>wie Sie sie mit einem "
                             "Agenten nutzen.</strong>"),
        "kesif_dizin_ara": "Werkzeug oder Beschreibung suchen…",
        "kesif_dizin_ara_etiket": "Werkzeug suchen",
        "kesif_dizin_sirala": "Sortieren",
        "kesif_dizin_siralar": [("stars", "Meiste Sterne"), ("date", "Neueste"), ("title", "A–Z")],
        "kesif_dizin_birim": "Projekte",
        "kesif_dizin_bos": "Kein Werkzeug passt dazu. Versuchen Sie eine andere Suche.",
        "kesif_dizin_kategori": "Kategorien",
        "rapor_gunler": ["Sonntag", "Montag", "Dienstag", "Mittwoch",
                         "Donnerstag", "Freitag", "Samstag"],
        "rapor_tarih": "{gun}. {ay} {yil} ({gunad})",
        "rapor_arsiv_esigi": "2026-08-15",
        "rapor_rozet": "Übersetztes Archiv",
        "rapor_sayfa_baslik": "{tarih} · Tagesbericht von TreScout",
        "rapor_sayfa_aciklama": ("Der Technik-Tagesbericht von TreScout vom {tarih}: Open-Source-Werkzeuge, "
                                 "Diskussionen auf Hacker News und Beiträge über künstliche Intelligenz, "
                                 "ausgewählt und zusammengefasst."),
        "rapor_sayfa_og": "Der Technik-Tagesbericht von TreScout vom {tarih}.",
        "rapor_eyebrow": "Technik-Tagesbericht",
        "rapor_eyebrow_arsiv": "· übersetzte Ausgabe",
        "rapor_arsiv": "Archiv",
        "rapor_ac": "PDF auf {dil} öffnen →",
        "rapor_indir": "PDF herunterladen",
        "rapor_oku": "Lesen →",
        "ceviri_notu_kisa": "Diese Seite wurde <strong>maschinell übersetzt</strong> aus dem türkischen Original · maßgeblich ist die türkische Fassung.",
        "ceviri_notu": ("Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und <strong>maschinell übersetzt</strong> aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an "),
        "rapor_cekim": "Daten erfasst am {an}",
        "rapor_cekim_not": "Die Quellen sind Momentaufnahmen · dieser Bericht gibt den oben genannten Zeitpunkt wieder, nicht den ganzen Kalendertag.",
        "rapor_snapshot_notu": "Die Zählungen und Metadaten dieses Berichts sind eine Momentaufnahme des oben genannten Zeitpunkts. Die Entdeckungsseiten können neuere Live-Werte der Quellen anzeigen.",
        "rapor_dil_adi": "Deutsch",
        "rapor_not": ("Vollständiges PDF: jeder Eintrag mit Zusammenfassung, die Links zu den Quellen und "
                      "das Glossar der Begriffe. Übersetzt aus der türkischen Originalausgabe."),
        "rapor_cta": ("<strong>Erhalten Sie den Tagesbericht in Ihr Postfach.</strong> TreScout "
                      "durchsucht, fasst zusammen und liefert. Sie lesen nur."),
        "rapor_cta_dugme": "Vorabzugang sichern →",
        "rapor_banner_baslik": "Über dieses übersetzte Archiv",
        "rapor_banner": ("Diese Seiten und die PDF-Dateien sind aus den türkischen Original-Tagesberichten "
                         "übersetzt. Die Auswahl der Einträge, die Kennzahlen und die Links sind mit der "
                         "türkischen Ausgabe identisch."),
        "rapor_cipler": {
            "Günün Modelleri": "Modelle des Tages",
            "Günün Makaleleri": "Beiträge des Tages",
            "öne çıkan": "hervorgehoben",
            "yeni": "neu",
        },
        "rapor_varyant": {
            "normal": {
                "geri": "Alle Berichte",
                "baslik": "Technik-Tagesberichte",
                "intro": ("Jeden Tag eine Zusammenfassung der Trends von GitHub Trending, Hacker News, "
                          "HuggingFace und Lobsters. Online lesen oder als PDF herunterladen."),
                "dizin_baslik": "Archiv der Tagesberichte · TreScout",
                "dizin_aciklama": ("Das Archiv der Technik-Tagesberichte von TreScout · die Trends von "
                                   "GitHub, Hacker News und HuggingFace, jeden Tag zusammengefasst."),
            },
            "fresh": {
                "geri": "Nur Neues",
                "baslik": "Berichte · nur Neues",
                "intro": ("Nur das Neue von heute. Repositorys, die in den letzten 30 Tagen schon "
                          "vorkamen, bleiben draußen, nichts wiederholt sich."),
                "dizin_baslik": "Berichtsarchiv · nur Neues · TreScout",
                "dizin_aciklama": "Die Tagesberichte von TreScout, ohne alles, was schon vorkam.",
            },
        },
        "onay_ipucu": "Lesen Sie den Datenschutzhinweis, um Ihre Einwilligung zu geben.",
        "modal_baslik": "Datenschutzhinweis",
        "modal_kapat": "Schließen",
        "modal_kaydir": "Scrollen Sie bis zum Ende des Textes, um Ihre Einwilligung zu geben",
        "modal_onayla": "Ich habe es gelesen und stimme zu",
        "ana_h1": "Technik zu verfolgen ist keine Last mehr.",
        "ana_lead": ("Jeden Tag durchsucht TreScout GitHub, Hacker News, HuggingFace und Lobsters, behält "
                     "das Wesentliche und fasst es in einem einzigen Bericht zusammen."),
        "ana_bolum": "Was Sie hier finden",
        "ana_kartlar": [
            ("Entdecken", "/de/discover/", "Die Open-Source-Werkzeuge, die wir jeden Tag finden, verständlich erklärt."),
            ("Glossar", "/de/dictionary/", "Die Fachbegriffe von heute, in verständlicher Sprache erklärt."),
        ],
        "ana_kayit": "Erhalten Sie den Tagesbericht, sobald wir öffnen.",
        "ana_not": ("Die deutschen Seiten werden maschinell aus dem türkischen Original übersetzt · "
                    "im Zweifelsfall gilt die türkische Fassung."),
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


DIL_ONEK = {"TR": "", "EN": "/en", "FR": "/fr", "PT": "/pt", "ES": "/es", "DE": "/de"}

# Türkçe kabuktaki dil düğmelerinin aria-label'ı · Türkçe nav Türkçe konuşur,
# İngilizce nav ise hedef dilin kendi metnini kullanır ("aria_gec").
ARIA_TR = {"en": "İngilizceye geç", "fr": "Fransızcaya geç", "pt": "Portekizceye geç",
           "es": "İspanyolcaya geç", "de": "Almancaya geç"}
_DUGME = re.compile(r'<a href="[^"]*" class="btn btn-ghost" aria-label="[^"]*">(TR|EN|FR|PT|ES|DE)</a>')


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
    if "--liste" in sys.argv:
        # Hat (dict-sync.yml) dilleri buradan okuyor · iş akışında dil adı
        # ELLE yazılmıyor. "en" dahil, üretim sırası tablodaki sıra.
        print(" ".join(DILLER))
    elif "--json" in sys.argv:
        kod = sys.argv[sys.argv.index("--json") + 1]
        print(json.dumps(dil(kod), ensure_ascii=False))
    else:
        print("Kullanım: diller.py --json <dil kodu>  ·  diller:", ", ".join(DILLER))
