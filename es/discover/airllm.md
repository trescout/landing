# Ejecute modelos de IA gigantes con 4 GB de VRAM

AirLLM permite ejecutar modelos de lenguajes grandes con 70 mil millones de parámetros en unidades de procesamiento de gráficos con solo 4 GB de memoria de video (VRAM). Esta biblioteca utiliza técnicas de optimización de memoria para permitir el uso de modelos de alta capacidad con bajos requisitos de hardware.

- ★ 30.796
- Jupyter Notebook
- GitHub Trending · 2026-06-04

## Qué aporta
- Posibilidad de ejecutar modelos con 70B de parámetros con 4GB de VRAM.
- Posibilidad de utilizar modelos 405B Llama3.1 con 8GB VRAM.
- Aumento de velocidad hasta 3 veces con compresión basada en bloques.

## Instalación
**Instalación del paquete**

```
pip install airllm
```


## Ejecución
**Cargar y ejecutar el modelo.**

```
from airllm import AutoModel

MAX_LENGTH = 128
# could use hugging face model repo id:
model = AutoModel.from_pretrained("garage-bAInd/Platypus2-70B-instruct")

# or use model's local path...
#model = AutoModel.from_pretrained("/home/ubuntu/.cache/huggingface/hub/models--garage-bAInd--Platypus2-70B-instruct/snapshots/b585e74bcaae02e52665d9ac6d23f4d0dbc81a0f")

input_text = [
        'What is the capital of United States?',
        #'I like',
    ]

input_tokens = model.tokenizer(input_text,
    return_tensors="pt", 
    return_attention_mask=False, 
    truncation=True, 
    max_length=MAX_LENGTH, 
    padding=False)
           
generation_output = model.generate(
    input_tokens['input_ids'].cuda(), 
    max_new_tokens=20,
    use_cache=True,
    return_dict_in_generate=True)

output = model.tokenizer.decode(generation_output.sequences[0])

print(output)
```


## Si no programa
Quiero ejecutar un modelo con parámetros de 70B usando la biblioteca AirLLM en mi tarjeta gráfica con baja capacidad de VRAM. Utilicé el comando pip install airllm para la instalación. ¿Cómo puedo crear la estructura de código Python necesaria para cargar mi modelo y generarlo con una simple entrada de texto, usando la clase AutoModel? Sé que necesito asegurarme de tener suficiente espacio en disco durante el proceso. ¿Puedes explicarme los pasos básicos que debo seguir para iniciar el proceso?

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/airllm/
