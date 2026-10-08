# Gestiona árboles de trabajo de Git

Worktrunk es una interfaz de línea de comandos (CLI) escrita en Rust que facilita la gestión de árboles de trabajo (worktrees) de Git. Desarrollada especialmente para soportar flujos de trabajo de agentes de inteligencia artificial en paralelo, esta herramienta acelera el trabajo en múltiples tareas simultáneamente.

- ★ 8.444
- Rust
- GitHub Trending · 2026-09-13

## Actualizaciones

- **28 de septiembre de 2026:** Estrellas 8,424 → 8,444, última versión v0.80.0 (27 de septiembre de 2026).
- **27 de septiembre de 2026:** Estrellas 7,964 → 8,424, última versión v0.79.0 (21 de septiembre de 2026).
- **17 de septiembre de 2026:** Estrellas 7,379 → 7,964, última versión v0.78.0 (16 de septiembre de 2026).
- **13 de septiembre de 2026:** Estrellas 7,376 → 7,379, última versión v0.77.0 (8 de septiembre de 2026).

## Qué aporta

- Crea fácilmente espacios de trabajo para ejecutar múltiples tareas a la vez
- Acelera los flujos de trabajo locales con ganchos automáticos
- Soporta el trabajo paralelo de agentes de inteligencia artificial

## Instalación

**Instalación con cerveza casera**

```
brew install worktrunk && wt config shell install
```

**Instalación con Cargo**

```
cargo install worktrunk && wt config shell install
```

## Ejecución

**Cambiar entre árboles de trabajo**

```
wt switch feat
```

**Crear e iniciar un nuevo árbol de trabajo**

```
wt switch -c -x claude feat
```

## Si no programa

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero crear un nuevo árbol de trabajo en mi proyecto Git existente usando Worktrunk y comenzar una tarea paralela en este espacio. ¿Cómo debo usar los comandos wt para gestionar los árboles de trabajo tan fácilmente como las ramas y cómo puedo aprovechar los ganchos (hooks) para automatizar mi flujo de trabajo?

## Términos relacionados del glosario

- [Worktree](https://trescout.com/es/dictionary/worktree/)
- [CLI](https://trescout.com/es/dictionary/cli/)
- [Rust](https://trescout.com/es/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Diseñado para desarrolladores que trabajan en múltiples tareas de software o agentes de inteligencia artificial al mismo tiempo.

## Enlaces

- [Repositorio en GitHub →](https://github.com/max-sixty/worktrunk)
- [Leer en turco →](https://trescout.com/discover/worktrunk/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-09-13: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/worktrunk/
