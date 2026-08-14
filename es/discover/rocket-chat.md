# Comunicación de equipo segura y personalizable

Rocket.Chat ofrece un sistema operativo de comunicaciones seguras diseñado para operaciones de misión crítica. La plataforma, desarrollada con el lenguaje TypeScript, tiene como objetivo centralizar los procesos internos de mensajería y colaboración.

- ★ 45.941
- TypeScript
- GitHub Trending · 2026-06-18

## Actualizar
- 7 de agosto de 2026: Estrella 45,919 → 45,941, última versión 8.7.0 (7 de agosto de 2026).
- 2 de agosto de 2026: Estrella 45,649 → 45,919, última versión 8.6.1 (10 de julio de 2026).

## Qué aporta
- Seguridad de datos con cifrado de extremo a extremo
- Posibilidad de alojar en su propio servidor
- Amplia integración y soporte de aplicaciones

## Instalación
**Linux · Paquete Snap (editor de Rocket.Chat)**

```
sudo snap install rocketchat-server
```

**Repositorio oficial de redacción de Docker**

```
git clone --depth 1 https://github.com/RocketChat/rocketchat-compose.git && cd rocketchat-compose && cp .env.example .env
```


## Ejecución
**Lanzar con Docker**

```
docker compose -f compose.database.yml -f compose.yml -f compose.nats.yml -f docker.yml up -d
```


## Cómo empezar
- Fuente oficial →
Para comenzar a instalar Rocket.Chat, puede revisar la Guía de implementación en la página de documentación oficial. Puede elegir uno de los métodos Docker, Podman o Kubernetes para alojar en su propio servidor, o considerar la opción Launchpad para un inicio más rápido. Para conocer todos los requisitos técnicos y los pasos de instalación detallados, visite el sitio de documentación oficial de Rocket.Chat.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/rocket-chat/
