# Configurar salidas de IA

La biblioteca Outlines permite que las respuestas de modelos de lenguaje grandes se presenten como resultados estructurados de acuerdo con esquemas predefinidos. Con esta herramienta basada en Python, los desarrolladores protegen la integridad de los datos restringiendo los resultados del modelo con expresiones regulares o reglas gramaticales libres de contexto.

- ★ 15.525
- Python
- GitHub Trending · 2026-07-22

## Qué aporta
- Restringe los resultados del modelo según esquemas predefinidos.
- Totalmente compatible con tipos de datos JSON o Python
- Elimina la necesidad de depurar resultados erróneos

## Instalación
**Instalar la biblioteca**

```
pip install outlines
```


## Ejecución
**Conecta el modelo**

```
import outlines
from transformers import AutoTokenizer, AutoModelForCausalLM


MODEL_NAME = "microsoft/Phi-3-mini-4k-instruct"
model = outlines.from_transformers(
    AutoModelForCausalLM.from_pretrained(MODEL_NAME, device_map="auto"),
    AutoTokenizer.from_pretrained(MODEL_NAME)
)
```


## Si no programa
Quiero restringir la respuesta de un modelo de IA a una estructura de datos de Pydantic o un tipo de Python específico (por ejemplo, int o Literal) usando la biblioteca Outlines. ¿Cómo puedo utilizar la función modelo (solicitud, tipo_salida) después de definir el objeto del modelo para garantizar que la salida del modelo siempre se ajuste al esquema que deseo? Explique con un ejemplo cómo definir el modelo Pydantic para objetos complejos y aplicar esta estructura a la salida del modelo.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/outlines/
