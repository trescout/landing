# Correo electrónico temporal gratuito en Cloudflare

Cloudflare Temp Email es una plataforma de código abierto para crear un servicio de correo electrónico temporal (desechable) totalmente gratuito, sin servidor (serverless) y con tu propio dominio mediante Cloudflare Workers, Pages y D1/KV. Protege la privacidad mediante gestión de buzón, soporte para archivos adjuntos, bot de Telegram y limpieza automatizada.

- ★ 11.734
- TypeScript
- GitHub Trending · 2026-07-23

## Actualizaciones
- 13 de septiembre de 2026: Estrellas 11.391 → 11.734, última versión v1.12.0 (13 de septiembre de 2026).
- 23 de agosto de 2026: Estrellas 11.332 → 11.391, última versión v1.11.1 (22 de agosto de 2026).
- 19 de agosto de 2026: Estrellas 11.156 → 11.332, última versión v1.11.0 (19 de agosto de 2026).
- 2 de agosto de 2026: Estrellas 10.884 → 11.156, última versión v1.10.0 (31 de julio de 2026).

## Qué aporta
- Coste cero de servidor y operación: Funciona con el generoso nivel gratuito de Cloudflare (100.000 peticiones Workers/día, Email Routing y Pages gratuitos) sin alquilar servidores externos.
- Dominio personalizado y direcciones desbloqueables: Genera cuentas desechables usando tu propio dominio, eludiendo las listas de bloqueo aplicadas a los servicios públicos de correo temporal.
- Análisis rápido de correo con Rust y WASM: Procesa mensajes complejos (MIME, multipart, HTML) en milisegundos mediante un módulo WebAssembly compilado en Rust.
- Bot de Telegram y notificaciones inmediatas: Recibe alertas de nuevos correos directamente en Telegram, lee el contenido o genera nuevas direcciones al instante mediante comandos.
- Limpieza automática y acceso protegido: Elimina automáticamente los mensajes y adjuntos caducados tras el periodo configurado y protege la administración con contraseña.

## Cómo empezar y opciones de despliegue

El despliegue solo requiere una cuenta en Cloudflare y un dominio gestionado en Cloudflare DNS. Puedes desplegar en un clic conectando el repositorio de GitHub con Cloudflare Pages o aprovisionar la base D1 y los Workers localmente mediante Wrangler CLI.
- [Guía oficial de instalación →](https://temp-mail-docs.awsl.uk)
- [Interfaz de demostración en vivo →](https://mail.awsl.uk)

## Arquitectura técnica y funcionamiento interno

Cloudflare Temp Email elimina la carga de mantener servidores de correo tradicionales (Postfix, Dovecot) mediante un diseño serverless moderno:
- Enrutamiento de correo de Cloudflare (Email Routing): El tráfico MX entrante se recibe en la red de Cloudflare y se redirige a la función Worker receptora (catch-all).
- Edge Worker y analizador Rust WASM: El flujo de correo en bruto es procesado por el motor Rust WASM optimizado para extraer cabeceras, cuerpo, HTML y adjuntos.
- Almacenamiento Cloudflare D1 y R2: Los mensajes y metadatos se guardan en la base SQLite distribuida Cloudflare D1, mientras que los adjuntos pueden derivarse a Cloudflare R2.
- Aplicación de página única (SPA) moderna: La interfaz web se entrega con latencia prácticamente nula a través de la red CDN global de Cloudflare Pages.
- API REST e integraciones externas: Puntos de enlace programables permiten a pruebas automatizadas o flujos de CI/CD generar direcciones temporales y obtener códigos de verificación.

## Instalación y ejemplo de despliegue

```bash
# 1. Clonar el repositorio e instalar dependencias
git clone https://github.com/dreamhunter2333/cloudflare_temp_email.git
cd cloudflare_temp_email
pnpm install

# 2. Crear la base de datos Cloudflare D1
npx wrangler d1 create temp_email_db

# 3. Aplicar el esquema y desplegar
npx wrangler d1 execute temp_email_db --file=./db/schema.sql
pnpm run deploy
```

## Si no programas
🤖 Pega esto en tu agente de IA (Claude Code · Codex · Antigravity) 
Quiero instalar el proyecto de código abierto dreamhunter2333/cloudflare_temp_email en Cloudflare con mi propio dominio. Dispongo de una cuenta de Cloudflare y un dominio configurado en Cloudflare DNS. ¿Podrías explicarme paso a paso cómo configurar las reglas de reenvío de Email Routing (catch-all), crear la base de datos D1 y publicar la interfaz en Cloudflare Pages? Además, ¿qué variables de entorno debo configurar para recibir alertas en un bot de Telegram?

- **Para quién:** Desarrolladores, evaluadores de control de calidad y usuarios enfocados en la privacidad que buscan alojar un servicio de correo desechable gratis con dominio propio. 
- **Licencia:** MIT (Código abierto) 
- **Infraestructura:** Cloudflare Workers, Pages, D1 (SQLite) y Email Routing 
- **Lenguajes y Herramientas:** TypeScript, Rust (WASM), Vue 3, Wrangler 

## Preguntas frecuentes
- ¿El plan gratuito de Cloudflare es suficiente para uso personal? Sí. El nivel gratuito ofrece 100.000 peticiones de Workers al día, junto con cuotas gratuitas de Email Routing y base de datos D1. Para usuarios individuales y pequeños equipos, superar estos límites es muy difícil; el sistema opera a coste cero.
- ¿Es obligatorio contar con un dominio personalizado? Sí. Para recibir correos electrónicos, necesitas un dominio o subdominio gestionado en Cloudflare DNS. Esto también previene que tus direcciones sean bloqueadas por plataformas web.
- ¿Los correos recibidos se guardan permanentemente? No, es un servicio de correo desechable. El administrador puede definir un periodo de retención (como 1 hora, 24 horas o 7 días); los registros expirados se eliminan automáticamente del almacenamiento.
- ¿El servicio permite responder o enviar correos al exterior? Sí. Aunque Cloudflare Email Routing solo gestiona la recepción, el proyecto soporta el envío de correos salientes al integrarse con APIs de Resend, Brevo o un servidor SMTP externo.

## Enlaces
- [Repositorio en GitHub →](https://github.com/dreamhunter2333/cloudflare_temp_email)
- [Leer en turco →](https://trescout.com/discover/cloudflare-temp-email/)

TreScout no desarrolló esta herramienta · la descubrimos en las tendencias de GitHub y la resumimos en español. Esta página describe el repositorio a fecha de 2026-07-23.

## Términos relacionados del glosario
Self-Hosted Cloud Computing Digital Privacy Open Source API Rust

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/cloudflare-temp-email/
