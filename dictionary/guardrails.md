# Guardrails nedir?

*Sözlük · Yapay Zekâ · Son güncelleme: 9 Ekim 2026*

Yapay zekâ modellerinin zararlı, yanıltıcı veya belirlenen kuralların dışına çıkan çıktılar üretmesini önleyen güvenlik ve denetim sınırlarıdır.

## Tanım

Guardrails, yapay zekâ uygulamalarının kullanıcıyla etkileşiminde belirli etik, operasyonel ve yasal kurallara bağlı kalmasını sağlayan programatik denetim mekanizmalarıdır. Modelin aldığı istemleri (prompt) ve ürettiği yanıtları gerçek zamanlı olarak denetler. Zararlı içerik, hassas veri sızıntısı, konu dışına çıkma veya halüsinasyon gibi riskleri tespit ederek yanıtı engeller ya da güvenli bir çerçeveye oturtur.

*Bir virajın kenarındaki çelik bariyerlere benzer. Aracınız ne kadar hızlı giderse gitsin, yoldan çıkıp uçuruma yuvarlanmasını fiziksel olarak engeller.*

## Nasıl çalışır?

Geliştiriciler belirli kurallar, kara listeler ve anlamsal kontroller tanımlar. Kullanıcıdan gelen istek modele ulaşmadan önce bir giriş filtresinden geçer; ardından modelin ürettiği yanıt da son kullanıcıya iletilmeden önce çıkış filtresiyle taranır. Tanımlanan güvenlik eşikleri aşıldığında sistem yanıtı sansürler, önceden belirlenmiş standart bir hata mesajı döner veya modeli yeniden güvenli bir yanıt üretmeye zorlar.

## Nerede kullanılır?

Müşteri hizmetleri sohbet botlarında, finans ve sağlık gibi regülasyona tabi sektörlerde, kurumsal arama motorlarında ve otonom çalışan yapay zekâ ajanlarında yaygın olarak kullanılır.

## Sık karıştırılanlar

Modelin temel eğitimi sırasında yapılan insan geri bildirimiyle pekiştirmeli öğrenme (RLHF) ile karıştırılabilir. Temel eğitim modelin iç karakterini belirlerken, guardrails modele dışarıdan takılan bağımsız bir güvenlik kabuğudur.

## Sıkça sorulanlar

**Guardrails sistemi yanıt sürelerini belirgin şekilde yavaşlatır mı?**

Ek kontrol katmanları sisteme çok küçük bir gecikme ekler ancak hafif kurallar ve optimize edilmiş küçük modeller sayesinde bu süre kullanıcı tarafından neredeyse fark edilmez.

**Guardrails kullanmak prompt injection saldırılarını tamamen engeller mi?**

Tek başına sihirli bir çözüm değildir fakat bilinen açıkların ve komut saptırma girişimlerinin büyük bir kısmını yakalayarak risk düzeyini ciddi oranda düşürür.

## İlgili terimler

- [Prompt Injection](https://trescout.com/dictionary/prompt-injection/)
- [Red Teaming](https://trescout.com/dictionary/red-teaming/)
- [Hallucination](https://trescout.com/dictionary/hallucination/)
- [Agent Governance Toolkit](https://trescout.com/dictionary/agent-governance-toolkit/)
- [RLHF](https://trescout.com/dictionary/rlhf/)

## İlgili araçlar

- [Litellm](https://trescout.com/discover/litellm/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/guardrails/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
