# Pollen Robotics Microduck için pekiştirmeli öğrenme ortamı

Pollen Robotics tarafından geliştirilen microduck_rl, Microduck robot platformu için MuJoCo ve mjlab üzerinde pekiştirmeli öğrenme (reinforcement learning) eğitim ortamları ve kontrol politikaları sunar.

- ★ 1.001
- Python
- GitHub Trending · 2026-08-31

## Güncelleme
- 31 Ağustos 2026: Yıldız 1.001, MuJoCo mjlab fizik motoru ve lokomosyon görevleri desteği.

## Ne kazandırır?
- Gerçekçi MuJoCo fizik simülasyonu: Robotun eklem torklarını, sürtünmesini ve yer çekimi etkilerini yüksek hızda simüle edebilme.
- Hazır lokomosyon ve denge görevleri: Yürüme (walk), denge kurma ve engelleri aşma senaryoları için önceden tanımlanmış ödül fonksiyonları.
- Sim-to-Real transferine uygunluk: Fiziksel Microduck donanımına kolayca aktarılabilen gürültü dirençli kontrol politikaları.
- Modern pekiştirmeli öğrenme algoritmaları: PPO (Proximal Policy Optimization) ve SAC destekli eğitim altyapısı.
- Görsel 3B değerlendirme arayüzü: Eğitilen robot ajanının hareketlerini ekranda 3 boyutlu simülatörde anlık izleme.

## Kurulum

**Depoyu klonlama ve simülasyon ortamını kurma**

```
git clone https://github.com/pollen-robotics/microduck_rl.git
cd microduck_rl
pip install -e .
```

## Çalıştırma

**Eğitim veya politika değerlendirme çalıştırma**

```
python -m microduck_rl.train --task walk
# Eğitilen politikayı simülatörde izleme:
python -m microduck_rl.enjoy --checkpoint checkpoint.pt
```

## Teknik mimari ve çalışma prensibi

microduck_rl, mjlab soyutlaması üzerinden MuJoCo simülatörünü Gymnasium API'si ile bağlar:
- MuJoCo ve mjlab Fizik Katmanı: Robotun kinematics, eklem sınırları ve eyleyici modellerini tanımlayan XML/MJCF dosyaları.
- Gymnasium Uyumlu Gözlem ve Eylem Uzayları: Motor açıları, hızlar, ivmeölçer (IMU) verileri ve hedef tork vektörlerinin standardizasyonu.
- Domain Randomization Mekanizması: Sürtünme katsayıları, kütle dağılımı ve sensör gürültülerini rastgele değiştirerek gerçek dünyaya dayanıklı modeller eğitme.

## Fizik simülasyonu ve robotik kontrol politikaları

Robotik araştırmacıları microduck_rl ile laboratuvar ortamında güvenli algoritmalar geliştirebilir:
- Donanım Hasarını Önleme: Robotun düşme ve bacak kırılma risklerini fiziksel robota geçmeden önce tamamen sanal ortamda çözün.
- Milyonlarca Adımı Hızlandırılmış Zamanda Eğitme: Fizik motorunu gerçek zamandan 100 kat daha hızlı işleterek günlerce sürecek eğitimi saatler içinde tamamlama.
- Özel Görev ve Arazi Tasarımı: Merdivenler, eğimli zeminler ve kaygan yüzeyler ekleyerek robotun farklı arazilere uyumunu test edin.

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Pollen Robotics'in microduck_rl kütüphanesini kullanarak Microduck robotu için bir yürüme (walking) politikası eğitmek istiyorum. MuJoCo ortamını nasıl yapılandıracağımı, PPO algoritması ile eğitim komutunu nasıl başlatacağımı ve ortaya çıkan kontrol politikasını fiziksel robota aktarma adımlarını açıklar mısın?

- **Kimin için:** Robotik araştırmacıları, mekatronik mühendisleri, pekiştirmeli öğrenme uzmanları ve hobiciler. 
- **Lisans:** Apache-2.0 (Açık kaynak lisansı) 
- **Çatı:** Python, MuJoCo & mjlab Robotik Çatısı 
- **Platformlar:** Linux, macOS, Windows 

## Sıkça sorulan sorular
- microduck_rl'i çalıştırmak için fiziksel Microduck robotuna sahip olmak şart mı? Hayır. Kod tabanı tamamen MuJoCo simülatörü üzerinde sanal olarak çalıştırılabilir; bilgisayarınızda robotun 3B simülasyonunu izleyebilirsiniz.
- GPU desteği gerekli mi? MuJoCo CPU üzerinde de oldukça hızlı çalışır; ancak paralel ortamlarla pekiştirmeli öğrenme eğitimi yaparken CUDA destekli bir GPU süreci ciddi oranda hızlandırır.
- Eğitilen model fiziksel robota nasıl aktarılır? Eğitim tamamlandığında üretilen ONNX veya PyTorch checkpoint dosyası, Microduck'ın yerleşik kontrol bilgisayarına yüklenerek doğrudan motor torklarına bağlanır.
- Farklı robot modellerini destekler mi? microduck_rl öncelikli olarak Microduck için optimize edilmiştir; ancak modüler yapısı sayesinde benzer bipedal veya quadruped robot MJCF modellerine uyarlanabilir.

## Bağlantılar
- [GitHub deposu →](https://github.com/pollen-robotics/microduck_rl)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-08-31 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Yapay Zekâ Açık Kaynak Makine Öğrenimi CLI Framework

---
Kaynak: TreScout Keşif · https://trescout.com/discover/microduck-rl/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
