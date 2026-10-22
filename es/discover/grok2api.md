# Gestión central de los servicios de Grok

Desarrollado para las plataformas Grok Build, Grok Web y Grok Console, este gateway (API gateway) reúne la gestión de múltiples cuentas en un solo centro. Escrita en lenguaje Go, la herramienta ofrece una interfaz manejable al estandarizar el acceso de los usuarios a diferentes servicios de Grok.

- ★ 7.817
- Go
- GitHub Trending · 2026-07-15

## Actualizaciones

- **18 de octubre de 2026:** Estrellas 7,669 → 7,817, última versión v3.1.7 (18 de octubre de 2026).
- **16 de septiembre de 2026:** Estrellas 7,543 → 7,669, última versión v3.1.6 (16 de septiembre de 2026).
- **27 de agosto de 2026:** Estrellas 7,459 → 7,543, última versión v3.1.5 (25 de agosto de 2026).
- **19 de agosto de 2026:** Estrellas 7,447 → 7,459, última versión v3.1.4 (19 de agosto de 2026).

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

Pegue esto en su agente (Claude Code · Codex · Antigravity)

Completé la instalación de Grok2API e inicié sesión en el panel de administración. Ahora bien, ¿cómo puedo definir mis cuentas Grok Build, Web o Console en el sistema, cómo hago coincidencias de modelos y qué pasos puedo seguir para generar la clave API para uso externo? Por favor explique este proceso paso a paso.

Repositorio: https://github.com/chenyme/grok2api. Sigue las instrucciones oficiales del archivo README de este repositorio para la instalación y ejecución.

Antes de empezar, comprueba en qué sistema operativo estamos y si las herramientas necesarias (ej. Python, Node.js, Git, Docker) están instaladas. Instala las que falten paso a paso según este sistema.

Crea una carpeta nueva y vacía para trabajar. No toques ningún archivo fuera de esta carpeta y no borres nada. Antes de ejecutar cada comando, dime qué vas a hacer en una frase.

Si se necesita una clave API, no me pidas que la escriba en el chat. Muéstrame cómo añadirla al archivo .env y asegúrate de que este archivo no se suba a Git.

Dime qué debería ver en la pantalla al final de cada paso. Si ocurre un error, te pegaré el mensaje de error tal cual y lo solucionaremos juntos.

## Términos relacionados del glosario

- [API Gateway](https://trescout.com/es/dictionary/api-gateway/)
- [Gateway](https://trescout.com/es/dictionary/gateway/)
- [API](https://trescout.com/es/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Es para desarrolladores que desean administrar varias cuentas de Grok y pretenden utilizar estos servicios en sus aplicaciones a través de una API estándar.
- **Licencia:** MIT

## Enlaces

- [Repositorio en GitHub →](https://github.com/chenyme/grok2api)
- [Leer en turco →](https://trescout.com/discover/grok2api/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-07-15: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. El texto de presentación se preparó con IA a partir de la propia documentación del repositorio y esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/grok2api/
