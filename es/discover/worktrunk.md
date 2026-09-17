# Gestiona árboles de trabajo de Git

Worktrunk es una interfaz de línea de comandos (CLI) escrita en Rust que facilita la gestión de árboles de trabajo (worktrees) de Git. Desarrollada especialmente para soportar flujos de trabajo de agentes de inteligencia artificial en paralelo, esta herramienta acelera el trabajo en múltiples tareas simultáneamente.

- ★ 7.964
- Rust
- GitHub Trending · 2026-09-13

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
Quiero crear un nuevo árbol de trabajo en mi proyecto Git existente usando Worktrunk y comenzar una tarea paralela en este espacio. ¿Cómo debo usar los comandos wt para gestionar los árboles de trabajo tan fácilmente como las ramas y cómo puedo aprovechar los ganchos (hooks) para automatizar mi flujo de trabajo?

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/worktrunk/
