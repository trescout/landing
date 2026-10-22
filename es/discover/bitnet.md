# Inferencia de IA eficiente en CPU

Desarrollado por Microsoft, BitNet ofrece un marco de inferencia oficial (inference framework) para modelos de lenguaje grandes (LLMs) de 1 bit. Escrita en C++, esta herramienta tiene como objetivo optimizar la ejecución de modelos de precisión de pocos bits.

- ★ 40.731
- C++
- GitHub Trending · 2026-10-12

## Qué aporta

- Ejecuta modelos de IA en procesadores informáticos estándar con alta velocidad y bajo consumo de energía.
- Permite utilizar modelos de lenguaje comprimidos de 1 bit en su dispositivo local sin pérdida de calidad.
- Gracias a la compatibilidad con el modo de diálogo, ofrece la posibilidad de chatear directamente con los modelos descargados.

## Instalación

**Descargue el código fuente**

```
git clone --recursive https://github.com/microsoft/BitNet.git
cd BitNet
```

**Prepare el entorno e instale las dependencias**

```
# (Recommended) Create a new conda environment
conda create -n bitnet-cpp python=3.10
conda activate bitnet-cpp

pip install -r requirements.txt
```

## Ejecución

**Descargue el modelo y configure el entorno**

```
# Manually download the model and run with local path
huggingface-cli download microsoft/BitNet-b1.58-2B-4T-gguf --local-dir models/BitNet-b1.58-2B-4T
python setup_env.py -md models/BitNet-b1.58-2B-4T -q i2_s
```

**Ejecute el modelo en modo chat**

```
# Run inference with the quantized model
python run_inference.py -m models/BitNet-b1.58-2B-4T/ggml-model-i2_s.gguf -p "You are a helpful assistant" -cnv
```

## Si no programa

Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero ejecutar un modelo de inteligencia artificial de 1 bit en mi ordenador utilizando la infraestructura de BitNet. En primer lugar, guíame paso a paso para clonar el proyecto con el comando 'git clone --recursive https://github.com/microsoft/BitNet.git' y entrar en su carpeta, crear un entorno de Python 3.10 con el gestor de paquetes Conda e instalar los requisitos. A continuación, explica con la sencillez necesaria para que alguien sin conocimientos de programación lo entienda cómo descargar el modelo microsoft/BitNet-b1.58-2B-4T-gguf desde la plataforma de modelos de código abierto Hugging Face, prepararlo con 'setup_env.py' y, por último, iniciar el modo chat mediante el script 'run_inference.py'.

Repositorio: https://github.com/microsoft/BitNet. Sigue las instrucciones oficiales del archivo README de este repositorio para la instalación y ejecución.

Antes de empezar, comprueba en qué sistema operativo estamos y si las herramientas necesarias (ej. Python, Node.js, Git, Docker) están instaladas. Instala las que falten paso a paso según este sistema.

Crea una carpeta nueva y vacía para trabajar. No toques ningún archivo fuera de esta carpeta y no borres nada. Antes de ejecutar cada comando, dime qué vas a hacer en una frase.

Dime qué debería ver en la pantalla al final de cada paso. Si ocurre un error, te pegaré el mensaje de error tal cual y lo solucionaremos juntos.

## Términos relacionados del glosario

- [Inference Framework](https://trescout.com/es/dictionary/inference-framework/)
- [Inference](https://trescout.com/es/dictionary/inference/)
- [Clone](https://trescout.com/es/dictionary/clone/)
- [Framework](https://trescout.com/es/dictionary/framework/)
- [Open Source](https://trescout.com/es/dictionary/open-source/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Está pensado para usuarios que desean ejecutar modelos de lenguaje rápidos y ligeros en el procesador de su propio ordenador, sin necesidad de tarjetas gráficas potentes.
- **Licencia:** MIT

## Enlaces

- [Repositorio en GitHub →](https://github.com/microsoft/BitNet)
- [Leer en turco →](https://trescout.com/discover/bitnet/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-10-12: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. El texto de presentación se preparó con IA a partir de la propia documentación del repositorio y esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/bitnet/
