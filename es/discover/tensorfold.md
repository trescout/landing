# Motor de inteligencia artificial local TensorFold

ashhart/TensorFold ofrece un motor de inferencia compatible con Metal, CUDA y Vulkan para modelos lingüísticos grandes (LLM). Desarrollada con el lenguaje Zig, esta herramienta permite ejecutar modelos directamente en Apple Silicon y unidades de procesamiento gráfico de NVIDIA sin necesidad de instalar Python o MLX.

- ★ 1.998
- Zig
- GitHub Trending · 2026-11-13

## Actualizaciones

- **13 de noviembre de 2026:** Estrellas 1,996 → 1,998, última versión v1.2.7 (11 de noviembre de 2026).

## Qué aporta

- Ejecuta modelos lingüísticos grandes directamente en Apple Silicon y tarjetas gráficas NVIDIA.
- Ofrece servicio a través de un archivo binario sin necesidad de instalar Python o MLX.
- Permite seleccionar modelos y chatear mediante una aplicación web local.

## Instalación

**Instalación en Mac**

```
brew install ashhart/tensorfold/tensorfold
tensorfold pull mlx-community/Qwen3.5-2B-MLX-4bit@93760be4f1f69842a46bc13dbdc0f19e291392a3
tensorfold serve mlx-community/Qwen3.5-2B-MLX-4bit --name local-model --context 8192 --no-thinking
```

## Ejecución

**Enviar solicitud**

```
curl -fsS http://127.0.0.1:8080/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{"model":"local-model","messages":[{"role":"user","content":"Say hello in one sentence."}],"max_tokens":128,"temperature":0}'
```

## Si no programa

Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero instalar la herramienta TensorFold en mi ordenador Mac con chip Apple Silicon, descargar el modelo Qwen3.5-2B e iniciar el servidor. Para ello, debes ejecutar los siguientes comandos en orden:

brew install ashhart/tensorfold/tensorfold
tensorfold pull mlx-community/Qwen3.5-2B-MLX-4bit@93760be4f1f69842a46bc13dbdc0f19e291392a3
tensorfold serve mlx-community/Qwen3.5-2B-MLX-4bit --name local-model --context 8192 --no-thinking

A continuación, para verificar que el servidor está funcionando, puedes enviar una solicitud con el siguiente comando:

curl -fsS http://127.0.0.1:8080/v1/chat/completions \
-H 'Content-Type: application/json' \
-d '{"model":"local-model","messages":[{"role":"user","content":"Say hello in one sentence."}],"max_tokens":128,"temperature":0}'

Repositorio: https://github.com/ashhart/TensorFold. Sigue las instrucciones oficiales del archivo README de este repositorio para la instalación y ejecución.

Antes de empezar, comprueba en qué sistema operativo estamos y si las herramientas necesarias (ej. Python, Node.js, Git, Docker) están instaladas. Instala las que falten paso a paso según este sistema.

Crea una carpeta nueva y vacía para trabajar. No toques ningún archivo fuera de esta carpeta y no borres nada. Antes de ejecutar cada comando, dime qué vas a hacer en una frase.

Dime qué debería ver en la pantalla al final de cada paso. Si ocurre un error, te pegaré el mensaje de error tal cual y lo solucionaremos juntos.

## Términos relacionados del glosario

- [Temperature](https://trescout.com/es/dictionary/temperature/)
- [Application](https://trescout.com/es/dictionary/application/)
- [Inference Engine](https://trescout.com/es/dictionary/inference-engine/)
- [Apple Silicon](https://trescout.com/es/dictionary/apple-silicon/)
- [Inference](https://trescout.com/es/dictionary/inference/)
- [LLM](https://trescout.com/es/dictionary/llm/)

- **Para quién es:** Está dirigido a desarrolladores que desean ejecutar modelos lingüísticos grandes en Apple Silicon o tarjetas gráficas NVIDIA sin instalar Python.
- **Licencia:** Apache-2.0

## Enlaces

- [Repositorio en GitHub →](https://github.com/ashhart/TensorFold)
- [Leer en turco →](https://trescout.com/discover/tensorfold/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-11-13: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. El texto de presentación se preparó con IA a partir de la propia documentación del repositorio y esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/tensorfold/
