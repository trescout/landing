# Virtual Machines nedir, ne demek?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-22

Virtual machine (Türkçe karşılığıyla **sanal makine**), donanımı bölüşen bağımsız bilgisayardır.

## Tanım ve Kelime Kökeni
"Virtual" **sanal** demektir. Tek makinede çok işletim sistemi koşar. Her biri kendi kaynağıyla izole çalışır, ana sisteme zarar vermez.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Sunucu:** Çok kiracılı barındırma.
- **Test:** Farklı sistem denemesi.
- **Geliştirme:** Temiz deneme ortamı.

## Teknik Derinlik ve Mimari
Katmanlar:
- **Hipervizör:** Donanımı bölen yazılım.
- **Konuk:** Üstte koşan sistem.
- **Snapshot:** Anlık görüntü, geri dönüş bileti.

Hızlı makine:

```
multipass launch --name test --cpus 2 --memory 4G
```

Konteyner farkı: Makine sistem taşır, konteyner uygulama taşır. Yalıtım makinede güçlüdür.

## Sık Karıştırılanlar
Konteyner sanılır. Makine tam sistemdir, konteyner paylaşımlı çekirdektir. Biri daire, diğeri oda arkadaşlığıdır.

## Farklı Disiplinlerde Kullanımı
- **Odalar:** Bağımsız kapılı bölmeler.
- **Daire:** Ortak bina, özel alan.
- **Bavul:** Bölmeli taşıma.

## Bir benzetmeyle
Tek evde kapısı ayrı odalar kiralamaya benzer.

## Sıkça sorulanlar

**Yavaşlatır mı?**  
Paylaşım bedeli vardır. Doğru boyutlandırmada fark edilmez.

**Virüs geçer mi?**  
Genelde hayır. İzolasyon güçlüdür, paylaşılan klasör denetlenir.

**Ne kadar kaynak verilir?**  
İşe göre belirlenir. İzleme ile kademeli ayarlanır.

**Konteyner farkı nedir?**  
Makine sistem taşır, konteyner uygulama. Yalıtım ve hız takas edilir.

## İlgili terimler
- [Containers](/dictionary/containers/)
- [Runtime](/dictionary/runtime/)
- [Self-hosting](/dictionary/self-hosting/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/virtual-machines/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
