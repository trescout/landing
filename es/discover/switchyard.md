# Router que gestiona el tráfico de inteligencia artificial

Desarrollado por NVIDIA, Switchyard es un motor de inferencia de inteligencia artificial de alto rendimiento escrito en lenguaje Rust. Ofrece un entorno de ejecución optimizado para ejecutar modelos de lenguaje grandes (LLM) de manera eficiente en diferentes infraestructuras de hardware.

- ★ 3.227
- Rust
- GitHub Trending · 2026-08-13

## Actualizaciones

- **27 de septiembre de 2026:** Estrellas 2,617 → 3,227, última versión v0.3.0 (22 de septiembre de 2026).
- **31 de agosto de 2026:** Estrellas 1,566 → 2,617, última versión v0.2.0 (10 de agosto de 2026).
- **15 de agosto de 2026:** Estrellas 923 → 1,566, última versión v0.2.0 (10 de agosto de 2026).

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

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Actúa como un enrutador de tráfico de IA para mí. Con Switchyard, quiero que distribuya las solicitudes de mis agentes de codificación como Claude Code o Codex entre diferentes modelos, traduzca automáticamente entre los formatos OpenAI y Anthropic API y supervise todas las métricas operativas. Administre las solicitudes entrantes con algoritmos de enrutamiento estructurados y realice pruebas A/B o equilibrio de carga entre diferentes modelos cuando sea necesario.

## Términos relacionados del glosario

- [Inference](https://trescout.com/es/dictionary/inference/)
- [Runtime](https://trescout.com/es/dictionary/runtime/)
- [LLM](https://trescout.com/es/dictionary/llm/)
- [Rust](https://trescout.com/es/dictionary/rust/)
- [API](https://trescout.com/es/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Es para desarrolladores que desean gestionar de manera eficiente grandes modelos de lenguaje en diferentes proveedores de hardware y servicios.
- **Licencia:** Apache-2.0

## Enlaces

- [Repositorio en GitHub →](https://github.com/NVIDIA-NeMo/Switchyard)
- [Leer en turco →](https://trescout.com/discover/switchyard/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-08-13: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/switchyard/
