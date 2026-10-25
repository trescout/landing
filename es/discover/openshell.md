# Entorno seguro para agentes de inteligencia artificial

Desarrollado por NVIDIA, OpenShell ofrece un entorno de tiempo de ejecución (runtime) seguro y centrado en la privacidad para agentes de inteligencia artificial autónomos. Escrita en el lenguaje Rust, esta infraestructura tiene como objetivo aislar el acceso de los agentes a los recursos del sistema para crear un espacio de ejecución seguro.

- ★ 19.581
- Rust
- GitHub Trending · 2026-09-29

## Actualizaciones

- **25 de octubre de 2026:** Estrellas 18,169 → 19,581, última versión v0.1.5 (20 de octubre de 2026).
- **23 de octubre de 2026:** Estrellas 16,850 → 18,169, última versión v0.1.5 (20 de octubre de 2026).
- **21 de octubre de 2026:** Estrellas 16,170 → 16,850, última versión v0.1.5 (20 de octubre de 2026).
- **14 de octubre de 2026:** Estrellas 15,577 → 16,170, última versión v0.1.4 (13 de octubre de 2026).

## Qué aporta

- Ejecuta agentes de inteligencia artificial en un entorno sandbox aislado
- Limita el acceso a archivos y redes mediante reglas
- Mejora la seguridad ocultando las credenciales

## Instalación

**Instalar herramienta y crear entorno de demostración**

```
curl -LsSf https://raw.githubusercontent.com/NVIDIA/OpenShell/main/install.sh | sh
openshell sandbox create --name demo
```

## Ejecución

**Agregar capacidades**

```
npx skills add NVIDIA/OpenShell
```

## Si no programa

Pegue esto en su agente (Claude Code · Codex · Antigravity)

Para instalar y probar la herramienta OpenShell, puedes usar los siguientes comandos: curl -LsSf https://raw.githubusercontent.com/NVIDIA/OpenShell/main/install.sh | sh y luego crear un entorno de demostración ejecutando el comando openshell sandbox create --name demo.

Repositorio: https://github.com/NVIDIA/OpenShell. Sigue las instrucciones oficiales del archivo README de este repositorio para la instalación y ejecución.

Antes de empezar, comprueba en qué sistema operativo estamos y si las herramientas necesarias (ej. Python, Node.js, Git, Docker) están instaladas. Instala las que falten paso a paso según este sistema.

Crea una carpeta nueva y vacía para trabajar. No toques ningún archivo fuera de esta carpeta y no borres nada. Antes de ejecutar cada comando, dime qué vas a hacer en una frase.

Dime qué debería ver en la pantalla al final de cada paso. Si ocurre un error, te pegaré el mensaje de error tal cual y lo solucionaremos juntos.

## Términos relacionados del glosario

- [Sandbox](https://trescout.com/es/dictionary/sandbox/)
- [Runtime](https://trescout.com/es/dictionary/runtime/)
- [Rust](https://trescout.com/es/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Desarrolladores que desean ejecutar agentes de inteligencia artificial en un entorno seguro y aislado sin otorgarles acceso total a todos los recursos del sistema.
- **Licencia:** Apache-2.0

## Enlaces

- [Repositorio en GitHub →](https://github.com/NVIDIA/OpenShell)
- [Leer en turco →](https://trescout.com/discover/openshell/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-09-29: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. El texto de presentación se preparó con IA a partir de la propia documentación del repositorio y esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/openshell/
