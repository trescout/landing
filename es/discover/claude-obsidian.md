# Sistema de información local para Claude Code

Organiza contenido de investigación en un vault de Obsidian enlazando fuentes y aplicando cambios aprobados mediante transacciones reversibles. Diseñado para priorizar el funcionamiento local y minimizar la dependencia de la nube.

- ★ 14.822
- Python
- GitHub Trending · 2026-08-25

## Actualizaciones

- **11 de septiembre de 2026:** Estrellas 14,727 → 14,822, última versión v2.2.0 (10 de septiembre de 2026).
- **8 de septiembre de 2026:** Estrellas 13,706 → 14,727, última versión v2.1.1 (25 de agosto de 2026).
- **27 de agosto de 2026:** Estrellas 12,404 → 13,706, última versión v2.1.1 (25 de agosto de 2026).

## Instalación

**Agregar el marketplace de Claude Code**

```
claude plugin marketplace add AgriciDaniel/claude-obsidian
```

**Instalar el plugin claude-obsidian**

```
claude plugin install claude-obsidian@agricidaniel-claude-obsidian
```

**Crear el plan para un vault separado**

```
python3 scripts/claude-obsidian.py init <new-vault> --generated-at <ISO-UTC> --operation-id init-reviewed
```

## Ejecución

**Verificar la instalación del plugin**

```
claude plugin list
```

**Iniciar el flujo wiki**

```
/claude-obsidian:wiki
```

## ¿Qué hace esta herramienta?

Organiza el contenido de investigación con libros de fuentes y de reclamaciones, páginas enlazadas y mapas de conocimiento. Agentes paralelos generan borradores y un orquestador aplica los cambios aprobados mediante una operación reversible.

## ¿Para quién es?

Quienes quieran construir una base de conocimiento local y citada en Obsidian para uso con Claude Code.

## Qué no esperar

No es adecuado como sistema de registro automático de transcripciones, para sincronización en la nube, como garantía de exactitud ni como sustituto de copias de seguridad o control de versiones.

## Aspectos destacados

- Diseñado para funcionar por defecto de forma local y con un enfoque de salida de red explícita
- Genera páginas enlazadas que citan fuentes mediante libros de fuentes y de reclamaciones
- Aplica cambios aprobados mediante operaciones que pueden revertirse

## Primer flujo de uso

1. Clona el repositorio y prepara un entorno con Python 3.11 o superior
2. Crea el plan inicial para un vault separado y revisa el plan JSON
3. Comprueba el valor approved_plan_sha256 y confirma el proceso completo
4. Abre el vault en Obsidian y ejecuta Claude Code con el plugin local
5. Inicia el flujo wiki y usa los pasos de agregar fuentes, consultar y guardar explícitamente

## Inicio seguro

El sistema no es una fuente de verdad. Usa además copias de seguridad y control de versiones para tus datos; revisa la salida de red y el plan aplicado.

## Primer prompt

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Inicia un flujo wiki local en Obsidian asociando las fuentes con libros de fuentes y de reclamaciones.

## Términos relacionados del glosario

- [Agent Skills](https://trescout.com/es/dictionary/agent-skills/)
- [AI Skills](https://trescout.com/es/dictionary/ai-skills/)
- [Agent](https://trescout.com/es/dictionary/agent/)

## Enlaces

- [Repositorio en GitHub →](https://github.com/AgriciDaniel/claude-obsidian)
- [Guía de instalación →](https://github.com/AgriciDaniel/claude-obsidian/blob/main/docs/install-guide.md)
- [README oficial →](https://github.com/AgriciDaniel/claude-obsidian)
- [Leer en turco →](https://trescout.com/discover/claude-obsidian/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-08-25: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/claude-obsidian/
