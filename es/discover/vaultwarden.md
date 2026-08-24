# Gestión de contraseñas en tu propio servidor

No se pudo producir un resumen de este artículo hoy; consulte el enlace fuente para obtener más detalles.

- ★ 65.982
- Rust
- GitHub Trending · 2026-08-24

## Qué aporta
- Totalmente compatible con los clientes oficiales de Bitwarden
- Puede alojarse en su propio servidor con bajo consumo de recursos.
- Ofrece autenticación de dos factores y acceso de emergencia.

## Instalación
**Descargue y ejecute el contenedor**

```
docker pull vaultwarden/server:latest
docker run --detach --name vaultwarden \
  --env DOMAIN="https://vw.domain.tld" \
  --volume /vw-data/:/data/ \
  --restart unless-stopped \
  --publish 127.0.0.1:8000:80 \
  vaultwarden/server:latest
```


## Si no programa
Ayúdame a instalar Vaultwarden, una herramienta que proporciona administración de contraseñas en mi propio servidor. Esta herramienta es un software de servidor compatible con los clientes Bitwarden. Dado que realizaré la instalación usando Docker, explico paso a paso cómo configurar los comandos de imagen para extraer y ejecutar, montar un volumen para conservar mis datos y tener en cuenta los requisitos de HTTPS.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/vaultwarden/
