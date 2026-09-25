# ¿Qué es el Open Weight?

> Pesos de Modelo Accesibles Públicamente

**Categoría:** AI  
**Última actualización:** 2026-09-22

Open weight describe los modelos de inteligencia artificial cuyos pesos y parámetros de entrenamiento se distribuyen de forma descargable, permitiendo su ejecución, cuantización y ajuste fino en hardware privado.

## Definición y etimología
Frente al monopolio de las API comerciales cerradas que cobran por cada interacción, los modelos open weight entregan la matriz de parámetros matemáticos directamente al usuario. Esto garantiza la privacidad estricta y desbloquea el desarrollo desconectado de la red.

## Contexto cotidiano e uso práctico
- **Inferencia Local Desconectada:** Despliegue de modelos en ordenadores portátiles o servidores internos sin conexión a Internet.
- **Protección de Datos Sensibles:** Seguridad de que la información corporativa confidencial no transita por centros de datos externos.
- **Ahorro de Costes Operativos:** Eliminación de cuotas recurrentes de facturación por uso intensivo de API.

## Profundidad técnica y arquitectura
Fundamentos Técnicos de los Pesos Abiertos:- **Formatos de Distribución:** Almacenamiento en archivos Safetensors o contenedores GGUF compatibles con cuantización INT4/INT8.
- **Plataformas de Inferencia:** Carga optimizada mediante herramientas de alto rendimiento como vLLM, llama.cpp y Ollama.
- **Adaptadores LoRA:** Especialización funcional de bajo coste computacional mediante matrices de bajo rango (PEFT).

## Suele confundirse con
A menudo se confunde con el software de código abierto en sentido estricto. El open source exige compartir los scripts y datos de origen; el open weight proporciona la red neuronal ya entrenada para su despliegue práctico.

## Perspectivas interdisciplinares
- **Panadería:** Recibir la masa lista para hornear en casa a su gusto frente a comprar una barra industrial empaquetada.
- **Software:** Descargar un ejecutable autónomo frente a utilizar una herramienta SaaS en la nube.
- **Grabación:** Disponer de las pistas maestras de una pista de audio frente a reproducir una pista cerrada en una plataforma digital.

## Por analogía
Equivale a entregar la masa y los ingredientes preparados para que cada uno pueda hornear y sazonar el plato en su propia cocina.

## Preguntas frecuentes

**¿Qué libertades ofrece disponer de los pesos abiertos?**  
Permite alojar el modelo en infraestructuras propias, cuantizarlo para dispositivos móviles y personalizarlo con datos privados.

**¿En qué aventaja a los servicios de API comerciales?**  
Garantiza soberanía absoluta sobre los datos, coste fijo predecible e inmunidad ante cambios arbitrarios de políticas de terceros.

**¿Qué requisitos de hardware exige un modelo 8B?**  
Un equipo con 16 GB de memoria unificada o una tarjeta gráfica de 8 a 12 GB de VRAM ejecuta modelos cuantizados a 4 bits con fluidez.

**¿Se pueden comercializar productos basados en open weight?**  
La inmensa mayoría de familias modernas (Llama, Mistral, Qwen) autorizan el uso comercial explícitamente en sus licencias.

## Términos relacionados
- [Open Source AI](/es/dictionary/open-source-ai/)
- [Foundation Model](/es/dictionary/foundation-model/)
- [SLM](/es/dictionary/slm/)

---
Fuente: Diccionario Tecnológico TreScout · https://trescout.com/es/dictionary/open-weight/
