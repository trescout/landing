# Gestionen juntos sus planes de viaje

TREK es una aplicación de planificación de viajes autohospedada que ofrece funciones como colaboración en tiempo real, mapas interactivos y gestión de presupuestos. Con soporte de aplicación web progresiva (PWA) e integración de inicio de sesión único (SSO), permite a los usuarios organizar sus procesos de viaje digitalmente.

- ★ 7.040
- GitHub Trending · 2026-06-26

## Qué aporta

- Crea rutas y planes de viaje diarios con arrastrar y soltar
- Seguimiento de los gastos del grupo y división por persona
- Gestión automática de viajes y presupuestos con integración de inteligencia artificial.

## Instalación

**Instalación rápida con Docker**

```
ENCRYPTION_KEY=$(openssl rand -hex 32) docker run -d -p 3000:3000 \
  -e ENCRYPTION_KEY=$ENCRYPTION_KEY \
  -v ./data:/app/data -v ./uploads:/app/uploads mauriceboe/trek
```

## Si no programa

Pegue esto en su agente (Claude Code · Codex · Antigravity)

Eres un asistente de viaje. Usando las herramientas MCP (Protocolo de contexto modelo) en TREK, cree un plan de viaje de 3 días a París para mí, ajuste mi presupuesto según los límites de gasto diario y cree una lista de equipaje para lo que necesito llevar conmigo.

Repositorio: https://github.com/mauriceboe/TREK. Sigue las instrucciones oficiales del archivo README de este repositorio para la instalación y ejecución.

Antes de empezar, comprueba en qué sistema operativo estamos y si las herramientas necesarias (ej. Python, Node.js, Git, Docker) están instaladas. Instala las que falten paso a paso según este sistema.

Crea una carpeta nueva y vacía para trabajar. No toques ningún archivo fuera de esta carpeta y no borres nada. Antes de ejecutar cada comando, dime qué vas a hacer en una frase.

Dime qué debería ver en la pantalla al final de cada paso. Si ocurre un error, te pegaré el mensaje de error tal cual y lo solucionaremos juntos.

## Términos relacionados del glosario

- [PWA](https://trescout.com/es/dictionary/pwa/)
- [SSO](https://trescout.com/es/dictionary/sso/)
- [Self-hosted](https://trescout.com/es/dictionary/self-hosted/)
- [Model Context Protocol](https://trescout.com/es/dictionary/model-context-protocol/)
- [Model Context Protocol](https://trescout.com/es/dictionary/model-context-protocol-mcp/)
- [Context](https://trescout.com/es/dictionary/context/)

- **Para quién es:** Es para viajeros que quieren organizar sus viajes digitalmente, realizar un seguimiento de sus gastos y tener control total sobre sus propios datos.
- **Licencia:** AGPL-3.0

## Enlaces

- [Repositorio en GitHub →](https://github.com/mauriceboe/TREK)
- [Leer en turco →](https://trescout.com/discover/trek/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-06-26: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. El texto de presentación se preparó con IA a partir de la propia documentación del repositorio y esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/trek/
