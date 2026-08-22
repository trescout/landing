# Investigación en profundidad con inteligencia artificial autónoma

Desarrollado por LangChain, la investigación abierta y profunda es un sistema autónomo que realiza búsquedas de varios pasos en Internet para responder preguntas complejas. Facilita procesos de investigación profundos al automatizar el proceso de investigación a través de etapas de planificación, recopilación de datos y síntesis.

- ★ 12.655
- Python
- GitHub Trending · 2026-07-22

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
Realice un análisis en profundidad de [ESCRIBA SU TEMA DE INVESTIGACIÓN AQUÍ] utilizando la herramienta Open Deep Research. Planifique su proceso de investigación, recopile datos en línea y sintetice sus hallazgos para crear un informe completo.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/open-deep-research/
