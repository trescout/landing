# Comunicación de equipo segura y personalizable

Rocket.Chat ofrece un sistema operativo de comunicaciones seguras diseñado para operaciones de misión crítica. La plataforma, desarrollada con el lenguaje TypeScript, tiene como objetivo centralizar los procesos internos de mensajería y colaboración.

- ★ 46.005
- TypeScript
- GitHub Trending · 2026-06-18

## Qué aporta
- Seguridad de datos con cifrado de extremo a extremo
- Posibilidad de alojar en su propio servidor
- Amplia integración y soporte de aplicaciones

## Instalación
**Clonar repositorio oficial de compose**

```
git clone --depth 1 https://github.com/RocketChat/rocketchat-compose.git
```

**Crear archivo de entorno**

```
cd rocketchat-compose
cp .env.example .env
```

**Iniciar servicios MongoDB y Rocket.Chat**

```
docker compose -f compose.database.yml -f compose.yml -f compose.nats.yml up -d
```


## Ejecución
**Acceder a la interfaz local**

```
http://localhost:3000
```


## Cómo empezar
- Fuente oficial →

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/rocket-chat/
