# Llevando datos inteligentes con inteligencia artificial

El curso Production-Agentic-Rag ofrece capacitación práctica en el desarrollo de sistemas de producción asistida por recuperación basados en agentes (Agentic RAG) que automatizan los procesos de recuperación de información de fuentes de datos complejas. Basado en el lenguaje Python, este recurso enseña la arquitectura técnica necesaria para crear aplicaciones de inteligencia artificial escalables y de nivel de producción.

- ★ 8.216
- GitHub Trending · 2026-06-03

## Qué aporta
- Establecer la infraestructura necesaria para los sistemas RAG a nivel de producción.
- Aplicar métodos híbridos de búsqueda y procesamiento inteligente de datos.
- Desarrollar mecanismos de decisión basados ​​en agentes con LangGraph.

## Instalación
**Clonación e instalación del repositorio.**

```
git clone <repository-url>
cd arxiv-paper-curator

# 2. Configure environment (IMPORTANT!)
cp .env.example .env
# The .env file contains all necessary configuration for OpenSearch, 
# arXiv API, and service connections. Defaults work out of the box.
# You need to add Jina embeddings free api key and langfuse keys (check the blogs)

# 3. Install dependencies
uv sync

# 4. Start all services
docker compose up --build -d

# 5. Verify everything works
curl http://localhost:8000/api/v1/health
```


## Ejecución
**Reproducir contenido de una semana específica**

```
git clone --branch <WEEK_TAG> https://github.com/jamwithai/arxiv-paper-curator
cd arxiv-paper-curator
uv sync
docker compose down -v
docker compose up --build -d

# Replace <WEEK_TAG> with: week1.0, week2.0, etc.
```


## Si no programa
Quiero desarrollar un asistente de investigación académica utilizando el proyecto del curso de trapo agente de producción. Para la instalación básica del proyecto, después de descargar el repositorio con el comando git clone, necesito configurar el archivo .env e instalar las dependencias con uv sync. Luego, quiero verificar que el sistema esté funcionando en http://localhost:8000/api/v1/health iniciando todos los servicios con el comando docker compose up --build -d. ¿Puede guiarme sobre las claves API y las configuraciones de servicios a las que debo prestar atención en este proceso?

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/production-agentic-rag-course/
