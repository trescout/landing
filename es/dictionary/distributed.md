# Distributed Systems Falacias, teorema CAP, consenso y patrón Saga


**Categoría:** Dev  

**Última actualización:** 2026-09-19


Un sistema distribuido es una arquitectura informática formada por múltiples ordenadores independientes interconectados por red que colaboran para ofrecer un servicio unificado y tolerante a fallos.


## Etimología y Naturaleza de los Sistemas Distribuidos
Procede del latín *distribuere* (dividir, repartir). Como sentenció Leslie Lamport : *«Un sistema distribuido es aquel en el que el fallo de un ordenador que ni siquiera sabías que existía puede hacer que tu propia máquina quede inservible.»* Renuncian a la sencillez para ofrecer disponibilidad geográfica continua y escala horizontal.

## Las 8 Falacias de la Computación Distribuida (Deutsch)
Recopiladas por ingenieros de Sun Microsystems, ignorar estas premisas teóricas causa fallos críticos en producción :
- La red es fiable.
- La latencia es cero.
- El ancho de banda es infinito.
- La red es segura.
- La topología de red nunca varía.
- Solo hay un administrador de sistemas.
- El coste de transporte es cero.
- La red es homogénea.

## El Teorema CAP y el Modelo PACELC
El **Teorema CAP** formulado por Eric Brewer demuestra que un sistema de almacenamiento distribuido solo puede preservar dos de tres garantías frente a una partición de red :
- **Consistencia (C):** Cada lectura devuelve la escritura más reciente o un error explícito.- **Disponibilidad (A):** Cada petición recibe respuesta sin garantía de contener el dato más nuevo.- **Tolerancia a Particiones (P):** La red soporta la pérdida de mensajes entre nodos. Al ser P inevitable, se opta por sistemas CP (Consistencia) o AP (Disponibilidad).
El esquema **PACELC** añade : *Si hay Partición (P), elige entre Disponibilidad (A) o Consistencia (C); Si no (Else), elige entre Latencia (L) o Consistencia (C).*

## Protocolos de Consenso: Raft y Paxos
Garantizar que varios servidores acuerden un estado unívoco ante fallos de conexión :
- **Paxos:** El algoritmo formal demostrado por Leslie Lamport, célebre por su dificultad de comprensión e implementación.- **Raft:** Diseñado expresamente para ser inteligible por programadores, dividiendo el problema en elección de líder y replicación de registros.

## El Problema del Tiempo y los Relojes Lógicos
Al no existir un reloj físico sincronizado a nivel atómico en cada placa base, deducir el orden cronológico estricto resulta un desafío :
- **Relojes Lógicos de Lamport y Vectoriales:** Contadores causales que determinan qué evento ocurrió antes sin consultar horas astronómicas.- **Google TrueTime:** Arquitectura de hardware basada en receptores GPS y relojes atómicos en centros de datos para acotar la incertidumbre temporal a pocos milisegundos.

## Gestión de Datos Distribuidos: El Patrón Saga
El bloqueo clásico de dos fases (2PC) penaliza el rendimiento. Las arquitecturas modernas de microservicios aplican el **Patrón Saga** :
- Una cadena de transacciones locales orquestadas por una máquina de estados o coordinadas por eventos.
- Si una transacción falla, se desencadenan transacciones de compensación hacia atrás que revierten los efectos previos sin bloqueos globales.

## Por analogía
Un sistema centralizado es como un chef que cocina solo en una furgoneta; un sistema distribuido es como una corporación de restauración que opera en decenas de países y debe coordinar ingredientes y pedidos soportando caídas de línea y retrasos en los repartos.

## Preguntas frecuentes

**¿Qué es un sistema distribuido?**  
Un conjunto de ordenadores conectados por red que coordinan sus acciones mediante mensajes para operar como una sola plataforma.

**¿Por qué el Teorema CAP obliga a renunciar a una propiedad?**  
Porque ante una desconexión de red entre máquinas, debes decidir si rechazas peticiones o si aceptas datos que causarán inconsistencias.

**¿Qué ventaja aporta Raft frente a Paxos?**  
Raft se creó específicamente para ser comprensible y reproducible por desarrolladores de software con plenas garantías de consenso.

**¿Cómo funciona el patrón Saga?**  
Encadena operaciones locales independientes y aplica acciones compensatorias de reversión si alguna falla en el camino.

## Términos relacionados
- [Cloud Computing](/es/dictionary/cloud-computing/)
- [Network Stack](/es/dictionary/network-stack/)
- [Deployment](/es/dictionary/deployment/)
- [Runtime](/es/dictionary/runtime/)

## Herramientas relacionadas
- [Elasticsearch](/es/discover/elasticsearch/)
- [Cassandra](/es/discover/cassandra/)

---
Fuente: Glosario técnico TreScout · https://trescout.com/es/dictionary/distributed/
