# Guía para prevenir rechazos en la tienda de aplicaciones

mjmirza/app-store-compliance ofrece una guía abierta que incluye 117 patrones de rechazo diferentes y sus soluciones encontrados en los procesos de revisión de la tienda de aplicaciones. Su objetivo es simplificar los procesos de aprobación de App Store y Google Play para los desarrolladores con herramientas como el seguimiento de normativas legales y avisos de privacidad.

- ★ 3.296
- Shell
- GitHub Trending · 2026-11-20

## Actualizaciones

- **21 de noviembre de 2026:** Estrellas 2,032 → 3,296, última versión v2.4.0 (15 de noviembre de 2026).
- **20 de noviembre de 2026:** Estrellas 2,003 → 2,032, última versión v2.4.0 (15 de noviembre de 2026).

## Qué aporta

- Puedes detectar posibles riesgos de rechazo escaneando tu aplicación antes de enviarla para su aprobación a Apple y Google.
- Puedes asociar directamente los artículos de rechazo encontrados con las reglas de revisión oficiales y los métodos de solución.
- Puedes verificar los avisos de privacidad y los requisitos de la cuenta de prueba antes de subir la aplicación a la tienda.

## Instalación

**Añade la herramienta a las herramientas de desarrollo de inteligencia artificial**

```
git clone https://github.com/mjmirza/app-store-compliance ~/repositories/app-store-compliance
bash ~/repositories/app-store-compliance/scripts/install.sh --tool all
```

## Ejecución

**Escanear la carpeta de la aplicación**

```
git clone https://github.com/mjmirza/app-store-compliance ~/repositories/app-store-compliance
bash ~/repositories/app-store-compliance/agent-os/hooks/app-store-compliance-guard.sh "/path/to/your/app"
```

## Si no programa

Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero revisar mi proyecto de aplicación móvil según las normas de revisión de App Store y Google Play y detectar de antemano posibles vulnerabilidades que puedan causar un rechazo. Para descargar la herramienta y presentarla a las herramientas de inteligencia artificial, ejecuta el comando "git clone https://github.com/mjmirza/app-store-compliance ~/repositories/app-store-compliance
bash ~/repositories/app-store-compliance/scripts/install.sh --tool all" y, a continuación, para escanear la carpeta de tu aplicación móvil, sustituye la parte "/path/to/your/app" por la ruta de tu propia aplicación y ejecuta el comando "git clone https://github.com/mjmirza/app-store-compliance ~/repositories/app-store-compliance
bash ~/repositories/app-store-compliance/agent-os/hooks/app-store-compliance-guard.sh "/path/to/your/app"".

Repositorio: https://github.com/mjmirza/app-store-compliance. Sigue las instrucciones oficiales del archivo README de este repositorio para la instalación y ejecución.

Antes de empezar, comprueba en qué sistema operativo estamos y si las herramientas necesarias (ej. Python, Node.js, Git, Docker) están instaladas. Instala las que falten paso a paso según este sistema.

Crea una carpeta nueva y vacía para trabajar. No toques ningún archivo fuera de esta carpeta y no borres nada. Antes de ejecutar cada comando, dime qué vas a hacer en una frase.

Dime qué debería ver en la pantalla al final de cada paso. Si ocurre un error, te pegaré el mensaje de error tal cual y lo solucionaremos juntos.

## Términos relacionados del glosario

- [Hooks](https://trescout.com/es/dictionary/hooks/)
- [Shell](https://trescout.com/es/dictionary/shell/)
- [Clone](https://trescout.com/es/dictionary/clone/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Está dirigido a equipos que preparan sus aplicaciones móviles para la aprobación en Apple App Store o Google Play y desean evitar rechazos en las revisiones de las tiendas.

## Enlaces

- [Repositorio en GitHub →](https://github.com/mjmirza/app-store-compliance)
- [Leer en turco →](https://trescout.com/discover/app-store-compliance/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-11-20: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. El texto de presentación se preparó con IA a partir de la propia documentación del repositorio y esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/app-store-compliance/
