# Correo electrónico temporal gratuito en Cloudflare

Cloudflare Temp Email es una plataforma de código abierto que le permite configurar un servicio de correo electrónico temporal (disposable email) totalmente gratuito, sin servidor (serverless) y que funciona con su propio dominio, utilizando la infraestructura de Cloudflare Workers, Pages y la base de datos D1/KV. Protege su privacidad personal mediante la gestión de bandejas de entrada, el almacenamiento de archivos adjuntos, la integración con bots de Telegram y mecanismos de limpieza automática.

- ★ 11.734
- TypeScript
- GitHub Trending · 2026-07-23

## Qué aporta
- Cero costes de servidor y operativos: funciona sobre el generoso plan gratuito de Cloudflare (100.000 solicitudes de Workers al día, Email Routing gratuito y alojamiento de Pages) sin necesidad de alquilar un servidor externo.
- Nombre de dominio personalizado y direcciones imposibles de bloquear: a diferencia de los servicios de correo electrónico temporal genéricos, genera direcciones de un solo uso con su propio nombre de dominio que no son detectadas por las listas negras de los sitios web.
- Análisis de correo electrónico rápido con Rust y WASM: procesa correos electrónicos complejos con contenido MIME, multipart y HTML en milisegundos gracias a un módulo de WebAssembly compilado con Rust.
- Bot de Telegram y notificaciones instantáneas: recibe notificaciones directamente a través de Telegram cuando llegue un nuevo correo electrónico, lee el contenido del mensaje o crea nuevas direcciones al instante mediante comandos del bot.
- Limpieza automática y acceso seguro: elimina automáticamente los mensajes y archivos adjuntos antiguos tras un periodo determinado; impide el acceso no autorizado mediante una contraseña de administrador.

## Cómo empezar y opciones de instalación
- Guía de instalación oficial →
- Interfaz de demostración en vivo →

## Arquitectura técnica y principio de funcionamiento
- Integración de Cloudflare Email Routing: Todo el tráfico MX que llega a su dominio es recibido en la infraestructura de Cloudflare y, mediante una regla catch-all, se redirige directamente a la función Worker de captura.
- Edge Worker y analizador Rust WASM: El flujo de correo electrónico entrante (raw stream) se transfiere a un motor Rust WASM optimizado que se ejecuta dentro del Worker para analizar rápidamente los encabezados, el cuerpo, el HTML y los archivos adjuntos.
- Almacenamiento en Cloudflare D1 y R2: Los textos y metadatos de los correos electrónicos se almacenan en Cloudflare D1, una base de datos SQLite en el borde. Los archivos adjuntos se escriben opcionalmente en el almacenamiento de objetos Cloudflare R2.
- Aplicación de página única (SPA) moderna: una interfaz web fácil de usar servida con latencia cero a través de la red CDN global de Cloudflare Pages.
- API REST e integraciones externas: brinda la oportunidad de derivar nuevas direcciones de correo electrónico y consultar la bandeja de entrada a través de puntos finales de API REST para pruebas automatizadas o software de terceros.

## Instalación y despliegue de ejemplo
**Pasos de despliegue con Wrangler CLI**

```
# 1. Depoyu klonlayin ve bagimliliklari kurun
git clone https://github.com/dreamhunter2333/cloudflare_temp_email.git
cd cloudflare_temp_email
pnpm install

# 2. Cloudflare D1 veritabanini olusturun
npx wrangler d1 create temp_email_db

# 3. Veritabani semasini calistirin ve yayinlayin
npx wrangler d1 execute temp_email_db --file=./db/schema.sql
pnpm run deploy
```


## Si no programa
Quiero configurar el proyecto de correo electrónico temporal de código abierto dreamhunter2333/cloudflare_temp_email que se ejecuta en Cloudflare con mi propio dominio. Tengo una cuenta de Cloudflare y un dominio vinculado a Cloudflare DNS. ¿Podrías explicarme paso a paso cómo configurar desde cero el enrutamiento de correo electrónico (Email Routing), la base de datos D1 y la interfaz de Cloudflare Pages a través del panel de control de Cloudflare? Además, ¿qué pasos de configuración debo seguir para redirigir los correos electrónicos entrantes a mi bot de Telegram?

## Preguntas frecuentes
- ¿Es suficiente el plan gratuito de Cloudflare para uso personal? Sí. El plan gratuito de Cloudflare ofrece 100.000 solicitudes de Worker al día, Email Routing gratuito y una cuota para la base de datos D1. Para uso personal y equipos pequeños, es casi imposible superar estos límites; el sistema funciona con un coste totalmente nulo.
- ¿Es necesario un dominio personalizado para utilizar el servicio? Sí. Para poder recibir correos electrónicos, debe disponer de un dominio (o subdominio, p. ej. mail.sudominio.com) gestionado a través de Cloudflare DNS. De este modo, podrá superar fácilmente los sitios que bloquean los servicios de correo electrónico temporal genéricos.
- ¿Los correos electrónicos entrantes se almacenan permanentemente? No, este es un servicio de correo electrónico temporal. Como administrador del sistema, puede determinar el período de retención de los correos electrónicos (por ejemplo, 1 hora, 24 horas o 7 días) desde el panel; Las grabaciones caducadas se eliminan automáticamente del almacenamiento D1 y R2.
- ¿Se pueden enviar respuestas de correo electrónico al exterior a través del servicio? Sí. Aunque Cloudflare Email Routing solo admite la recepción de correos electrónicos, el proyecto también permite enviar y responder correos electrónicos al exterior desde el panel web cuando se conecta una API de Resend, Brevo o un servidor SMTP personalizado.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/cloudflare-temp-email/
