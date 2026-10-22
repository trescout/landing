# Backdoor nedir?

*Geliştirme · Son güncelleme: 22 Ekim 2026*

Standart kimlik doğrulama mekanizmalarını atlayarak bir sisteme gizlice uzaktan erişim sağlayan yöntem veya yazılımdır.

## Tanım

Backdoor (arka kapı), yazılım geliştiriciler tarafından hata ayıklama amacıyla kasıtlı bırakılabilen veya saldırganlar tarafından sisteme sonradan yerleştirilen gizli bir giriş kapısıdır. Bu yöntem sayesinde geleneksel kullanıcı adı, parola veya şifreleme denetimleri devre dışı bırakılır. Sisteme fark edilmeden sızan zararlı odaklar, arka kapıyı kullanarak uzun süre boyunca yönetim yetkileriyle işlem yapabilir.

*Bir kalenin ana girişinde nöbetçiler beklerken duvarın arkasına kimsenin bilmediği gizli bir tünel açmaya benzer.*

## Nasıl çalışır?

Arka kapılar kaynak koda gizlenen bir mantık denetimiyle veya sistemde açık bırakılan gizli bir ağ portuyla kurulur. Bazen güncellemeler yoluyla tedarik zincirine sızdırılır bazen de exploit kullanılarak içeri bırakılan küçük bir komut satırı aracıyla tetiklenir. Saldırgan dışarıdan özel bir sinyal veya anahtar gönderdiğinde arka kapı doğrudan uzaktan erişim oturumu başlatır.

## Nerede kullanılır?

Tedarik zinciri saldırılarında, kurumsal casusluk vakalarında ve gelişmiş kalıcı tehdit operasyonlarında sıkça görülür. Donanım yazılımlarında veya açık kaynak paketlerine sızdırılan zararlı kodlarda da tespit edilir.

## Sık karıştırılanlar

Truva atı (Trojan) ile karıştırılabilir. Truva atı zararlı yazılımı bulaştırmak için kullanılan aldatıcı kabuktur; backdoor ise sistemde kalıcı ve gizli erişim sağlayan işlevdir.

## Sorular ve yanıtlar

**Geliştiriciler neden sisteme arka kapı koyar?**

Bazı durumlarda bakım kolaylığı veya acil erişim amacıyla bilerek bırakılır ancak bu durum sistemi büyük bir güvenlik riskine açık hale getirir.

**Bir backdoor nasıl tespit edilir?**

Anormal ağ trafiği izleme, dosya bütünlüğü denetimi ve derinlemesine statik kod analizleri sayesinde yakalanabilir.

## İlgili terimler

- [Exploit](https://trescout.com/dictionary/exploit/)
- [Remote Code Execution](https://trescout.com/dictionary/remote-code-execution/)
- [Penetration Testing](https://trescout.com/dictionary/penetration-testing/)
- [Vulnerability Scanning](https://trescout.com/dictionary/vulnerability-scanning/)

Bu açıklama TreScout için yapay zekâ ile sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/backdoor/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
