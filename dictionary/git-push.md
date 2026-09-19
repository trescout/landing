# Git Push ne demek, nedir ve nasıl kullanılır?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

Git Push, yerel geliştirme ortamınızda commit edilmiş kod bloklarını, commit geçmişini ve nesneleri uzak bir Git sunucusuna (GitHub, GitLab, Bitbucket vb.) aktaran ve uzak dalı güncelleyen temel Git komutudur.

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

`git push` çalıştırıldığında yalnızca metin farkları (diff) gönderilmez; Git'in nesne tabanındaki **Commit**, **Tree** (dizin yapısı) ve **Blob** (dosya içerikleri) nesneleri sıkıştırılmış bir paket dosyası (packfile) halinde SSH veya HTTPS protokolüyle uzak sunucuya pompalanır ve uzaktaki dal referansı (`refs/heads/*`) ileri taşınır.

## 2. En sık kullanılan komut şablonları (Cheatsheet)

### İlk Kez Dal Gönderme ve Upstream Bağlama
```bash
git push -u origin feature/auth
```
`-u` veya `--set-upstream` bayrağı, yerel `feature/auth` dalınızı uzaktaki `origin/feature/auth` dalına kalıcı olarak bağlar. Bu eşleştirmeden sonra aynı daldayken yalnızca `git push` veya `git pull` yazmanız yeterlidir.

### Güvenli Zorla Gönderme: `--force-with-lease`
```bash
git push --force-with-lease
```
`git commit --amend` veya `git rebase` sonrası geçmişi yeniden yazdığınızda standart `git push` reddedilir. `git push -f` (force push) körü körüne sunucudaki her şeyi ezer ve ekip arkadaşlarınızın commit'lerini silebilir. `--force-with-lease` ise yalnızca sizden sonra başkası o dala commit atmadıysa ezme işlemine izin veren hayati bir güvenlik kilididir.

### Uzak Dalı ve Etiketleri Silme
```bash
# Uzaktaki dalı silmek için:
git push origin --delete eski-ozellik-dali

# Yereldeki tüm sürüm etiketlerini (tags) göndermek için:
git push origin --tags
```

## 3. En sık karşılaşılan Git Push hataları ve çözümleri

### 1. `fatal: [rejected - non-fast-forward]`
- **Neden Olur?** Siz yerelde kod yazarken bir ekip arkadaşınız uzak depoya yeni commit'ler göndermiştir. Uzak dal, sizin yerel dalınızın bilmediği yeni bir geçmişe sahiptir.
- **Çözüm:** Önce uzaktaki commit'leri yerel geçmişinizin üzerine rebase ederek çekin, ardından push yapın:
  ```bash
  git pull --rebase origin <dal-adi>
  git push origin <dal-adi>
  ```

### 2. `fatal: The current branch has no upstream branch`
- **Neden Olur?** Yerelde yeni oluşturduğunuz bir dalın uzakta hangi isimle eşleşeceği henüz tanımlanmamıştır.
- **Çözüm:**
  ```bash
  git push -u origin HEAD
  ```

### 3. `remote rejected: pre-receive hook declined`
- **Neden Olur?** Şirketin veya GitHub'ın sunucu tarafı kural motoru devreye girmiştir (örneğin korumalı dala doğrudan push yapılması yasaklanmış, commit mesajı kurallara uymamış veya kodda API anahtarı/secret tespit edilmiştir).
- **Çözüm:** Doğrudan `main` yerine bir özellik dalı (feature branch) açıp Pull Request (PR) oluşturun.

## Bir benzetmeyle

Bilgisayarınızda yazdığınız bir kitabın bölümlerini yerel taslak klasörünüze kaydettikten sonra, matbaanın ortak baskı merkezine "bu bölümleri resmi arşive yükle ve baskı kuyruğuna al" diyerek kuryeyle teslim etmek gibidir.

## Sık karıştırılanlar

- **Git Commit vs Git Push:** Commit kendi yerel bilgisayarınızdaki çevrimdışı veritabanına kayıt atar (uçakta internet yokken bile çalışır); Push ise bu kayıtları internetteki sunucuya yükler.
- **Git Push vs Git Pull:** Push yerelden sunucuya veri aktarırken, Pull sunucudaki güncellemeleri yerel çalışma alanınıza indirir ve birleştirir.

## Sıkça sorulanlar

**Git push ne demek ve ne işe yarar?**  
Git Push, yerel bilgisayarınızda tamamlanan commit'leri GitHub, GitLab veya Bitbucket gibi uzak sunuculara yükleyerek uzak depoları yerel durumla eşitleyen temel komuttur.

**`git push -u origin main` komutundaki `-u` ne anlama gelir?**  
`-u` (`--set-upstream`) bayrağı, yerel dal ile uzaktaki dal arasında izleme (tracking) bağlantısı kurar. Böylece sonraki seferlerde hedef belirtmeden sadece `git push` yazabilirsiniz.

**`git push -f` yerine neden `--force-with-lease` kullanılmalıdır?**  
`git push -f` uzak depoda başkalarının yaptığı değişiklikleri kontrol etmeksizin kalıcı olarak siler. `--force-with-lease` ise yalnızca dal son çektiğiniz durumdaysa ezmeye izin vererek ekip arkadaşlarının kodunu korur.

**`non-fast-forward` hatası nasıl çözülür?**  
Uzak depodaki yeni commit'ler henüz yerelinizde olmadığı için oluşur. Çözüm için `git pull --rebase origin <dal>` çalıştırılarak commit'ler güncellenmeli ve ardından tekrar `git push` yapılmalıdır.

## İlgili terimler

- [CLI](/dictionary/cli/)
- [Deployment](/dictionary/deployment/)
- [Production Pipeline](/dictionary/production-pipeline/)
- [Patch](/dictionary/patch/)
- [Tech Stack](/dictionary/tech-stack/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/git-push/  
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
