# Herramienta de evaluación de capacidades de agentes de inteligencia artificial

Desarrollado por NVIDIA, SkillEvaluator es un marco (framework) multicapa que evalúa las capacidades de los agentes de inteligencia artificial mediante métodos como el control de calidad, la detección de solapamiento semántico y la generación de datos sintéticos. Esta herramienta ofrece procesos de evaluación en vivo para medir los efectos en el comportamiento de los agentes.

- ★ 4.572
- Python
- GitHub Trending · 2026-11-16

## Actualizaciones

- **26 de noviembre de 2026:** Estrellas 4,483 → 4,572, última versión v1.2.1 (25 de noviembre de 2026).
- **24 de noviembre de 2026:** Estrellas 4,449 → 4,483, última versión v1.2.0 (24 de noviembre de 2026).
- **23 de noviembre de 2026:** Estrellas 4,448 → 4,449, última versión v1.0.1 (18 de noviembre de 2026).
- **23 de noviembre de 2026:** Estrellas 3,655 → 4,448, última versión v1.1.0 (23 de noviembre de 2026).

## Qué aporta

- Controla la calidad de las capacidades de los agentes de inteligencia artificial
- Mide el impacto de las habilidades de los agentes en los resultados de las tareas
- Ofrece informes detallados con un marco estructurado por capas

## Instalación

**Instalar el paquete**

```
pip install skillevaluator
```

## Ejecución

**Realizar control de calidad**

```
uv run --python 3.13 skillevaluator quality-check \
  src/skillevaluator/tier3/reference_skills/text-analyzer \
  -r cli -r json -o reports/first-quality
```

## Si no programa

Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero evaluar las capacidades de un agente de inteligencia artificial. Con este fin, completa la instalación ejecutando el comando pip install skillevaluator a través de la terminal y, a continuación, ejecuta el comando uv run --python 3.13 skillevaluator quality-check \
src/skillevaluator/tier3/reference_skills/text-analyzer \
-r cli -r json -o reports/first-quality para realizar una prueba de control de calidad de ejemplo.

Repositorio: https://github.com/NVIDIA/SkillEvaluator. Sigue las instrucciones oficiales del archivo README de este repositorio para la instalación y ejecución.

Antes de empezar, comprueba en qué sistema operativo estamos y si las herramientas necesarias (ej. Python, Node.js, Git, Docker) están instaladas. Instala las que falten paso a paso según este sistema.

Crea una carpeta nueva y vacía para trabajar. No toques ningún archivo fuera de esta carpeta y no borres nada. Antes de ejecutar cada comando, dime qué vas a hacer en una frase.

Dime qué debería ver en la pantalla al final de cada paso. Si ocurre un error, te pegaré el mensaje de error tal cual y lo solucionaremos juntos.

## Términos relacionados del glosario

- [Framework](https://trescout.com/es/dictionary/framework/)
- [Terminal](https://trescout.com/es/dictionary/terminal/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Está dirigido a desarrolladores que crean agentes de inteligencia artificial y desean probar el rendimiento de sus habilidades.
- **Licencia:** Apache-2.0

## Enlaces

- [Repositorio en GitHub →](https://github.com/NVIDIA/SkillEvaluator)
- [Leer en turco →](https://trescout.com/discover/skillevaluator/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-11-16: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. El texto de presentación se preparó con IA a partir de la propia documentación del repositorio y esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/skillevaluator/
