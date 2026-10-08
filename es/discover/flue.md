# Marco TypeScript para agentes de IA

Desarrollado por el equipo de Astro, Flue se destaca como un marco de agente sandbox basado en TypeScript. Esta estructura permite a los desarrolladores crear agentes de inteligencia artificial en entornos seguros y aislados.

- ★ 8.393
- TypeScript
- GitHub Trending · 2026-06-06

## Actualizaciones

- **29 de septiembre de 2026:** Estrellas 8,374 → 8,393, última versión @flue/cli@2.2.2 (28 de septiembre de 2026).
- **27 de septiembre de 2026:** Estrellas 8,295 → 8,374, última versión @flue/cli@2.1.1 (23 de septiembre de 2026).
- **19 de septiembre de 2026:** Estrellas 8,255 → 8,295, última versión @flue/cli@2.1.0 (18 de septiembre de 2026).
- **17 de septiembre de 2026:** Estrellas 8,244 → 8,255, última versión @flue/cli@2.0.8 (16 de septiembre de 2026).

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

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero desarrollar un agente de inteligencia artificial utilizando el marco Flue. ¿Cómo puedo definir un flujo de trabajo usando TypeScript en mi proyecto? Específicamente, ¿cómo puedo configurar el modelo con la función createAgent e interactuar con mi agente con session.prompt? Usando un ejemplo simple de "hola mundo", ¿puedes explicar paso a paso cómo puedo iniciar un agente en tiempo de ejecución y obtener resultados?

## Términos relacionados del glosario

- [Sandbox Agent Framework](https://trescout.com/es/dictionary/sandbox-agent-framework/)
- [Prompt](https://trescout.com/es/dictionary/prompt/)
- [CI/CD](https://trescout.com/es/dictionary/ci-cd/)
- [Sandbox](https://trescout.com/es/dictionary/sandbox/)
- [Runtime](https://trescout.com/es/dictionary/runtime/)
- [Framework](https://trescout.com/es/dictionary/framework/)

- **Para quién es:** Es adecuado para desarrolladores de software que quieran desarrollar sus propios agentes autónomos de inteligencia artificial con TypeScript y ejecutarlos en diferentes plataformas.
- **Licencia:** Apache-2.0

## Enlaces

- [Repositorio en GitHub →](https://github.com/withastro/flue)
- [Leer en turco →](https://trescout.com/discover/flue/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-06-06: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/flue/
