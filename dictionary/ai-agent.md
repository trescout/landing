# AI Agent nedir, ne demek?

**Kategori:** Yapay Zekâ  
**Son güncelleme:** 2026-09-22

AI agent (Türkçe karşılığıyla **yapay zekâ ajanı**), hedefe ulaşmak için araç kullanan ve karar alan otonom yazılımdır.

## Tanım ve Kelime Kökeni
Sohbet robotu soruyu yanıtlar, ajan işi bitirir. Hedef verilir, adımları planlar, arama yapar, dosya okur, araç çağırır. Kendi başına görevi tamamlamaya çalışır. Bu yüzden asistanın ötesinde, çalışanın taslağıdır.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **E-posta:** Gelen kutusunu toplayıp özet çıkarma.
- **Araştırma:** Kaynak tarayıp rapor yazma.
- **Kod:** Depoda gezip yama önerme.

## Teknik Derinlik ve Mimari
Döngü şöyledir:

```
hedef → plan → araç çağır → sonucu gözle → bitir ya da revize et
```

Parçalar:
- **Planlama:** Hedefin alt görevlere bölünmesi.
- **Araçlar:** Arama, dosya, API çağrıları.
- **Hafıza:** Konuşma ve görev geçmişi.
- **İnsan onayı (HITL):** Kritik adımda durup sorma.

Kural: Yetki, görevin ciddiyetine göre verilir. Okuma serbest, yazma onaylı, ödeme çift onaylı olur.

## Sık Karıştırılanlar
Chatbot sanılır. Chatbot konuşur, ajan aksiyon alır. Sohbet arayüzü aynı görünür, arkada çalışan farklıdır.

## Farklı Disiplinlerde Kullanımı
- **Aşçı yardımcısı:** Tarifi okuyup yemeği pişirme.
- **Vale:** Anahtarı alıp işi bitirip getirme.
- **Seyahat acentesi:** Bilet, otel ve transferi toplama.

## Bir benzetmeyle
Sadece tarif veren kitap değil, mutfağa girip tarife göre yemeği pişiren, eksik malzeme varsa markete gidip alan aşçı yardımcısı gibidir.

## Sıkça sorulanlar

**Agentlar tehlikeli olabilir mi?**  
Denetimsiz bırakılırsa yanlış işlem yapabilir. Yetki kademesi ve insan onayı riski yönetir.

**Agentlar nasıl karar verir?**  
Hedef ve kurallara göre olasılık hesabı yapar, araç sonuçlarına bakarak planı günceller.

**Chatbot ile farkı nedir?**  
Chatbot yanıt üretir, ajan iş bitirir. Ajan araç çağırır ve dış dünyada değişiklik yapar.

**Hangi araçları kullanır?**  
Arama, dosya, takvim, API ve kod çalıştırma gibi tanımlı yetenekleri. Liste göreve göre açılır.

## İlgili terimler
- [Agentic AI](/dictionary/agentic-ai/)
- [AI Skills](/dictionary/ai-skills/)
- [MCP](/dictionary/mcp/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/ai-agent/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
