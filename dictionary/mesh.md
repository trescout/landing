# Mesh nedir, ne demek?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-22

Mesh (Türkçe karşılığıyla **örgü ağ**), cihaz veya hizmetlerin merkezi bir sunucuya bağlı kalmadan birbirine bağlanıp veri aktardığı ağ yapısıdır.

## Tanım ve Kelime Kökeni
"Mesh" İngilizcede **örgü, file** anlamına gelir. Balıkçı ağındaki düğümlerin birbirine bağlanması gibi, mesh ağındaki her düğüm de komşularına bağlıdır. Kablosuz ağlarda **mesh Wi-Fi**, mikro hizmet mimarilerinde ise **service mesh** (ör. Istio, Linkerd) bu kavramın iki yaygın kullanımıdır.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Evde mesh Wi-Fi:** Tek modem bir odada zayıf kalırken, eve yerleştirilen 2-3 mesh ünitesi tek bir ağ adı altında kesintisiz kapsama sağlar. Odalar arası geçerken bağlantınız kopmaz.
- **Akıllı ev:** Lamba, termostat ve sensörler birbirine bağlanır, biri kapanırsa sinyal komşu cihaz üzerinden yoluna devam eder.
- **Acil durum ağları:** Altyapının zarar gördüğü bölgelerde telefonların birbirine bağlanarak mesaj taşıması.

## Teknik Derinlik ve Mimari
Mesh yapısını ayakta tutan üç mekanizma vardır:
- **Düğüm keşfi (Discovery):** Her düğüm, çevresindeki düğümleri bulur ve bağlantı listesini güncel tutar.
- **Yönlendirme:** Veri, kaynaktan hedefe düğümden düğüme aktarılır. Bazı protokoller mesajı herkese yayar, bazıları en kısa yolu hesaplar.
- **Kendini iyileştirme:** Bir düğüm devre dışı kalırsa trafik otomatik olarak başka yola kayar. Tek bir arıza noktası bulunmaz.

Bu dayanıklılığın bir bedeli vardır: Her atlama (hop) gecikme ekler ve düğümler birbirinin trafiğini taşıdığı için toplam bant genişliği paylaşılır. Bu yüzden mesh, kapsama ve dayanıklılığın hızdan önemli olduğu yerlerde tercih edilir.

Mikro hizmetlerdeki service mesh biraz farklıdır: Servislerin yanına **sidecar** adı verilen küçük bir vekil konur. Trafik bu vekiller üzerinden akar, böylece gözlem, güvenlik ve yeniden deneme politikaları her servise ayrı kod yazmadan uygulanır.

## Farklı Disiplinlerde Kullanımı
- **Şehircilik:** Izgara planlı sokaklar. Bir cadde kapanırsa trafik komşu sokaklardan akar.
- **Tekstil:** Kumaş örgüsü. Tek iplik kopsa bile doku bütününü korur.
- **Biyoloji:** Sinir ağları. Sinyal, hasarlı bölgenin çevresinden dolanabilir.

## Bir benzetmeyle
Orkestra şefi olmadan, tüm müzisyenlerin birbirini dinleyerek uyum içinde çalması gibidir.

## Sıkça sorulanlar

**Mesh Wi-Fi ne işe yarar?**  
Evin her odasında tek ağ adıyla güçlü sinyal sağlar. Menzil genişleticilerden farkı, odalar arası geçişte bağlantıyı koparmamaya çalışmasıdır.

**Service mesh ile mesh ağ aynı şey midir?**  
Hayır. Mesh ağ, cihazların bağlantı biçimidir. Service mesh ise mikro hizmetler arası trafiği yöneten yazılım katmanıdır. İkisi de merkezsiz bağlantı fikrinden beslenir.

**Mesh her zaman daha mı iyidir?**  
Hayır. Küçük ev veya az cihazlı ortamlarda tek güçlü modem daha basit ve hızlı olabilir. Mesh, kapsama sorunu veya çok düğümlü yapılar için anlamlıdır.

**Kurulumu zor mudur?**  
Ev tipi mesh kitleri genellikle mobil uygulamayla dakikalar içinde kurulur. Kurumsal veya service mesh kurulumu ise planlama ister.

## İlgili terimler
- [Service Mesh](/dictionary/service-mesh/)
- [Network Stack](/dictionary/network-stack/)
- [Distributed](/dictionary/distributed/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/mesh/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
