# Consulta tu repositorio de códigos con inteligencia artificial

Code-graph-rag combina gráficos de conocimiento y generación asistida por recuperación (RAG) para comprender y consultar estructuras complejas en grandes repositorios de código. Permite a los desarrolladores analizar y editar bases de código en diferentes idiomas con la ayuda de inteligencia artificial.

- ★ 4.782
- Python
- GitHub Trending · 2026-08-10

## Qué aporta
- Vea relaciones complejas convirtiendo el código base en un gráfico de conocimiento
- Obtenga respuestas sobre la estructura del código haciendo preguntas en lenguaje natural
- Realice cambios precisos en el código con herramientas estructuradas de búsqueda y edición

## Instalación
**Instalación con administrador de paquetes.**

```
uv tool install "code-graph-rag[treesitter-full,semantic]"
```

**Método de instalación alternativo**

```
pipx install "code-graph-rag[treesitter-full,semantic]"
```


## Ejecución
**Iniciando la base de datos**

```
cgr daemon up
```

**Analizar y consultar el almacén.**

```
cgr start --repo-path /path/to/repo --update-graph
```


## Si no programa
Analice mi repositorio de código usando la herramienta Code-Graph-RAG. Responda mis preguntas utilizando relaciones entre funciones, clases y módulos en su código base. Sugerir cambios u optimizaciones que debo realizar en el código utilizando las capacidades de análisis estructural proporcionadas por la herramienta.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/code-graph-rag/
