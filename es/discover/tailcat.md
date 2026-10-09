# Túneles Netcat seguros en redes Tailscale

Tailcat aporta la funcionalidad clásica de netcat a la capa de malla de Tailscale VPN, proporcionando una transferencia de datos segura sin necesidad de un plano de control o un puerto abierto.

- ★ 7.746
- Go
- GitHub Trending · 2026-08-28

## Actualizaciones

- **27 de septiembre de 2026:** Estrellas 2,435 → 7,746, última versión v0.7.0 (20 de septiembre de 2026).

## Qué aporta

- Reenvío de puerto cero (Port Forwarding): Comunicación directa entre dispositivos detrás de NAT o firewall restringida sin abrir puertos abiertos.
- Cifrado WireGuard de extremo a extremo: cifre automáticamente todas las transferencias TCP y de datos sin procesar con autenticación Tailscale y WireGuard.
- Biblioteca tsnet integrada: funciona como un nodo Tailscale independiente sin la necesidad de instalar un cliente Tailscale a nivel del sistema operativo.
- Transferencia rápida de archivos y canales: fluya comandos tar, gzip o dd entre máquinas a través de canales estándar de entrada/salida (stdin/stdout).
- Depuración y diagnóstico de red: prueba de accesibilidad de puertos entre microservicios y máquinas remotas con comandos prácticos como el netcat tradicional.

## Instalación

**Instalación directa con Go**

```
go install tailscale.com/cmd/tailcat@latest
```

## Ejecución

**Iniciar el modo de escucha y conectar un cliente**

```
# Sunucu düğümde dinle:
tailcat -l 8080
# İstemci düğümden bağlan:
tailcat hedef-node 8080
```

## Arquitectura técnica y principio de funcionamiento

- Red de área de usuario tsnet: crea una sesión VPN directamente dentro de la aplicación sin necesidad de privilegios de root o un dispositivo TUN virtual.
- Resolución de nodo MagicDNS: capacidad de conectarse instantáneamente con nombres de máquinas de Tailscale como "nodo de servidor" en lugar de direcciones IP.
- Soporte de retransmisión DERP: reanudación de la transferencia de datos a través de retransmisiones DERP de Tailscale en redes extremadamente restrictivas donde no es posible la conexión P2P directa.

## Túneles de red seguros y escenarios de extremo a extremo

- Transferencia de archivos rápida y segura: transferencia sin configuración con `tailcat -l 9000 > backup.tar.gz` en el receptor y `tailcat destinación 9000 \< backup.tar.gz` en el remitente.
- Servicio compartido temporal HTTP: abrir el servidor web local en desarrollo a sus colegas en la red tailnet con un solo comando.
- Acceso a dispositivos integrados y Raspberry Pi: envíe datos de forma remota y segura a dispositivos IoT restringidos con IP dinámica y en la red doméstica.

## Si no programa

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero configurar un túnel de transferencia de archivos cifrados entre dos servidores diferentes a través de la red de malla de Tailscale usando la herramienta Tailcat. ¿Puede explicar cómo iniciar el oyente en el lado del servidor, cómo transmitir el archivo tar desde la salida estándar en el lado del cliente y cómo administrar la autenticación tsnet?

## Preguntas frecuentes

- ¿Necesito un cliente Tailscale instalado en mi máquina? No. Tailcat tiene el motor tsnet integrado; Lanza su propio enlace Tailscale como binario independiente.
- ¿Está realmente cifrado el tráfico de un extremo a otro? Sí. Tailcat utiliza el protocolo WireGuard en el núcleo de la red Tailscale; los datos se cifran directamente entre dispositivos.
- ¿Admite tráfico UDP? Tailcat está optimizado principalmente para flujos TCP y túneles de sockets; Asegura las capacidades TCP del netcat clásico.
- ¿Cómo autenticarse para la conexión? Cuando Tailcat se ejecuta por primera vez, proporciona un enlace de inicio de sesión de Tailscale en la terminal o se autentica automáticamente con la variable de entorno TAILSCALE_AUTHKEY.

## Términos relacionados del glosario

- [Root](https://trescout.com/es/dictionary/root/)
- [IoT](https://trescout.com/es/dictionary/iot/)
- [VPN](https://trescout.com/es/dictionary/vpn/)
- [Mesh](https://trescout.com/es/dictionary/mesh/)
- [Open Source](https://trescout.com/es/dictionary/open-source/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Administradores de sistemas, ingenieros de DevOps, expertos en redes y arquitectos de la nube.
- **Licencia:** BSD 3-Clause (Esnek açık kaynak lisansı)
- **Marco:** Biblioteca tsnet Go & Tailscale
- **Plataformas:** Linux, Mac OS, Windows

## Enlaces

- [Repositorio en GitHub →](https://github.com/tailscale/tailcat)
- [Leer en turco →](https://trescout.com/discover/tailcat/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-08-28: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/tailcat/
