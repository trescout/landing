# Open Source AI nedir, ne demek?

**Kategori:** Yapay Zekâ  
**Son güncelleme:** 2026-09-22

Open source AI (Türkçe karşılığıyla **açık kaynak yapay zekâ**), ağırlık ve kodları herkesin inceleyip çalıştırabildiği modellerdir.

## Tanım ve Kelime Kökeni
Kapalı modellerin tersine bu modeller şeffaftır: İsteyen indirir, kendi verisiyle inceler, üzerinde değişiklik yapar. Llama, Mistral ve DeepSeek bilinen örneklerdir. Eğitim verisinin de açık olması gerektiği tartışılır; OSI bu konuda ayrı bir tanım çalışması yürütür.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Yerel sohbet:** İnternetsiz çalışan kişisel asistan.
- **Araştırma:** Üzerinde deney yapılan taban model.
- **Kurumsal:** Veriyi dışarı çıkarmadan şirket içi çözüm.

## Teknik Derinlik ve Mimari
Bileşenler:
- **Ağırlıklar:** Eğitilmiş model dosyaları, Hugging Face üzerinden dağıtılır.
- **Lisans:** Apache ve MIT permissif sayılır. Bazı topluluk lisansları ticari kullanıma sınır koyar, metni okumanız gerekir.
- **Kuantizasyon:** Modelin küçültülmüş hali (GGUF), düşük bellekte çalışır.
- **Çalıştırma:** Ollama gibi araçlar tek komutla model açar:

```
ollama run llama3
```

Donanım kuralı: Parametre büyüdükçe bellek ister. Küçük modeller dizüstünde, büyükler sunucuda koşar.

## Sık Karıştırılanlar
Open Weights ile karıştırılabilir. Open Weights yalnızca ağırlıkların açık olmasıdır. Open source AI ise kod ve süreç şeffaflığını da kapsar, kapsamı daha geniştir.

## Farklı Disiplinlerde Kullanımı
- **Tarif:** Malzemesi ve ölçüsüyle paylaşılan yemek tarifi.
- **Ders kitabı:** Herkesin okuyup düzeltebildiği açık kaynak.
- **Tohum bankası:** Çiftçilerin paylaştığı ata tohumu.

## Bir benzetmeyle
Bir yemeğin gizli tarifini saklamak yerine, herkesin üzerinde denemeler yapıp geliştirebilmesi için tarifi paylaşmak gibidir.

## Sıkça sorulanlar

**Açık kaynaklı modeller daha mı zayıftır?**  
Eskiden öyleydi, ancak günümüzde birçok açık model kapalı rakipleriyle yarışır. Zirve yarışında kapalı modeller öndedir, pratik işlerde fark kapanmıştır.

**Neden açık kaynak kullanmalıyım?**  
Veri gizliliği, maliyet ve tam entegrasyon için. Veriniz dışarı çıkmaz, lisans bedeli ödemezsiniz.

**Ticari kullanım serbest mi?**  
Lisansa göre değişir. Apache ve MIT serbesttir, bazı topluluk lisansları kullanıcı sayısı veya gelir sınırı koyar.

**Hangisiyle başlanmalı?**  
Küçük ve kuantize modellerle yerelde başlayın. İhtiyaç büyürse sunucuya taşırsınız.

## İlgili terimler
- [Open Weights](/dictionary/open-weights/)
- [Self-Hosting](/dictionary/self-hosting/)
- [Open Source](/dictionary/open-source/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/open-source-ai/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
