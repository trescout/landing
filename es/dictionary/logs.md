# ¿Qué es Logs?

*Glosario · Dev · Última actualización: 22 de septiembre de 2026*

Un log (registro en español) es una línea de eventos del sistema con marca de tiempo.

## Definición y origen de la palabra

"Log" significa diario de a bordo: el capitán escribe lo que sucede en el cuaderno. El software también escribe línea por línea lo que hace en segundo plano. En caso de error, se abre el cuaderno y se mira la hora. Es la primera fuente de salud del sistema.

***Analogía:** Es como la caja negra de un avión; se mantiene un registro durante todo el vuelo y se rebobina en caso de problemas.*

## ¿Cómo saberlo y utilizarlo en la vida diaria?

**Presentador:** Depuración.
**Aplicación:** Informe de bloqueo.
**Seguridad:** Seguimiento de eventos.

## Profundidad técnica y arquitectura

Reglas de un buen registro:

**Marca de tiempo:** Hora en cada línea.
**Nivel:** Distinción entre INFO y ERROR.
**Rotación:** Archivo cuando el archivo crece.
**Prohibición de PII:** Los datos personales no se registran.

Línea de ejemplo:

```
2026-09-22T10:00:01 sipariş=4521 sonuc=ok sure_ms=38
```

La búsqueda se facilita en este formato. El texto desordenado no se puede buscar, se busca un registro organizado.

## Cosas frecuentemente mezcladas

Se confunde con el rastreo (trace). El log es el registro de un evento, el trace es el camino del evento. Uno es una fotografía, el otro es una película.

## Uso en diferentes disciplinas

**Caja negra:** Datos de vuelo.
**Diario:** Notas en orden cronológico.
**Recibo de caja:** Registro de transacciones.

## Preguntas frecuentes

**¿Por qué se necesitan registros (logs)?**

La causa del fallo está en el registro. Un sistema sin registros vuela a ciegas.

**¿Dónde se escribe?**

En un archivo o en un sistema central. En producción, se recomienda la recopilación centralizada.

**¿Cuánto tiempo se almacena?**

Depende de la política. La depuración requiere semanas, la auditoría requiere años.

**¿Se registran datos personales?**

No. Las contraseñas y la identidad no entran en el registro, se enmascaran.

## Términos relacionados

- [Observability](https://trescout.com/es/dictionary/observability/)
- [QA](https://trescout.com/es/dictionary/qa/)
- [Traces](https://trescout.com/es/dictionary/traces/)

## Herramientas relacionadas

- [Grafana](https://trescout.com/es/discover/grafana/)
- [Modly](https://trescout.com/es/discover/modly/)

Esta explicación se redactó en lenguaje sencillo para TreScout y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/logs/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/logs/
