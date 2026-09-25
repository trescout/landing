# ¿Qué es la Serialización (Serialization)?

> Inglés: Serialization · Etimología: latín series (sucesión, cadena) + facere (hacer)

**Categoría:** Dev  
**Última actualización:** 2026-09-19

La serialización (serialization) es el proceso mediante el cual estructuras de datos en memoria, objetos y grafos de punteros se transforman en una secuencia lineal de bytes o texto plano apta para transmitirse por red o guardarse en disco.

## ¿Qué es la Serialización y por qué es necesaria? Modelo de Memoria
En los sistemas operativos modernos, los procesos se ejecutan en espacios de memoria virtual independientes. Los objetos creados en el montón (heap) se comunican mediante punteros que solo son válidos localmente. La serialización aplana estas complejas relaciones de memoria para que puedan persistirse o compartirse entre distintas máquinas y lenguajes.

## Formatos de Serialización: Texto frente a Protocolos Binarios
La elección del formato responde a compromisos de rendimiento y legibilidad:
- **Formatos basados en texto (JSON, YAML, XML):** Fáciles de inspeccionar por personas y con soporte nativo en la web, aunque exigen mayor uso de CPU al parsear y consumen más ancho de banda.- **Formatos binarios (Protocol Buffers, MessagePack, Avro):** Codificación binaria optimizada con tipado estricto, reduciendo drásticamente el tamaño del mensaje.- **Evolución de Esquemas:** Tecnologías como Protobuf aseguran compatibilidad hacia atrás y adelante entre microservicios con versiones dispares.

## Arquitectura de Deserialización Zero-Copy
La deserialización habitual aloca nuevos objetos en el heap para reconstruir la estructura. Sistemas avanzados como Cap'n Proto o FlatBuffers implementan **Zero-Copy**:
- **Alineación en Memoria:** Los datos se colocan con desplazamientos relativos estandarizados.- **Acceso Directo:** La aplicación lee atributos directamente del búfer de red o de archivos mapeados (mmap) sin realizar copias ni alocaciones secundarias.

## Seguridad: Insecure Deserialization (CWE-502)
Si un framework no solo serializa datos puros sino también clases u objetos ejecutables (como pickle en Python o la serialización nativa de Java), se presentan riesgos severos:
- **Ejecución Remota de Código (RCE):** Un atacante puede fabricar cadenas de objetos (gadget chains) que ejecutan comandos del sistema en cuanto se procesa el mensaje.- **Mitigaciones:** Limitar la comunicación externa a formatos estrictos de datos (JSON, Protobuf) y validar la autenticidad del mensaje mediante HMAC o TLS.

## Por analogía
Es como desarmar un mueble en piezas planas para meterlo en una caja estrecha de mudanza y volver a montarlo con el manual al llegar a casa.

## Preguntas frecuentes

**¿Cuál es la diferencia entre serialización y deserialización?**  
La serialización aplana el grafo de objetos en una secuencia de bytes; la deserialización recupera los objetos en memoria a partir de esa secuencia.

**¿Por qué no se debe usar pickle con datos externos?**  
Pickle puede ejecutar llamadas arbitrarias durante la deserialización, permitiendo a un atacante ejecutar código malicioso en el servidor.

**¿Cómo logra FlatBuffers el rendimiento Zero-Copy?**  
Mediante desplazamientos binarios calculados de antemano que permiten consultar campos directamente en el búfer sin crear nuevos objetos.

**¿Cuándo conviene elegir JSON frente a Protobuf?**  
Cuando la claridad para depurar manualmente y la integración directa con clientes web son más valiosas que la eficiencia binaria estricta.

## Términos relacionados
- [API](/es/dictionary/api/)
- [Data Pipeline](/es/dictionary/data-pipeline/)
- [Buffer](/es/dictionary/buffer/)

## Herramientas relacionadas
- [YAML Cpp](/es/discover/yaml-cpp/)

---
Fuente: Diccionario Tecnológico TreScout · https://trescout.com/es/dictionary/serialization/
