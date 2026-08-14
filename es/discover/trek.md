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
Eres un asistente de viaje. Usando las herramientas MCP (Protocolo de contexto modelo) en TREK, cree un plan de viaje de 3 días a París para mí, ajuste mi presupuesto según los límites de gasto diario y cree una lista de equipaje para lo que necesito llevar conmigo.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/trek/
