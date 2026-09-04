# Servidor de inferencia para agentes de inteligencia artificial

SIE, desarrollado por Superlinked, es un servidor de inferencia de código abierto y un clúster de producción utilizado para ejecutar los modelos que necesitan los agentes de inteligencia artificial. Esta estructura basada en Python tiene como objetivo gestionar despliegues de modelos complejos y ofrecer una infraestructura escalable.

- ★ 3.198
- Python
- GitHub Trending · 2026-09-03

## Qué aporta
- Gestiona modelos de código abierto a través de un único clúster
- Proporciona una fácil integración gracias a su interfaz compatible con OpenAI
- Admite tareas como búsqueda, extracción de datos y generación de texto

## Instalación
**Instalación del SDK**

```
pip install sie-sdk                # Python
npm install @superlinked/sie-sdk   # TypeScript (pnpm and yarn work too)
```


## Ejecución
**Primer intento de despliegue**

```
curl http://localhost:8080/v1/embeddings \
  -H 'Content-Type: application/json' \
  -d '{"model": "sentence-transformers/all-MiniLM-L6-v2", "input": "Hello world"}'
# {"object": "list", "data": [{"object": "embedding", "embedding": [-0.0344, 0.0310, ...
```


## Si no programa
Quiero ejecutar un modelo para un agente de IA a través del servidor SIE. ¿Cómo puedo gestionar las tareas que necesita mi agente, como la búsqueda, la extracción de datos y la generación de texto, a través de una única API? ¿Cómo puedo configurar los procesos de creación de embeddings y generación de texto utilizando los puntos finales compatibles con OpenAI que ofrece SIE?

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/sie/
