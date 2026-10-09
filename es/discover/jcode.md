# Marco de alto rendimiento para agentes de codificación

Desarrollado con el lenguaje Rust, jcode ofrece un marco para probar y evaluar agentes de inteligencia artificial orientados a la codificación. Proporciona una infraestructura estándar para medir el desempeño de los agentes utilizados en los procesos de desarrollo de software.

- ★ 20.361
- Rust
- GitHub Trending · 2026-06-21

## Actualizaciones

- **9 de octubre de 2026:** Estrellas 20,324 → 20,361, última versión v0.93.0 (9 de octubre de 2026).
- **6 de octubre de 2026:** Estrellas 20,303 → 20,324, última versión v0.91.0 (6 de octubre de 2026).
- **5 de octubre de 2026:** Estrellas 20,262 → 20,303, última versión v0.90.1 (5 de octubre de 2026).
- **2 de octubre de 2026:** Estrellas 20,218 → 20,262, última versión v0.90.0 (1 de octubre de 2026).

## Qué aporta

- Alta eficiencia de recursos en flujos de trabajo de múltiples sesiones
- Bajo uso de memoria y tiempo de inicio rápido
- Infraestructura de prueba para agentes de inteligencia artificial orientados a la codificación

## Instalación

**Instalación de macOS y Linux**

```
curl -fsSL https://raw.githubusercontent.com/1jehuang/jcode/master/scripts/install.sh | bash
```

**Instalación con cerveza casera**

```
brew tap 1jehuang/jcode
brew install jcode
```

## Ejecución

**Primera carrera con Ollama**

```
ollama pull llama3.2
jcode login --provider ollama
jcode --provider ollama --model llama3.2 run 'hello'
```

## Si no programa

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero probar el rendimiento y la capacidad de gestión de sesiones múltiples de mi agente de IA centrado en la codificación. Permítame optimizar el uso de recursos de mi agente y configurar un entorno de prueba estándar utilizando el marco jcode.

## Términos relacionados del glosario

- [Harness](https://trescout.com/es/dictionary/harness/)
- [Rust](https://trescout.com/es/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Es para desarrolladores que quieran probar agentes de inteligencia artificial utilizados en procesos de desarrollo de software y medir su desempeño.
- **Licencia:** MIT

## Enlaces

- [Repositorio en GitHub →](https://github.com/1jehuang/jcode)
- [Leer en turco →](https://trescout.com/discover/jcode/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-06-21: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/jcode/
