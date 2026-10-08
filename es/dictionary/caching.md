# ¿Qué es Caching?

*Glosario · Data · Última actualización: 22 de septiembre de 2026*

El almacenamiento en caché (caching) es la copia de datos frecuentes en una capa rápida.

## Definición y origen de la palabra

Caché significa almacenamiento oculto. El sistema entrega los datos desde una copia en lugar de volver a calcularlos. El tiempo de respuesta disminuye y la carga se aligera. Funciona en todos los niveles, desde el navegador hasta el centro de datos.

***Analogía:** Es como llevar el libro favorito en la mochila; no hace falta ir a la biblioteca cada vez.*

## ¿Cómo saberlo y utilizarlo en la vida diaria?

**Navegador:** Almacenamiento de páginas e imágenes.
**Aplicación:** Copia sin conexión.
**Presentador:** Almacenamiento de resultados de consultas.

## Profundidad técnica y arquitectura

Estrategias:

**LRU:** Elimina el menos utilizado recientemente.
**TTL:** Lo que expira, se elimina.
**Cache-aside:** La aplicación lo gestiona.

Directiva del navegador:

```
Cache-Control: public, max-age=3600
```

Esta línea indica que la copia es válida durante una hora. Existe un coste de consistencia: cuando el recurso cambia, la copia queda obsoleta; en datos críticos, el tiempo se mantiene corto.

## Cosas frecuentemente mezcladas

Se confunde con la base de datos. La base de datos es persistente y extensa, la caché es temporal y rápida. Una es la caja fuerte, la otra es la cartera de bolsillo.

## Uso en diferentes disciplinas

**Bolso:** Libros frecuentes a mano.
**Nevera:** Comida diaria al frente.
**Despensa:** Stock masivo en segundo plano.

## Preguntas frecuentes

**¿Qué sucede si el caché se llena?**

Lo antiguo y poco usado se elimina, lo nuevo se escribe. La política gestiona esto.

**¿Cuándo se limpia?**

Cuando expira el tiempo, se supera la capacidad o manualmente. Los datos críticos se conservan por poco tiempo.

**¿Puede haber inconsistencias?**

Es posible. Cuando la fuente cambia, la copia queda obsoleta; se requiere disciplina de versiones y tiempos.

**¿Dónde se almacena?**

En memoria, disco o en el borde de la CDN. Se elige según el equilibrio entre velocidad y capacidad.

## Términos relacionados

- [KV Cache](https://trescout.com/es/dictionary/kv-cache/)
- [Prefix Cache](https://trescout.com/es/dictionary/prefix-cache/)
- [Database](https://trescout.com/es/dictionary/database/)

## Herramientas relacionadas

- [Free for Dev](https://trescout.com/es/discover/free-for-dev/)
- [OmniRoute](https://trescout.com/es/discover/omniroute/)
- [Guava](https://trescout.com/es/discover/guava/)
- [Omlx](https://trescout.com/es/discover/omlx/)

Esta explicación se redactó en lenguaje sencillo para TreScout y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/caching/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/caching/
