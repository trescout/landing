# Marco de alto rendimiento para agentes de codificación

Desarrollado con el lenguaje Rust, jcode ofrece un marco para probar y evaluar agentes de inteligencia artificial orientados a la codificación. Proporciona una infraestructura estándar para medir el desempeño de los agentes utilizados en los procesos de desarrollo de software.

- ★ 17.227
- Rust
- GitHub Trending · 2026-06-21

## Actualizar
- 12 de agosto de 2026: Star 16.663 → 17.227, última versión v0.75.3 (11 de agosto de 2026).
- 10 de agosto de 2026: Star 16.653 → 16.663, última versión v0.75.0 (10 de agosto de 2026).
- 10 de agosto de 2026: Star 16.505 → 16.653, última versión v0.74.0 (10 de agosto de 2026).
- 9 de agosto de 2026: Star 16,378 → 16,505, última versión v0.72.0 (8 de agosto de 2026).

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
Quiero probar el rendimiento y la capacidad de gestión de sesiones múltiples de mi agente de IA centrado en la codificación. Permítame optimizar el uso de recursos de mi agente y configurar un entorno de prueba estándar utilizando el marco jcode.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/jcode/
