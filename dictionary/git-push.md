# Git Push ne demek, nedir ve nasıl kullanılır?

*Sözlük · Geliştirme · Son güncelleme: 19 Eylül 2026*

Git Push, yerel geliştirme ortamınızda commit edilmiş kod bloklarını, commit geçmişini ve nesneleri uzak bir Git sunucusuna aktaran ve uzak dalı güncelleyen temel Git komutudur.

## 1. Tanım ve Git'in 4 katmanlı veri modeli

Git dağıtık bir versiyon kontrol sistemidir (DVCS). Bu mimaride kod değişiklikleri uzak bir sunucuya ulaşana kadar 4 farklı çalışma alanından geçer:

```
[Çalışma Dizini] ──git add──> [Staging / Index] ──git commit──> [Yerel Depo] ──git push──> [Uzak Depo]
(Working Directory)            (Hazırlık Alanı)                 (.git veritabanı)            (GitHub/GitLab)
```

1. **Working Directory (Çalışma Dizini):** Dosyaları düzenlediğiniz canlı kod alanı.
2. **Staging Area / Index (Hazırlık Alanı):** `git add` ile bir sonraki kayda dâhil edilmek üzere seçtiğiniz değişiklikler.
3. **Local Repository (Yerel Depo):** `git commit` ile kendi diskinizdeki `.git` dizinine kalıcı olarak mühürlenen kontrol noktaları.
4. **Remote Repository (Uzak Depo):** `git push` ile ekip arkadaşlarınızın görebileceği, CI/CD hatlarının tetikleneceği merkezi sunucu.

`git push` çalıştırıldığında yalnızca metin farkları gönderilmez; Git'in nesne tabanındaki Commit, Tree ve Blob nesneleri sıkıştırılmış bir paket dosyası (packfile) halinde uzak sunucuya aktarılır ve uzaktaki dal referansı ileri taşınır.

## 2. En sık kullanılan komut şablonları (Cheatsheet)

### İlk Kez Dal Gönderme ve Upstream Bağlama

```
git push -u origin feature/auth
```

`-u` veya `--set-upstream` bayrağı, yerel dalınızı uzaktaki dala kalıcı olarak bağlar. Bu eşleştirmeden sonra aynı daldayken yalnızca `git push` veya `git pull` yazmanız yeterlidir.

### Güvenli Zorla Gönderme: --force-with-lease

```
git push --force-with-lease
```

`git commit --amend` veya `git rebase` sonrası standart push reddedildiğinde `git push -f` kullanmak sunucudaki ekip arkadaşlarınızın commit'lerini silebilir. `--force-with-lease` ise yalnızca sizden sonra başkası o dala commit atmadıysa ezme işlemine izin veren güvenlik kilididir.

### Uzak Dalı ve Etiketleri Silme

```
git push origin --delete eski-ozellik-dali
git push origin --tags
```

## 3. En sık karşılaşılan Git Push hataları ve çözümleri

- **fatal: [rejected - non-fast-forward]:** Uzak dalda henüz yerelinizde olmayan commit'ler vardır. Çözüm için `git pull --rebase origin <dal>` ardından `git push` yapılmalıdır.
- **fatal: The current branch has no upstream branch:** Dalın uzak karşılığı tanımlanmamıştır. Çözüm: `git push -u origin HEAD`.
- **remote rejected: pre-receive hook declined:** Korumalı dal kuralı veya eksik izin engeline takılmıştır; doğrudan push yerine Pull Request (PR) açılmalıdır.

*Bilgisayarınızda yazdığınız bir kitabın bölümlerini yerel taslak klasörünüze kaydettikten sonra, matbaanın ortak baskı merkezine "bu bölümleri resmi arşive yükle ve baskı kuyruğuna al" diyerek kuryeyle teslim etmek gibidir.*

## Sıkça sorulanlar

**Git push ne demek ve ne işe yarar?**

Git Push, yerel bilgisayarınızda tamamlanan commit'leri GitHub, GitLab veya Bitbucket gibi uzak sunuculara yükleyerek uzak depoları yerel durumla eşitleyen temel komuttur.

**git push -u origin main komutundaki -u ne anlama gelir?**

-u (--set-upstream) bayrağı, yerel dal ile uzaktaki dal arasında izleme (tracking) bağlantısı kurar. Böylece sonraki seferlerde hedef belirtmeden sadece git push yazabilirsiniz.

**git push -f yerine neden --force-with-lease kullanılmalıdır?**

git push -f uzak depoda başkalarının yaptığı değişiklikleri kontrol etmeksizin kalıcı olarak siler. --force-with-lease ise yalnızca dal son çektiğiniz durumdaysa ezmeye izin vererek ekip arkadaşlarının kodunu korur.

**non-fast-forward hatası nasıl çözülür?**

Uzak depodaki yeni commit'ler henüz yerelinizde olmadığı için oluşur. Çözüm için git pull --rebase origin \<dal> çalıştırılarak commit'ler güncellenmeli ve ardından tekrar git push yapılmalıdır.

## İlgili terimler

- [CLI](https://trescout.com/dictionary/cli/)
- [Deployment](https://trescout.com/dictionary/deployment/)
- [Production Pipeline](https://trescout.com/dictionary/production-pipeline/)
- [Patch](https://trescout.com/dictionary/patch/)
- [Tech Stack](https://trescout.com/dictionary/tech-stack/)

## İlgili araçlar

- [No Mistakes](https://trescout.com/discover/no-mistakes/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/git-push/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
