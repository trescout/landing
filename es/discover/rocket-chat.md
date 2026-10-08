# Comunicación de equipo segura y personalizable

Rocket.Chat ofrece un sistema operativo de comunicaciones seguras diseñado para operaciones de misión crítica. La plataforma, desarrollada con el lenguaje TypeScript, tiene como objetivo centralizar los procesos internos de mensajería y colaboración.

- ★ 46.215
- TypeScript
- GitHub Trending · 2026-06-18

## Actualizaciones

- **6 de octubre de 2026:** Estrellas 46,098 → 46,215, última versión 8.9.0 (5 de octubre de 2026).
- **10 de septiembre de 2026:** Estrellas 46,064 → 46,098, última versión 8.8.1 (9 de septiembre de 2026).
- **2 de septiembre de 2026:** Estrellas 46,005 → 46,064, última versión 8.8.0 (1 de septiembre de 2026).
- **19 de agosto de 2026:** Estrellas 45,941 → 46,005, última versión 8.7.1 (19 de agosto de 2026).

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

- [Communications Operating System](https://trescout.com/es/dictionary/communications-operating-system/)
- [Deployment](https://trescout.com/es/dictionary/deployment/)

- **Para quién es:** Fue desarrollado para organizaciones que se preocupan por la privacidad de los datos y desean tener control total sobre su propia infraestructura.

## Enlaces

- [Repositorio en GitHub →](https://rocket.chat/)
- [Leer en turco →](https://trescout.com/discover/rocket-chat/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-06-18: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/rocket-chat/
