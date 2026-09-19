# Patent disclosure nedir, ne demek?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-20

Patent disclosure (patent açıklaması veya buluş bildirimi), bir buluşun patent koruması alabilmesi için teknik çalışma prensiplerinin, yenilikçi iddialarının ve uygulama yöntemlerinin yasal şartnamede kamuya açıkça beyan edilmesidir.

## Etimoloji ve Toplumsal Takas İlkesi
Patent disclosure kavramı, fikri mülkiyet hukukunun ve modern sanayinin temelindeki "toplumsal takas" prensibine dayanır. Devletler veya tescil ofisleri (USPTO, EPO, TürkPatent), mucide veya şirkete buluşu üzerinde 20 yıllık bir tekel ve ticari koruma hakkı tanır. Ancak bu ayrıcalığın karşılığında mucidin, buluşunu bir sır olarak saklamaktan vazgeçmesi ve o alandaki uzman bir mühendisin (person skilled in the art) aynısını yapıp uygulayabileceği açıklıkta detaylandırması şart koşulur.

Yazılım, yapay zekâ ve bilgisayar bilimleri alanında patent disclosure süreci, şirketlerin AR-GE ekipleriyle patent vekilleri arasındaki İcat Bildirim Formu (Invention Disclosure Form - IDF) ile başlar. Yazılımın saf bir matematiksel algoritma mı yoksa somut bir teknik problemi çözen yeni bir sistem mimarisi mi olduğu bu süreçte analiz edilir. Yetersiz veya muğlak bir patent disclosure, başvurunun doğrudan reddedilmesine ya da patentin gelecekte mahkemelerde kolayca geçersiz kılınmasına neden olur.

## Bir Benzetmeyle: Fırıncılar Loncasının Açık Tarifi
Şöyle düşünün: Bir aşçının kimsenin bilmediği sihirli bir ekmek pişirme tekniği geliştirdiğini hayal edin. Aşçı bu tekniği sır olarak saklarsa (ticari sır - trade secret), bir rakibi tekniği çözdüğünde hiçbir yasal hak iddia edemez. Patent disclosure ise aşçının yerel fırıncılar loncasına gidip fırının ısısından mayalanma süresine, un oranlarından pişirme kabına kadar tüm tarifi harfi harfine açıklaması gibidir. Lonca bu açık tarif karşılığında aşçıya 20 yıl boyunca o ekmeği sadece kendisinin satabileceğini garanti eder. 20 yılın sonunda ise tarif tüm insanlığın ortak mirası haline gelir ve herkes o ekmeği pişirebilir. Patent disclosure, tekel hakkı kazanmak için sırrı kamuyla paylaşma taahhüdüdür.

## Teknik ve Hukuki Sistem Mimarisi
Teknik düzeyde eksiksiz bir patent disclosure süreci dört aşamalı bir mimari üzerine kuruludur:

1. İcat Bildirim Formu (Invention Disclosure Form - IDF): Mühendisler ve araştırmacılar yeni bir sistem (örneğin yeni bir önbellek algoritması veya dağıtık veri modeli) geliştirdiğinde ilk resmi adımı atar. Formda çözülen teknik problem, mevcut yöntemlerin yetersiz kaldığı noktalar ve buluşun getirdiği yenilikçi mekanizma şemalarla belgelenir.

2. Mevcut Tekniğin Durumu (Prior Art) Analizi: Buluşun gerçekten yeni (novel) ve buluş basamağına (inventive step / non-obviousness) sahip olup olmadığını anlamak için dünya genelindeki tüm akademik yayınlar, açık kaynak kod depoları ve tescilli patentler taranır.

3. Yazılım Patentlenebilirliği ve Alice Kriterleri: Yazılım dünyasında saf matematiksel formüller veya soyut fikirler (abstract ideas) patentlenemez (Alice Corp. v. CLS Bank emsal davası). Patent disclosure metni, yazılımın donanım kaynaklarını (CPU, bellek, ağ trafiği) nasıl daha verimli hale getirdiğini veya somut bir teknik iyileştirme sağladığını kesin teknik terimlerle kanıtlamalıdır.

4. İstemler (Claims) ve Spesifikasyon Mimarisi: Patent metni iki kısımdan oluşur: Buluşun çalışma mantığını anlatan detaylı açıklama (specification) ve yasal koruma sınırlarını çizen istemler (claims). Bağımsız istemler buluşun en geniş halini korurken, bağımlı istemler spesifik varyasyonları zırhlandırır.

## Sosyolojik Boyut: Açık İnovasyon ve Fikri Mülkiyet Dengesi
Patent disclosure, teknolojik ilerleme ile ekonomik tekel arasındaki hassas dengeyi temsil eder. Eğer patent disclosure yükümlülüğü olmasaydı, şirketler geliştirdikleri tüm kritik teknolojileri ticari sır olarak kilitli kasalarda saklar, inovasyon silolar halinde hapsolurdu. 

Buna karşılık yazılım dünyasında açık kaynak hareketi (FOSS) ile patent sistemi arasında tarihsel bir gerilim vardır. Büyük teknoloji şirketleri bazen rakiplerini boğmak için patent trolleri (NPE) aracılığıyla savunmacı veya saldırgan patent portföyleri kurar. Bu gerilimi aşmak için Apache 2.0 ve GPLv3 gibi açık kaynak lisansları açık patent koruma maddeleri içerir; ayrıca Open Invention Network (OIN) gibi konsorsiyumlar açık kaynak yazılımları patent davalarına karşı korur.

## Sık Yapılan Hatalar ve Yanılgılar
Patent disclosure sürecinde en sık yapılan kritik hatalar şunlardır:
- Erken Kamuya Açıklama (Premature Disclosure): Resmi patent başvurusu yapılmadan önce teknolojinin bir konferansta anlatılması, blog yazısında paylaşılması veya GitHub'da açık repo yapılması buluşun "yenilik" vasfını anında öldürür.
- Yetersiz Teknik Açıklama (Enablement Requirement İhlali): Sistemin nasıl çalıştığını eksik bırakıp sadece sonucunu yazmak patentin geçersiz kılınmasına yol açar; uzman bir mühendisin uygulayabileceği detay verilmelidir.
- Yanlış veya Eksik Mucit Beyanı: Buluşun fikir aşamasında katkısı olmayan yöneticileri eklemek veya asıl kodu yazan mühendisi çıkarmak patentin yasal meşruiyetini sakatlar.

## Sıkça Sorulanlar

**Patent disclosure (buluş bildirimi) ne zaman yapılmalıdır?**  
Teknoloji kamuya, müşterilere veya açık kaynak depolara açıklanmadan önce şirket içi patent komitesine ve resmi patent ofisine yazılı olarak sunulmalıdır; aksi takdirde yenilik vasfı kaybedilir.

**Yazılım algoritmaları için patent disclosure nasıl hazırlanır?**  
Saf matematiksel kod yerine, yazılımın donanım kaynaklarını yönetme biçimi, bellek tasarrufu, veri işleme hızı veya ağ gecikmesini azaltma gibi somut teknik etkileri şemalarla açıklanarak hazırlanır.

**Ticari sır (trade secret) ile patent disclosure arasındaki fark nedir?**  
Ticari sırda algoritma veya tarif kamuoyundan tamamen gizlenir ve süresiz korunabilir; patentte ise bilgi kamuya açılır, buna karşılık devlet tarafından 20 yıllık yasal tekel koruması verilir.

**Açık kaynak projeler patent disclosure süreçlerinden nasıl etkilenir?**  
Açık kaynak lisansları (Apache 2.0 vb.) kullanıcılara patent hakkı da tanır; ayrıca GitHub'a push edilen açık kodlar anında önceki teknik (prior art) sayılarak başkalarının o fikri patentlemesini engeller.

## İlgili terimler
- [Open Source](/dictionary/open-source/)
- [Digital Privacy](/dictionary/digital-privacy/)
- [Regulatory Restriction](/dictionary/regulatory-restriction/)
- [SBOM](/dictionary/sbom/)
- [Security Scanner](/dictionary/security-scanner/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/patent-disclosure/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
