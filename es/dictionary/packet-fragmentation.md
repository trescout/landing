# ¿Qué es Packet Fragmentation?

Es el proceso de dividir los datos enviados a través de Internet en partes más pequeñas según la capacidad de carga de la red.

## Definición
Al enviar datos por Internet, cada red tiene un tamaño máximo que puede transportar. Si los datos que envía son mayores que este tamaño, el sistema los divide en pedazos pequeños, los entrega al destino y los vuelve a ensamblar allí.

## Cómo funciona
A medida que se envían los datos, los dispositivos de red verifican el tamaño del paquete. Si se excede el límite, el paquete se fragmenta y a cada fragmento se le asigna un "número de secuencia". El dispositivo receptor mira estos números y ensambla las piezas en el orden correcto.

## Dónde se usa
Ocurre constantemente en segundo plano durante los protocolos de Internet y los procesos de red.

## Suele confundirse con
Puede confundirse con la pérdida de datos, pero se trata de un proceso de partición controlado.

## Preguntas frecuentes
**¿Qué pasa si se pierden piezas?**
El dispositivo receptor se da cuenta de que faltan piezas y le pide al remitente que las reenvíe.


## Términos relacionados
- [Networking Stack](/es/dictionary/networking-stack/)
- [DNS Tunneling](/es/dictionary/dns-tunneling/)

## Herramientas relacionadas
- [Zapret Discord Youtube](/es/discover/zapret-discord-youtube/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/packet-fragmentation/
