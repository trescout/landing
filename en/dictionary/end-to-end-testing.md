# What is End-to-End Testing?

*Dictionary · Dev · Last updated: September 22, 2026*

> E2E Testing

End-to-end testing (E2E testing for short) is testing the application from start to finish like the user.

## Definition and Word Origin

"End-to-end" means end-to-end. The whole is tried, not the part: The input is made, the button is pressed, the data goes, the result is returned. It is the gateway to pre-publication compliance.

***Analogy:** It's like trying to drive off by turning the key instead of turning the engine.*

## How to Know and Use in Daily Life?

**Broadcasting:** Pre-release tour.
**Shopping centre:** Purchase path.
**Form:** Registration flow.

## Technical Depth and Architecture

Order:

**Critical path:** First the flow that makes money.
**Automation:** Scanner driving vehicle.
**Data:** Test account and reset.

Example:

```
test("giriş", async () => {
  await sayfa.goto("/giris");
  await bekle("#panel");
});
```

Reason for slowness: The actual browser opens. The critical path is chosen, not everything is tested.

## Frequently Mixed Things

It is considered a unit test. He looks at the part, this one looks at the whole. One is screw, the other is driving test.

## Use in Different Disciplines

**Car:** Starting from the key.
**Rehearsal:** General repetition.
**Final:** Broadcast rehearsal.

## Frequently Asked Questions

**Why isn't just this done?**

It is slow, the fault location is blurred. Used with the unit.

**How often does he run?**

Pre-broadcast and overnight. The critical subset runs in each commit.

**Who writes?**

Developer and tester write together. The owner is known.

**Is it fragile?**

It breaks when the interface changes. It is written selectively and durable.

## Related terms

- [Unit Testing](https://trescout.com/en/dictionary/unit-testing/)
- [Testing Framework](https://trescout.com/en/dictionary/testing-framework/)
- [Web Interface](https://trescout.com/en/dictionary/web-interface/)

## Related tools

- [Cypress](https://trescout.com/en/discover/cypress/)
- [E2e](https://trescout.com/en/discover/e2e/)

This explanation was written in plain language for TreScout and **machine-translated** from the Turkish original · the Turkish version prevails. If something looks wrong or missing, write to [hello@trescout.com](mailto:hello@trescout.com). [Read in Turkish →](https://trescout.com/dictionary/end-to-end-testing/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/end-to-end-testing/
