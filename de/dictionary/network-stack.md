# Was ist Network Stack?

*Glossar · Dev · Zuletzt aktualisiert: 19. September 2026*

Network Stack ist der Satz von Hardware-Treiber-, Kernel- und User-Space-Protokollschichten, die es einem Betriebssystem oder einer Hardware ermöglichen, Datenpakete über das Netzwerk zu übertragen, weiterzuleiten und zu empfangen.

## Schicht-1-Architektur: OSI-Schicht 7 vs. TCP/IP-Schicht 4

In der Netzwerkkommunikation wird theoretisch das von der ISO definierte OSI-7-Schichten-Modell und in der Praxis das TCP/IP-Modell verwendet, das das Rückgrat des Internets bildet:

- Anwendungsschicht (L7): HTTP/HTTPS, DNS, SSH, gRPC. Es ist die Ebene, auf der Daten dem Benutzer präsentiert oder produziert werden.
- Transportschicht (L4): TCP (zuverlässige und sequentielle Übertragung), UDP (ratenorientiertes Streaming) und QUIC (Basis HTTP/3). Die Protokolldateneinheit wird Segment genannt.
- Internet-/Netzwerkschicht (L3): IPv4, IPv6, ICMP, BGP. Es ermöglicht die Weiterleitung von Paketen rund um die Welt. Die Protokolldateneinheit heißt Paket.
- Netzwerkschnittstelle/Verbindungsschicht (L2/L1): Ethernet (802.3), Wi-Fi (802.11), Glasfaser- und Kupferleitungen. Die Protokolldateneinheit ist als Frame definiert.

***Analogie:** Es ähnelt einem internationalen Frachtvorgang: Sie schreiben den Brief (Antrag), stecken den Brief in den Umschlag und fügen die eingeschriebene Quittung bei (TCP), legen den Umschlag in ein Paket mit einer internationalen Adresse (IP), das Paket wird in einen Container verladen (Ethernet Frame) und überquert den Ozean auf dem Frachtschiff (physische Linie).*

## 2. Paketkapselungs- und Decodierungsfluss

Wenn ein Client eine Anfrage an den Webserver sendet, fügt jede Ebene ihren eigenen Header hinzu, während die Daten im Stapel nach unten verschoben werden:

```
[Kullanıcı Verisi: "GET / HTTP/1.1"]
                   ↓ (Taşıma Katmanı - TCP başlığı eklenir: Portlar, Sıra No)
[TCP Header | Payload]  --> TCP Segment (MSS ~1460 bayt)
                   ↓ (Ağ Katmanı - IP başlığı eklenir: Kaynak/Hedef IP)
[IP Header | TCP Header | Payload]  --> IP Paketi (MTU: 1500 bayt)
                   ↓ (Veri Bağı Katmanı - Ethernet başlığı ve FCS kuyruğu eklenir)
[Ethernet Header | IP Header | TCP Header | Payload | FCS Tail]  --> Ethernet Frame
```

Beim Erreichen des Zielservers wird der Vorgang umgekehrt (Entkapselung); Schicht für Schicht werden die Header entfernt und die Daten an den Socket geliefert.

## 3. Netzwerk-Stack-Lebenszyklus im Linux-Kernel

1. Hardware und Ringpuffer: Die Netzwerkkarte erfasst das Paket und kopiert es per DMA in den RX-Ringpuffer im RAM.
2. Hard IRQ und SoftIRQ (NAPI): NIC löst Hardware-Interrupt aus; Der Kernel fragt Pakete mit ksoftirqd im NAPI-Modus ab, um eine CPU-Blockierung zu vermeiden.
3. sk_buff (Socket-Puffer): Der Kernel weist die sk_buff-Datenstruktur zu, die Zeiger für jedes Paket trägt.
4. Filterung und Routing: nftables-Regeln werden gescannt und wenn das Paket zum lokalen Socket gehört, wird es an die TCP-Statusmaschine übergeben.
5. Systemaufruf: Das Paket wird in den Empfangspuffer des Sockets gestellt (recv-Q); Die Anwendung liest die Daten mit epoll_wait().

## 4. Kernel-Bypass und Netzwerk der nächsten Generation: eBPF / XDP und DPDK

- eBPF und XDP (eXpress Data Path): Das Paket wird auf der Netzwerkkartentreiberebene gefiltert, bevor der sk_buff zugewiesen wird; Hier reduzieren Giganten wie Cloudflare DDoS-Angriffe, ohne den Kern zu belasten.
- DPDK (Data Plane Development Kit): Umgeht den Kernel vollständig; Die Anwendung im Benutzerbereich greift ohne Kopien direkt auf den Netzwerkkartenspeicher zu.
- QUIC / HTTP/3: Anstelle von Core-TCP auf der Transportschicht wurde auf ein UDP-basiertes verschlüsseltes Protokoll umgestellt, das im Userspace läuft und Head-of-Line-Blocking überwindet.

## Häufige Fragen

**Was bedeutet Netzwerk-Stack und was ist sein türkisches Äquivalent?**

Auf Türkisch wird es „Netzwerk-Stack“ oder „Protokoll-Stack“ genannt. Es handelt sich um eine Hierarchie überlappender Hardware- und Softwareregeln, die es einem Computer ermöglichen, über ein Netzwerk zu kommunizieren.

**Wo liegt der Hauptunterschied zwischen TCP und UDP im Netzwerkstapel?**

Es befindet sich in der Übertragungsschicht (Transport Layer / L4). TCP garantiert mit einem Bestätigungsmechanismus (ACK), dass Pakete vollständig und in der richtigen Reihenfolge ankommen; UDP hingegen sendet Pakete mit höchster Geschwindigkeit, ohne auf eine Bestätigung zu warten.

**Was ist MTU (Maximum Transmission Unit)?**

Dies ist die größte Paketgröße, die eine Netzwerkschnittstelle in einem einzelnen Frame ohne Fragmentierung übertragen kann. Der MTU-Wert für Standard-Ethernet beträgt 1500 Byte.

**Warum wird die Kernel-Bypass-Architektur verwendet?**

Eliminierung der Interrupt- und Speicherkopiekosten des Linux-Kernels bei extrem hohen Datenmengen wie 100 Gbit/s; Es wird mit DPDK und eBPF/XDP verwendet, um Pakete direkt auf Hardwareebene ohne Latenz zu verarbeiten.

## Verwandte Begriffe

- [VPN](https://trescout.com/de/dictionary/vpn/)
- [Runtime](https://trescout.com/de/dictionary/runtime/)
- [Memory Management](https://trescout.com/de/dictionary/memory-management/)
- [Packet Fragmentation](https://trescout.com/de/dictionary/packet-fragmentation/)
- [API](https://trescout.com/de/dictionary/api/)

## Verwandte Werkzeuge

- [OpenFlux](https://trescout.com/de/discover/openflux/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/network-stack/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/network-stack/
