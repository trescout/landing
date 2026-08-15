# Comunicación de equipo segura y personalizable

Rocket.Chat ofrece un sistema operativo de comunicaciones seguras diseñado para operaciones de misión crítica. La plataforma, desarrollada con el lenguaje TypeScript, tiene como objetivo centralizar los procesos internos de mensajería y colaboración.

- ★ 45.941
- TypeScript
- GitHub Trending · 2026-06-18

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

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/rocket-chat/
