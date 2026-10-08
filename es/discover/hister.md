# Motor de búsqueda privado para páginas y archivos personales

Indexa páginas y archivos en infraestructura controlada por el usuario sin requerir un servicio en la nube ni telemetría obligatoria. Ofrece indexación de texto completo, filtros avanzados y búsqueda semántica opcional que envía textos al endpoint de embeddings seleccionado.

- ★ 5.740
- Go
- GitHub Trending · 2026-08-25

## Actualizaciones

- **27 de septiembre de 2026:** Estrellas 4,602 → 5,740, última versión v0.20.0 (24 de septiembre de 2026).
- **18 de septiembre de 2026:** Estrellas 3,574 → 4,602, última versión v0.19.0 (3 de septiembre de 2026).
- **4 de septiembre de 2026:** Estrellas 3,100 → 3,574, última versión v0.19.0 (3 de septiembre de 2026).
- **27 de agosto de 2026:** Estrellas 2,620 → 3,100, última versión v0.18.0 (23 de agosto de 2026).

## Instalación

**Hacer el binario ejecutable**

```
chmod +x hister
```

## Ejecución

**Iniciar el servidor Hister**

```
./hister listen
```

**Acceder a la interfaz local**

```
http://127.0.0.1:4433
```

## ¿Qué hace esta herramienta?

Hister puede ejecutarse localmente o en la infraestructura que controles; no requiere un servicio en la nube ni telemetría obligatoria. Indexa páginas mediante extensiones para Chrome y Firefox, y ofrece opciones de rastreo de sitios y de importación del historial del navegador. Si se activa la búsqueda semántica, el texto del documento se envía al endpoint de embeddings seleccionado.

## ¿Para quién es?

Quienes quieran consultar páginas web y archivos personales en una infraestructura de búsqueda que controlen.

## Qué no esperar

Casos que exijan un servicio en la nube obligatorio o telemetría, o flujos de indexación del navegador que no permitan enviar contenido al servidor Hister configurado.

## Aspectos destacados

- Funciona localmente o en infraestructura controlada sin telemetría ni servicios en la nube obligatorios
- Consultas con texto completo, filtros por campo, frases, comodines, negaciones y prioridades
- Clientes web, terminal, TUI, CLI y MCP, con búsqueda semántica opcional

## Primer flujo de uso

1. Descarga el binario adecuado para tu plataforma y hazlo ejecutable en Linux o macOS
2. Inicia el servidor Hister en modo escucha local
3. Abre la interfaz web local
4. Instala la extensión de Chrome o Firefox y selecciona las páginas que quieres indexar

## Inicio seguro

La extensión del navegador envía el contenido de las páginas indexadas al servidor Hister configurado, aparte de descargar favicons. La búsqueda semántica opcional envía el texto del documento al endpoint de embeddings seleccionado.

## Primer prompt

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Abre la interfaz local y, usando la extensión del navegador, indexa las páginas seleccionadas y valida la búsqueda usando filtros de consulta.

## Términos relacionados del glosario

- [TUI](https://trescout.com/es/dictionary/tui/)
- [Binary](https://trescout.com/es/dictionary/binary/)
- [MCP](https://trescout.com/es/dictionary/mcp/)
- [Terminal](https://trescout.com/es/dictionary/terminal/)
- [CLI](https://trescout.com/es/dictionary/cli/)

## Enlaces

- [Repositorio en GitHub →](https://github.com/asciimoo/hister)
- [Inicio rápido →](https://hister.org/docs/quickstart)
- [README de privacidad y uso →](https://github.com/asciimoo/hister)
- [Flujo de uso →](https://hister.org/posts/how-i-use-hister)
- [Leer en turco →](https://trescout.com/discover/hister/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-08-25: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/hister/
