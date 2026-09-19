# Git Push ne demek, nedir?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

Git Push, yerel bilgisayarınızdaki commit edilmiş kod değişikliklerini uzak bir Git sunucusuna (GitHub, GitLab vb.) yükleme ve eşitleme işlemidir.

## Tanım ve çalışma prensibi
Yazılım geliştirirken kodlarınızı kendi bilgisayarınızdaki yerel Git deposunda (local repository) düzenler ve `git commit` ile kaydedersiniz. Ancak bu değişikliklerin çalışma arkadaşlarınız tarafından görülebilmesi, CI/CD hatlarının tetiklenebilmesi ve kodun bulutta yedeklenmesi için `git push` komutuyla uzak depoya (remote repository) aktarılması gerekir.

## Bir benzetmeyle
Bilgisayarınızda hazırladığınız bir rapor taslağını, şirketin ortak bulut klasörüne 'kaydet ve ekiple paylaş' tuşuna basarak yüklemek gibidir; siz o tuşa basana kadar hazırlık sadece sizin ekranınızda kalır.

## Nasıl çalışır?
Terminal veya editörünüzün entegre Git arayüzü üzerinden şu adımlarla kullanılır:
1. `git add .` ile yapılan değişiklikler evreye (stage) alınır.
2. `git commit -m "mesaj"` ile yerel kontrol noktası oluşturulur.
3. `git push origin <dal-adı>` komutu ile yerel commit paketleri şifreli SSH veya HTTPS protokolüyle uzak sunucuya aktarılır.

## Nerede kullanılır?
Takım halinde yazılım geliştirmede, açık kaynak projelere katkı sağlarken ve otomatik test/dağıtım süreçlerini tetiklerken geliştiricilerin her gün defalarca kullandığı temel komuttur.

## Sık karıştırılanlar
- **Git Commit vs Git Push:** Commit sadece kendi bilgisayarınızdaki yerel veritabanına kayıt atar; Push ise bu kayıtları internetteki sunucuya yükler.
- **Git Push vs Git Pull:** Push yerelden sunucuya kod gönderir; Pull ise sunucudaki güncel değişiklikleri yerel bilgisayara çeker.

## Sıkça sorulanlar

**Git push ne demek ve ne işe yarar?**  
İngilizce 'push' (itmek/göndermek) eyleminden gelir. Yerel depoda onaylanmış yazılım değişikliklerini GitHub veya GitLab gibi merkezi depolara göndermeye yarar.

**git push -u origin main komutu ne anlama gelir?**  
`-u` (upstream) parametresi, yerel `main` dalınızı uzaktaki `origin/main` dalıyla kalıcı olarak eşleştirir; sonraki güncellemelerde sadece `git push` yazmanız yeterli olur.

**Force push (git push -f) ne zaman kullanılır ve riskleri nelerdir?**  
Uzak depodaki geçmişi yerel geçmişle zorla ezmek için kullanılır. Ortak çalışılan dallarda diğer geliştiricilerin commit'lerini silebileceği için dikkatle kullanılmalıdır.

## İlgili terimler
- [CLI](/dictionary/cli/)
- [Tech Stack](/dictionary/tech-stack/)
- [Deployment](/dictionary/deployment/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/git-push/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
