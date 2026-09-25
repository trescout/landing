# Gestiona tu servidor en la nube personal

CasaOS es un sistema operativo de nube personal de código abierto, ligero y elegante, diseñado para administrar aplicaciones basadas en Docker con un solo clic en servidores domésticos, mini PC y Raspberry Pi. Desarrollado en Go, permite construir tu soberanía digital sin complicaciones en la terminal.

- ★ 36.953
- Go
- GitHub Trending · 2026-06-26

## Actualizaciones
- 2 de agosto de 2026: Estrellas 34.992 → 36.953, última versión v0.4.15 (19 de diciembre de 2024).

## Qué te aporta
- Tienda de aplicaciones en un solo clic: Instala Nextcloud, Plex, Jellyfin, AdGuard Home, qBittorrent, Home Assistant y más de 100 servicios autoalojados en segundos.
- Panel de control web limpio e intuitivo: Monitoriza el uso de CPU, RAM, espacio en disco, actividad de red y contenedores activos en tiempo real mediante elegantes tarjetas de widgets.
- Almacenamiento visual y gestión de archivos: Conecta discos duros externos y llaves USB automáticamente y comparte carpetas en tu red local mediante Samba (SMB).
- Compatibilidad con Docker Compose personalizado: Despliega cualquier contenedor ausente en la tienda pegando el archivo Docker Compose directamente en la interfaz web.
- Núcleo ligero en Go sin sobrecarga: Funciona con un consumo mínimo de memoria en segundo plano, rindiendo de forma fluida incluso en Raspberry Pi 4/5 o portátiles antiguos.

## Instalación

**Comando de instalación**

```
curl -fsSL https://get.casaos.io | sudo bash
```

## Ejecución

**Comando de actualización**

```
curl -fsSL https://get.casaos.io/update | sudo bash
```

## Arquitectura técnica y principio de funcionamiento

En lugar de reemplazar el sistema operativo base, CasaOS actúa como una capa moderna de orquestación Docker sobre tu distribución Debian, Ubuntu o Raspberry Pi OS. Esta arquitectura mantiene intactos los controladores de hardware mientras organiza las funciones en microservicios modulares:
- Arquitectura de microservicios en Go: El núcleo de CasaOS (Gateway, MessageBus, LocalStorage y UserService) opera como servicios Go ligeros e independientes comunicados por REST y WebSockets.
- Abstracción del ciclo de vida de contenedores: Se conecta con el daemon de Docker para resolver conflictos de puertos y traducir volúmenes y variables de entorno en campos claros e intuitivos.
- Ecosistema ZimaOS e IceWhale: Respaldado por IceWhale Technology (creadores de ZimaBoard y ZimaBlade), asegura máxima integración con hardware para nube doméstica.
- Unificación inteligente de discos: Agrupa discos duros de distintas capacidades en un único espacio de almacenamiento lógico para copias de seguridad y contenido multimedia.

## Guía paso a paso para montar tu servidor casero

Para convertir un ordenador viejo o un mini PC en una nube personal completa, sigue estos pasos esenciales:
- Instalación básica de Linux: Instala Ubuntu Server o Debian minimal en tu equipo y conéctalo al router mediante cable Ethernet.
- Instalación de CasaOS en una sola línea: Ejecuta el script oficial en la terminal; se encargará de instalar y configurar Docker y todas las dependencias necesarias.
- Acceso al panel desde el navegador: Desde cualquier dispositivo de tu red local, introduce la IP del servidor (ej. http://192.168.1.100) y crea tu cuenta de administrador.
- Puesta en marcha de aplicaciones: Ve a la pestaña App Store para instalar Nextcloud para tus archivos o Jellyfin para tus series y películas con un solo clic.

## Si no programas
🤖 Si no programas
Tengo CasaOS instalado en mi servidor doméstico. Quiero configurar AdGuard Home (bloqueador de anuncios), Jellyfin (reproducción de medios) y Tailscale (acceso remoto seguro) para todos los dispositivos de la casa. ¿Podrías explicarme paso a paso cómo instalar estos servicios desde la tienda de CasaOS o mediante Docker Compose, y cómo configurar el almacenamiento compartido de los discos?

- **Para quién:** Usuarios y aficionados al homelab que buscan crear nubes personales y gestionar apps Docker sin la fricción de la terminal.
- **Licencia:** Apache-2.0 (Licencia permisiva de código abierto)
- **Desarrollador:** IceWhale Technology y la comunidad de código abierto
- **Sistemas soportados:** Ubuntu, Debian, Raspberry Pi OS, Armbian (x86_64, aarch64, armv7)

## Preguntas frecuentes
- ¿Elimina CasaOS mi sistema operativo Linux o mis archivos? No. CasaOS no borra tu sistema; se instala como una capa de administración y Docker sobre Linux. Todos los archivos presentes en tus discos se conservan intactos.
- ¿Cómo puedo acceder a CasaOS fuera de casa de forma segura? En lugar de abrir puertos peligrosos en el router, instala Tailscale o WireGuard en CasaOS. Esto creará un túnel VPN cifrado para acceder desde cualquier lugar como si estuvieras en casa.
- ¿Qué diferencia hay entre CasaOS, TrueNAS y Unraid? TrueNAS y Unraid son sistemas operativos dedicados al almacenamiento masivo y configuraciones avanzadas de RAID y ZFS. CasaOS busca una experiencia ligera, sencilla y orientada a apps caseras.
- ¿Se inician las aplicaciones solas tras un corte de luz? Sí. Todos los contenedores Docker en CasaOS se configuran con la directiva <code>restart: unless-stopped</code>, retomando su actividad en cuanto el servidor vuelve a encenderse.

## Enlaces
- [GitHub →](https://github.com/IceWhaleTech/CasaOS)

## Términos relacionados del glosario
Self-Hosted Offline Open Source Local

---
Source: TreScout Discover · https://trescout.com/es/discover/casaos/
