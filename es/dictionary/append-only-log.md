# ¿Qué es Append-only log?

*Datos e infraestructura · Última actualización: 20 de septiembre de 2026*

El registro de solo agregar es una arquitectura de estructura de datos inmutable en la que los datos nunca se modifican ni eliminan in situ; cada nueva transacción se agrega al final del archivo en orden cronológico.

## Etimología y paradigma de invariancia

El concepto de registro de sólo agregar se desarrolló como una alternativa radical al paradigma de "actualización in situ" de las bases de datos tradicionales. En las bases de datos clásicas, cuando se actualiza un saldo o perfil, los datos antiguos del disco se eliminan y el nuevo valor se escribe sobre ellos. Este enfoque crea serios problemas de confiabilidad debido a escrituras incompletas que corrompen los datos en caso de una falla del sistema, cuellos de botella y acceso aleatorio al disco (E/S aleatoria).

En la arquitectura de registro de solo anexos, la historia es sagrada y no se puede alterar. En lugar de cambiar directamente el saldo de una cuenta bancaria, cada transacción de depósito y retiro se agrega como un nuevo registro al final del diario. El estado actual del sistema es el resultado natural de plegar/reducir todos estos eventos agregados del pasado al presente en orden cronológico. Este principio forma la columna vertebral de los sistemas distribuidos modernos, los motores de almacenamiento de alto rendimiento y las redes blockchain.

***Analogía:** Imagínese el diario oficial que lleva un contador. Cuando el contador comete un error en una línea, no puede abrir las páginas anteriores y borrar el número anterior con el líquido corrector. En su lugar, agrega una nueva línea de entrada inversa a la última línea en blanco del libro mayor, corrigiendo el error. El libro mayor sólo crece hacia adelante, el pasado nunca cambia; Cuándo y cómo se mueve el dinero se puede auditar retrospectivamente. El registro de solo anexar es exactamente ese libro de contabilidad digital; Registra datos como una historia viva, no como una instantánea.*

## Profundidad técnica y arquitectura del sistema

A nivel técnico, la arquitectura de registro de solo anexos se basa en tres pilares principales en términos de optimizaciones de hardware y coherencia de datos:

Acceso secuencial a disco (Sequential I/O) y WAL: Los discos magnéticos (HDD) e incluso las unidades de estado sólido modernas (SSD/NVMe) funcionan con un rendimiento exponencialmente mayor al escribir en bloques consecutivos que al escribir en direcciones aleatorias. Por esta razón, bases de datos como PostgreSQL, MySQL y SQLite utilizan el registro de escritura anticipada (Write-Ahead Logging o WAL). Cuando llega una transacción, primero se escribe una línea de registro de solo adición (append-only) de forma secuencial en el disco y se ejecuta fsync. De este modo, incluso si el servidor sufre un corte eléctrico repentino, al reiniciarse se lee el registro desde el principio y la base de datos se restaura a su estado de consistencia total en cuestión de segundos.
LSM-Tree y compactación de datos: Los motores NoSQL de alta intensidad de escritura como RocksDB, Apache Cassandra y Bigtable utilizan la arquitectura Log-Structured Merge-Tree (LSM-Tree). Todos los datos entrantes se añaden primero a una estructura ordenada en memoria (MemTable) y a un registro de solo anexión (append-only) simultáneo. Cuando la MemTable se llena, se vuelca al disco como archivos SSTable inmutables. Los datos antiguos o no válidos que se acumulan con el tiempo se limpian mediante procesos de compactación que se ejecutan en segundo plano.
Event Sourcing y Flujo Distribuido (Kafka): En arquitecturas de microservicios, las plataformas de mensajería distribuida como Apache Kafka y Redpanda funcionan como registros masivos distribuidos de solo anexado (append-only). En lugar de almacenar los estados de la aplicación en una base de datos, los eventos generados se escriben en registros inmutables. Los diferentes servicios consumen este registro a su propio ritmo para construir sus estados locales.
Inmutabilidad criptográfica y blockchain: Las tecnologías de registro distribuido (DLT), como Bitcoin y Ethereum, son registros de solo adición (append-only) distribuidos en los que cada bloque contiene el resumen criptográfico (hash) del bloque anterior. Ningún nodo de la red puede modificar los bloques pasados; solo se pueden añadir nuevos bloques al final del registro siguiendo las reglas de consenso.

## Dimensión sociológica: memoria digital y pista de auditoría

Más que un simple patrón de software, el registro de solo agregar representa una filosofía de responsabilidad y transparencia digitales. En el mundo empresarial y la administración pública, responder a la pregunta "quién cambió qué y cuándo" con precisión indestructible es la válvula de seguridad más importante para prevenir crisis de confianza.

En los sistemas tradicionales, la capacidad del administrador de la base de datos para eliminar y reescribir el historial con un único comando SQL hace que la memoria corporativa sea frágil. Los sistemas de solo anexos, por otro lado, garantizan que el pasado no pueda reescribirse, creando un escudo de inmunidad matemática contra errores humanos, amenazas internas y abuso de autoridad.

## Errores y conceptos erróneos comunes

No prever el consumo de disco: Si se olvida que los registros solo crecen y no se establecen estrategias adecuadas de retención y compactación de datos, el espacio en disco se agotará rápidamente.
Ignorar el rendimiento de lectura: escanear (reproducir) millones de líneas de registro de principio a fin para calcular el estado actual paraliza los tiempos de lectura; se deben tomar instantáneas (snapshots) del estado de forma regular.
Ignorar el derecho al olvido del RGPD: cuando las leyes de protección de datos personales exigen el derecho de supresión, eliminar datos de registros inmutables supone un desafío arquitectónico; este problema debe resolverse mediante el método de cripto-borrado (crypto-shredding), donde los datos se vuelven ilegibles al eliminar la clave de cifrado.

## Preguntas y respuestas

**¿Por qué la arquitectura de registro de solo agregar es más rápida que el modelo de actualización in situ?**

Escribir siempre datos secuencialmente hasta el final del archivo (escritura secuencial), en lugar de buscar bloques aleatorios en el disco, proporciona velocidades de escritura muy altas al minimizar el movimiento del cabezal del disco y la latencia de E/S.

**¿Cómo administrar el espacio en disco si el registro de solo agregar crece para siempre?**

Los sistemas toman una instantánea de la situación actual a intervalos regulares y eliminan o archivan de forma segura los registros antiguos ejecutando procesos de compactación o limpieza de segmentos en segundo plano.

**¿Cómo utilizar el registro de solo agregar en sistemas distribuidos y Apache Kafka?**

Los temas de Kafka son registros particionados de solo agregar donde los mensajes se agregan en orden cronológico; Varios consumidores leen el registro sin pérdidas y a alta velocidad con valores de compensación independientes.

**¿Cómo se aplica el derecho al olvido del RGPD a los sistemas de registro de solo anexos?**

Los datos del usuario en el archivo inmutable se cifran con una clave privada; Cuando el usuario solicita la eliminación, solo se destruye la clave de cifrado de ese usuario (cripto-trituración), lo que hace que los datos sean ilegibles sin dañar el registro.

## Términos relacionados

- [Distributed](https://trescout.com/es/dictionary/distributed/)
- [Serialization](https://trescout.com/es/dictionary/serialization/)
- [Local](https://trescout.com/es/dictionary/local/)
- [Self-hosted](https://trescout.com/es/dictionary/self-hosted/)
- [Runtime](https://trescout.com/es/dictionary/runtime/)
- [Memory Management](https://trescout.com/es/dictionary/memory-management/)

Esta explicación se redactó en lenguaje sencillo para TreScout con IA y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/append-only-log/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/append-only-log/
