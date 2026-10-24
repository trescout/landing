# Shellcode nedir?

*Geliştirme · Son güncelleme: 24 Ekim 2026*

Sistemlerdeki güvenlik açıklarını kullanarak hedef makinede komut satırı erişimi veya özel komutlar çalıştırmayı sağlayan küçük boyutlu makine kodudur.

## Tanım

Siber güvenlik dünyasında ve sızma testlerinde kullanılan bu özel kod parçacığı, sistem belleğine doğrudan enjekte edilir. İsmini tarihsel olarak hedef sistemde bir komut kabuğu açma amacından alır. Günümüzde sadece komut kabuğu açmakla kalmayıp sistemde istenen her türlü özel talimatı çalıştırmak için tasarlanmaktadır.

*Bir binanın kilitli kapısından içeri gizlice süzülüp güvenlik odasının kontrol panelini ele geçiren küçük bir anahtar kartına benzetebilirsiniz.*

## Nasıl çalışır?

Güvenlik araştırmacıları veya saldırganlar, yazılımdaki bellek taşması gibi açıkları tespit eder. Ardından hazırladıkları küçük makine kodunu işlemcinin doğrudan anlayacağı bayt dizilimi halinde belleğe yerleştirir. İşlemci bu komutları yürüttüğünde hedef sistem üzerinde yetkisiz kontrol elde edilir.

## Nerede kullanılır?

Güvenlik analizlerinde, sızma testlerinde ve zararlı yazılım incelemelerinde karşınıza çıkar.

## Sık karıştırılanlar

Kabuk betikleri ile karıştırılmamalıdır. Kabuk betikleri metin tabanlı yüksek seviyeli kodlarken bu kavram doğrudan işlemci seviyesinde çalışan ikili bayt kodudur.

## Sorular ve yanıtlar

**Shellcode sadece zararlı amaçlarla mı kullanılır?**

Güvenlik uzmanları sistemlerin savunma direncini test etmek ve açıkları kapatmak amacıyla da bu kodları kullanır.

**Bu kod parçacıkları neden çok küçük boyutlu yazılır?**

Bellekteki kısıtlı alanlara sızabilmek ve güvenlik filtrelerine takılmadan çalışabilmek için olabildiğince küçük tasarlanırlar.

## İlgili terimler

- [Exploit](https://trescout.com/dictionary/exploit/)
- [Penetration Testing](https://trescout.com/dictionary/penetration-testing/)
- [Vulnerability Scanning](https://trescout.com/dictionary/vulnerability-scanning/)
- [Backdoor](https://trescout.com/dictionary/backdoor/)

Bu açıklama TreScout için yapay zekâ ile sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/shellcode/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
