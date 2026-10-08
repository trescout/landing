# Administre su servidor personal en la nube

CasaOS es un sistema operativo de nube personal de código abierto, ligero y elegante que permite gestionar aplicaciones basadas en Docker con un solo clic en servidores domésticos, mini PC y dispositivos Raspberry Pi. Desarrollado en el lenguaje Go, la plataforma te permite establecer tu propia soberanía digital sin necesidad de comandos de terminal complejos.

- ★ 36.953
- Go
- GitHub Trending · 2026-06-26

## Actualizaciones

- **2 de agosto de 2026:** Estrellas 34,992 → 36,953, última versión v0.4.15 (19 de diciembre de 2024).

## Qué aporta

- Tienda de aplicaciones enriquecidas con un solo clic: instala Nextcloud, Plex, Jellyfin, AdGuard Home, qBittorrent, Home Assistant y más de 100 servicios autohospedados populares en segundos.
- Panel de control web elegante e intuitivo: supervise en tiempo real la carga de CPU y RAM, las tasas de ocupación de disco, la actividad de red y los contenedores en ejecución a través de elegantes tarjetas de widgets.
- Almacenamiento visual y gestión de archivos: conecte automáticamente discos duros externos y unidades USB, comparta sus carpetas en la red local mediante el protocolo Samba (SMB) con sus dispositivos Windows/Mac.
- Soporte especial para Docker Compose: Da vida a tus contenedores personalizados sin esfuerzo pegando cualquier archivo Docker Compose que no se encuentre en la tienda oficial directamente en la interfaz web.
- Ligero núcleo de Go y cero carga del sistema: Al consumir un mínimo de memoria en segundo plano, ofrece un rendimiento fluido incluso en la Raspberry Pi 4/5 más modestas o en portátiles antiguos.

## Instalación

**comando de instalación**

```
curl -fsSL https://get.casaos.io | sudo bash
```

## Ejecución

**comando de actualización**

```
curl -fsSL https://get.casaos.io/update | sudo bash
```

## Arquitectura técnica y principio de funcionamiento

- Arquitectura de microservicios en Go: El núcleo de CasaOS (CasaOS-Gateway, MessageBus, LocalStorage y UserService) consta de servicios ligeros en Go que operan de forma independiente. La comunicación entre servicios se realiza a través de REST y WebSocket.
- Abstracción del ciclo de vida del contenedor: al comunicarse directamente con el demonio de Docker, detecta automáticamente los conflictos de puertos y transforma las variables de entorno y las rutas de montaje de volúmenes persistentes en formularios fáciles de usar.
- Ecosistema de ZimaOS e IceWhale: respaldado por IceWhale Technology, el fabricante del hardware ZimaBoard y ZimaBlade, el proyecto ofrece total compatibilidad con el hardware de nube local.
- Combinación inteligente de discos: combina discos duros de diferentes tamaños en un único grupo de almacenamiento lógico, creando un espacio flexible para medios domésticos y copias de seguridad.

## Guía paso a paso para configurar tu propio servidor doméstico

- Instalación básica de Linux: Instale una versión limpia de Ubuntu Server o Debian minimal en su dispositivo y conéctelo a su red local mediante un cable Ethernet.
- Instalación de CasaOS con una sola línea: ejecute el script de instalación oficial a través de la terminal; el script configura automáticamente Docker y las dependencias.
- Acceso a la interfaz desde el navegador: cree su primera cuenta de administrador escribiendo la dirección IP de su servidor (por ejemplo, http://192.168.1.100) en el navegador desde cualquier ordenador de la red.
- Despliegue de aplicaciones: entra en la pestaña App Store para instalar tu nube personal con Nextcloud y tu biblioteca de películas y series con Jellyfin con un solo clic.

## Si no programa

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Tengo CasaOS instalado en mi servidor doméstico. Quiero instalar y configurar los servicios AdGuard Home (bloqueador de anuncios), Jellyfin (streaming multimedia) y Tailscale (acceso seguro desde fuera de casa) para todos los dispositivos de mi hogar. ¿Podrías explicarme paso a paso cómo instalar estos servicios desde el panel web de CasaOS usando Docker Compose personalizado o la tienda de aplicaciones, y cómo configurar el uso compartido de discos?

## Preguntas frecuentes

- ¿Borra CasaOS mi sistema operativo o datos actuales de Linux? No. CasaOS no borra su sistema operativo actual; se instala sobre él como una capa de administración de escritorios y Docker. Los archivos existentes en sus discos se conservan y quedan accesibles a través del panel.
- ¿Cómo puedo acceder de forma segura a mi servidor CasaOS cuando estoy fuera de casa? En lugar de realizar un reenvío de puertos (port forwarding) inseguro, puedes instalar Tailscale o WireGuard en CasaOS con un solo clic. De este modo, puedes acceder al panel desde cualquier parte del mundo a través de un túnel VPN cifrado, como si estuvieras en tu red doméstica.
- ¿Cuál es la diferencia entre CasaOS y TrueNAS o Unraid? TrueNAS y Unraid son sistemas operativos independientes que se centran en la gestión avanzada de almacenamiento y configuraciones RAID. Por su parte, CasaOS ofrece una experiencia de nube doméstica ligera, extremadamente fácil de usar y centrada en las aplicaciones.
- ¿Se iniciarán automáticamente las aplicaciones instaladas después de un corte de energía? Sí. Todos los contenedores de Docker en CasaOS se inician de forma predeterminada con la política restart: unless-stopped. Cuando se reinicie su servidor, todos sus servicios continuarán funcionando automáticamente desde donde se quedaron.

## Términos relacionados del glosario

- [VPN](https://trescout.com/es/dictionary/vpn/)
- [RAM](https://trescout.com/es/dictionary/ram/)
- [Self-hosted](https://trescout.com/es/dictionary/self-hosted/)
- [CPU](https://trescout.com/es/dictionary/cpu/)
- [Terminal](https://trescout.com/es/dictionary/terminal/)
- [Open Source](https://trescout.com/es/dictionary/open-source/)

- **Para quién es:** Está dirigido a usuarios que desean configurar un servidor doméstico (Homelab) o una nube personal, evitando la complejidad de la terminal y con el objetivo de gestionar aplicaciones de Docker con un solo clic.
- **Licencia:** Apache-2.0 (Geniş özgürlük sunan açık kaynak lisansı)
- **Desarrollador:** IceWhale Technology y la Comunidad de Código Abierto
- **Sistemas compatibles:** Ubuntu, Debian, Raspberry Pi OS, Armbian (x86_64, aarch64, armv7)

## Enlaces

- [Repositorio en GitHub →](https://github.com/IceWhaleTech/CasaOS)
- [Leer en turco →](https://trescout.com/discover/casaos/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-06-26: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/casaos/
