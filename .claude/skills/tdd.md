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

1. Test dosyasını oluştur (örn. `lib/utils/budget.test.ts`)
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

## İyi örnek

```typescript
// 1. RED · failing test
test('budget tracker rejects over 20 RPD', () => {
  const b = new BudgetTracker(20);
  for (let i = 0; i < 20; i++) b.consume();
  expect(() => b.consume()).toThrow('RPD exceeded');
});

// 2. GREEN · minimum kod (test geçer)
class BudgetTracker {
  constructor(private limit: number, private count = 0) {}
  consume() {
    if (this.count >= this.limit) throw new Error('RPD exceeded');
    this.count++;
  }
}

// 3. REFACTOR · isim iyileştir, davranış değiştirme
class GeminiBudgetTracker {
  private count = 0;
  constructor(private rpdLimit: number) {}
  /** Throws if RPD limit exceeded */
  consume(): void {
    if (this.count >= this.rpdLimit) {
      throw new Error(`Gemini RPD limit (${this.rpdLimit}) exceeded`);
    }
    this.count++;
  }
}
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
