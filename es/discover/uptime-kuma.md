# Herramienta de monitoreo del estado de servidores y servicios

Uptime Kuma es una herramienta de monitoreo autohospedada con una interfaz visual. Esta aplicación basada en JavaScript, que permite realizar un seguimiento del estado operativo de sitios web y servicios, ofrece una experiencia fácil de usar.

- ★ 93.936
- JavaScript
- GitHub Trending · 2026-11-14

## Actualizaciones

- **14 de noviembre de 2026:** Estrellas 93,934 → 93,936, última versión 2.5.11 (12 de noviembre de 2026).

## Qué aporta

- Monitorea sitios web y servicios en tiempo real
- Obtén soporte multilingüe y de notificaciones
- Crea páginas de estado visuales

## Instalación

**Instalación con Docker Compose**

```
mkdir uptime-kuma
cd uptime-kuma
curl -o compose.yaml https://raw.githubusercontent.com/louislam/uptime-kuma/master/compose.yaml
docker compose up -d
```

**Instalación con comandos de Docker**

```
docker run -d --restart=always -p 3001:3001 -v uptime-kuma:/app/data --name uptime-kuma louislam/uptime-kuma:2
```

## Ejecución

**Ejecutando con Docker**

```
docker compose up -d
```

## Si no programa

Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero instalar la herramienta de monitorización llamada Uptime Kuma. Para usar Docker Compose, necesito ejecutar el siguiente comando: mkdir uptime-kuma
cd uptime-kuma
curl -o compose.yaml https://raw.githubusercontent.com/louislam/uptime-kuma/master/compose.yaml
docker compose up -d. ¿Me ayudas a completar estos pasos?

Repositorio: https://github.com/louislam/uptime-kuma. Sigue las instrucciones oficiales del archivo README de este repositorio para la instalación y ejecución.

Antes de empezar, comprueba en qué sistema operativo estamos y si las herramientas necesarias (ej. Python, Node.js, Git, Docker) están instaladas. Instala las que falten paso a paso según este sistema.

Crea una carpeta nueva y vacía para trabajar. No toques ningún archivo fuera de esta carpeta y no borres nada. Antes de ejecutar cada comando, dime qué vas a hacer en una frase.

Dime qué debería ver en la pantalla al final de cada paso. Si ocurre un error, te pegaré el mensaje de error tal cual y lo solucionaremos juntos.

## Términos relacionados del glosario

- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Ideal para cualquier persona que quiera realizar un seguimiento del estado de sitios web y servidores en su propio servidor.
- **Licencia:** MIT

## Enlaces

- [Repositorio en GitHub →](https://github.com/louislam/uptime-kuma)
- [Leer en turco →](https://trescout.com/discover/uptime-kuma/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-11-14: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. El texto de presentación se preparó con IA a partir de la propia documentación del repositorio y esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/uptime-kuma/
