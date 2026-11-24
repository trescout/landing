# Capacidades seguras de IA

Desarrollado por NVIDIA, SkillSpector es una herramienta de escaneo que detecta vulnerabilidades y patrones maliciosos en los paquetes de habilidades de los agentes de inteligencia artificial. Este software basado en Python tiene como objetivo analizar los riesgos de seguridad encontrados durante el proceso de desarrollo de sistemas basados ​​en agentes.

- ★ 27.458
- Python
- GitHub Trending · 2026-06-12

## Actualizaciones

- **24 de noviembre de 2026:** Estrellas 26,489 → 27,458, última versión v2.13.7 (24 de noviembre de 2026).
- **17 de noviembre de 2026:** Estrellas 26,321 → 26,489, última versión v2.13.6 (16 de noviembre de 2026).
- **16 de noviembre de 2026:** Estrellas 25,734 → 26,321, última versión v2.13.5 (16 de noviembre de 2026).
- **13 de noviembre de 2026:** Estrellas 24,403 → 25,734, última versión v2.13.4 (4 de noviembre de 2026).

## Qué aporta

- La IA detecta vulnerabilidades y patrones maliciosos en las capacidades de los agentes.
- Ofrece escaneo de seguridad en dos etapas con análisis estático y evaluación de IA opcional.
- Permite verificar la seguridad de los agentes con puntuación de riesgos e informes detallados.

## Instalación

**Clonando el repositorio y creando un entorno virtual**

```
# Clone the repository
git clone https://github.com/NVIDIA/skillspector.git
cd skillspector

# Create and activate virtual environment
uv venv .venv && source .venv/bin/activate
# or: python3 -m venv .venv && source .venv/bin/activate
```

**Completa la configuración**

```
# Install for production use
make install

# Or install with development dependencies
make install-dev
```

## Ejecución

**Escanear directorio local**

```
skillspector scan ./my-skill/
```

**Escanea el repositorio de Git**

```
skillspector scan https://github.com/user/my-skill
```

## Si no programa

Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero realizar un control de seguridad de la habilidad de un agente de IA utilizando la herramienta SkillSpector. ¿Cómo uso el comando 'skillspector scan ./my-skill/' para buscar talentos en un directorio local y qué parámetros debo agregar al comando para guardar los resultados del escaneo en 'report.json' en formato JSON?

Repositorio: https://github.com/NVIDIA/SkillSpector. Sigue las instrucciones oficiales del archivo README de este repositorio para la instalación y ejecución.

Antes de empezar, comprueba en qué sistema operativo estamos y si las herramientas necesarias (ej. Python, Node.js, Git, Docker) están instaladas. Instala las que falten paso a paso según este sistema.

Crea una carpeta nueva y vacía para trabajar. No toques ningún archivo fuera de esta carpeta y no borres nada. Antes de ejecutar cada comando, dime qué vas a hacer en una frase.

Dime qué debería ver en la pantalla al final de cada paso. Si ocurre un error, te pegaré el mensaje de error tal cual y lo solucionaremos juntos.

## Términos relacionados del glosario

- [AI Skills](https://trescout.com/es/dictionary/ai-skills/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Es para desarrolladores de software que desarrollan agentes de IA y desean analizar los riesgos de seguridad de los paquetes de capacidades que utilizan.
- **Licencia:** Apache-2.0

## Enlaces

- [Repositorio en GitHub →](https://github.com/NVIDIA/SkillSpector)
- [Leer en turco →](https://trescout.com/discover/skillspector/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-06-12: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. El texto de presentación se preparó con IA a partir de la propia documentación del repositorio y esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/skillspector/
