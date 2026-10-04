# Was ist Network Stack?

Network Stack ist der Satz von Hardware-Treiber-, Kernel- und User-Space-Protokollschichten, die es einem Betriebssystem oder einer Hardware ermöglichen, Datenpakete über das Netzwerk zu übertragen, weiterzuleiten und zu empfangen.

## Schicht-1-Architektur: OSI-Schicht 7 vs. TCP/IP-Schicht 4
In der Netzwerkkommunikation wird theoretisch das von der ISO definierte OSI-7-Schichten-Modell und in der Praxis das TCP/IP-Modell verwendet, das das Rückgrat des Internets bildet:

## 2. Paketkapselungs- und Decodierungsfluss
Wenn ein Client eine Anfrage an den Webserver sendet, fügt jede Ebene ihren eigenen Header hinzu, während die Daten im Stapel nach unten verschoben werden:

## 3. Netzwerk-Stack-Lebenszyklus im Linux-Kernel

## 4. Kernel-Bypass und Netzwerk der nächsten Generation: eBPF / XDP und DPDK

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
- [VPN](/de/dictionary/vpn/)
- [Runtime](/de/dictionary/runtime/)
- [Memory Management](/de/dictionary/memory-management/)
- [Packet Fragmentation](/de/dictionary/packet-fragmentation/)
- [API](/de/dictionary/api/)

## Verwandte Werkzeuge
- [OpenFlux](/de/discover/openflux/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/network-stack/
