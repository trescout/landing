# Container nedir, ne demek?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-22

Container (Türkçe karşılığıyla **konteyner**), uygulamanın kod ve bağımlılıklarıyla tek pakette, her ortamda aynı çalışmasıdır.

## Tanım ve Kelime Kökeni
Konteynerler uygulamanın kodunu, kütüphanelerini ve ayarlarını tek pakete koyar. Sizin bilgisayarınızda nasıl çalışıyorsa sunucuda da öyle çalışır. Fikir eskidir (chroot, LXC), 2013 sonrası Docker ile yaygınlaştı, bugün OCI standardıyla tanımlanır.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Dağıtım:** Geliştiriciden canlıya aynı paket.
- **Mikro hizmet:** Her servisin kendi kutusu.
- **CI:** Her testin temiz kutuda koşması.

## Teknik Derinlik ve Mimari
Kavramlar:
- **İmaj:** Salt okunur kalıp, katmanlardan oluşur.
- **Konteyner:** İmajın çalışan örneği.
- **Dockerfile:** Kalıbın tarifi.
- **Kayıt (Registry):** İmajların tutulduğu depo.

Basit bir tarif:

```
FROM python:3.12-slim
COPY . /uygulama
WORKDIR /uygulama
CMD ["python", "app.py"]
```

Derleme ve çalıştırma:

```
docker build -t ornek:1.0 .
docker run -p 8000:8000 ornek:1.0
```

Sanal makine farkı: Makine kendi işletim sistemini taşır, konteyner ana çekirdeği paylaşır. Bu yüzden konteynerler daha hafif ve hızlı açılır.

## Sık Karıştırılanlar
Sanal makine sanılır. Makine tam işletim sistemi taşır, konteyner yalnızca uygulamayı taşır. Yalıtım makinede güçlü, konteynerde yeterlidir; seçim yüke göre yapılır.

## Farklı Disiplinlerde Kullanımı
- **Nakliye:** Standart boy konteynerle gemi, tren, kamyon uyumu.
- **Mutfak:** Malzemesi içinde hazır yemek kutusu.
- **Kamp:** Çantasında düzeniyle taşınan kamp seti.

## Bir benzetmeyle
Her yemek için gerekli tüm malzemeleri, baharatları ve araçları tek bir kutuya koyup istediğiniz yere götürmek gibidir; nerede açarsanız açın, aynı yemeği pişirirsiniz.

## Sıkça sorulanlar

**Konteyner neden bu kadar popüler?**  
Her ortamda aynı çalışmayı ve hızlı kurulumu sağladığı için. Mikro hizmet ve bulut düzeniyle birlikte standart haline geldi.

**Konteyner ile sanal makine farkı nedir?**  
Makine kendi işletim sistemini taşır, konteyner ana çekirdeği paylaşır. Konteyner hafif ve hızlı, makine yalıtımda güçlüdür.

**Konteyner güvenli midir?**  
Çekirdek paylaşıldığı için makine kadar izole değildir. İmajları güvenilir kaynaktan çekmeniz ve güncel tutmanız gerekir.

**Ne zaman sanal makine tercih edilir?**  
Farklı işletim sistemi veya güçlü yalıtım gerektiğinde. Geri kalan çoğu iş yükünde konteyner yeterlidir.

## İlgili terimler
- [Containers](/dictionary/containers/)
- [Virtual Machines](/dictionary/virtual-machines/)
- [Deployment](/dictionary/deployment/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/container/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
