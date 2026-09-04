---
name: tdd
description: Test-Driven Development · RED → GREEN → REFACTOR cycle. Test öncelikli geliştirme.
trigger: Yeni feature, bug fix, refactor yapıyorken
applies-to:
  - "**/*.ts"
  - "**/*.tsx"
  - "**/*.js"
  - "**/*.py"
---

# Skill · TDD

## Ne zaman aktif

Yeni feature ekleyeceksen, bug fix yapacaksan, refactor yapacaksan. `CLAUDE.md §4` "Hedef Odaklı" prensibinin somut hali.

## Procedure

### RED · Failing test yaz

1. Test dosyasını oluştur (örn. `lib/ai/rpd-budget.test.ts`)
2. Hedef davranışı test eden assertion yaz
3. Çalıştır → **failing** olmalı (testi yazdığını doğrulamak için)

### GREEN · Minimum kod yaz

1. Sadece testi geçirecek minimum kodu yaz
2. Çalıştır → **passing** olmalı
3. **Spekülasyon yok** · ek özellik ekleme, basit tut

### REFACTOR · Temizle

1. Kod tekrarı (DRY) varsa kaldır
2. İsim/yapı iyileştirmesi yap
3. Test hâlâ **passing** olmalı
4. Yeni davranış EKLEME · sadece mevcut kodu temizle

## İyi örnek (gerçek kod: `lib/ai/rpd-budget.test.ts`)

```typescript
// 1. RED · failing test
test('taşan plan açık hata verir · rapor hiç başlamaz', async () => {
  await assert.rejects(() => assertBudget(1_000_000), /bütçesi yetersiz/);
});

// 2. GREEN · minimum kod (gerçek karşılık: lib/ai/rpd-budget.ts → assertBudget)
export async function assertBudget(planned: number): Promise<void> {
  const remaining = ...; // 1500 limit − 100 tampon − sayaç
  if (planned > remaining) throw new Error(`Gemini RPD bütçesi yetersiz ...`);
}

// 3. REFACTOR · isim iyileştir, davranış değiştirme
// (ör. mesaj formatı, sabit adları · limit matematiği aynı kalır)
```

## Anti-patterns

- ❌ Önce kod, sonra test (failing test yokken passing'i nasıl bilirsin?)
- ❌ Test'i implementasyona göre yazmak (test, davranışı tanımlamalı)
- ❌ REFACTOR adımında yeni özellik eklemek
- ❌ Spekülatif test (gelecekte gerekebilecek diye)
- ❌ "Bu trivial, test'e gerek yok" · kritik logic için her zaman test

## Detay

- `CLAUDE.md §4 Hedef Odaklı` · "Tercihen test-first" prensibi
- `AGENTS.md §3.e DoD` · "Birim test eklendi (kritik logic için)"
- Kaynak: obra/superpowers `test-driven-development` skill'i
