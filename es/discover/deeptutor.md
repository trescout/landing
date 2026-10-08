# Formación personalizada apoyada en inteligencia artificial

DeepTutor es un sistema de tutoría privada basado en el aprendizaje permanente que ofrece procesos educativos personalizados utilizando los datos de los estudiantes. El proyecto tiene como objetivo optimizar la experiencia de aprendizaje con métodos de tutoría individualizados respaldados por inteligencia artificial.

- ★ 40.928
- Python
- GitHub Trending · 2026-07-16

## Actualizaciones

- **8 de octubre de 2026:** Estrellas 40,808 → 40,928, última versión v1.6.14 (8 de octubre de 2026).
- **5 de octubre de 2026:** Estrellas 40,358 → 40,808, última versión v1.6.13 (4 de octubre de 2026).
- **27 de septiembre de 2026:** Estrellas 40,334 → 40,358, última versión v1.6.12 (27 de septiembre de 2026).
- **27 de septiembre de 2026:** Estrellas 39,561 → 40,334, última versión v1.6.11 (24 de septiembre de 2026).

## Qué aporta

- Sistema de lecciones privadas enfocadas al aprendizaje permanente
- Interacción con agentes de inteligencia artificial personalizados
- Base de conocimientos avanzada y soporte RAG

## Instalación

**Instalación rápida**

```
mkdir -p my-deeptutor && cd my-deeptutor
pip install -U deeptutor
deeptutor init     # prompts for ports + LLM provider + optional embedding
deeptutor start    # starts backend + frontend; keep the terminal open
```

**Ejecutando con Docker**

```
docker run --rm --name deeptutor \
  -p 127.0.0.1:3782:3782 \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

## Ejecución

**Inicialización del sistema**

```
deeptutor start    # starts backend + frontend; keep the terminal open
```

## Si no programa

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

¿Cómo puedo personalizar mi proceso de aprendizaje utilizando el sistema DeepTutor? Explique los pasos básicos que debo seguir para crear mis propios socios de IA y optimizar mi experiencia de aprendizaje permanente integrando mis materiales de capacitación personalizados en este sistema.

## Términos relacionados del glosario

- [Lifelong Learning](https://trescout.com/es/dictionary/lifelong-learning/)
- [Personalized Tutoring](https://trescout.com/es/dictionary/personalized-tutoring/)
- [Tutoring](https://trescout.com/es/dictionary/tutoring/)
- [RAG](https://trescout.com/es/dictionary/rag/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Es adecuado para estudiantes e instructores que desean crear su propio asistente educativo privado y establecer un entorno de aprendizaje personalizado.
- **Licencia:** Apache-2.0

## Enlaces

- [Repositorio en GitHub →](https://github.com/HKUDS/DeepTutor)
- [Leer en turco →](https://trescout.com/discover/deeptutor/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-07-16: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/deeptutor/
