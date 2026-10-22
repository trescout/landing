# ¿Qué es Distributed?

*Desarrollo · Última actualización: 19 de septiembre de 2026*

Distribuido, en el mundo de la informática, es compartir hardware, datos y procesos de cálculo entre muchos servidores (nodos) independientes conectados entre sí a través de la red, en lugar de una única máquina central, y este sistema sirve al usuario final como si fuera un único ordenador completo.

## Etimología y naturaleza de los sistemas distribuidos

La palabra "distributed" significa distribuido en español. Uno de los pioneros de la informática, Leslie Lamport, definió los sistemas distribuidos con esta célebre frase que ha pasado a la historia: "Un sistema distribuido es aquel en el que el fallo de un ordenador del que ni siquiera sabías que existía puede hacer que tu propio ordenador quede inutilizable".

En arquitecturas centralizadas (monolíticas), todas las operaciones ocurren en una única memoria principal y procesador. En los sistemas distribuidos, cientos de nodos distribuidos físicamente en centros de datos en diferentes continentes del mundo cumplen un propósito común al comunicarse a través de cables de red poco confiables.

## 8 falacias de la computación distribuida

En la década de 1990, los ingenieros de Sun Microsystems, L. Peter Deutsch y James Gosling, enumeraron los "8 errores mortales" cometidos por los desarrolladores de software que desarrollaban sistemas distribuidos. Todas las líneas de defensa de las arquitecturas modernas de nube y microservicios se construyen de acuerdo con estos conceptos erróneos:

1. La red es fiable: En realidad, los paquetes se pierden, las líneas de fibra se cortan y los routers se bloquean.
2. La latencia es cero: La velocidad de la luz y el retardo de conmutación de red entre dos máquinas siempre están presentes.
3. El ancho de banda es infinito: a medida que aumenta el volumen de datos, las tuberías de la red se obstruyen.
4. La red es segura: todas las comunicaciones distribuidas pasan por líneas abiertas y requieren protección criptográfica.
5. Invarianza de topología: Los servidores se encienden y apagan constantemente, las direcciones IP cambian.
6. Yalnızca bir sistem yöneticisi vardır: Múltiples equipos y proveedores de nube están involucrados.
7. El coste de transporte es cero: Los costes de serialización y empaquetado de CPU no pueden ignorarse.
8. La red es homogénea: Linux, Windows, ARM, x86 y diferentes protocolos funcionan juntos en el sistema.

## Teorema CAP y modelo PACELC

El Teorema CAP, propuesto por Eric Brewer, establece los límites fundamentales de la gestión de datos distribuidos. Ante una partición de red (Network Partition - P), el sistema debe elegir una de dos opciones:

- CP (Consistencia + Tolerancia a particiones): El sistema elige la consistencia. Los nodos con datos desactualizados rechazan responder; se sacrifica la disponibilidad (por ejemplo, en transacciones financieras y bancarias).
- AP (Disponibilidad + Tolerancia a particiones): El sistema prioriza la disponibilidad. Los nodos siguen respondiendo, pero algunos usuarios pueden ver datos desactualizados de hace unos segundos (por ejemplo, feeds de redes sociales).

En los sistemas modernos se utiliza el modelo PACELC de Daniel Abadi: cuando la red se divide (P), ¿se prioriza la disponibilidad (Availability) o la consistencia (Consistency)?; y cuando el sistema funciona normalmente (E), ¿se busca una menor latencia (Latency) o una consistencia inmediata (Consistency)?

## Protocolos de Consenso: Raft y Paxos

Se han desarrollado algoritmos de consenso para que servidores independientes que no confían entre sí y que pueden fallar en cualquier momento puedan ponerse de acuerdo sobre una única verdad:

Paxos: Desarrollado por Leslie Lamport, es un algoritmo de consenso matemáticamente probado pero extremadamente complejo de implementar en la práctica.
- Raft: El protocolo de consenso diseñado para ser comprensible por humanos, desarrollado por Diego Ongaro y John Ousterhout con el fin de resolver la complejidad de Paxos. Se basa en máquinas de estados para la elección de líder (Leader Election), la replicación de registros (Log Replication) y la seguridad (Safety) (funciona en el núcleo de sistemas gigantes como etcd, Kubernetes y Consul).
Tolerancia a fallas bizantinas (BFT): Es la base de los protocolos de cadena de bloques que logran el consenso incluso en entornos donde algunos nodos difunden información errónea o malintencionada de forma deliberada.

## El Problema del Tiempo en Sistemas Distribuidos y Soluciones

En una computadora central, el reloj de hardware muestra una sola verdad. En los sistemas distribuidos, en cambio, los relojes de los servidores muestran desviaciones físicas (drift del reloj) y el NTP (Network Time Protocol) es insuficiente para una precisión de milisegundos:

Relojes lógicos de Lamport (Lamport Timestamps): Definen el "orden de ocurrencia de los eventos" en lugar del tiempo físico.
Relojes vectoriales (Vector Clocks): Detectan conflictos de datos determinando qué dato es la causa o el efecto del otro.
Google TrueTime: combinación de relojes atómicos y antenas GPS utilizada en la base de datos distribuida Google Spanner. Reduce el margen de incertidumbre a unos pocos milisegundos, permitiendo transacciones ACID a escala global.

## Gestión de Datos y Procesamiento Distribuidos: El Patrón Saga

En los sistemas monolíticos, las transacciones de base de datos (transacciones ACID) son reemplazadas en los microservicios por el enfoque del Patrón Saga (Saga Pattern). En lugar de bloquear pasos distribuidos de larga duración con bloqueos de dos fases (2PC - Two Phase Commit), se utilizan arquitecturas orientadas a eventos donde cada servicio realiza su propia transacción local y, en caso de error, se activan transacciones compensatorias (Compensating Transactions) para revertir los cambios.

## Preguntas y respuestas

**¿Qué significa "Distributed" (significado en turco)?**

Significa 'distribuido' en la terminología informática. Es la distribución de la potencia de cálculo, el espacio de memoria o la base de datos a un gran número de máquinas independientes que se comunican a través de una red en lugar de un solo servidor.

**¿Qué significa el Teorema CAP en la práctica?**

Expresa que, cuando se produce una interrupción o retraso (partición) en la conexión de red, el sistema debe garantizar los datos más actualizados y hacer esperar algunas solicitudes (Consistencia) o responder instantáneamente a cada solicitud a costa de proporcionar datos obsoletos (Disponibilidad).

**¿Por qué se utiliza el algoritmo de consenso Raft en sistemas distribuidos?**

Se utiliza para garantizar que, incluso si algunos de los servidores de la red fallan, la mayoría restante de los nodos (Quorum) pueda elegir un nuevo líder entre ellos y sincronizar los registros de la base de datos sin pérdida en todo el clúster.

**¿Por qué se prefiere el patrón Saga en lugar del Compromiso de Dos Fases (2PC)?**

2PC (Two-Phase Commit) bloquea los recursos de la base de datos en los nodos distribuidos y bloquea todo el sistema cuando una máquina no responde. El patrón Saga, por otro lado, mantiene la alta disponibilidad del sistema utilizando eventos asíncronos y pasos de compensación.

## Términos relacionados

- [Cloud Computing](https://trescout.com/es/dictionary/cloud-computing/)
- [Network Stack](https://trescout.com/es/dictionary/network-stack/)
- [Deployment](https://trescout.com/es/dictionary/deployment/)
- [Runtime](https://trescout.com/es/dictionary/runtime/)

## Herramientas relacionadas

- [Elasticsearch](https://trescout.com/es/discover/elasticsearch/)
- [Cassandra](https://trescout.com/es/discover/cassandra/)

Esta explicación se redactó en lenguaje sencillo para TreScout con IA y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/distributed/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/distributed/
