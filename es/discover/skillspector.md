# Capacidades seguras de IA

Desarrollado por NVIDIA, SkillSpector es una herramienta de escaneo que detecta vulnerabilidades y patrones maliciosos en los paquetes de habilidades de los agentes de inteligencia artificial. Este software basado en Python tiene como objetivo analizar los riesgos de seguridad encontrados durante el proceso de desarrollo de sistemas basados ​​en agentes.

- ★ 14.760
- Python
- GitHub Trending · 2026-06-12

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
Quiero realizar un control de seguridad de la habilidad de un agente de IA utilizando la herramienta SkillSpector. ¿Cómo uso el comando 'skillspector scan ./my-skill/' para buscar talentos en un directorio local y qué parámetros debo agregar al comando para guardar los resultados del escaneo en 'report.json' en formato JSON?

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/skillspector/
