# ¿Qué es Network Stack?

Network Stack es el conjunto de capas de protocolo de espacio de usuario, kernel y controlador de hardware que permiten a un sistema operativo o hardware transmitir, enrutar y recibir paquetes de datos a través de la red.

## Arquitectura de capa 1: OSI Capa 7 frente a TCP/IP Capa 4
En la comunicación de red, en teoría se utiliza el modelo OSI de 7 capas definido por ISO y en la práctica el modelo TCP/IP, que forma la columna vertebral de Internet:

## 2. Flujo de encapsulación y decodificación de paquetes
Cuando un cliente envía una solicitud al servidor web, cada capa agrega su propio encabezado a medida que los datos descienden por la pila:

## 3. Ciclo de vida de Network Stack en el kernel de Linux

## 4. Kernel Bypass y redes de próxima generación: eBPF/XDP y DPDK

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
- [VPN](/es/dictionary/vpn/)
- [Runtime](/es/dictionary/runtime/)
- [Memory Management](/es/dictionary/memory-management/)
- [Packet Fragmentation](/es/dictionary/packet-fragmentation/)
- [API](/es/dictionary/api/)

## Herramientas relacionadas
- [OpenFlux](/es/discover/openflux/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/network-stack/
