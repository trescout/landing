# Task Runner nedir, ne demek?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-22

Task runner (Türkçe karşılığıyla **görev koşturucu**), tekrarlı işleri sırayla çalıştıran araçtır.

## Tanım ve Kelime Kökeni
Test, sıkıştırma ve dağıtım gibi angarya işler tek komuta bağlanır. Liste takip edilir, süreç hızlanır, hata düşer.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Web:** Derleme ve sıkıştırma.
- **CI:** Hat adımları.
- **Yayın:** Tek komutla dağıtım.

## Teknik Derinlik ve Mimari
Npm betikleri:

```
"scripts": {
  "test": "pytest",
  "build": "vite build"
}
```

Çalıştırma `npm run test` biçimindedir. Makefile ve Just alternatifleridir. Kural: Üç kez elle yapılan iş betiğe yazılır.

## Sık Karıştırılanlar
Terminal sanılır. Terminal çalıştırır, koşturucu yönetir. Biri sahne, diğeri yönetmendir.

## Farklı Disiplinlerde Kullanımı
- **Robot:** Sıralı mutfak işleri.
- **Çamaşır makinesi:** Programlı yıkama.
- **Otopilot:** Rota takibi.

## Bir benzetmeyle
Mutfak işlerini sırayla yapan robot gibidir; liste verilir, süreç işler.

## Sıkça sorulanlar

**Hangi işlerde kullanılır?**  
Test, derleme ve dağıtımda. Tekrar eden her iş adaydır.

**Hangisi seçilmeli?**  
Ekosistem belirler: JS tarafında npm, sistemde Make yaygındır.

**CI farkı nedir?**  
Koşturucu yerelde çalışır, CI bulutta koşar. İkisi birlikte kullanılır.

**Ne zaman yazılır?**  
Üçüncü tekrarda. İlki elle, ikincisi notla, üçüncü betikle yapılır.

## İlgili terimler
- [CLI](/dictionary/cli/)
- [Continuous Integration](/dictionary/continuous-integration/)
- [Script](/dictionary/script/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/task-runner/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
