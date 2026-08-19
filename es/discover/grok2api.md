# Gestión central de los servicios de Grok

Desarrollado para las plataformas Grok Build, Grok Web y Grok Console, este gateway (API gateway) reúne la gestión de múltiples cuentas en un solo centro. Escrita en lenguaje Go, la herramienta ofrece una interfaz manejable al estandarizar el acceso de los usuarios a diferentes servicios de Grok.

- ★ 7.459
- Go
- GitHub Trending · 2026-07-15

## Qué aporta
- Grok Build combina cuentas web y de consola en un solo panel
- Proporciona una interfaz API estándar compatible con OpenAI y Anthropic
- Proporciona gestión avanzada de cuentas, enrutamiento de modelos y manejo de errores.

## Instalación
**Instalación rápida con Docker**

```
git clone https://github.com/chenyme/grok2api.git
cd grok2api
cp config.example.yaml config.yaml
```

**Iniciar el servicio**

```
docker compose pull
docker compose up -d
```


## Ejecución
**gestión de servicios**

```
docker compose logs -f grok2api
docker compose restart grok2api
docker compose down
```


## Si no programa
Completé la instalación de Grok2API e inicié sesión en el panel de administración. Ahora bien, ¿cómo puedo definir mis cuentas Grok Build, Web o Console en el sistema, cómo hago coincidencias de modelos y qué pasos puedo seguir para generar la clave API para uso externo? Por favor explique este proceso paso a paso.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/grok2api/
