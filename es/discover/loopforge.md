# Flujos de trabajo gestionables para tus agentes de codificación

Desarrollado por Tencent, LoopForge es una herramienta de flujo de trabajo autohospedada que se utiliza para gestionar los procesos de entrega de los agentes de codificación. Admite procesos de asistentes de codificación locales mediante la organización de software como CodeBuddy, Codex y Claude Code con scripts y mecanismos de aprobación humana.

- ★ 3.785
- Go
- GitHub Trending · 2026-11-15

## Actualizaciones

- **18 de noviembre de 2026:** Estrellas 2,090 → 3,785, última versión v0.4.0 (17 de noviembre de 2026).
- **16 de noviembre de 2026:** Estrellas 986 → 2,090, última versión v0.3.8 (12 de noviembre de 2026).
- **15 de noviembre de 2026:** Estrellas 983 → 986, última versión v0.3.8 (12 de noviembre de 2026).

## Qué aporta

- Ejecuta herramientas de codificación de inteligencia artificial de forma segura en entornos aislados (sandboxes).
- Garantiza entregas repetibles con procesos estándar y pasos de aprobación humana.
- Asigna tareas a roles desde la interfaz de chat o ejecuta flujos de trabajo paso a paso.

## Instalación

**Clonar el repositorio e iniciar el sistema**

```
git clone https://github.com/Tencent/LoopForge.git
cd LoopForge
./start.sh
```

**Iniciar con una fuente de imagen alternativa**

```
MIRROR=ghcr.nju.edu.cn ./start.sh
```

## Ejecución

**Instalar el asistente de codificación dentro del proyecto**

```
# Run inside your target project, e.g. for Claude Code
npx -y loopforge-cli@latest install claude
```

## Si no programa

Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero configurar el sistema LoopForge para poder gestionar los procesos de entrega de los agentes de codificación en mi propio servidor. Primero, clone el repositorio e inicie el sistema ejecutando la secuencia de comandos `git clone https://github.com/Tencent/LoopForge.git
cd LoopForge
./start.sh`. Si experimenta bloqueos durante la fase de descarga, utilice el comando `MIRROR=ghcr.nju.edu.cn ./start.sh` para extraer las imágenes del servidor alternativo y completar el inicio. Para instalar el asistente de codificación dentro de su proyecto de destino, ejecute el comando `# Run inside your target project, e.g. for Claude Code
npx -y loopforge-cli@latest install claude`.

Repositorio: https://github.com/Tencent/LoopForge. Sigue las instrucciones oficiales del archivo README de este repositorio para la instalación y ejecución.

Antes de empezar, comprueba en qué sistema operativo estamos y si las herramientas necesarias (ej. Python, Node.js, Git, Docker) están instaladas. Instala las que falten paso a paso según este sistema.

Crea una carpeta nueva y vacía para trabajar. No toques ningún archivo fuera de esta carpeta y no borres nada. Antes de ejecutar cada comando, dime qué vas a hacer en una frase.

Dime qué debería ver en la pantalla al final de cada paso. Si ocurre un error, te pegaré el mensaje de error tal cual y lo solucionaremos juntos.

## Términos relacionados del glosario

- [Self-hosted](https://trescout.com/es/dictionary/self-hosted/)
- [Clone](https://trescout.com/es/dictionary/clone/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Es adecuado para equipos que desean gestionar agentes de codificación impulsados por inteligencia artificial en su propia infraestructura con aprobación humana y flujos de trabajo estándar.

## Enlaces

- [Repositorio en GitHub →](https://github.com/Tencent/LoopForge)
- [Leer en turco →](https://trescout.com/discover/loopforge/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-11-15: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. El texto de presentación se preparó con IA a partir de la propia documentación del repositorio y esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/loopforge/
