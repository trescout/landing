# Jailed nedir?

*Sözlük · Geliştirme · Son güncelleme: 29 Eylül 2026*

Bir programın işletim sisteminin geri kalanına erişmesini engelleyerek izole ve kısıtlı bir alanda çalıştırılması durumudur.

## Tanım

Jailed, bir yazılım sürecinin yalnızca kendisine izin verilen dosya dizinine, belleğe ve ağ kaynaklarına erişebildiği güvenlik durumunu ifade eder. İşletim sistemi düzeyinde uygulanan bu sınırlandırma, programın ana sisteme veya diğer kullanıcılara zarar vermesini engeller. Güvenilmeyen kodları test ederken veya zararlı yazılım riskini izole ederken kritik bir savunma hattı oluşturur.

*Evdeki bir misafirin tüm odaları gezmesine izin vermek yerine, sadece konuk odasında oturmasına izin verip diğer tüm kapıları kilitlemeye benzer.*

## Nasıl çalışır?

İşletim sistemi çekirdeği (kernel), sürecin kök dizinini ve sistem çağrılarını özel kısıtlamalarla sınırlar. Süreç kendisini ana sistemde sansa bile aslında sadece sanal bir alt dizini görebilir. Eğer bu izole alandaki bir program çökerse veya saldırıya uğrarsa, hasar yalnızca o kısıtlı alanda kalır.

## Nerede kullanılır?

Web sunucularında kullanıcı işlemlerini ayırırken, eklenti (plugin) çalıştıran uygulamalarda ve çevrim içi kod çalıştırma platformlarında yaygın olarak kullanılır.

## Sık karıştırılanlar

Sandbox kavramıyla çok yakındır; ancak jail genellikle Unix/Linux sistemlerindeki dosya sistemi izolasyonuna (chroot veya FreeBSD jail gibi) odaklanan daha geleneksel bir terimdir.

## Sıkça sorulanlar

**Jailed durumundaki bir program ana sisteme erişebilir mi?**

Normal koşullarda hayır. Ancak çekirdek düzeyinde bir açık (jailbreak açığı) bulunursa bu sınırlar aşılabilir.

**Konteyner teknolojileri de birer jail midir?**

Modern konteyner yapıları (Docker gibi), geleneksel jail mantığının çok daha gelişmiş ve özellikli birer evrimidir.

## İlgili terimler

- [Sandbox](https://trescout.com/dictionary/sandbox/)
- [Containers](https://trescout.com/dictionary/containers/)
- [Runtime](https://trescout.com/dictionary/runtime/)
- [Security Scanner](https://trescout.com/dictionary/security-scanner/)

## İlgili araçlar

- [Madeira](https://trescout.com/discover/madeira/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/jailed/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
