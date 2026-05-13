# Sprint 0.7 · Müşteri görüşmesi e-posta şablonları

> **Durum:** Onaylı · Gemini revize + Claude denetiminden geçti (2026-05-10).
> **Ne zaman kullanılır:** Erken erişim listesi 30+ kişiye ulaştığında, 5-8 aday seçip tek tek manuel gönderilir (Resend'den toplu **değil**, `hello@`'dan kişisel mail).
> **Akış:** Davet → Calendly ile slot rezerve → görüşme → teşekkür maili.

---

## Gerekli ön hazırlık

- [ ] Calendly hesabı açık (`hello@trescout.com` ile signup)
- [ ] Event tipi: **"TreScout · Yüz yüze kahve sohbeti"** · 30 dk · in-person
- [ ] Calendly link'i hazır (örn. `https://calendly.com/trescout/kahve`)
- [ ] Şehir filtresi belli (örn. İstanbul)
- [ ] 2-3 cafe önerisi listesi (sakin, wifi'lı, merkezi)
- [ ] `INTERVIEW-SCRIPT.md` (`trescout-brand-kit/docs/`) elinde, sorulara hakimsin
- [ ] Aday listesi: 5-8 kişi (lokasyon uygun, tech background, hızlı yanıt verecek profil)

---

## 1️⃣ Davet maili

> Hep aynı şablon · sadece `[Şehir]` ve `[CALENDLY LİNKİ]` yerine doldur. Gönderen: `hello@trescout.com`.

**Konu satırı:**

```
Tecrübelerinize danışmak isterim · TreScout
```

> Alternatifler (gerekirse): "TreScout için bir kahve içelim mi?" / "[Şehir]'de kısa bir kahve molası?"

**Gövde:**

```
Merhaba,

Birkaç gün önce TreScout erken erişim listesine katıldığınız için teşekkürler.

Şu an TreScout'u inşa ediyoruz; ancak ilerlemeden önce sizin gibi bu alanla ilgilenen birkaç kişiyle samimi bir 30 dakikalık kahve sohbeti yapmak istiyorum. İş akışınızda nelerin tıkandığını ve nelerin gerçekten işe yaradığını sizden dinlemek benim için çok kıymetli.

Bu bir satış veya pazarlama görüşmesi değil. Amacım, ürünü doğrudan sizin gerçek ihtiyaçlarınıza göre şekillendirebilmek. Kahveler benden.

Eğer [Şehir]'deyseniz ve uygun bir zamanınız varsa buradan randevulaşabiliriz: [CALENDLY LİNKİ]

Sizin bildiğiniz sakin bir yer varsa orada, yoksa ortak bir noktada buluşabiliriz. Vaktiniz yoksa da hiç sorun değil; lansman döneminde sizi mutlaka bilgilendireceğim.

Saygılarımla,
Burhan Arıkan
TreScout · Kurucu
trescout.com
```

---

## 2️⃣ Görüşme onayı (Calendly otomatik gönderir)

Calendly default onay mailini kullanabilirsin. Custom yapacaksan:

```
Konu: TreScout sohbeti · [tarih saat]

Merhaba,

Buluşmamız onaylandı: [Cal'dan gelen tarih + saat].

Yer: [seçilen cafe veya "buluşma yerini önce konuşalım"]

Sizi bekliyor olacağım. Eğer ani bir aksilik olursa bu maile cevap vermeniz yeterli.

Burhan
trescout.com
```

---

## 3️⃣ Görüşme sonrası teşekkür maili

> Aynı gün veya ertesi gün gönder. Gönderen: `hello@trescout.com`.

**Konu:**

```
Keyifli sohbetiniz için teşekkürler
```

**Gövde:**

```
Merhaba,

Bugün vakit ayırıp tecrübelerinizi paylaştığınız için çok teşekkür ederim. Paylaştığınız detaylar, TreScout'un mutfağında alacağımız kararları doğrudan etkileyecek; buna emin olabilirsiniz.

Ürün hazır olduğunda size kişisel olarak haber vereceğim. Erken erişim listesinde önceliğiniz baki, herkesten önce deneyimlemeniz için davetiyenizi ileteceğim.

Bu süreçte aklınıza takılan bir sorun, ihtiyaç veya geri bildirim olursa doğrudan bu e-postayı yanıtlayabilirsiniz; mesajınız direkt bana ulaşıyor.

Sevgiler,
Burhan Arıkan
TreScout · Kurucu
trescout.com
```

---

## Notlar

### Mom Test prensibi
- **Pazarlama yapma.** Ürünü açıklamayı bekleme · gelirse cevap ver.
- **Hipotezini test etme**, "şunu sevdiniz mi?" sorma. Geçmiş davranışı sor: "Son ay teknoloji takibi için kaç saat harcadınız?"
- **Hayatlarındaki problemi öğren**, çözümünü değil.

### Kayıt stratejisi
- Görüşme öncesi: **"Kayıt almamın sakıncası var mı? Sadece notları sonradan hatırlamam için."** %95 evet der.
- Telefonu masaya çevirip ses kaydı. Cebe değil.
- İzin vermezse: not defteri, kısa cümleler.

### Görüşme sonrası
- 2-3 saat içinde insight'ları yaz · taze zamanda hatırlama keskindir
- Hangi cümleler doğrudan PRD'ye etki edebilir, hangi feature talebi geldi (PRD-v2'ye not düş)
- Aday listesinde "görüşüldü" işaretle, takip için sonraki adımı belirle

### Sprint 0.7 sonu
- 5-8 görüşmenin synthesis'i: `INTERVIEW-SCRIPT.md`'nin altına bulgu özetini ekle veya ayrı bir `docs/SPRINT-0.7-FINDINGS.md` aç
- PRD-v2 Karar Tarihçesi'ne ne öğrenildi, ne değiştirildi notu

---

> Bu doküman canlı. Akış kötü gidiyorsa metni revize et, sonraki turda kullan.
