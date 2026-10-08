# ¿Qué es Virtual Machines?

*Glosario · Dev · Última actualización: 22 de septiembre de 2026*

Una máquina virtual (conocida en inglés como *virtual machine*) es un ordenador independiente que comparte el hardware.

## Definición y origen de la palabra

Virtual significa virtual. Múltiples sistemas operativos se ejecutan en una sola máquina. Cada uno funciona de forma aislada con sus propios recursos y no daña el sistema principal.

***Analogía:** Es como alquilar habitaciones con puerta independiente en una misma casa.*

## ¿Cómo saberlo y utilizarlo en la vida diaria?

**Presentador:** Alojamiento multiinquilino.
**Prueba:** Prueba de diferentes sistemas.
**Desarrollo:** Entorno de prueba limpio.

## Profundidad técnica y arquitectura

Capas:

**Hipervisor:** El software que divide el hardware.
**Invitado:** El sistema que corre encima.
**Instantánea:** Captura instantánea, billete de vuelta.

Máquina rápida:

```
multipass launch --name test --cpus 2 --memory 4G
```

La diferencia de los contenedores: La máquina transporta el sistema, el contenedor transporta la aplicación. El aislamiento es fuerte en la máquina.

## Cosas frecuentemente mezcladas

Se confunde con un contenedor. La máquina es un sistema completo, el contenedor comparte el núcleo. Uno es un apartamento, el otro es compartir piso.

## Uso en diferentes disciplinas

**Habitaciones:** Compartimentos con puertas independientes.
**Apartamento:** Edificio común, espacio privado.
**Maleta:** Transporte compartimentado.

## Preguntas frecuentes

**¿Lo ralentiza?**

Tiene un coste de compartición. No se nota con un dimensionamiento correcto.

**¿Se propaga el virus?**

Generalmente no. El aislamiento es fuerte, la carpeta compartida está supervisada.

**¿Cuántos recursos se asignan?**

Se determina según la tarea. Se ajusta gradualmente mediante monitorización.

**¿Cuál es la diferencia con el contenedor?**

La máquina transporta el sistema, el contenedor la aplicación. Se intercambian aislamiento y velocidad.

## Términos relacionados

- [Containers](https://trescout.com/es/dictionary/containers/)
- [Runtime](https://trescout.com/es/dictionary/runtime/)
- [Self-hosting](https://trescout.com/es/dictionary/self-hosting/)

## Herramientas relacionadas

- [Container](https://trescout.com/es/discover/container/)

Esta explicación se redactó en lenguaje sencillo para TreScout y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/virtual-machines/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/virtual-machines/
