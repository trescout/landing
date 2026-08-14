# ¿Qué es Protocol Buffers?

> Protobuf

Es un método que permite que diferentes software empaqueten y transporten datos muy rápidamente y en tamaños pequeños mientras hablan entre sí.

## Definición
El software suele utilizar archivos de texto cuando se envían datos entre sí, pero a veces estos archivos pueden ser muy grandes. Los buffers de protocolo convierten los datos a un formato binario, lo que permite que ocupen mucho menos espacio y se transmitan mucho más rápido. Fue desarrollado por Google y ahora se considera el estándar en la comunicación entre sistemas.

## Cómo funciona
Primero se define la estructura de los datos en un archivo de plantilla. Luego, su software empaqueta los datos usando esta plantilla y los envía a la otra parte. El lado receptor restaura los datos utilizando la misma plantilla.

## Dónde se usa
Se utiliza en arquitecturas de microservicios, comunicación de aplicaciones móviles con servidores y sistemas que requieren un alto rendimiento.

## Suele confundirse con
Puede confundirse con formatos de datos basados ​​en texto como JSON o XML, pero es mucho más rápido y más pequeño.

## Preguntas frecuentes
**¿Puede la gente leer?**
No, los datos no pueden ser leídos directamente por humanos ya que están en formato binario, están diseñados para que sólo las computadoras puedan entenderlos.


## Términos relacionados
- [API](/es/dictionary/api/)
- [Networking Stack](/es/dictionary/networking-stack/)
- [Serialization](/es/dictionary/serialization/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/protocol-buffers/
