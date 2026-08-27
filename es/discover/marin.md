# Plataforma de desarrollo abierta para investigación de modelos base

Ejecuta experimentos como pasos dependientes en orden topológico y documenta código, datos, decisiones y experimentos fallidos. La primera guía oficial muestra cómo tokenizar TinyStories y entrenar un modelo de lenguaje pequeño.

- ★ 1.967
- Python
- GitHub Trending · 2026-08-25

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
- Clona el repositorio oficial y crea un entorno virtual con Python 3.12 o superior
- Sincroniza las dependencias con uv
- Configura la variable de entorno MARIN_PREFIX
- Ejecuta la prueba smoke offline de TinyStories en CPU

## Inicio seguro

## Primer prompt
Ejecuta como verificación inicial el flujo offline de TinyStories entrenando un modelo pequeño en CPU.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Documentación de instalación →
- Primer experimento →
- README oficial →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/marin/
