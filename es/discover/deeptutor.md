# Formación personalizada apoyada en inteligencia artificial

DeepTutor es un sistema de tutoría privada basado en el aprendizaje permanente que ofrece procesos educativos personalizados utilizando los datos de los estudiantes. El proyecto tiene como objetivo optimizar la experiencia de aprendizaje con métodos de tutoría individualizados respaldados por inteligencia artificial.

- ★ 33.415
- Python
- GitHub Trending · 2026-07-16

## Actualizar
- 10 de agosto de 2026: Star 32 944 → 33 415, última versión v1.5.11 (9 de agosto de 2026).
- 7 de agosto de 2026: Star 32,640 → 32,944, última versión v1.5.10 (7 de agosto de 2026).
- 6 de agosto de 2026: Star 31,925 → 32,640, última versión v1.5.9 (4 de agosto de 2026).
- 2 de agosto de 2026: Star 26,461 → 31,925, última versión v1.5.8 (2 de agosto de 2026).

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
¿Cómo puedo personalizar mi proceso de aprendizaje utilizando el sistema DeepTutor? Explique los pasos básicos que debo seguir para crear mis propios socios de IA y optimizar mi experiencia de aprendizaje permanente integrando mis materiales de capacitación personalizados en este sistema.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/deeptutor/
