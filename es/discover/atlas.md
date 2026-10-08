# Control de versiones para agentes de inteligencia artificial

Atlas es un sistema de control de versiones (source control) para agentes de inteligencia artificial utilizados en procesos de desarrollo de software. Permite monitorear y consultar desde un único centro los cambios realizados por múltiples agentes de codificación.

- ★ 8.872
- Rust
- GitHub Trending · 2026-09-03

## Actualizaciones

- **3 de octubre de 2026:** Estrellas 7,855 → 8,872, última versión alpha-0.3.4 (27 de septiembre de 2026).
- **27 de septiembre de 2026:** Estrellas 7,448 → 7,855, última versión alpha-0.3.4 (27 de septiembre de 2026).
- **27 de septiembre de 2026:** Estrellas 4,722 → 7,448, última versión alpha-0.3.3 (19 de septiembre de 2026).
- **19 de septiembre de 2026:** Estrellas 4,762 → 4,722, última versión alpha-0.3.3 (19 de septiembre de 2026).

## Qué aporta

- Monitorea desde un centro único los cambios realizados por diferentes agentes de codificación.
- Permite continuar exactamente donde te quedaste en las transiciones de tareas mediante una memoria compartida entre agentes.
- Asocia cada cambio de código con la justificación y los comandos del agente que realizó dicho cambio.

## Instalación

**Instalación de las dependencias necesarias**

```
sudo apt install -y libglib2.0-dev libgtk-3-dev libwebkit2gtk-4.1-dev
```

**Compilación de la aplicación desde el código fuente**

```
git clone https://github.com/pacifio/atlas
cd atlas
bun install
bun run dev:app
```

## Si no programa

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Eres un asistente de desarrollo de software. Registra todos los cambios de código que realices, las decisiones tomadas y las herramientas utilizadas junto con el historial de la sesión utilizando Atlas. Si necesitas cambiar entre diferentes agentes como Claude Code o Codex mientras trabajas, lee los planes y notas de arquitectura de la sesión anterior desde la memoria compartida. Mantén el contexto llamando a archivos, carpetas o sesiones anteriores en la base de código mediante el símbolo '@' y documenta la razón de cada cambio que realices junto con las justificaciones de la sesión correspondiente.

## Términos relacionados del glosario

- [Source Control](https://trescout.com/es/dictionary/source-control/)
- [Rust](https://trescout.com/es/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Está destinado a desarrolladores de software que trabajan con múltiples agentes de inteligencia artificial y desean realizar un seguimiento de las justificaciones lógicas de los cambios realizados en los procesos de codificación.
- **Licencia:** MIT

## Enlaces

- [Repositorio en GitHub →](https://github.com/pacifio/atlas)
- [Leer en turco →](https://trescout.com/discover/atlas/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-09-03: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/atlas/
