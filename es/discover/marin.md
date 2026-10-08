# Plataforma de desarrollo abierta para investigación de modelos base

Ejecuta experimentos como pasos dependientes en orden topológico y documenta código, datos, decisiones y experimentos fallidos. La primera guía oficial muestra cómo tokenizar TinyStories y entrenar un modelo de lenguaje pequeño.

- ★ 3.089
- Python
- GitHub Trending · 2026-08-25

## Actualizaciones

- **31 de agosto de 2026:** Estrellas 1,967 → 3,089.

## Instalación

**Clonar el repositorio oficial**

```
git clone https://github.com/marin-community/marin.git
```

**Crear el entorno Python**

```
uv venv --python 3.12
```

**Instalar las dependencias**

```
uv sync --all-packages
```

## Ejecución

**Ejecutar la prueba smoke en CPU**

```
wandb offline
uv run python experiments/tutorials/train_tiny_model.py --device cpu --dataset tinystories --version dev --run
```

## ¿Qué hace esta herramienta?

Ejecuta experimentos como pasos dependientes en orden topológico. El primer experimento oficial demuestra la tokenización de TinyStories y el entrenamiento de un modelo de lenguaje pequeño; el enfoque de desarrollo abierto también documenta el código, los datos, las decisiones y los experimentos fallidos.

## ¿Para quién es?

Equipos que investigan curación, transformación y filtrado de datos, tokenización, entrenamiento de modelos y evaluación.

## Qué no esperar

Tareas de desarrollo de aplicaciones simples que no forman parte de la investigación de modelos base, o quienes no quieran configurar el entorno de Python y las herramientas de desarrollo necesarias.

## Aspectos destacados

- Cobertura de investigación desde el procesamiento de datos hasta el preentrenamiento, fine-tuning y evaluación
- Flujo de experimentos que ejecuta pasos dependientes en orden topológico
- Documentación abierta que incluye experimentos fallidos y decisiones de desarrollo

## Primer flujo de uso

1. Clona el repositorio oficial y crea un entorno virtual con Python 3.12 o superior
2. Sincroniza las dependencias con uv
3. Configura la variable de entorno MARIN_PREFIX
4. Ejecuta la prueba smoke offline de TinyStories en CPU

## Inicio seguro

La prueba smoke en CPU es sólo para la verificación inicial. Las dependencias para CPU, GPU y TPU pueden requerir hardware adicional. WANDB_API_KEY y HF_TOKEN sólo son necesarios para flujos de monitorización o modelos cerrados correspondientes.

## Primer prompt

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Ejecuta como verificación inicial el flujo offline de TinyStories entrenando un modelo pequeño en CPU.

## Términos relacionados del glosario

- [CPU](https://trescout.com/es/dictionary/cpu/)
- [GPU](https://trescout.com/es/dictionary/gpu/)

## Enlaces

- [Repositorio en GitHub →](https://github.com/marin-community/marin)
- [Documentación de instalación →](https://marin.readthedocs.io/en/latest/tutorials/installation/)
- [Primer experimento →](https://marin.readthedocs.io/en/latest/tutorials/first-experiment/)
- [README oficial →](https://github.com/marin-community/marin)
- [Leer en turco →](https://trescout.com/discover/marin/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-08-25: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/marin/
