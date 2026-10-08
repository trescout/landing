# Investigación en profundidad con inteligencia artificial autónoma

Desarrollado por LangChain, la investigación abierta y profunda es un sistema autónomo que realiza búsquedas de varios pasos en Internet para responder preguntas complejas. Facilita procesos de investigación profundos al automatizar el proceso de investigación a través de etapas de planificación, recopilación de datos y síntesis.

- ★ 12.655
- Python
- GitHub Trending · 2026-07-22

## Actualizaciones

- **22 de agosto de 2026:** Estrellas 12,307 → 12,655, repositorio archivado, desarrollo detenido.

## Qué aporta

- Investigación autónoma de varios pasos para preguntas complejas
- Compatibilidad con diferentes proveedores de modelos y herramientas de búsqueda.
- Procesos de investigación visualizados a través de LangGraph

## Instalación

**Clonación del repositorio y preparación del entorno.**

```
git clone https://github.com/langchain-ai/open_deep_research.git
cd open_deep_research
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

**Instalando dependencias**

```
uv sync
# or
uv pip install -r pyproject.toml
```

## Ejecución

**Iniciando el servidor**

```
# Install dependencies and start the LangGraph server
uvx --refresh --from "langgraph-cli[inmem]" --with-editable . --python 3.11 langgraph dev --allow-blocking
```

## Si no programa

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Realice un análisis en profundidad de [ESCRIBA SU TEMA DE INVESTIGACIÓN AQUÍ] utilizando la herramienta Open Deep Research. Planifique su proceso de investigación, recopile datos en línea y sintetice sus hallazgos para crear un informe completo.

## Términos relacionados del glosario

- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Es para desarrolladores e investigadores que desean automatizar procesos de investigación autónomos sobre temas complejos.
- **Licencia:** MIT

## Enlaces

- [Repositorio en GitHub →](https://github.com/langchain-ai/open_deep_research)
- [Leer en turco →](https://trescout.com/discover/open-deep-research/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-07-22: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/open-deep-research/
