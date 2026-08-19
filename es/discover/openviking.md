# Memoria del sistema de archivos para agentes de inteligencia artificial.

Desarrollado por Volcengine, OpenViking ofrece una base de datos de contexto de mejora automática para agentes de IA. Este sistema combina memoria de agente, procesos de recuperación de información (RAG) y capacidades bajo un mismo techo.

- ★ 29.066
- Python
- GitHub Trending · 2026-08-18

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
Construya una gestión de contexto para un agente de inteligencia artificial utilizando la base de datos OpenViking. Estructura la información a través del protocolo viking:// separando la información en capas de resumen L0, descripción general L1 y detalle L2. Al colocar la memoria, los recursos y las capacidades del agente en este sistema de archivos virtual, le permite navegar por directorios durante el interrogatorio y crear memoria a largo plazo aprendiendo de sesiones pasadas.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/openviking/
