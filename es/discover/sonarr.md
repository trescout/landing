# Gestione automáticamente su archivo de series

Sonarr es un grabador de vídeo personal (PVR) inteligente y de código abierto y un administrador de automatización de medios desarrollado para usuarios de Usenet (grupos de noticias) y BitTorrent. Plataforma desarrollada con infraestructura C# y .NET; realiza un seguimiento de los episodios recién publicados, se comunica con los clientes de descarga, cambia el nombre y transfiere archivos a las bibliotecas Plex y Jellyfin de forma regular.

- ★ 16.274
- C#
- GitHub Trending · 2026-09-12

## Qué aporta
- Seguimiento automático de episodios y calendario: realice un seguimiento de las fechas de emisión de sus series favoritas a través del calendario integrado y descargue automáticamente nuevos episodios tan pronto como se publiquen.
- Actualizaciones de calidad inteligentes: reemplace automáticamente las secciones de menor resolución (HDTV de 720p) con versiones de mayor calidad (1080p/4K HDR WEB-DL) con el tiempo.
- Compatibilidad con enlaces duros: mantener los archivos descargados en torrents compartidos y presentarlos al servidor de medios en el mismo disco sin duplicarlos.
- Amplia integración de cliente e indexador: trabajo sin fricción con qBittorrent, Transmission, Deluge, SABnzbd y NZBGet.
- Nombramiento de archivos personalizable: Nomenclatura y carpetas automáticas de archivos de episodios de acuerdo con los estándares de los servidores de medios (Plex, Jellyfin, Emby).

## Opciones de instalación: Docker y servicio local
**Instalación con Docker Compose**

```
services:
  sonarr:
    image: lscr.io/linuxserver/sonarr:latest
    container_name: sonarr
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/Istanbul
    volumes:
      - /opt/sonarr/data:/config
      - /mnt/storage/media/tv:/tv
      - /mnt/storage/downloads:/downloads
    ports:
      - 8989:8989
    restart: unless-stopped
```


## Funcionamiento y configuración básica.
**Iniciando el contenedor**

```
docker compose up -d
```

**Acceso a la interfaz web**

```
http://localhost:8989
```


## Arquitectura técnica y principio de funcionamiento
- Puente de protocolo Torznab y Newznab: se comunica con indexadores (a través de Jackett o Prowlarr) a través de API XML/JSON estándar a través de canales RSS y consultas de búsqueda.
- Movimiento atómico de archivos y enlace duro: reduce la carga de escritura en el disco y el desperdicio de almacenamiento a cero al montar el inodo del sistema de archivos en lugar de copiar el archivo cuando finaliza la descarga.
- Motor de puntuación de formatos personalizados: selecciona la mejor versión puntuando los códecs de audio preferidos (Atmos, DTS-HD), los formatos de vídeo (AV1, HEVC) y los grupos de editores.

## Integración del ecosistema de medios (Plex, Jellyfin, Prowlarr)
- Sincronización del indexador con Prowlarr: importe automáticamente rastreadores de torrents e indexadores de Usenet a Sonarr desde un único centro.
- Gestión de descargas con qBittorrent / SABnzbd: controle la velocidad de descarga y la tasa de uso compartido a través de categorías designadas.
- Notificación de la biblioteca Plex o Jellyfin: envía una notificación instantánea al servidor de medios cuando se escribe un nuevo episodio en el disco y escanea la biblioteca.

## Si no programa
Quiero ejecutar los servicios Sonarr, qBittorrent, Prowlarr y Jellyfin juntos en Docker en mi servidor doméstico. ¿Puede explicar paso a paso el archivo docker-compose.yml completo que contiene una estructura de montaje de volumen único y las primeras configuraciones que necesito realizar en el panel web de Sonarr para que los enlaces físicos funcionen sin problemas?

## Preguntas frecuentes
- ¿Sonarr descarga el archivo directamente? No. Sonarr no es un cliente de descargas; es un gerente. Busca, envía el archivo torrent/NZB a clientes como qBittorrent o SABnzbd y mueve el archivo descargado a la carpeta de archivo.
- ¿Qué es hardlink y llena el disco el doble? No. Hardlinking consiste en colocar un segundo puntero de ruta a los datos físicos del archivo en el disco. Aparece tanto en la carpeta de descargas como en la de TV, pero ocupa tanto espacio en el disco como un solo archivo.
- ¿Cuál es la diferencia entre Sonarr y Radarr? Mientras Sonarr dirige series, temporadas y episodios de televisión; Radarr ofrece la misma arquitectura para largometrajes.
- ¿Es necesario utilizar una VPN? Dado que Sonarr sólo realiza consultas RSS y metadatos, generalmente no requiere una VPN; sin embargo, se recomienda que el cliente de descarga de torrents (qBittorrent) se ejecute detrás de un túnel VPN.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/sonarr/
