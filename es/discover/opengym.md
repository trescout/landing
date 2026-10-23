# Software de seguimiento de entrenamiento que se ejecuta en tu propio servidor

OpenGym es una herramienta de gestión de gimnasio de código abierto diseñada para planificar rutinas de entrenamiento y realizar un seguimiento de los ejercicios con peso corporal. Al permitir a los usuarios alojar sus datos en sus propios servidores, este software admite la importación de datos desde aplicaciones de fitness populares (Strong, Hevy).

- ★ 15.063
- JavaScript
- GitHub Trending · 2026-10-05

## Actualizaciones

- **23 de octubre de 2026:** Estrellas 14,645 → 15,063, última versión v1.4.2 (23 de octubre de 2026).
- **22 de octubre de 2026:** Estrellas 13,304 → 14,645, última versión v1.4.1 (10 de octubre de 2026).
- **18 de octubre de 2026:** Estrellas 12,021 → 13,304, última versión v1.4.1 (10 de octubre de 2026).
- **15 de octubre de 2026:** Estrellas 10,912 → 12,021, última versión v1.4.1 (10 de octubre de 2026).

## Qué aporta

- Puedes almacenar tus datos de entrenamiento en un espacio seguro que tú controlas, en lugar de en los servidores de empresas de terceros.
- Puedes importar fácilmente tus datos de ejercicio anteriores desde aplicaciones de fitness populares como Strong y Hevy.
- Puedes planificar y realizar un seguimiento de tus entrenamientos desde tu teléfono o computadora incluso cuando no tengas conexión a internet.

## Instalación

**Con la plataforma de gestión de contenedores Docker, c**

```
git clone https://github.com/DuarteSantos8/openGym
cd openGym
cp .env.example .env
docker compose pull      # prebuilt images, amd64 + arm64 (skip this to build from source)
docker compose up -d
```

## Si no programa

Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero instalar el software de seguimiento de entrenamiento openGym en la plataforma de gestión de contenedores Docker. ¿Podrías explicarme paso a paso los pasos de instalación que comienzan con el comando 'git clone https://github.com/DuarteSantos8/openGym', cómo configurar el archivo de variables de entorno '.env' y cómo acceder a la aplicación desde el navegador una vez completada la instalación?

Repositorio: https://github.com/DuarteSantos8/openGym. Sigue las instrucciones oficiales del archivo README de este repositorio para la instalación y ejecución.

Antes de empezar, comprueba en qué sistema operativo estamos y si las herramientas necesarias (ej. Python, Node.js, Git, Docker) están instaladas. Instala las que falten paso a paso según este sistema.

Crea una carpeta nueva y vacía para trabajar. No toques ningún archivo fuera de esta carpeta y no borres nada. Antes de ejecutar cada comando, dime qué vas a hacer en una frase.

Si se necesita una clave API, no me pidas que la escriba en el chat. Muéstrame cómo añadirla al archivo .env y asegúrate de que este archivo no se suba a Git.

Dime qué debería ver en la pantalla al final de cada paso. Si ocurre un error, te pegaré el mensaje de error tal cual y lo solucionaremos juntos.

## Términos relacionados del glosario

- [Clone](https://trescout.com/es/dictionary/clone/)
- [API](https://trescout.com/es/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Está dirigido a entusiastas del deporte que valoran la privacidad de sus datos de entrenamiento y desean realizar un seguimiento gratuito de sus rutinas de gimnasio en su propio servidor.
- **Licencia:** AGPL-3.0

## Enlaces

- [Repositorio en GitHub →](https://github.com/DuarteSantos8/openGym)
- [Leer en turco →](https://trescout.com/discover/opengym/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-10-05: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. El texto de presentación se preparó con IA a partir de la propia documentación del repositorio y esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/opengym/
