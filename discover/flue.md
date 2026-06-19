# yapay zekâ ajanları için TypeScript çatısı

Astro ekibi tarafından geliştirilen Flue, TypeScript tabanlı bir kum havuzu ajan çatısı (sandbox agent framework) olarak öne çıkıyor. Bu yapı, geliştiricilerin güvenli ve izole edilmiş ortamlarda yapay zekâ ajanları oluşturmasına olanak tanıyor.

- ★ 4.594
- TypeScript
- GitHub Trending · 2026-06-06

## Ne kazandırır?
- TypeScript tabanlı, programlanabilir ve başsız ajanlar oluşturma.
- Sanal kum havuzu ile hızlı ve ölçeklenebilir çalışma ortamı.
- Node.js, Cloudflare ve CI/CD süreçlerinde çok yönlü dağıtım.

## Kurulum

**Node.js Geliştirme Sunucusu**

```
flue dev --target node
```

**Derleme**

```
flue build --target node # Node.js server (single bundled .mjs)
flue build --target cloudflare # Cloudflare Workers + Durable Objects
```

## Çalıştırma

**Hello World İş Akışını Çalıştırma**

```
flue run hello --target node \
--payload '{"text": "Hello world", "language": "French"}'
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Flue framework'ünü kullanarak bir yapay zekâ ajanı geliştirmek istiyorum. Projemde TypeScript kullanarak nasıl bir iş akışı (workflow) tanımlayabilirim? Özellikle createAgent fonksiyonu ile model yapılandırmasını nasıl yaparım ve session.prompt ile ajanımı nasıl etkileşime sokabilirim? Basit bir 'hello-world' örneği üzerinden, çalışma zamanında (runtime) bir ajanı nasıl başlatıp sonuç alabileceğimi adım adım açıklar mısın?

- **Kimin için:** Kendi otonom yapay zekâ ajanlarını TypeScript ile geliştirmek ve bunları farklı platformlarda çalıştırmak isteyen yazılımcılar için uygundur. 
- **Lisans:** Apache-2.0 

## Bağlantılar
- [GitHub deposu →](https://github.com/withastro/flue)

## İlgili sözlük terimleri
Sandbox Agent Framework Runtime Sandbox Framework Artificial Intelligence 

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Yıldız ve sayılar keşif tarihindeki değerlerdir.

---
Kaynak: TreScout Keşif · https://trescout.com/discover/flue/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
