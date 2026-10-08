# ¿Qué es Environment Variables?

*Glosario · Dev · Última actualización: 22 de septiembre de 2026*

Las variables de entorno son identificadores que mantienen la configuración fuera del código.

## Definición y origen de la palabra

"Medio ambiente" significa medio ambiente. La contraseña y la dirección no permanecen en el código, permanecen en el sistema. El mismo código se comporta de manera diferente en diferentes entornos.

***Analogía:** Es como una tarjeta que se inserta y cambia en lugar de un ajuste integrado en el dispositivo.*

## ¿Cómo saberlo y utilizarlo en la vida diaria?

**Presentador:** Cadenas de conexión.
**Aplicación:** Selección de modo.
**CI:** Claves secretas.

## Profundidad técnica y arquitectura

Diseño:

**.env:** Archivo local, no se incluye en el repositorio.
**Prioridad:** El sistema de entorno sobrescribe el archivo.
**Esquema:** Lista de nombres requeridos.

Valor de ejemplo:

```
DATABASE_URL=postgres://kullanici:parola@localhost:5432/db
```

Regla: El valor real no se escribe en el ejemplo, se coloca un marcador de posición. La clave filtrada se cancela.

## Cosas frecuentemente mezcladas

Se considera un valor constante. Permanece en el código fijo, la variable está afuera. Uno es un tatuaje, el otro es una insignia.

## Uso en diferentes disciplinas

**Tarjeta:** Tarjeta de configuración variable.
**Batería del control remoto:** Energía extraíble.
**Llavero:** Acceso portátil.

## Preguntas frecuentes

**¿Por qué se mantiene oculto?**

Si se comparte, se descubre y se accede a la cuenta. Si permanece oculto, el riesgo disminuye.

**¿Qué es .env?**

Es un archivo de valores locales. No entra en el repositorio, pero sí su ejemplo.

**¿Qué sucede si se filtra?**

La clave se cancela y se auditan los registros. El retraso es considerable.

**¿Cuál es la prioridad?**

El entorno del sistema sobrescribe el archivo. El valor en vivo proviene del sistema.

## Términos relacionados

- [Secrets](https://trescout.com/es/dictionary/secrets/)
- [Runtime](https://trescout.com/es/dictionary/runtime/)
- [API](https://trescout.com/es/dictionary/api/)

## Herramientas relacionadas

- [Mise](https://trescout.com/es/discover/mise/)

Esta explicación se redactó en lenguaje sencillo para TreScout y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/environment-variables/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/environment-variables/
