# ¿Qué es Self-hosted?

*Desarrollo · Última actualización: 19 de septiembre de 2026*

Self-hosted (autoalojamiento o alojamiento local) es una arquitectura para ejecutar y gestionar un software, base de datos o servicio digital en un servidor físico bajo su control total, hardware local (homelab) o servidor privado virtual (VPS), sin depender de una empresa de nube de terceros (SaaS).

## Etimología y equivalente en turco

El término, formado por la combinación de las palabras de origen inglés *self* (uno mismo) y *host* (alojar), se denomina en español autoalojamiento, alojamiento propio o alojamiento local.

En el modelo tradicional de SaaS (Software como Servicio), los usuarios son solo inquilinos; los datos y la infraestructura están bloqueados en los centros de datos de empresas extranjeras. En el enfoque de alojamiento propio (self-hosted), usted es directamente el administrador del sistema y el propietario: la base de datos, los discos de almacenamiento, las reglas de red y las claves de cifrado son completamente de su propiedad física o lógica.

## 1. Del agotamiento del SaaS a la repatriación a la nube (Cloud Repatriation)

En la última década, la transición de todo software a un modelo de suscripción mensual recurrente ha generado un grave agotamiento por suscripciones tanto en individuos como en instituciones:

- Callejón sin salida de costos: Las herramientas de SaaS que cuestan entre 10 y 50 dólares al mes por usuario se convierten en costos descontrolados de cientos de miles de dólares a medida que el equipo crece. De hecho, el hecho de que líderes tecnológicos globales como 37signals (Basecamp) hayan abandonado la nube para volver a su propio hardware (repatriación a la nube) ha demostrado la racionalidad económica del enfoque autohospedado.
- Soberanía de datos y privacidad: El autohospedaje es el escudo más fuerte contra el riesgo de que las empresas cambien unilateralmente las condiciones de uso, utilicen los datos para entrenar modelos de inteligencia artificial o cierren cuentas repentinamente. Mantener los datos confidenciales de los clientes dentro de sus propias fronteras de acuerdo con las normativas de la LOPD y el RGPD también garantiza el cumplimiento legal.

## 2. Arquitectura de hardware y ecosistema Homelab

El mundo del alojamiento propio ha pasado hoy de los costosos gabinetes de servidores corporativos a las salas de estar y laboratorios domésticos (Homelab):

- Hardware de bajo consumo: Los mini PC basados en Intel N100, Raspberry Pi 5 o portátiles antiguos pueden funcionar ininterrumpidamente 24/7 con un consumo eléctrico de solo unos pocos cientos de liras al año.
- Almacenamiento y Seguridad de Datos (ZFS y RAID): Las matrices RAID donde se espejan múltiples discos duros y el sistema de archivos ZFS hacen que la pérdida de datos sea imposible, incluso si un disco falla físicamente. Sistemas operativos como TrueNAS y unRAID transforman este hardware en grupos de almacenamiento profesionales.
- Alternativa de VPS en la nube: Para quienes no desean alojar hardware en casa, los servidores virtuales (VPS) económicos alquilados a proveedores como Hetzner u OVH combinan la libertad del alojamiento propio (self-hosted) con la fiabilidad de la nube.

## 3. Stack de software moderno para self-hosting

Los días en los que había que compilar PHP y MySQL manualmente en Linux han quedado atrás. La arquitectura moderna se basa en tres pilares:

- Contenedorización (Docker y Docker Compose): Cada servicio (Nextcloud, Vaultwarden, Jellyfin) funciona dentro de un contenedor Docker aislado con sus propias bibliotecas. Gracias al archivo docker-compose.yml, decenas de servicios se pueden poner en marcha con un solo comando.
- Servidor Proxy Inverso (Reverse Proxy): Nginx, Traefik o Caddy; recibe las solicitudes web entrantes, dirige los nombres de dominio al contenedor correcto y renueva automáticamente certificados SSL/TLS gratuitos a través de Let's Encrypt.
- Túneles de red seguros (Zero-Trust y Mesh VPN): Abrir puertos al exterior en el router doméstico es una invitación a los ciberataques. Los usuarios modernos de autohospedaje (self-hosted) utilizan Tailscale, WireGuard o Cloudflare Tunnels para ejecutar sus sistemas de forma segura en una red interna (Mesh VPN) cerrada al mundo exterior y abierta únicamente a sus dispositivos autorizados.

## 4. Soluciones populares de Self-Hosted

- Nube personal y fotos: En lugar de Google Drive, Nextcloud; en lugar de Google Photos, Immich con reconocimiento facial por inteligencia artificial.
- Gestión de contraseñas: Vaultwarden (compatible con Bitwarden), una alternativa ligera y de código abierto a 1Password.
- Transmisión de medios: Jellyfin y Plex, donde gestionas tu propio archivo en lugar de Netflix y Spotify.
- Inteligencia Artificial Local: Ollama y Open WebUI ejecutándose en tu propia tarjeta gráfica en lugar de una suscripción a ChatGPT.
- Hogar Inteligente: Home Assistant funcionando de forma completamente local en lugar de depender de fabricantes dependientes de la nube.

## 5. Responsabilidades: Regla de respaldo 3-2-1

La libertad conlleva responsabilidad. No hay ninguna empresa en la nube detrás de ti para abrir un ticket de soporte en caso de fallo de hardware. Por eso, la regla de copia de seguridad 3-2-1 es obligatoria:

Mantenga al menos 3 copias de sus datos.
Guarda estas copias en 2 soportes físicos diferentes (por ejemplo, un disco interno y un USB externo).
- Aloje al menos 1 de las copias en una ubicación física diferente (servidor remoto cifrado o almacenamiento externo) para protegerla contra incendios y robos.

## Preguntas frecuentes

**¿Qué es 'self-hosted' y qué significa en español?**

Es un concepto de origen inglés que significa 'autoalojamiento' o 'alojamiento en servidor propio'. Se refiere a ejecutar software en el propio hardware o servidor del usuario en lugar de utilizar proveedores de nube de terceros.

**¿Es necesario saber programación avanzada para configurar un sistema autohospedado (self-hosted)?**

No, no necesita escribir código. Es suficiente con tener conocimientos básicos de la línea de comandos de Linux y entender la lógica de Docker. Además, sistemas modernos como CasaOS y Umbrel ofrecen la posibilidad de realizar instalaciones con un solo clic mediante una lógica de tienda de aplicaciones.

**¿Es seguro ejecutar servicios autohospedados en un servidor doméstico (Homelab)?**

Cuando se configura correctamente, es más seguro que las nubes comerciales porque sus datos no se comparten con empresas. Sin embargo, es fundamental utilizar túneles VPN como Tailscale en lugar de abrir puertos directamente en el módem y no descuidar las actualizaciones de seguridad.

**¿Por qué es vital la regla de respaldo 3-2-1?**

En los sistemas autohospedados, no existe un servicio de atención al cliente que recupere los datos si el hardware falla. La regla de 3 copias, 2 soportes diferentes y 1 ubicación externa evita la pérdida de datos en caso de incendio o avería del hardware.

## Términos relacionados

- [Local](https://trescout.com/es/dictionary/local/)
- [Offline](https://trescout.com/es/dictionary/offline/)
- [Open Source](https://trescout.com/es/dictionary/open-source/)
- [Deployment](https://trescout.com/es/dictionary/deployment/)

## Herramientas relacionadas

- [Immich](https://trescout.com/es/discover/immich/)
- [CasaOS](https://trescout.com/es/discover/casaos/)
- [Chatwoot](https://trescout.com/es/discover/chatwoot/)
- [Open-Generative-AI](https://trescout.com/es/discover/open-generative-ai/)
- [OpenWA](https://trescout.com/es/discover/openwa/)
- [Openship](https://trescout.com/es/discover/openship/)
- [Instatic](https://trescout.com/es/discover/instatic/)
- [TREK](https://trescout.com/es/discover/trek/)

Esta explicación se redactó en lenguaje sencillo para TreScout y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/self-hosted/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/self-hosted/
