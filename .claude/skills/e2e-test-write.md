---
name: e2e-test-write
description: Playwright E2E test yazma · Page Object Pattern, data-testid locator, wait pattern, test isolation.
trigger: Yeni E2E test, browser flow test, kritik user journey doğrulama
applies-to:
  - "tests/e2e/**"
  - "**/*.spec.ts"
  - "playwright.config.ts"
---

# Skill · E2E Test Write

## Ne zaman aktif

Kritik user journey test'i yazılacaksa (signup, payment, report delivery, dashboard nav). Birim test (Vitest/Jest) ile karıştırma · E2E gerçek browser ile tüm stack'i test eder.

## Procedure

### 1. Test scope'unu seç

E2E pahalıdır (yavaş, flaky risk). Şuna ayır:

- ✓ **E2E**: Kritik user journey (signup → first report)
- ✓ **E2E**: Integration sınırı (Stripe checkout, Resend email gönderim)
- ✗ **E2E değil**: Component davranışı (testing-library), util function (vitest), API endpoint (supertest)

### 2. Page Object Pattern (POM)

Selectorları test dosyasında değil, sayfa nesnesinde topla:

```typescript
// tests/e2e/pages/SignupPage.ts
export class SignupPage {
  constructor(private page: Page) {}
  
  async goto() { await this.page.goto('/signup'); }
  async fillEmail(email: string) { await this.page.getByTestId('email-input').fill(email); }
  async submit() { await this.page.getByTestId('signup-submit').click(); }
  async waitForSuccess() { await this.page.getByTestId('signup-success').waitFor(); }
}

// tests/e2e/signup.spec.ts
test('user can sign up with email', async ({ page }) => {
  const signup = new SignupPage(page);
  await signup.goto();
  await signup.fillEmail('test@example.com');
  await signup.submit();
  await signup.waitForSuccess();
});
```

### 3. Locator strategy

Öncelik sırası (en stabil önce):

1. `getByTestId('xxx')` · `data-testid` attribute · **tercih**
2. `getByRole('button', { name: '...' })` · accessibility-aware
3. `getByText('...')` · görsel · ama text değişince kırılır
4. CSS selector · son çare, brittle

```typescript
// ✓ İyi
await page.getByTestId('hero-cta').click();

// ✗ Kötü (brittle)
await page.click('.hero > div:nth-child(2) > button');
```

### 4. Wait pattern

Sleep yok · Playwright'ın auto-wait'i kullan + explicit wait'ler:

```typescript
// ✓ Doğru
await page.waitForLoadState('networkidle');  // ağ trafiği durunca
await page.getByTestId('result').waitFor({ state: 'visible' });

// ✗ Yanlış (flaky)
await page.waitForTimeout(2000);   // arbitrary sleep
```

### 5. Test isolation

Her test bağımsız çalışmalı · sırasız:

```typescript
test.describe('Dashboard', () => {
  test.beforeEach(async ({ page }) => {
    // Her test'ten önce login
    await loginAsTestUser(page);
  });

  test('shows reports list', async ({ page }) => { ... });
  test('opens report detail', async ({ page }) => { ... });
});
```

Test data:
- DB'ye test user inject (seed script)
- Veya unique data per test (`Date.now()` suffix)
- Test sonrası cleanup (afterEach veya global teardown)

### 6. Visual regression (opsiyonel)

Marka için kritikse:

```typescript
await expect(page).toHaveScreenshot('hero-section.png', {
  maxDiffPixels: 100,
});
```

İlk run'da baseline kaydet · sonraki run'larda compare.

### 7. CI integration

`playwright.config.ts`:

```typescript
export default defineConfig({
  testDir: './tests/e2e',
  workers: process.env.CI ? 2 : 4,
  retries: process.env.CI ? 2 : 0,
  reporter: process.env.CI ? 'github' : 'list',
  use: {
    baseURL: process.env.CI ? 'https://trescout-app-preview-xxx.vercel.app' : 'http://localhost:3000',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
  },
});
```

CI step (`.github/workflows/`):

```yaml
- run: npm ci
- run: npx playwright install --with-deps chromium
- run: npm run test:e2e
- uses: actions/upload-artifact@v4
  if: failure()
  with:
    name: playwright-report
    path: playwright-report/
```

### 8. Vercel preview ile test

Production-like environment için CI'da Vercel preview URL'sini al, ona karşı çalıştır. Local'de `playwright dev` ile.

## İyi örnek

`tests/e2e/signup.spec.ts`:

```typescript
import { test, expect } from '@playwright/test';
import { SignupPage } from './pages/SignupPage';

test.describe('Signup flow', () => {
  test('valid email creates account and triggers welcome email', async ({ page }) => {
    const signup = new SignupPage(page);
    const testEmail = `test-${Date.now()}@trescout.com`;
    
    await signup.goto();
    await signup.fillEmail(testEmail);
    await signup.submit();
    await signup.waitForSuccess();
    
    // DB'de kayıt oluştu mu (test helper)
    const user = await getUserByEmail(testEmail);
    expect(user).toBeTruthy();
    expect(user.status).toBe('active');
  });
});
```

## Anti-patterns

- ❌ `waitForTimeout(N)` ile sleep · flaky
- ❌ CSS selector hierarchy · `.hero > div:nth-child(2)` · DOM değişince kırılır
- ❌ Test'ler sıra bağımlı · test A çalışmadan test B fail
- ❌ Production DB'ye test data write · gerçek user'ları kirletir
- ❌ Login flow'u her test'te tekrar yazmak (helper'a çıkar)
- ❌ Screenshot baseline'ı CI'da güncellemek (local'de bilinçli güncelle, commit et)
- ❌ Network call mock'lamak istemediğin halde (E2E gerçek stack'i test eder)

## Detay

- `playwright.config.ts` · global config
- `tests/e2e/` · test dosyaları
- `tests/e2e/pages/` · Page Object'ler
- `AGENTS.md §3.e DoD` · "Birim test eklendi" · kritik logic E2E ile de doğrulanır
- Bu skill **landing ve app reposu için** (brand-kit'te browser flow yok)
- Cross-skill: [`tdd`](tdd.md) (unit/integration), [`code-review-pre`](code-review-pre.md)
