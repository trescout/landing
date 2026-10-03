# ¿Qué es Serialization?

La serialización es el proceso de convertir objetos, estructuras de datos y gráficos de punteros asignados dinámicamente en la memoria de trabajo (RAM) de un lenguaje de programación en un flujo de bytes plano y lineal o en un formato de texto que puede transmitirse a través de una red o almacenarse en un disco.

## ¿Qué significa la serialización y por qué es obligatoria? Modelo de memoria
En los sistemas operativos modernos, cada proceso se ejecuta en su propio espacio de direcciones virtuales aislado. Un objeto en tiempo de ejecución; Contiene variables locales en la pila, bloques de memoria asignados dinámicamente en el montón, punteros de función (vtable) y direcciones de referencia (0x7ffee4b2...).

## Formatos de serialización: Basados en texto vs. Binarios
Elegir el formato de serialización correcto en la arquitectura de software requiere un equilibrio entre la legibilidad humana, el costo de análisis (parsing) de CPU, el ancho de banda de red y la seguridad de tipos.

## Arquitectura de deserialización de copia cero (Zero-Copy)
En las bibliotecas de serialización clásicas (analizadores JSON o Protobuf estándar), el proceso de deserialización se lleva a cabo con los siguientes pasos:

## Dimensión de seguridad: Deserialización insegura (CWE-502)
Surgen vulnerabilidades de seguridad catastróficas cuando la serialización intenta serializar clases de objetos y comportamientos de tiempo de ejecución en lugar de simplemente mover datos puros. La deserialización insegura (Serialización inversa insegura), que se encuentra en la lista OWASP Top 10, permite al atacante ejecutar código arbitrario (Ejecución remota de código - RCE) en el sistema.

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
- [API](/es/dictionary/api/)
- [Data Pipeline](/es/dictionary/data-pipeline/)
- [Memory Management](/es/dictionary/memory-management/)
- [Network Stack](/es/dictionary/network-stack/)

## Herramientas relacionadas
- [YAML Cpp](/es/discover/yaml-cpp/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/serialization/
