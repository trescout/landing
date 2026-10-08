# Self-Hosted: Homelabs, repatriación de la nube e infraestructura propia

*Glosario · Dev · Última actualización: 19 de septiembre de 2026*

Self-hosted (autoalojamiento) es la práctica técnica de instalar, configurar y operar servicios informáticos y aplicaciones web en servidores físicos propios en lugar de contratar servicios comerciales SaaS.

## Etimología y Fundamento Conceptual

El vocablo anglosajón *self-hosted* sintetiza autonomía e infraestructura de alojamiento. En informática representa la emancipación digital : mantener el control absoluto sobre los datos, sistemas operativos y aplicaciones sin ataduras con proveedores comerciales.

## 1. De la Saturación de SaaS a la Repatriación de la Nube

El entusiasmo por el software por suscripción ha derivado en costes mensuales imprevistos y dependencia técnica. Inspirada por empresas como Basecamp, la **repatriación de la nube** promueve devolver cargas de trabajo estables a servidores dedicados propios para ahorrar costes notables.

## 2. Arquitectura de Hardware y la Cultura de Homelabs

Los profesionales despliegan sus servicios sobre diversos equipos :

- **Microordenadores de Bajo Consumo:** Dispositivos Raspberry Pi y mini PCs compactos (Intel N100) con consumos inferiores a 15 vatios.
- **Servidores de Segunda Mano:** Servidores en rack reutilizados con memorias ECC y discos redundantes para entornos de virtualización avanzada.
- **Hipervisores Base:** Distribuciones como Proxmox VE y TrueNAS orientadas a levantar contenedores y máquinas virtuales con solidez.

## 3. El Ecosistema de Software para Autoalojamiento

La generalización de los contenedores ha transformado el mantenimiento :

- **Contenedores con Docker:** Automatización declarativa mediante ficheros Docker Compose que orquestan servicios en pocos segundos.
- **Proxies Inversos:** Servidores como Nginx Proxy Manager o Traefik que tramitan certificados TLS gratuitos de Let's Encrypt al vuelo.
- **Redes Privadas Virtuales:** Soluciones seguras como WireGuard o Tailscale para conectar dispositivos remotos sin abrir puertos inseguros en el router.

## 4. Aplicaciones Libres Populares para Autoalojar

El código abierto brinda alternativas completas para las necesidades corporativas :

- **Almacenamiento y Documentos:** Nextcloud para archivos colaborativos, Immich para imágenes y Vaultwarden para contraseñas.
- **Servidores Multimedia:** Jellyfin y Plex para disfrutar de series y películas en red doméstica.
- **Domótica Integrada:** Home Assistant administrando la vivienda inteligente con procesamiento estrictamente local.

## 5. Obligaciones Ineludibles: La Regla de Copia 3-2-1

Ser el dueño del servidor exige protegerse contra posibles accidentes físicos :

- **La Estrategia 3-2-1:** Disponer de **3** copias de los datos en **2** soportes de almacenamiento diferentes, guardando **1** copia en una ubicación exterior.
- **Comprobación Periódica:** Una copia de seguridad que no se prueba restaurando datos periódicamente no ofrece garantías reales.

*Usar SaaS es como alquilar una habitación donde el dueño puede subirte el precio o cambiarte las llaves cuando quiera; autoalojar es ser propietario de tu propia casa: te encargas de la fontanería y las goteras, pero disfrutas de total libertad y privacidad.*

## Preguntas frecuentes

**¿Qué significa la expresión self-hosted?**

Es el acto de poner en marcha y gestionar programas informáticos en servidores propios en vez de depender de servicios de terceros en la nube.

**¿En qué difiere Local de Self-Hosted?**

Local se ejecuta directamente en el ordenador que estás manejando ahora; self-hosted opera en un servidor dedicado encendido de forma continuada en red.

**¿Cómo conectarse a los servicios de casa de forma segura?**

Mediante redes privadas virtuales como Tailscale o WireGuard que crean canales cifrados punto a punto sin abrir puertos públicos.

**¿En qué consiste la regla de copia de seguridad 3-2-1?**

Guardar 3 copias de la información en 2 tipos de almacenamiento distintos, dejando 1 de ellas fuera de las instalaciones principales.

## Términos relacionados

- [Local](https://trescout.com/es/dictionary/local/)
- [Offline](https://trescout.com/es/dictionary/offline/)
- [Open Source](https://trescout.com/es/dictionary/open-source/)
- [Deployment](https://trescout.com/es/dictionary/deployment/)

## Herramientas relacionadas

- [Immich](https://trescout.com/es/discover/immich/)
- [Chatwoot](https://trescout.com/es/discover/chatwoot/)
- [Open-Generative-AI](https://trescout.com/es/discover/open-generative-ai/)
- [OpenWA](https://trescout.com/es/discover/openwa/)
- [Openship](https://trescout.com/es/discover/openship/)
- [Instatic](https://trescout.com/es/discover/instatic/)
- [TREK](https://trescout.com/es/discover/trek/)
- [Celld](https://trescout.com/es/discover/celld/)

Esta explicación se redactó en lenguaje llano para TreScout y se **tradujo automáticamente** a partir del original en turco · la versión en turco es la que prevalece. Si detecta algún error o carencia, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/self-hosted/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/self-hosted/
