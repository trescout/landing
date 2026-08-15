# Router que gestiona el tráfico de inteligencia artificial

Desarrollado por NVIDIA, Switchyard es un motor de inferencia de inteligencia artificial de alto rendimiento escrito en lenguaje Rust. Ofrece un entorno de ejecución optimizado para ejecutar modelos de lenguaje grandes (LLM) de manera eficiente en diferentes infraestructuras de hardware.

- ★ 923
- Rust
- GitHub Trending · 2026-08-13

## Qué aporta
- Enrutamiento del tráfico entre diferentes modelos de inteligencia artificial
- Traducción entre los formatos OpenAI y Anthropic API
- Seguimiento de métricas de transacciones y registros de errores

## Instalación
**Instalación como herramienta de línea de comando**

```
curl -LsSf https://astral.sh/uv/install.sh | sh
source "$HOME/.local/bin/env"
uv tool install --python 3.10 "nemo-switchyard[cli]"
```

**Instalación como servidor**

```
cargo install --locked switchyard-server
switchyard-server --help
```


## Ejecución
**Verificar el estado del servidor**

```
curl http://localhost:4000/health
```


## Si no programa
Actúa como un enrutador de tráfico de IA para mí. Con Switchyard, quiero que distribuya las solicitudes de mis agentes de codificación como Claude Code o Codex entre diferentes modelos, traduzca automáticamente entre los formatos OpenAI y Anthropic API y supervise todas las métricas operativas. Administre las solicitudes entrantes con algoritmos de enrutamiento estructurados y realice pruebas A/B o equilibrio de carga entre diferentes modelos cuando sea necesario.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/switchyard/
