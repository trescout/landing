# Kit de IA autónomo para antigravedad

Ag-kit es una biblioteca de desarrollo que proporciona las herramientas y estructuras necesarias para crear agentes autónomos de inteligencia artificial (agentes de IA) en proyectos basados en TypeScript. Permite a los desarrolladores diseñar rápidamente sistemas de agentes que puedan gestionar flujos de trabajo complejos.

- ★ 8.084
- TypeScript
- GitHub Trending · 2026-07-28

## Actualizar
- 2 de agosto de 2026: Star 8.020 → 8.084, última versión v2026.7.27 (26 de julio de 2026).

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
En este proyecto, configuré un espacio de trabajo Antigravity y activé las herramientas del AG Kit. Quiero administrar mis tareas usando las reglas, roles de agentes expertos y flujos de trabajo definidos en la carpeta .agents/ en el directorio del proyecto. Asegúrese de que el gancho de seguridad esté activo y planifique flujos de trabajo complejos con los comandos /coordinate u /orchetrate.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/ag-kit/
