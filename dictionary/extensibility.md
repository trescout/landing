# Extensibility nedir, ne demek?

*Sözlük · Geliştirme · Son güncelleme: 22 Eylül 2026*

Extensibility (Türkçe karşılığıyla **genişletilebilirlik**), bir yazılımın ana koduna dokunmadan eklenti ve modüllerle yeni yetenekler kazanabilmesidir.

## Tanım ve Kelime Kökeni

"Extensibility" terimi, İngilizce **extend** (genişletmek) kökünden türemiştir. Yazılım mühendisliğinde açık-kapalı ilkesi (Open-Closed Principle) ile yakından ilişkilidir: Bir modül genişletmeye açık, değişikliğe kapalı olmalıdır. Yani yeni bir özellik gerektiğinde mevcut kodu bozmak yerine, sisteme yeni bir parça eklemeniz yeterlidir.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?

Son kullanıcı olarak genişletilebilirlikle her gün karşılaşırsınız:

**Tarayıcı eklentileri:** Reklam engelleyici veya parola yöneticisini tarayıcınıza kurmanız.
**Editör eklentileri:** VS Code içine Python veya Prettier eklentisi eklemeniz.
**İçerik sistemleri:** WordPress sitesine iletişim formu veya önbellek eklentisi kurmanız.
**Tasarım araçları:** Figma topluluğundan hazır bileşen paketi yüklemeniz.

## Teknik Derinlik ve Mimari

Genişletilebilir bir sistemin çekirdeği küçüktür, çevresi eklentilerle büyür. Bu mimarinin tipik parçaları şunlardır:

**Eklenti arayüzü (Plugin API):** Çekirdeğin eklentilere açtığı kontrollü kapıdır. Eklenti yalnızca bu arayüz üzerinden sisteme dokunur.
**Kanca ve olay sistemi (Hooks & Events):** Çekirdek, belirli anlarda olay yayınlar. Eklentiler bu olaylara abone olur.
**Bildirim dosyası (Manifest):** Her eklenti, adını, sürümünü ve istediği izinleri bildiren küçük bir dosya taşır. Sistem, kurallara uymayan eklentiyi yüklemez.
**Korumalı alan (Sandbox) ve izinler:** Eklentilerin erişimi sınırlanır. Böylece hatalı bir eklenti tüm sistemi çökertemez.
**Sürüm uyumluluğu:** Çekirdek güncellenirken arayüzün geriye uyumlu tutulması gerekir. Aksi halde eklentiler bozulur.

Küçük bir örnek, tipik bir eklenti bildirimi şöyledir:

```
{
  "name": "ornek-eklenti",
  "version": "1.0.0"
}
```

## Farklı Disiplinlerde Kullanımı

**Mimari:** Taşıyıcı duvarlara dokunmadan yeni modüller eklenebilen prefabrik yapılar.
**Üretim:** Aynı gövdeye farklı aparatlar takılabilen mutfak robotları.
**Oyun:** Ana oyunu değiştirmeden yeni harita ve görev ekleyen mod toplulukları.

*Bir İsviçre çakısı gibidir; gövde aynı kalır, üzerine yeni bir tornavida veya fener ucu ekleyebilirsiniz.*

## Sıkça Sorulanlar

**Her yazılım genişletilebilir mi?**

Hayır. Yazılım en baştan bu esneklikle tasarlanmadıysa, sonradan eklenti desteği eklemek genellikle pahalı ve riskli olur.

**Eklenti ile çatallama (fork) arasındaki fark nedir?**

Eklentide ana kodu kopyalamazsınız, sisteme dışarıdan bağlanırsınız. Çatallamada ise kodun tamamını kopyalayıp ayrı bir yola gidersiniz.

**Eklentiler güvenli midir?**

Kaynağına göre değişir. Resmi mağazalardan, güncel ve çok kullanılan eklentileri tercih edin. Gereksiz izin isteyen eklentilere dikkat edin.

**Genişletilebilirlik performansı düşürür mü?**

Her eklenti bir miktar yük getirir. Az ve bakımlı eklenti kullandığınızda etkisi genellikle fark edilmez.

## İlgili terimler

- [Plugin](https://trescout.com/dictionary/plugin/)
- [API](https://trescout.com/dictionary/api/)
- [Framework](https://trescout.com/dictionary/framework/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/extensibility/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
