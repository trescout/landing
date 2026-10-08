# Gestión de contraseñas en tu propio servidor

Vaultwarden es un software de servidor de código abierto desarrollado en Rust que funciona de manera compatible con la herramienta de gestión de contraseñas Bitwarden.

- ★ 68.594
- Rust
- GitHub Trending · 2026-08-24

## Actualizaciones

- **6 de octubre de 2026:** Estrellas 67,398 → 68,594, última versión 1.37.4 (5 de octubre de 2026).
- **14 de septiembre de 2026:** Estrellas 65,982 → 67,398, última versión 1.37.3 (13 de septiembre de 2026).
- **24 de agosto de 2026:** Estrellas 65,983 → 65,982, última versión 1.37.2 (22 de agosto de 2026).

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

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Ayúdame a instalar Vaultwarden, una herramienta que proporciona administración de contraseñas en mi propio servidor. Esta herramienta es un software de servidor compatible con los clientes Bitwarden. Dado que realizaré la instalación usando Docker, explico paso a paso cómo configurar los comandos de imagen para extraer y ejecutar, montar un volumen para conservar mis datos y tener en cuenta los requisitos de HTTPS.

## Términos relacionados del glosario

- [Rust](https://trescout.com/es/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Es para usuarios que desean alojar sus propias contraseñas y datos confidenciales en su propio servidor en lugar de depender de servicios en la nube de terceros.
- **Licencia:** AGPL-3.0

## Enlaces

- [Repositorio en GitHub →](https://github.com/dani-garcia/vaultwarden)
- [Leer en turco →](https://trescout.com/discover/vaultwarden/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-08-24: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/vaultwarden/
