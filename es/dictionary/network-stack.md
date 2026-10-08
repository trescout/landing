# ¿Qué es Network Stack?

*Glosario · Dev · Última actualización: 19 de septiembre de 2026*

Network Stack es el conjunto de capas de protocolo de espacio de usuario, kernel y controlador de hardware que permiten a un sistema operativo o hardware transmitir, enrutar y recibir paquetes de datos a través de la red.

## Arquitectura de capa 1: OSI Capa 7 frente a TCP/IP Capa 4

En la comunicación de red, en teoría se utiliza el modelo OSI de 7 capas definido por ISO y en la práctica el modelo TCP/IP, que forma la columna vertebral de Internet:

- Capa de aplicación (L7): HTTP/HTTPS, DNS, SSH, gRPC. Es el nivel en el que los datos se presentan o producen al usuario.
- Capa de transporte (L4): TCP (transmisión confiable y secuencial), UDP (streaming orientado a velocidad) y QUIC (HTTP/3 base). La unidad de datos del protocolo se llama Segmento.
- Capa de Internet/Red (L3): IPv4, IPv6, ICMP, BGP. Permite enrutar paquetes alrededor del mundo. La unidad de datos del protocolo se llama Paquete.
- Interfaz de Red / Capa de Enlace (L2/L1): Ethernet (802.3), Wi-Fi (802.11), fibra óptica y líneas de cobre. La unidad de datos del protocolo se define como Trama.

***Analogía:** Es similar a una operación de carga internacional: se escribe la carta (Solicitud), se mete la carta en el sobre y se adjunta el recibo certificado (TCP), se coloca el sobre en un paquete con una dirección internacional (IP), el paquete se carga en un contenedor (Ethernet Frame) y cruza el océano en el buque de carga (Physical line).*

## 2. Flujo de encapsulación y decodificación de paquetes

Cuando un cliente envía una solicitud al servidor web, cada capa agrega su propio encabezado a medida que los datos descienden por la pila:

```
[Kullanıcı Verisi: "GET / HTTP/1.1"]
                   ↓ (Taşıma Katmanı - TCP başlığı eklenir: Portlar, Sıra No)
[TCP Header | Payload]  --> TCP Segment (MSS ~1460 bayt)
                   ↓ (Ağ Katmanı - IP başlığı eklenir: Kaynak/Hedef IP)
[IP Header | TCP Header | Payload]  --> IP Paketi (MTU: 1500 bayt)
                   ↓ (Veri Bağı Katmanı - Ethernet başlığı ve FCS kuyruğu eklenir)
[Ethernet Header | IP Header | TCP Header | Payload | FCS Tail]  --> Ethernet Frame
```

Cuando llega al servidor de destino, el proceso se invierte (Decapsulación); Capa por capa se eliminan los encabezados y los datos se entregan al socket.

## 3. Ciclo de vida de Network Stack en el kernel de Linux

1. Hardware y búfer de anillo: la NIC captura el paquete y lo copia a través de DMA al búfer de anillo RX en la RAM.
2. Hard IRQ y SoftIRQ (NAPI): la NIC genera una interrupción de hardware; El kernel sondea los paquetes con ksoftirqd en modo NAPI para evitar el bloqueo de la CPU.
3. sk_buff (Socket Buffer): el kernel asigna la estructura de datos sk_buff que transporta punteros para cada paquete.
4. Filtrado y enrutamiento: las reglas de nftables se escanean y, si el paquete pertenece al socket local, se entrega a la máquina de estado TCP.
5. Llamada al sistema: el paquete se coloca en el búfer de recepción del socket (recv-Q); La aplicación lee los datos con epoll_wait().

## 4. Kernel Bypass y redes de próxima generación: eBPF/XDP y DPDK

- eBPF y XDP (eXpress Data Path): el paquete se filtra en la capa del controlador de la tarjeta de red antes de que se asigne sk_buff; Aquí es donde gigantes como Cloudflare reducen los ataques DDoS sin cargar el núcleo.
- DPDK (Kit de desarrollo de plano de datos): omite el kernel por completo; La aplicación en el espacio del usuario accede directamente a la memoria de la tarjeta de red sin copias.
- QUIC / HTTP/3: en lugar de TCP central en la capa de transporte, se ha cambiado un protocolo cifrado basado en UDP que se ejecuta en el espacio del usuario y supera el bloqueo de cabecera.

## Preguntas frecuentes

**¿Qué significa pila de red y cuál es su equivalente turco?**

Se llama "pila de red" o "pila de protocolos" en turco. Es una jerarquía de reglas de hardware y software superpuestas que permiten que una computadora se comunique a través de una red.

**¿Dónde está la principal diferencia entre TCP y UDP en la pila de red?**

Se encuentra ubicado en la capa de transmisión (Capa de Transporte/L4). TCP garantiza que los paquetes lleguen completos y en orden con un mecanismo de reconocimiento (ACK); UDP, por otro lado, envía paquetes a la mayor velocidad sin esperar confirmación.

**¿Qué es MTU (Unidad de transmisión máxima)?**

Es el tamaño de paquete más grande que una interfaz de red puede transportar en una sola trama sin fragmentación. El valor de MTU para Ethernet estándar es de 1500 bytes.

**¿Por qué se utiliza la arquitectura Kernel Bypass?**

Eliminar los costos de interrupción y copia de memoria del kernel de Linux en volúmenes de datos extremadamente altos, como 100 Gbps; Se utiliza con DPDK y eBPF/XDP para procesar paquetes directamente a nivel de hardware con latencia cero.

## Términos relacionados

- [VPN](https://trescout.com/es/dictionary/vpn/)
- [Runtime](https://trescout.com/es/dictionary/runtime/)
- [Memory Management](https://trescout.com/es/dictionary/memory-management/)
- [Packet Fragmentation](https://trescout.com/es/dictionary/packet-fragmentation/)
- [API](https://trescout.com/es/dictionary/api/)

## Herramientas relacionadas

- [OpenFlux](https://trescout.com/es/discover/openflux/)

Esta explicación se redactó en lenguaje sencillo para TreScout y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/network-stack/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/network-stack/
