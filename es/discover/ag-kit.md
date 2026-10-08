# Kit de IA autónomo para antigravedad

Ag-kit es una biblioteca de desarrollo que proporciona las herramientas y estructuras necesarias para crear agentes autónomos de inteligencia artificial (agentes de IA) en proyectos basados en TypeScript. Permite a los desarrolladores diseñar rápidamente sistemas de agentes que puedan gestionar flujos de trabajo complejos.

- ★ 8.159
- TypeScript
- GitHub Trending · 2026-07-28

## Actualizaciones

- **31 de agosto de 2026:** Estrellas 8,084 → 8,159, última versión v2026.8.31 (31 de agosto de 2026).
- **2 de agosto de 2026:** Estrellas 8,020 → 8,084, última versión v2026.7.27 (26 de julio de 2026).

## Qué aporta

- 20 roles diferentes de expertos en IA
- Control seguro de ejecución de comandos
- Gestión de flujo de trabajo y memoria persistente

## Instalación

**Instalación en el proyecto.**

```
npx @vudovn/ag-kit init
```

**Instalación global**

```
npm install -g @vudovn/ag-kit
ag-kit init
```

## Ejecución

**Verificación del espacio de trabajo**

```
npm run check:agents
npm run check:antigravity
npm run test:antigravity
```

**Probando el gancho de seguridad**

```
printf '%s' '{"tool_args":{"CommandLine":"rm -rf /"}}' \
  | node .agents/hooks/validate-tool-call.mjs
```

## Si no programa

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

En este proyecto, configuré un espacio de trabajo Antigravity y activé las herramientas del AG Kit. Quiero administrar mis tareas usando las reglas, roles de agentes expertos y flujos de trabajo definidos en la carpeta .agents/ en el directorio del proyecto. Asegúrese de que el gancho de seguridad esté activo y planifique flujos de trabajo complejos con los comandos /coordinate u /orchetrate.

## Términos relacionados del glosario

- [Agentic](https://trescout.com/es/dictionary/agentic/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Es para desarrolladores de software que utilizan el espacio de trabajo Antigravity en sus proyectos basados ​​en TypeScript y desean desarrollar sistemas de agentes autónomos.
- **Licencia:** MIT

## Enlaces

- [Repositorio en GitHub →](https://github.com/vudovn/ag-kit)
- [Leer en turco →](https://trescout.com/discover/ag-kit/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-07-28: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/ag-kit/
