# Weights nedir?

**Kategori:** Yapay Zekâ  
**Son güncelleme:** 2026-09-27

Yapay zekâ modellerinin eğitim sırasında öğrendiği ve kararlarını şekillendiren sayısal değerlerdir.

## Tanım
Bir yapay zekâ modelinin beynindeki sinaps bağlantılarının gücünü temsil eden devasa sayı tablolarıdır. Model eğitilirken bu sayılar sürekli güncellenir ve hangi bilginin ne kadar önemli olduğu bu sayede belirlenir. Modelin bir girdiyi alıp doğru bir çıktı üretmesini sağlayan asıl bilgi birikimi bu değerlerde saklıdır.

## Bir benzetmeyle
Bir yemeğin tarifindeki malzemelerin hassas ölçülerine benzer. Hangi malzemeden kaç gram koyacağınız yemeğin tadını belirler; yapay zekâdaki sayılar da kararların doğruluğunu belirler.

## Nasıl çalışır?
Model milyonlarca veriyle eğitilirken her hata yaptığında bu sayısal değerler küçük miktarlarda ayarlanır. Eğitim bittiğinde bu değerler sabitlenir ve model artık yeni gelen sorulara bu optimize edilmiş sayılar üzerinden yanıt verir.

## Nerede kullanılır?
Büyük dil modellerinin yani LLM indirilip bilgisayarda çalıştırılabilen dosyalarında, örneğin GGUF formatlarında doğrudan bu sayısal veriler yer alır.

## Sık karıştırılanlar
Model mimarisi ile karıştırılır. Mimari, boş bir binanın odalarının planı gibidir; ağırlıklar ise o odaların içine yerleştirilen ve binayı yaşanabilir kılan eşyalardır.

## Sıkça sorulanlar

**Bu sayısal değerleri elle değiştirebilir miyiz?**  
Teorik olarak mümkündür ancak milyarlarca parametre olduğu için bunu elle yapmak yerine bilgisayarların otomatik olarak eğitmesi tercih edilir.

**Açık kaynaklı modellerde bu değerler paylaşılır mı?**  
Evet, açık ağırlıklı yani open weights modellerde bu sayısal değerler herkesin indirip kullanabilmesi için halka açık olarak sunulur.

## İlgili terimler
- [Open Weights](/dictionary/open-weights/)
- [LLM](/dictionary/llm/)
- [Fine-tuning](/dictionary/fine-tuning/)
- [GGUF](/dictionary/gguf/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/weights/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
