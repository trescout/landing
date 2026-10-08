# Memoria del sistema de archivos para agentes de inteligencia artificial.

Desarrollado por Volcengine, OpenViking ofrece una base de datos de contexto de mejora automática para agentes de IA. Este sistema combina memoria de agente, procesos de recuperación de información (RAG) y capacidades bajo un mismo techo.

- ★ 39.151
- Python
- GitHub Trending · 2026-08-18

## Actualizaciones

- **3 de octubre de 2026:** Estrellas 38,859 → 39,151, última versión v0.4.23 (2 de octubre de 2026).
- **28 de septiembre de 2026:** Estrellas 38,733 → 38,859, última versión v0.4.22 (28 de septiembre de 2026).
- **27 de septiembre de 2026:** Estrellas 37,128 → 38,733, última versión v0.4.21 (20 de septiembre de 2026).
- **14 de septiembre de 2026:** Estrellas 36,182 → 37,128, última versión v0.4.20 (14 de septiembre de 2026).

## Qué aporta

- Organiza la información jerárquicamente como un sistema de archivos.
- Reduce el costo de la inteligencia artificial con carga en capas.
- Hace que el historial del agente sea rastreable y depurable.

## Instalación

**Instalación y puesta en marcha del servidor.**

```
pip install openviking --upgrade
openviking-server init      # interactive wizard: providers, models, ov.conf
openviking-server doctor    # validate setup
openviking-server           # start (background: nohup openviking-server > openviking.log 2>&1 &)
```

## Ejecución

**Iniciar un chat con soporte de bot**

```
pip install "openviking[bot]"
openviking-server --with-bot
ov chat   # in another terminal
```

## Si no programa

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Construya una gestión de contexto para un agente de inteligencia artificial utilizando la base de datos OpenViking. Estructura la información a través del protocolo viking:// separando la información en capas de resumen L0, descripción general L1 y detalle L2. Al colocar la memoria, los recursos y las capacidades del agente en este sistema de archivos virtual, le permite navegar por directorios durante el interrogatorio y crear memoria a largo plazo aprendiendo de sesiones pasadas.

## Términos relacionados del glosario

- [RAG](https://trescout.com/es/dictionary/rag/)
- [AI Skills](https://trescout.com/es/dictionary/ai-skills/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Es para desarrolladores que desean combinar la gestión de memoria, los procesos de recuperación de información y las capacidades de los agentes de IA en un sistema organizado.
- **Licencia:** AGPL-3.0

## Enlaces

- [Repositorio en GitHub →](https://github.com/volcengine/OpenViking)
- [Leer en turco →](https://trescout.com/discover/openviking/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-08-18: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/openviking/
