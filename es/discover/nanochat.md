# Herramienta de entrenamiento de modelos de inteligencia artificial

karpathy/nanochat es un marco de software experimental diseñado para entrenar grandes modelos de lenguaje (LLM) que puede ejecutarse en una sola unidad de procesamiento gráfico (GPU). Este proyecto, que abarca los procesos de tokenización, preentrenamiento, ajuste fino (fine-tuning), evaluación e inferencia, ofrece a los desarrolladores una estructura minimalista y modificable.

- ★ 59.998
- Python
- GitHub Trending · 2026-11-03

## Qué aporta

- Te permite entrenar un modelo de inteligencia artificial en una sola unidad de procesamiento gráfico.
- Te permite gestionar los pasos de generación de texto a través de la línea de comandos.
- Ofrece opciones de instalación flexibles para diferentes tipos de hardware.

## Instalación

**Instalando dependencias**

```
uv sync --extra gpu    # Use for CUDA (A100/H100/etc.)
uv sync --extra cpu    # (or) Use for CPU-only / MPS
source .venv/bin/activate
```

## Ejecución

**Iniciar el proceso de entrenamiento**

```
bash runs/speedrun.sh
```

**Chatear con el modelo**

```
python -m scripts.chat_cli
```

## Si no programa

Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero instalar y ejecutar la herramienta de inteligencia artificial llamada nanochat. Primero, instala las dependencias y activa el entorno virtual usando los comandos uv sync --extra gpu # Use for CUDA (A100/H100/etc.)
uv sync --extra cpu # (or) Use for CPU-only / MPS
source .venv/bin/activate. A continuación, inicia el proceso con el comando bash runs/speedrun.sh y, cuando termine, comunícate con el modelo ejecutando python -m scripts.chat_cli.

Repositorio: https://github.com/karpathy/nanochat. Sigue las instrucciones oficiales del archivo README de este repositorio para la instalación y ejecución.

Antes de empezar, comprueba en qué sistema operativo estamos y si las herramientas necesarias (ej. Python, Node.js, Git, Docker) están instaladas. Instala las que falten paso a paso según este sistema.

Crea una carpeta nueva y vacía para trabajar. No toques ningún archivo fuera de esta carpeta y no borres nada. Antes de ejecutar cada comando, dime qué vas a hacer en una frase.

Dime qué debería ver en la pantalla al final de cada paso. Si ocurre un error, te pegaré el mensaje de error tal cual y lo solucionaremos juntos.

## Términos relacionados del glosario

- [Fine-tuning](https://trescout.com/es/dictionary/fine-tuning/)
- [GPU](https://trescout.com/es/dictionary/gpu/)
- [LLM](https://trescout.com/es/dictionary/llm/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Está dirigido a desarrolladores que desean entrenar y probar grandes modelos de lenguaje desde cero.
- **Licencia:** MIT

## Enlaces

- [Repositorio en GitHub →](https://github.com/karpathy/nanochat)
- [Leer en turco →](https://trescout.com/discover/nanochat/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-11-03: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. El texto de presentación se preparó con IA a partir de la propia documentación del repositorio y esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/nanochat/
