# Evite los bloqueos de censura con túneles DNS

MasterDnsVPN es una solución de red privada virtual (VPN) de túnel de sistema de nombres de dominio (túnel DNS) de baja carga desarrollada para superar las barreras de la censura. Escrita en lenguaje Go, la herramienta ofrece alta estabilidad de pérdida de paquetes y funciones de equilibrio de carga de resolución en la transmisión de datos.

- ★ 6.870
- Go
- GitHub Trending · 2026-06-11

## Actualizar
- 2 de agosto de 2026: Star 5.411 → 6.870, última versión v2026.06.13.234407-7de2476 (13 de junio de 2026).

## Qué aporta
- Proporciona transmisión de datos en redes censuradas mediante el método de túnel DNS.
- Ofrece rutas múltiples y equilibrio de carga para una baja pérdida de paquetes y alta velocidad.
- Optimizado para una conexión estable incluso en condiciones de red restringidas.

## Instalación
**Configuración automática del servidor**

```
bash <(curl -Ls https://raw.githubusercontent.com/masterking32/MasterDnsVPN/main/server_linux_install.sh)
```

**Ejecutando con Docker**

```
docker run -d \
  --name masterdnsvpn \
  --restart unless-stopped \
  -e DOMAIN=v.example.com \
  -v $(pwd)/data:/data \
  -p 53:53/tcp \
  -p 53:53/udp \
  ghcr.io/masterking32/masterdnsvpn:latest
```


## Si no programa
Quiero establecer una conexión segura mediante un túnel DNS en una red censurada utilizando la herramienta MasterDnsVPN. ¿Cómo puedo configurar el lado del servidor usando el script de instalación automática compartido y qué pasos básicos debo seguir para asegurar la conexión en el lado del cliente? Detalle los requisitos de red a los que debo prestar atención durante el proceso de instalación y el método para ejecutarlo a través de Docker.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/masterdnsvpn/
