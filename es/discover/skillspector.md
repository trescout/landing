# Capacidades seguras de IA

Desarrollado por NVIDIA, SkillSpector es una herramienta de escaneo que detecta vulnerabilidades y patrones maliciosos en los paquetes de habilidades de los agentes de inteligencia artificial. Este software basado en Python tiene como objetivo analizar los riesgos de seguridad encontrados durante el proceso de desarrollo de sistemas basados ​​en agentes.

- ★ 19.418
- Python
- GitHub Trending · 2026-06-12

## Actualizaciones

- **5 de octubre de 2026:** Estrellas 18,381 → 19,418, última versión v2.12.0 (23 de septiembre de 2026).
- **27 de septiembre de 2026:** Estrellas 16,828 → 18,381, última versión v2.12.0 (23 de septiembre de 2026).
- **10 de septiembre de 2026:** Estrellas 16,595 → 16,828, última versión v2.11.2 (9 de septiembre de 2026).
- **8 de septiembre de 2026:** Estrellas 16,471 → 16,595, última versión v2.11.1 (7 de septiembre de 2026).

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

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero realizar un control de seguridad de la habilidad de un agente de IA utilizando la herramienta SkillSpector. ¿Cómo uso el comando 'skillspector scan ./my-skill/' para buscar talentos en un directorio local y qué parámetros debo agregar al comando para guardar los resultados del escaneo en 'report.json' en formato JSON?

## Términos relacionados del glosario

- [AI Skills](https://trescout.com/es/dictionary/ai-skills/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Es para desarrolladores de software que desarrollan agentes de IA y desean analizar los riesgos de seguridad de los paquetes de capacidades que utilizan.
- **Licencia:** Apache-2.0

## Enlaces

- [Repositorio en GitHub →](https://github.com/NVIDIA/SkillSpector)
- [Leer en turco →](https://trescout.com/discover/skillspector/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-06-12: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/skillspector/
