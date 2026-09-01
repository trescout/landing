# Conjunto de reglas para agentes de codificación con IA

Aplica reglas orientadas a tareas para reducir código innecesario y garantizar validación, seguridad y accesibilidad durante el flujo de codificación agentic. Está pensado para integrarse como plugin o adaptador en varios host de agentes.

- ★ 119.108
- JavaScript
- GitHub Trending · 2026-08-25

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
- Instala la integración de Ponytail para el host de agentes que utilices
- Verifica que la instalación esté activa dentro del host
- Elige el nivel de Ponytail adecuado
- Ejecuta un flujo de revisión o auditoría sobre los cambios

## Inicio seguro

## Primer prompt
Escribe sólo el código necesario para la tarea y luego revisa los cambios en términos de validación, manejo de errores, seguridad y accesibilidad.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- README oficial →
- Método del benchmark agéntico →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/ponytail/
