# Automatiza tu videoteca de series y streaming multimedia

Sonarr es un grabador de vídeo personal (PVR) y gestor de automatización multimedia de código abierto diseñado para usuarios de Usenet y BitTorrent. Desarrollado en C# y .NET, monitoriza nuevos episodios, se comunica con clientes de descarga y organiza los archivos para servidores como Plex y Jellyfin.

- ★ 16.274
- C#
- GitHub Trending · 2026-09-12

## Actualizaciones
- 17 de septiembre de 2026: Estrellas 16.274, última versión v4.0.20.3014 (optimizaciones de rendimiento en .NET 8 y mejoras en Custom Formats).

## Qué te aporta
- Seguimiento automático y calendario de episodios: Sigue las fechas de emisión en un calendario integrado y lanza descargas automáticas en cuanto se publican.
- Mejora inteligente de calidad (Quality Upgrades): Sustituye gradualmente archivos de calidad básica por versiones superiores (1080p o 4K HDR) con el tiempo.
- Soporte para enlaces duros (Hardlinks): Mantiene los torrents compartiendo sin duplicar espacio en disco y dejándolos listos para ver.
- Amplia integración de clientes e indexadores: Funciona fluidamente con qBittorrent, Transmission, Deluge, SABnzbd y NZBGet.
- Organización y renombrado automático: Limpia títulos y organiza temporadas siguiendo las pautas de Plex, Jellyfin y Emby.

## Opciones de instalación: Docker y servicio local

**Configuración con Docker Compose**

```yaml
services:
  sonarr:
    image: lscr.io/linuxserver/sonarr:latest
    container_name: sonarr
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/Madrid
    volumes:
      - /opt/sonarr/data:/config
      - /mnt/storage/media/tv:/tv
      - /mnt/storage/downloads:/downloads
    ports:
      - 8989:8989
    restart: unless-stopped
```

## Ejecución y configuración básica

**Iniciar el contenedor**

```
docker compose up -d
```

**Acceder al panel web**

```
http://localhost:8989
```

## Arquitectura técnica y principio de funcionamiento

Sonarr opera como el núcleo de orquestación en infraestructuras de medios autoalojadas:
- Puente de protocolos Torznab y Newznab: Consulta indexadores mediante Prowlarr o Jackett a través de APIs estándar en XML y JSON.
- Operaciones atómicas y Hardlinks: Conecta los inodos del sistema de archivos en lugar de copiar archivos gigantescos, evitando desgaste de disco.
- Motor de puntuación de formatos personalizados: Evalúa releases asignando puntuaciones según códecs de audio (Atmos, DTS), vídeo (HEVC, AV1) y grupos de ripeo.

## Integración en el ecosistema multimedia (Plex, Jellyfin, Prowlarr)

Para un servidor casero completo, Sonarr se enlaza con herramientas complementarias:
- Sincronización de indexadores con Prowlarr: Centraliza tus trackers y feeds Usenet y transmítelos a Sonarr en segundos.
- Control de descargas con qBittorrent / SABnzbd: Asigna categorías y ratios de compartición específicos para series.
- Notificación instantánea a Plex o Jellyfin: Fuerza la actualización de la biblioteca en cuanto se importa un nuevo episodio.

## Si no programas
🤖 Si no programas
Quiero montar Sonarr, qBittorrent, Prowlarr y Jellyfin usando Docker Compose. ¿Podrías darme un archivo docker-compose.yml con las rutas de volúmenes configuradas para que los hardlinks funcionen sin duplicar espacio en disco, y explicarme los primeros ajustes que debo hacer en Sonarr?

- **Para quién:** Usuarios de homelab, aficionados a series y quienes deseen una videoteca organizada sin mantenimiento manual.
- **Licencia:** GPL-3.0 (Licencia de código abierto)
- **Tecnología:** Aplicación web escrita en C# y .NET
- **Puerto Web:** 8989 por defecto

## Preguntas frecuentes
- ¿Descarga Sonarr los archivos directamente? No. Sonarr no es un cliente de descarga; busca los contenidos, envía las órdenes a qBittorrent o SABnzbd y organiza los archivos completados en sus carpetas.
- ¿Qué es un hardlink y duplica el espacio en disco? No. Un enlace duro es un segundo puntero a los mismos sectores físicos del disco. Aparece en ambas carpetas pero solo ocupa espacio una vez.
- ¿Cuál es la diferencia entre Sonarr y Radarr? Sonarr está especializado en series de televisión y temporadas, mientras que Radarr traslada el mismo modelo al catálogo de películas.
- ¿Se necesita una VPN para usar Sonarr? Sonarr solo realiza consultas de metadatos y no requiere VPN. Sin embargo, se aconseja encarecidamente utilizar una VPN para el cliente de descarga (qBittorrent).

## Enlaces
- [GitHub →](https://github.com/Sonarr/Sonarr)

## Términos relacionados del glosario
Self-Hosted Offline Open Source Local

---
Source: TreScout Discover · https://trescout.com/es/discover/sonarr/
