# Motor de búsqueda privado para páginas y archivos personales

Indexa páginas y archivos en infraestructura controlada por el usuario sin requerir un servicio en la nube ni telemetría obligatoria. Ofrece indexación de texto completo, filtros avanzados y búsqueda semántica opcional que envía textos al endpoint de embeddings seleccionado.

- ★ 3.100
- Go
- GitHub Trending · 2026-08-25

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
- Descarga el binario adecuado para tu plataforma y hazlo ejecutable en Linux o macOS
- Inicia el servidor Hister en modo escucha local
- Abre la interfaz web local
- Instala la extensión de Chrome o Firefox y selecciona las páginas que quieres indexar

## Inicio seguro

## Primer prompt
Abre la interfaz local y, usando la extensión del navegador, indexa las páginas seleccionadas y valida la búsqueda usando filtros de consulta.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Inicio rápido →
- README de privacidad y uso →
- Flujo de uso →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/hister/
