# Marco TypeScript para agentes de IA

Desarrollado por el equipo de Astro, Flue se destaca como un marco de agente sandbox basado en TypeScript. Esta estructura permite a los desarrolladores crear agentes de inteligencia artificial en entornos seguros y aislados.

- ★ 7.625
- TypeScript
- GitHub Trending · 2026-06-06

## Qué aporta
- Creación de agentes programables y headless basados ​​en TypeScript.
- Entorno de trabajo rápido y escalable con sandbox virtual.
- Implementación versátil en procesos de Node.js, Cloudflare y CI/CD.

## Instalación
**Servidor de desarrollo Node.js**

```
flue dev --target node
```

**compilacion**

```
flue build --target node          # Node.js server (single bundled .mjs)
flue build --target cloudflare    # Cloudflare Workers + Durable Objects
```


## Ejecución
**Ejecución del flujo de trabajo Hola mundo**

```
flue run hello --target node \
  --payload '{"text": "Hello world", "language": "French"}'
```


## Si no programa
Quiero desarrollar un agente de inteligencia artificial utilizando el marco Flue. ¿Cómo puedo definir un flujo de trabajo usando TypeScript en mi proyecto? Específicamente, ¿cómo puedo configurar el modelo con la función createAgent e interactuar con mi agente con session.prompt? Usando un ejemplo simple de "hola mundo", ¿puedes explicar paso a paso cómo puedo iniciar un agente en tiempo de ejecución y obtener resultados?

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/flue/
