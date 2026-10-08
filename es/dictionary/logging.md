# ¿Qué es Logging?

*Glosario · Dev · Última actualización: 22 de septiembre de 2026*

El logging (o registro de eventos) es la escritura cronológica de los eventos de un programa.

## Definición y origen de la palabra

Log significa registro o historial. Cuando un programa falla silenciosamente, se puede leer en el registro lo que hizo hasta ese momento. Es como la caja negra de un avión: es el primer lugar donde se mira después de un accidente.

***Analogía:** Es como la caja negra de un avión que registra los datos de vuelo; las acciones del programa se registran en el diario.*

## ¿Cómo saberlo y utilizarlo en la vida diaria?

**Presentador:** Depuración.
**Producto:** Monitoreo de uso.
**Seguridad:** Registro de eventos.

## Profundidad técnica y arquitectura

Niveles:

**DEBUG:** Detalle para desarrolladores.
**INFO:** Flujo normal.
**ADVERTENCIA:** Situación sospechosa.
**ERROR:** Tarea fallida.

Reglas:

**Registro estructurado:** Formato JSON, capacidad de búsqueda.
**Prohibición de PII:** Las contraseñas y las identidades no se incluyen en el registro.
**Rotación:** El archivo se archiva cuando crece.

Ejemplo:

```
import logging
logging.basicConfig(level=logging.INFO)
logging.info("Ödeme alındı: sipariş=%s", siparis_id)
```

Demasiados registros ralentizan el sistema, muy pocos dejan ciego al sistema. Se activa INFO en producción y DEBUG cuando hay problemas.

## Cosas frecuentemente mezcladas

Se confunde con la observabilidad. Sin embargo, el registro es su bloque de construcción: el log es la materia prima, la capacidad de observación es el producto.

## Uso en diferentes disciplinas

**Caja negra:** Registro de datos de vuelo.
**Diario:** Notas en orden cronológico.
**Grabación de cámara:** Archivo de eventos.

## Preguntas frecuentes

**¿Es bueno guardarlo todo?**

No. Demasiado ralentiza y oculta lo importante, se mantiene un registro equilibrado.

**¿Qué es el nivel?**

Es la etiqueta de urgencia del registro. Actúa como filtro en la búsqueda.

**¿Dónde se escriben los registros?**

En un archivo, sistema central o servicio en la nube. En producción, se recomienda la recopilación centralizada.

**¿Cuánto tiempo se almacena?**

Depende de la política. La depuración requiere semanas, la auditoría requiere años.

## Términos relacionados

- [Observability](https://trescout.com/es/dictionary/observability/)
- [Traces](https://trescout.com/es/dictionary/traces/)
- [Logs](https://trescout.com/es/dictionary/logs/)

## Herramientas relacionadas

- [OmniRoute](https://trescout.com/es/discover/omniroute/)
- [Spdlog](https://trescout.com/es/discover/spdlog/)

Esta explicación se redactó en lenguaje sencillo para TreScout y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/logging/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/logging/
