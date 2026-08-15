# Modelos de inteligencia artificial para sistemas físicos.

Desarrollada por NVIDIA, Cosmos es una plataforma abierta que proporciona modelos mundiales, conjuntos de datos y herramientas para sistemas físicos como robots y vehículos autónomos. Proporciona una infraestructura que facilita a los desarrolladores la creación de aplicaciones físicas de IA.

- ★ 11.343
- Jupyter Notebook
- GitHub Trending · 2026-06-05

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
Quiero desarrollar aplicaciones de inteligencia artificial física utilizando la plataforma NVIDIA Cosmos. Explicar con detalle técnico las capacidades que ofrece la familia de modelos Cosmos 3, especialmente las diferencias en el uso de las superficies 'Reasoner' y 'Generator', y cómo se pueden configurar estos modelos en escenarios como la planificación de misiones o la simulación mundial en sistemas robóticos y autónomos. Además, resuma el proceso de trabajo con la herramienta 'uv' y la biblioteca 'vllm-omni' durante la fase de instalación, paso a paso, teniendo en cuenta los requisitos del controlador CUDA.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/cosmos/
