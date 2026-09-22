# Compiler nedir, ne demek?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-22

Compiler (Türkçe karşılığıyla **derleyici**), yazdığınız kodu bilgisayarın çalıştırabileceği makine diline çeviren programdır.

## Tanım ve Kelime Kökeni
"Compile" **derlemek, toplamak** demektir. Bilgisayarlar yalnızca 0 ve 1 dizilerini anlar. Yazılımcılar ise okunabilir dilde yazar. Derleyici, bu iki dünya arasında çevirmenlik yapar: Kodu tarar, hata yoksa çalıştırılabilir dosyaya dönüştürür.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Uygulama kurma:** İndirdiğiniz programın derlenmiş hali çalışır.
- **Hata mesajları:** Noktalı virgül unuttuğunuzda derleyici uyarır.
- **Oyun motorları:** Her platform için ayrı derleme çıktısı.

## Teknik Derinlik ve Mimari
Derleme dört aşamadan geçer:
- **Tarama ve çözümleme:** Kod parçalara ayrılır, cümle yapısı çıkarılır.
- **Anlam denetimi:** Tanımsız değişken ve tür uyuşmazlığı aranır.
- **Optimizasyon:** Eşdeğer ama daha hızlı kod üretilir.
- **Kod üretimi:** İşlemciye özel makine kodu yazılır.

C dilinde derleme şöyledir:

```
gcc merhaba.c -o merhaba
./merhaba
```

İlk satır çevirir, ikinci satır çalıştırır. Yorumlayıcı (interpreter) ise satır satır çalıştırır, ayrı çıktı dosyası üretmez.

## Farklı Disiplinlerde Kullanımı
- **Tercümanlık:** Simültane çeviri (yorumlayıcı) ve yazılı çeviri (derleyici) ayrımı.
- **Matbaa:** Taslağın baskı kalıbına dönüştürülmesi.
- **Mutfak:** Tarifin önceden hazırlanmış yemeğe dönüşmesi.

## Bir benzetmeyle
İngilizce yazılmış bir yemek tarifini, hiç İngilizce bilmeyen bir şefe onun anlayacağı dilde yazılı bir talimata dönüştürmek gibidir.

## Sıkça sorulanlar

**Her dilin derleyicisi farklı mı?**  
Evet. Her dil kendi kurallarına uygun derleyici veya yorumlayıcı ister. Bazı diller ikisini birlikte kullanır.

**Interpreter ile farkı nedir?**  
Derleyici kodu önceden çevirip dosya üretir, program sonra hızlı çalışır. Yorumlayıcı satır satır çevirip çalıştırır, esnektir ama genellikle yavaştır.

**JIT nedir?**  
Just-in-time derleme, çalışırken sık kullanılan bölümleri makine koduna çevirir. İkisinin arası bir yoldur, Java ve JavaScript kullanır.

**İlk derleyiciyi kim derledi?**  
Tavuk-yumurta sorusudur. İlk derleyiciler makine koduyla elle yazıldı, sonrakiler önceki derleyiciyle derlendi (bootstrapping).

## İlgili terimler
- [Rust](/dictionary/rust/)
- [Runtime](/dictionary/runtime/)
- [Compile-time](/dictionary/compile-time/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/compiler/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
