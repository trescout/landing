# Copia de seguridad de fotos y vídeos en su propio servidor

Immich es una solución de alto rendimiento diseñada para realizar copias de seguridad de sus fotos y vídeos personales, que puede alojar directamente en su propio servidor.

- ★ 109.538
- GitHub Trending · 2026-07-05

## ¿Qué hace esta herramienta?
Immich es una solución de alto rendimiento diseñada para realizar copias de seguridad de sus fotos y vídeos personales, que puede alojar directamente en su propio servidor. Le permite gestionar su biblioteca multimedia a través de aplicaciones móviles y web.

## ¿Para quién es?
Aquellos que deseen almacenar y gestionar sus fotos y vídeos en su propio hardware en lugar de utilizar servicios en la nube de terceros.

## Qué no esperar
Usuarios que no deseen gestionar su propio servidor o que no quieran lidiar con procesos de instalación técnica.

## Aspectos destacados
- Realiza copias de seguridad de fotos y vídeos en su calidad original.
- Ofrece acceso a través de aplicaciones web y móviles.
- Garantiza la privacidad de los datos al alojarlos en su propio hardware.
- Crea espacios para miembros de la familia o equipos con soporte multiusuario.

## Primer flujo de uso
- Asegúrese de cumplir con los requisitos de hardware especificados en la documentación oficial.
- Inicie los contenedores de Immich utilizando Docker y Docker Compose.
- Descargue la aplicación móvil en su dispositivo y conéctese introduciendo la dirección de su servidor.
- Cree la primera cuenta de administrador e inicie el proceso de copia de seguridad.

## Inicio seguro

## Primer prompt
¿Cómo añadir un nuevo usuario en la instalación de Immich?

## Instalación
**Descargar la configuración de Docker Compose**

```
mkdir immich-app && cd immich-app
wget -O docker-compose.yml https://github.com/immich-app/immich/releases/latest/download/docker-compose.yml
wget -O .env https://github.com/immich-app/immich/releases/latest/download/example.env
```


## Ejecución
**Iniciar servicios Docker**

```
docker compose up -d
```


## Enlaces
- Repositorio en GitHub →
- README oficial de Immich →
- Sitio oficial de Immich →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/immich/
