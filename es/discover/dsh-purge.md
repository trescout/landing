# Pruebas de seguridad para modelos de inteligencia artificial

YuJunZhiXue/dsh-purge es una herramienta de JavaScript destinada a eludir restricciones de seguridad (jailbreak) mediante el uso de instrucciones personalizables (prompts) para diferentes modelos de inteligencia artificial. El proyecto permite a los usuarios definir sus propios comandos para distintos modelos y se enfoca por defecto en modelos locales.

- ★ 10.161
- JavaScript
- GitHub Trending · 2026-10-19

## Actualizaciones

- **20 de octubre de 2026:** Estrellas 7,527 → 10,161, última versión v1.1.71 (11 de octubre de 2026).
- **19 de octubre de 2026:** Estrellas 7,496 → 7,527, última versión v1.1.71 (11 de octubre de 2026).

## Qué aporta

- Puede probar localmente las reglas de seguridad y auditoría en el entorno de ejecución de inteligencia artificial DeepSeek Harness.
- Puede examinar directamente las respuestas del modelo y los filtros del sistema definiendo instrucciones personalizadas para diferentes modelos.
- Puede gestionar los parches del sistema realizados a través de la interfaz de desarrollador y volver al estado anterior en cualquier momento.

## Instalación

**Clonar el repositorio en el directorio de complementos**

```
git clone https://github.com/YuJunZhiXue/dsh-purge.git "$DSH_HOME/plugins/dsh-purge"
```

**Cambiar al directorio del perfil correspondiente y dependenci**

```
cd "$DSH_HOME/profiles/web"   # 或 profiles/desktop
pnpm install
```

## Ejecución

**Validación de la sintaxis del código**

```
node --check lib/index.js
node --check lib/core.js
node --check lib/rewind.js
node --check lib/skills.js
node --check client.js
```

## Si no programa

Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero instalar y verificar el complemento dsh-purge para realizar una evaluación de seguridad en el entorno de ejecución de IA DeepSeek Harness. En primer lugar, ejecuta el comando git clone https://github.com/YuJunZhiXue/dsh-purge.git "$DSH_HOME/plugins/dsh-purge" para descargar el repositorio con el software de control de versiones Git. A continuación, completa el paso cd "$DSH_HOME/profiles/web" # 或 profiles/desktop\npnpm install para instalar las dependencias del perfil con el gestor de paquetes pnpm. Como último paso, ejecuta el comando node --check lib/index.js\nnode --check lib/core.js\nnode --check lib/rewind.js\nnode --check lib/skills.js\nnode --check client.js para verificar los archivos con el entorno de ejecución de JavaScript Node.js.

Repositorio: https://github.com/YuJunZhiXue/dsh-purge. Sigue las instrucciones oficiales del archivo README de este repositorio para la instalación y ejecución.

Antes de empezar, comprueba en qué sistema operativo estamos y si las herramientas necesarias (ej. Python, Node.js, Git, Docker) están instaladas. Instala las que falten paso a paso según este sistema.

Crea una carpeta nueva y vacía para trabajar. No toques ningún archivo fuera de esta carpeta y no borres nada. Antes de ejecutar cada comando, dime qué vas a hacer en una frase.

Dime qué debería ver en la pantalla al final de cada paso. Si ocurre un error, te pegaré el mensaje de error tal cual y lo solucionaremos juntos.

## Términos relacionados del glosario

- [Jailbreak](https://trescout.com/es/dictionary/jailbreak/)
- [Harness](https://trescout.com/es/dictionary/harness/)
- [Clone](https://trescout.com/es/dictionary/clone/)
- [AI Skills](https://trescout.com/es/dictionary/ai-skills/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Está dirigido a investigadores que desean auditar los límites de seguridad y los filtros del sistema de modelos de inteligencia artificial en su propio entorno local.
- **Licencia:** MIT

## Enlaces

- [Repositorio en GitHub →](https://github.com/YuJunZhiXue/dsh-purge)
- [Leer en turco →](https://trescout.com/discover/dsh-purge/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-10-19: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. El texto de presentación se preparó con IA a partir de la propia documentación del repositorio y esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/dsh-purge/
