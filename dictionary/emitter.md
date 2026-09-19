# Emitter ne demek, nedir?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

Emitter, yazılımda olayları tetikleyen (event emitter) veya derleyicilerde işlenmiş veriyi hedef çıktı formatına dönüştürüp yayan programlama bileşenidir.

## Tanım ve kullanım bağlamları
Emitter (yayıcı), yazılım mühendisliğinde iki temel mimari bağlamda kullanılır:

1. **Olay Tabanlı Mimari (Event Emitter):** Bir durum gerçekleştiğinde (örneğin bir veri paketi ulaştığında veya kullanıcı işlem yaptığında) bu olayı dinleyen tüm dinleyicilere (listeners / subscribers) sinyal ve veri aktaran mekanizmadır. Bileşenlerin birbirine sıkı bağımlı olmasını (tight coupling) engeller.
2. **Derleyici ve AST Dönüştürücüleri (Code Emitter):** Parser tarafından çözümlenip soyut sözdizimi ağacına (AST) dönüştürülen kaynak kodu alarak hedef platformun çalıştırabileceği makine koduna, baytkoda veya JSON/YAML formatına döken son aşama modülüdür.

## Bir benzetmeyle
Bir radyo vericisi gibidir; stüdyodaki sesi (işlenmiş veriyi) dalgalar halinde yayar (emit eder). Radyoyu o frekansa ayarlayan tüm alıcılar (event listener'lar) yayını anında duyar ve buna göre tepki verir.

## Nasıl çalışır?
- **Olay Yayıcılar:** Kod içerisinde `emitter.emit('veriGirdi', payload)` çağrısı yapıldığında, daha önce `emitter.on('veriGirdi', callback)` ile kayıt edilmiş tüm fonksiyonlar sıralı veya asenkron olarak tetiklenir.
- **Derleyici Yayıcılar:** Bellekteki AST ağacını düğüm düğüm dolaşarak (visitor pattern) her bir yapıyı hedef dilin veya makinenin kurallarına uygun baytlara çevirir.

## Nerede kullanılır?
Node.js çekirdek kütüphanelerinde (EventEmitter), web soket uygulamalarında, mesaj kuyruklarında (RabbitMQ, Kafka), TypeScript ve Babel gibi transpiler araçlarında yaygın olarak kullanılır.

## Sıkça sorulanlar

**Emitter ne demek ve Türkçe karşılığı nedir?**  
İngilizce 'yaymak, dışarı vermek' anlamına gelen 'emit' fiilinden türemiştir; yazılımda 'yayıcı' veya 'olay vericisi' olarak kullanılır.

**Emitter ile Parser arasındaki fark nedir?**  
Parser ham veriyi içeri alıp gramer kurallarına göre analiz eden bileşendir. Emitter ise bu analizin sonucunda ortaya çıkan soyut yapıyı hedef kitleye veya sisteme sunulabilir bir çıktıya dönüştürüp yayınlayan taraftır.

**Node.js'te EventEmitter neden bu kadar önemlidir?**  
Node.js'in asenkron, olay güdümlü (event-driven) yapısının temel omurgasını oluşturur. Dosya okuma, HTTP istekleri ve veri akışları (streams) bu mekanizmayla yönetilir.

## İlgili terimler
- [Parser](/dictionary/parser/)
- [API](/dictionary/api/)
- [Data Pipeline](/dictionary/data-pipeline/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/emitter/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
