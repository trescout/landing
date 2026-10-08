# Anima diferentes esqueletos de personajes con un solo modelo

UniMate es una tecnología de animación que permite animar diferentes estructuras esqueléticas a través de un único modelo. Presentado en SIGGRAPH Asia 2026, este trabajo tiene como objetivo estandarizar los procesos de animación de personajes.

- ★ 1.166
- Python
- GitHub Trending · 2026-10-02

## Qué aporta

- Anima diferentes estructuras esqueléticas, como humanos, animales y objetos, con un solo modelo de inteligencia artificial.
- Ofrece un soporte de animación integral con el conjunto de datos a gran escala UniML3D.
- Acelera el flujo de trabajo estandarizando los procesos de animación de personajes.

## Instalación

**Preparación del entorno**

```
conda create -n unimate python=3.10 -y
conda activate unimate
pip install "setuptools<81"
pip install -r requirements.txt --no-build-isolation
```

## Ejecución

**Generación de animación de muestra**

```
python -m unimate.inference.sample \
    --exp_dir outputs/uniml3d_60frames_graph_adaln \
    --test_cases_json test_cases.json \
    --num_repetitions 3
```

## Si no programa

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

¿Cómo puedo animar mis modelos de personajes con diferentes estructuras esqueléticas en un formato estándar utilizando el proyecto UniMate? Explica paso a paso el proceso de creación de animaciones aprovechando el conjunto de datos UniML3D y los puntos de control preentrenados que ofrece el proyecto.

## Términos relacionados del glosario

- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Dirigido a artistas 3D y desarrolladores que buscan automatizar los procesos de animación de personajes y realizar transiciones entre diferentes estructuras esqueléticas.
- **Licencia:** MIT

## Enlaces

- [Repositorio en GitHub →](https://github.com/Friedrich-M/UniMate)
- [Leer en turco →](https://trescout.com/discover/unimate/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-10-02: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/unimate/
