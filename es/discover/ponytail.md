# Conjunto de reglas para agentes de codificación con IA

Aplica reglas orientadas a tareas para reducir código innecesario y garantizar validación, seguridad y accesibilidad durante el flujo de codificación agentic. Está pensado para integrarse como plugin o adaptador en varios host de agentes.

- ★ 156.385
- JavaScript
- GitHub Trending · 2026-08-25

## Actualizaciones

- **6 de octubre de 2026:** Estrellas 155,501 → 156,385, última versión v4.13.0 (5 de octubre de 2026).
- **5 de octubre de 2026:** Estrellas 152,240 → 155,501, última versión v4.12.0 (5 de octubre de 2026).
- **3 de octubre de 2026:** Estrellas 146,524 → 152,240, última versión v4.10.3 (3 de octubre de 2026).
- **27 de septiembre de 2026:** Estrellas 138,874 → 146,524, última versión v4.10.0 (14 de septiembre de 2026).

## Instalación

**Agregar el marketplace de Claude Code**

```
/plugin marketplace add DietrichGebert/ponytail
```

**Instalar el plugin de Claude Code**

```
/plugin install ponytail@ponytail
```

## Ejecución

**Seleccionar el nivel de Ponytail**

```
/ponytail full
```

**Iniciar la revisión de diffs**

```
/ponytail-review
```

## ¿Qué hace esta herramienta?

La escalera de reglas se aplica después de leer el código afectado por un cambio. Un benchmark agentic corregido informó que, en 12 tareas sobre un repositorio real de FastAPI y React con Haiku 4.5, el promedio fue un 54% menos de líneas de código, un 22% menos de tokens, un 20% menos de coste y un 27% menos de tiempo frente a la línea base sin habilidades; estos resultados están limitados a condiciones de prueba específicas.

## ¿Para quién es?

Quienes quieran añadir reglas de validación, seguridad y accesibilidad al flujo de codificación en Claude Code, Codex, Gemini CLI y otros host de agentes compatibles.

## Qué no esperar

Generalizar resultados de benchmarks específicos a todos los proyectos o aplicar cambios críticos de producción sin revisión humana.

## Aspectos destacados

- Reglas centradas en tareas para reducir código innecesario
- Enfoque de revisión que preserva validación, manejo de errores, seguridad y accesibilidad
- Plugins o adaptadores de instrucciones para Claude Code, Codex, Gemini CLI y otros host

## Primer flujo de uso

1. Instala la integración de Ponytail para el host de agentes que utilices
2. Verifica que la instalación esté activa dentro del host
3. Elige el nivel de Ponytail adecuado
4. Ejecuta un flujo de revisión o auditoría sobre los cambios

## Inicio seguro

Los porcentajes provienen de promedios de un benchmark agentic corregido en 12 tareas sobre un repositorio real de FastAPI y React, con Haiku 4.5 y n=4. Se informó seguridad del 100% en una capa adversarial separada. El rango único antiguo del 80% al 94% no representa una media general.

## Primer prompt

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Escribe sólo el código necesario para la tarea y luego revisa los cambios en términos de validación, manejo de errores, seguridad y accesibilidad.

## Términos relacionados del glosario

- [Benchmark](https://trescout.com/es/dictionary/benchmark/)
- [Agentic](https://trescout.com/es/dictionary/agentic/)
- [Token](https://trescout.com/es/dictionary/token/)
- [Agent](https://trescout.com/es/dictionary/agent/)
- [CLI](https://trescout.com/es/dictionary/cli/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

## Enlaces

- [Repositorio en GitHub →](https://github.com/DietrichGebert/ponytail)
- [README oficial →](https://github.com/DietrichGebert/ponytail)
- [Método del benchmark agéntico →](https://github.com/DietrichGebert/ponytail/blob/main/benchmarks/results/2026-06-18-agentic.md)
- [Leer en turco →](https://trescout.com/discover/ponytail/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-08-25: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/ponytail/
