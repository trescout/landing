# What is Identity Provider?

*Dictionary · Dev · Last updated: September 22, 2026*

An identity provider is a centralized service that authenticates logins.

## Definition and Word Origin

Instead of a separate password for each application, sign-in is done from a single center. The application asks who you are to the service and gets approval. Your password is not distributed to applications, it stays at the center.

***Analogy:** It is like showing your passport at a hotel reception to get a key card; the room door trusts the reception's approval.*

## How to Know and Use in Daily Life?

**Company:** All systems with a single sign-on.
**Web:** Sign in with a social account.
**Institutional:** Employee lifecycle.

## Technical Depth and Architecture

Flow:

```
giriş → doğrulama → jeton → uygulama
```

Parts:

**ID token:** The proof of who you are.
**Access token:** The permission of what you can do.
**MFA:** Additional proof beyond the password.
**Session:** Single Sign-On (SSO).

Rule: Token lifespan is kept short, renewal runs in the background.

## Frequently Mixed Things

Mistaken for a password manager. One stores the password, the other verifies the identity. One is a safe, the other is a notary.

## Use in Different Disciplines

**Reception:** Key card versus passport.
**Notary:** Identity verification.
**Passport control:** Passage with a stamp.

## Frequently Asked Questions

**Is it safe?**

Yes. Since the password is not distributed to every application, the attack surface is reduced.

**What happens if the system crashes?**

Connected applications are affected. Redundancy and an emergency access plan are essential.

**What is the difference of SSO?**

SSO is a single sign-on experience and provider infrastructure. One is the face, the other is the backbone.

**Can I set it up myself?**

Yes, there are open-source options. Patching and backup discipline belong to you.

## Related terms

- [SSO](https://trescout.com/en/dictionary/sso/)
- [OIDC](https://trescout.com/en/dictionary/oidc/)
- [RBAC](https://trescout.com/en/dictionary/rbac/)

This explanation was written in plain language for TreScout and **machine-translated** from the Turkish original · the Turkish version prevails. If something looks wrong or missing, write to [hello@trescout.com](mailto:hello@trescout.com). [Read in Turkish →](https://trescout.com/dictionary/identity-provider/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/identity-provider/
