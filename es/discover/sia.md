# Pruebe modelos de IA de forma autónoma

SIA es un marco de IA de mejora automática desarrollado para mejorar de forma autónoma el rendimiento de los modelos y agentes de IA en tareas de referencia específicas. Este sistema basado en Python permite a los sistemas de inteligencia artificial optimizar sus procesos analizando sus propios resultados.

- ★ 1.478
- Python
- GitHub Trending · 2026-06-12

## Qué aporta

- Mejora de forma autónoma el desempeño de tareas de los modelos de inteligencia artificial.
- Meta proporciona un refinamiento cíclico entre los agentes objetivo y de retroalimentación.
- Ofrece alta precisión y eficiencia en la velocidad de procesamiento en tareas de referencia.

## Instalación

**Instalación con modelos Claude**

```
python3 -m venv .venv && source .venv/bin/activate
pip install 'sia-agent[claude]'
export ANTHROPIC_API_KEY="..."
```

**Configuración con múltiples proveedores (OpenHands)**

```
python3 -m venv .venv && source .venv/bin/activate
pip install 'sia-agent[openhands]'

# Export the key(s) for the provider(s) you'll use:
export ANTHROPIC_API_KEY="..."   # for anthropic/* models
export GEMINI_API_KEY="..."      # for gemini/* models (or GOOGLE_API_KEY)
export OPENAI_API_KEY="..."      # for openai/* models
```

## Ejecución

**Comenzando el ciclo de autocuración**

```
sia run --task gpqa --max_gen 5 --run_id 1
```

**Panel de visualización**

```
sia web
```

## Si no programa

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero mejorar el rendimiento de un agente de IA utilizando el marco SIA. Después de completar la instalación, ¿qué comando debo usar para iniciar el ciclo de mejora personal seleccionando una de las tareas disponibles (por ejemplo, gpqa) y cómo debo interpretar los resultados al final del proceso (target_agent.py, agent_execution.json, Improvement.md)? Además, ¿cómo puedo incluir mi propio directorio de tareas personalizado en el sistema?

## Términos relacionados del glosario

- [Benchmark](https://trescout.com/es/dictionary/benchmark/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Es adecuado para desarrolladores e investigadores que quieran optimizar el rendimiento de los modelos de IA mediante procesos de mejora autónomos.
- **Licencia:** MIT

## Enlaces

- [Repositorio en GitHub →](https://github.com/hexo-ai/sia)
- [Leer en turco →](https://trescout.com/discover/sia/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-06-12: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/sia/
