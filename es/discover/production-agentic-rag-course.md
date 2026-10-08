# Llevando datos inteligentes con inteligencia artificial

El curso Production-Agentic-Rag ofrece capacitación práctica en el desarrollo de sistemas de producción asistida por recuperación basados en agentes (Agentic RAG) que automatizan los procesos de recuperación de información de fuentes de datos complejas. Basado en el lenguaje Python, este recurso enseña la arquitectura técnica necesaria para crear aplicaciones de inteligencia artificial escalables y de nivel de producción.

- ★ 9.265
- GitHub Trending · 2026-06-03

## Actualizaciones

- **3 de octubre de 2026:** Estrellas 8,216 → 9,265, última versión week7.0 (26 de noviembre de 2025).
- **2 de agosto de 2026:** Estrellas 6,536 → 8,216, última versión week7.0 (26 de noviembre de 2025).

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

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero desarrollar un asistente de investigación académica utilizando el proyecto del curso de trapo agente de producción. Para la instalación básica del proyecto, después de descargar el repositorio con el comando git clone, necesito configurar el archivo .env e instalar las dependencias con uv sync. Luego, quiero verificar que el sistema esté funcionando en http://localhost:8000/api/v1/health iniciando todos los servicios con el comando docker compose up --build -d. ¿Puede guiarme sobre las claves API y las configuraciones de servicios a las que debo prestar atención en este proceso?

## Términos relacionados del glosario

- [Clone](https://trescout.com/es/dictionary/clone/)
- [Agentic](https://trescout.com/es/dictionary/agentic/)
- [Localhost](https://trescout.com/es/dictionary/localhost/)
- [RAG](https://trescout.com/es/dictionary/rag/)
- [API](https://trescout.com/es/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Para ingenieros y desarrolladores de IA que desean desarrollar sistemas RAG basados ​​en agentes, escalables y de nivel de producción.
- **Licencia:** MIT

## Enlaces

- [Repositorio en GitHub →](https://github.com/jamwithai/production-agentic-rag-course)
- [Leer en turco →](https://trescout.com/discover/production-agentic-rag-course/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-06-03: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/production-agentic-rag-course/
