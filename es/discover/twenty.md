# CRM moderno y de código abierto

Twenty es una alternativa de código abierto a Salesforce que permite a los equipos técnicos crear un CRM moderno que se puede personalizar según sus procesos comerciales. Puede alojar este sistema, que se centra en flujos de trabajo respaldados por inteligencia artificial, en su propio servidor.

- ★ 55.660
- TypeScript
- Lisans: özel
- GitHub Trending · 26 May 2026

## Qué aporta
- Una alternativa gratuita y de código abierto a Salesforce.
- Control total sobre tus datos con la opción de autohospedaje.
- Flujos de trabajo modernos impulsados por IA.
- Bloques de construcción flexibles que se pueden adaptar a las necesidades de su negocio.

## Instalación
**Descargar plantilla de entorno**

```
curl -o .env https://raw.githubusercontent.com/twentyhq/twenty/refs/heads/main/packages/twenty-docker/.env.example
```

**Descargar archivo Compose**

```
curl -o docker-compose.yml https://raw.githubusercontent.com/twentyhq/twenty/refs/heads/main/packages/twenty-docker/docker-compose.yml
```

**Generar clave de cifrado**

```
openssl rand -base64 32
```

**Iniciar servicios**

```
docker compose up -d
```


## Ejecución
**Acceder a la interfaz local**

```
http://localhost:3000
```


## ¿Cómo instalar?
Suele instalarse en tu propio servidor con Docker; Los pasos de instalación se encuentran en la documentación. Requiere algunos conocimientos técnicos para gestionarlo.

## ¿Cómo instalar, cómo utilizar?
Quiero instalar un CRM de código abierto llamado Twenty; cree una nueva aplicación en la terminal con el comando 'npx create-twenty-app my-app', luego publíquela en mi espacio de trabajo con 'npx veinte app:publish --private'. Dígame también cómo ejecutarlo con Docker Compose para autohospedaje.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/twenty/
