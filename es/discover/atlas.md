# Control de versiones para agentes de inteligencia artificial

Atlas es un sistema de control de versiones (source control) para agentes de inteligencia artificial utilizados en procesos de desarrollo de software. Permite monitorear y consultar desde un único centro los cambios realizados por múltiples agentes de codificación.

- ★ 3.058
- Rust
- GitHub Trending · 2026-09-03

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
Eres un asistente de desarrollo de software. Registra todos los cambios de código que realices, las decisiones tomadas y las herramientas utilizadas junto con el historial de la sesión utilizando Atlas. Si necesitas cambiar entre diferentes agentes como Claude Code o Codex mientras trabajas, lee los planes y notas de arquitectura de la sesión anterior desde la memoria compartida. Mantén el contexto llamando a archivos, carpetas o sesiones anteriores en la base de código mediante el símbolo '@' y documenta la razón de cada cambio que realices junto con las justificaciones de la sesión correspondiente.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/atlas/
