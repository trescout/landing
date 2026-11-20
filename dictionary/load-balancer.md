# Load Balancer nedir?

*Geliştirme · Son güncelleme: 20 Kasım 2026*

Gelen ağ trafiğini birden fazla sunucu arasında paylaştırarak sistemin çökmesini önleyen ve performansı artıran trafik yönlendiricisidir.

## Tanım

Load Balancer (yük dengeleyici), bir web sitesine veya dijital servise gelen kullanıcı isteklerini arka plandaki sunucu havuzuna dengeli biçimde dağıtır. Tek bir sunucunun aşırı yük altında ezilmesini engeller ve donanım arızalarında trafiği anında sağlıklı sunuculara aktarır. Böylece sisteminizin kesintisiz, hızlı ve güvenilir bir şekilde hizmet vermesini sağlarsınız.

*Yoğun bir banka şubesinde tek bir gişenin önünde yığılma olmaması için müşterileri sırayla boşalan gişelere yönlendiren sıra matik sistemine benzer.*

## Nasıl çalışır?

Kullanıcıdan gelen ağ isteği doğrudan sunucuya gitmek yerine önce yük dengeleyiciyi karşılar. Sistem; sırayla dağıtım (Round Robin), en az bağlantı sayısı veya sunucu yanıt süresi gibi algoritmaları kullanarak isteği en uygun sunucuya yönlendirir. Eş zamanlı olarak sunucuların sağlık durumunu kontrol eder ve arızalananları trafik akışından otomatik olarak çıkarır.

## Nerede kullanılır?

Milyonlarca kullanıcıya hizmet veren e-ticaret platformlarında, mikroservis tabanlı bulut mimarilerinde ve kesintiye tahammülü olmayan finans sistemlerinde kullanılır.

## Sık karıştırılanlar

API Gateway ile karıştırılabilir. API Gateway kimlik doğrulama, istek dönüştürme ve API yönetimi gibi işlevlere odaklanırken yük dengeleyici temel olarak trafiği sunucular arasında verimli dağıtmayı hedefler.

## Sorular ve yanıtlar

**Yük dengeleyici kullanmak zorunlu mudur?**

Düşük trafikli basit siteler için zorunlu değildir fakat uygulamanız büyüdüğünde ve tek bir sunucu yetersiz kaldığında kesintileri önlemek için vazgeçilmez hâle gelir.

**Yazılımsal ve donanımsal yük dengeleyici arasındaki fark nedir?**

Donanımsal modeller veri merkezlerine yerleştirilen özel fiziksel cihazlardır. NGINX veya HAProxy gibi yazılımsal modeller ise bulut ortamlarında ve standart sunucularda çalışan esnek yazılımlardır.

## İlgili terimler

- [API Gateway](https://trescout.com/dictionary/api-gateway/)
- [Reverse Proxy](https://trescout.com/dictionary/reverse-proxy/)
- [Microservices](https://trescout.com/dictionary/microservices/)
- [Cloud Computing](https://trescout.com/dictionary/cloud-computing/)

Bu açıklama TreScout için yapay zekâ ile sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/load-balancer/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
