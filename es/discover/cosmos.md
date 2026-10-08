# Modelos de inteligencia artificial para sistemas físicos.

Desarrollada por NVIDIA, Cosmos es una plataforma abierta que proporciona modelos mundiales, conjuntos de datos y herramientas para sistemas físicos como robots y vehículos autónomos. Proporciona una infraestructura que facilita a los desarrolladores la creación de aplicaciones físicas de IA.

- ★ 11.343
- Jupyter Notebook
- GitHub Trending · 2026-06-05

## Actualizaciones

- **2 de agosto de 2026:** Estrellas 9,173 → 11,343, última versión Cosmos3 (1 de junio de 2026).

## Qué aporta

- Proporciona modelos mundiales, conjuntos de datos y herramientas para aplicaciones físicas de IA.
- Puede procesar y producir secuencias de texto, visuales, de audio y de acción en una arquitectura unificada.
- Proporciona capacidades de previsión, planificación y simulación para sistemas robóticos y autónomos.

## Instalación

**Instalación con vLLM-Omni**

```
uv pip install --torch-backend=cu130 \
  "vllm-omni @ git+https://github.com/vllm-project/vllm-omni.git@main"
```

## Ejecución

**Producción de vídeo**

```
curl -sS -X POST http://localhost:8000/v1/videos/sync \
  --form-string "prompt=A small warehouse robot moves a blue box across a clean floor." \
  --form-string 'extra_params={"guardrails":false,"use_resolution_template":false,"use_duration_template":false}' \
  -o cosmos3_t2v.mp4
```

## Si no programa

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero desarrollar aplicaciones de inteligencia artificial física utilizando la plataforma NVIDIA Cosmos. Explicar con detalle técnico las capacidades que ofrece la familia de modelos Cosmos 3, especialmente las diferencias en el uso de las superficies 'Reasoner' y 'Generator', y cómo se pueden configurar estos modelos en escenarios como la planificación de misiones o la simulación mundial en sistemas robóticos y autónomos. Además, resuma el proceso de trabajo con la herramienta 'uv' y la biblioteca 'vllm-omni' durante la fase de instalación, paso a paso, teniendo en cuenta los requisitos del controlador CUDA.

## Términos relacionados del glosario

- [Physical AI](https://trescout.com/es/dictionary/physical-ai/)
- [Jupyter Notebooks](https://trescout.com/es/dictionary/jupyter-notebooks/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Para desarrolladores que trabajan en IA física, sistemas robóticos y vehículos autónomos, que estén interesados ​​en modelos mundiales y procesamiento de datos multimodal.

## Enlaces

- [Repositorio en GitHub →](https://github.com/NVIDIA/cosmos)
- [Leer en turco →](https://trescout.com/discover/cosmos/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-06-05: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/cosmos/
