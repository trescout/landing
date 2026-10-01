# ¿Qué es Logs?

Un log (registro en español) es una línea de eventos del sistema con marca de tiempo.

## Definición y origen de la palabra
"Log" significa diario de a bordo: el capitán escribe lo que sucede en el cuaderno. El software también escribe línea por línea lo que hace en segundo plano. En caso de error, se abre el cuaderno y se mira la hora. Es la primera fuente de salud del sistema.

## ¿Cómo saberlo y utilizarlo en la vida diaria?
Presentador: Depuración.Aplicación: Informe de bloqueo.Seguridad: Seguimiento de eventos.

## Profundidad técnica y arquitectura
Reglas de un buen registro:

## Cosas frecuentemente mezcladas
Se confunde con el rastreo (trace). El log es el registro de un evento, el trace es el camino del evento. Uno es una fotografía, el otro es una película.

## Uso en diferentes disciplinas
Caja negra: Datos de vuelo.Diario: Notas en orden cronológico.Recibo de caja: Registro de transacciones.

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
- [Observability](/es/dictionary/observability/)
- [QA](/es/dictionary/qa/)
- [Traces](/es/dictionary/traces/)

## Herramientas relacionadas
- [Grafana](/es/discover/grafana/)
- [Modly](/es/discover/modly/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/logs/
