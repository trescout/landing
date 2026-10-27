# Motor de búsqueda de empleo de código abierto

Desarrollado en el lenguaje Go, freehire es un motor de búsqueda de código abierto (con código fuente abierto al acceso y desarrollo de todos) diseñado para personas que buscan empleo. Ofrece una plataforma que permite a los usuarios examinar y encontrar ofertas de trabajo.

- ★ 3.186
- Go
- GitHub Trending · 2026-10-22

## Actualizaciones

- **27 de octubre de 2026:** Estrellas 3,063 → 3,186, última versión backend-v0.1.1 (26 de octubre de 2026).
- **26 de octubre de 2026:** Estrellas 2,880 → 3,063, última versión backend-v0.1.0 (25 de octubre de 2026).
- **23 de octubre de 2026:** Estrellas 2,661 → 2,880, última versión extension-v0.1.12 (23 de octubre de 2026).
- **22 de octubre de 2026:** Estrellas 2,643 → 2,661, última versión extension-v0.1.10 (21 de octubre de 2026).

## Qué aporta

- Acceda directamente y al día a las ofertas de empleo tecnológico recopiladas directamente de las páginas de empleo de las empresas, sin intermediarios.
- Elimine las publicaciones duplicadas de diferentes sitios web de empleo y examínelas en una lista limpia y filtrable.
- Gestione su proceso de búsqueda de empleo con un análisis de compatibilidad de currículum y un panel de seguimiento de solicitudes impulsado por inteligencia artificial.

## Instalación

**Instalación de todo el sistema en un entorno de contenedores y**

```
make up        # build + start the whole stack in Docker:
               # api, web, postgres, meilisearch, redis, s3
curl localhost:8080/health
curl localhost:8080/api/v1/jobs
```

## Ejecución

**Si el puerto predeterminado está ocupado, con un puerto diferente**

```
HIRE_HOST_PORT=8090 make up
```

## Si no programa

Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero ejecutar la aplicación de la plataforma de búsqueda de empleo de código abierto Freehire en mi propio sistema. Utiliza el software de gestión de contenedores Docker y la herramienta de automatización Make para iniciar todos los servicios y verificar el estado de la API ejecutando los siguientes comandos en orden: make up # build + start the whole stack in Docker:
# api, web, postgres, meilisearch, redis, s3
curl localhost:8080/health
curl localhost:8080/api/v1/jobs

Repositorio: https://github.com/strelov1/freehire. Sigue las instrucciones oficiales del archivo README de este repositorio para la instalación y ejecución.

Antes de empezar, comprueba en qué sistema operativo estamos y si las herramientas necesarias (ej. Python, Node.js, Git, Docker) están instaladas. Instala las que falten paso a paso según este sistema.

Crea una carpeta nueva y vacía para trabajar. No toques ningún archivo fuera de esta carpeta y no borres nada. Antes de ejecutar cada comando, dime qué vas a hacer en una frase.

Dime qué debería ver en la pantalla al final de cada paso. Si ocurre un error, te pegaré el mensaje de error tal cual y lo solucionaremos juntos.

## Términos relacionados del glosario

- [Localhost](https://trescout.com/es/dictionary/localhost/)
- [API](https://trescout.com/es/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Está dirigido a quienes desean seguir los anuncios de software y tecnología directamente en las páginas de carreras de las empresas sin intermediarios, o ejecutar su propio motor de búsqueda de empleo independiente.
- **Licencia:** MIT

## Enlaces

- [Repositorio en GitHub →](https://github.com/strelov1/freehire)
- [Leer en turco →](https://trescout.com/discover/freehire/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-10-22: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. El texto de presentación se preparó con IA a partir de la propia documentación del repositorio y esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/freehire/
