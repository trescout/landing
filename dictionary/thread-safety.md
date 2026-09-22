# Thread Safety nedir, ne demek?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-22

Thread safety (Türkçe karşılığıyla **iş parçacığı güvenliği**), bir kodun aynı anda birden çok iş parçacığı tarafından çalıştırıldığında veriyi bozmamasıdır.

## Tanım ve Kelime Kökeni
"Thread" **iş parçacığı**, "safety" ise **güvenlik** demektir. Buradaki güvenlik, korsanlara karşı korunmak değil, verinin tutarlı kalmasıdır: İki işlem aynı hesabı aynı anda güncellerse sonuç yanlış çıkabilir. Thread-safe kod, bu yarışı kurallara bağlar. Bankacılık uygulamaları, web sunucuları ve çok işlemcili tüm yazılımlar buna ihtiyaç duyar.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Bankacılık:** Aynı hesaptan iki para çekme isteğinin bakiyeyi eksiye düşürmemesi.
- **Bilet satışı:** Son koltuğun iki kişiye birden satılmaması.
- **Sayaçlar:** Ziyaretçi sayacının her istekte tam bir artması.

## Teknik Derinlik ve Mimari
Tipik araçlar şunlardır:
- **Kilit (Mutex/Lock):** Kritik bölgeye aynı anda tek iş parçacığı girer, diğeri bekler.
- **Atomik işlem:** Bölünemeyen tek adımda okuma ve yazma.
- **Değişmez veri (Immutable):** Değiştirilemeyen veri yarışa girmez, kopyası çıkarılır.
- **Mesajlaşma:** Ortak veri yerine kuyruk üzerinden haberleşme (ör. Go kanalları).

Küçük bir Python örneği:

```
import threading
kilit = threading.Lock()
with kilit:
    bakiye += 100
```

Kilitli satırlar çalışırken başka iş parçacığı araya giremez. Kilit unutulursa veya yanlış sırada alınırsa program takılabilir (deadlock). Bu yüzden kritik bölge kısa tutulur.

## Sık Karıştırılanlar
Siber güvenlikle ilgili değildir. Konu korsanlar değil, veri tutarlılığıdır: Aynı veriye aynı anda dokunan iki işlemin birbirini ezmemesi.

## Farklı Disiplinlerde Kullanımı
- **Trafik:** Tek şeritli köprüde geçiş sırasını belirleyen ışıklar.
- **Mutfak:** Tek bıçağı sırayla kullanan aşçılar.
- **Kütüphane:** Tek nüsha kitabın ödünç defteriyle el değiştirmesi.

## Bir benzetmeyle
Tek tuvaletli bir evde kapıya kilit takmak gibidir; biri içerideyken diğeri beklemek zorundadır.

## Sıkça sorulanlar

**Thread-safe olmazsa ne olur?**  
Veriler karışır, hesaplar yanlış çıkar veya uygulama çöker. Hata her çalışta tekrarlanmadığı için ayıklaması zordur.

**Her koda kilit eklenmeli midir?**  
Hayır. Tek iş parçacıklı kodda kilit gereksiz yük getirir. Yalnızca ortak veriye dokunan eşzamanlı bölümler korunur.

**Deadlock nedir, nasıl önlenir?**  
İki işlemin birbirinin kilidini bekleyip takılmasıdır. Kilitleri hep aynı sırada almak ve kritik bölgeyi kısa tutmak riski azaltır.

**Test ile yakalanır mı?**  
Zor yakalanır, çünkü hata zamanlamaya bağlıdır. Yük testi ve özel yarış dedektörleri (race detector) kullanılır.

## İlgili terimler
- [Concurrency](/dictionary/concurrency/)
- [System Programming Language](/dictionary/system-programming-language/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/thread-safety/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
