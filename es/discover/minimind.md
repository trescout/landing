# Modelo de lenguaje de 64 millones de parámetros entrenado desde cero en dos horas

MiniMind ofrece etapas de tokenización, entrenamiento previo, ajuste fino supervisado (SFT), LoRA y DPO con códigos PyTorch desnudos para desarrolladores que desean comprender los principios de funcionamiento de modelos de lenguaje grandes (LLM).

- ★ 62.670
- Python
- GitHub Trending · 2026-08-31

## Qué aporta
- Capacitación de 2 horas sobre hardware de consumo: Arquitectura compacta que se puede entrenar desde cero en aproximadamente 2 horas en una sola tarjeta gráfica NVIDIA RTX 3090/4090.
- Ciclo de vida completo de la capacitación de LLM: tokenización de BPE, capacitación previa, ajuste supervisado (SFT), adaptación de LoRA y proceso de alineación de DPO.
- Base de código minimalista y legible: bloques Transformer transparentes escritos en PyTorch puro, sin abstracciones complejas de terceros.
- Compatibilidad con MoE (Expert Mix): capacidad de probar y ejecutar arquitectura MoE 8x desde cero, así como modelos densos.
- Excelente recurso educativo y pedagógico: la guía ideal para investigadores que desean obtener información empírica sobre el funcionamiento interno de grandes modelos lingüísticos.

## Instalación
**Clonando el repositorio e instalando dependencias**

```
git clone https://github.com/jingyaogong/minimind.git
cd minimind
pip install -r requirements.txt
```


## Ejecución
**Inicie el entrenamiento previo y pruebe la salida del modelo**

```
python 1-pretrain.py
# Eğitilen modelle test çıkarımı:
python 5-eval.py
```


## Arquitectura técnica y principio de funcionamiento
- Activaciones RoPE y SwiGLU: estándares arquitectónicos modernos con incrustaciones de posición giratoria y funciones de activación SwiGLU.
- Flujo de gradiente estable con RMSNorm: uso de una normalización de capas RMSNorm más rápida y estable en lugar de LayerNorm tradicional.
- Integración de Flash Attention: optimización de Flash Attention v2 para calcular rápidamente grandes matrices de atención en la memoria de la GPU.

## Etapas de formación: Pre-formación, PFT y DPO
- Etapa 1: Preentrenamiento (1-pretrain.py): aprende gramática y conocimiento general del mundo con la lógica de predecir el siguiente token en textos sin formato.
- Fase 2: Ajuste fino supervisado (2-sft.py): transforma el modelo en un asistente que obedece las órdenes del usuario con conjuntos de datos de preguntas, respuestas e instrucciones.
- Etapa 3: Alineación de DPO (4-dpo.py): optimiza directamente el modelo según las preferencias del usuario a través de pares de respuestas buenas y malas.

## Si no programa
Quiero entrenar un modelo de lenguaje de 64M de parámetros desde cero con PyTorch usando el repositorio MiniMind. ¿Puedes explicar paso a paso cómo preparar el tokenizador basado en mi propio conjunto de datos de texto turco, ejecutar el script 1-pretrain.py y luego ajustarlo con LoRA?

## Preguntas frecuentes
- ¿Cuánta VRAM se requiere para entrenar MiniMind? El modelo de parámetros de 64M se puede entrenar cómodamente con 6GB a 12GB de VRAM dependiendo de la configuración del tamaño del lote; Incluso RTX 3060 o RTX 4060 es suficiente.
- ¿Funciona en Apple Silicon (serie Mac M)? Sí. El entrenamiento y la inferencia también se pueden realizar en computadoras Mac con aceleración PyTorch MPS (Metal Performance Shaders).
- ¿Son suficientes los resultados del modelo para la conversación diaria? El 64M es un modelo pequeño; Está optimizado para mostrar la estructura del lenguaje, la capacidad de responder preguntas básicas y texto completo en lugar de razonamiento lógico complejo.
- ¿Qué conjuntos de datos vienen ya preparados? El repositorio ofrece comandos para descargar automáticamente conjuntos de datos abiertos filtrados para preentrenamiento en chino e inglés y SFT.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/minimind/
