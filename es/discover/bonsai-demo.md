# Modelos de IA en dispositivo local

El proyecto de demostración Bonsai proporciona un conjunto de herramientas diseñado para simplificar los procesos de implementación de modelos de aprendizaje automático. El software ayuda a los desarrolladores a optimizar los procesos de sus aplicaciones al convertir arquitecturas de modelos complejos en flujos de trabajo manejables.

- ★ 2.706
- Shell
- GitHub Trending · 2026-07-17

## Actualizaciones

- **19 de septiembre de 2026:** Estrellas 1,587 → 2,706.

## Qué aporta

- Ejecuta modelos de alto rendimiento localmente con bajo uso de memoria.
- Ofrece funciones avanzadas como procesamiento visual y transporte compartido.
- Proporciona amplia compatibilidad con diferentes arquitecturas de hardware.

## Instalación

**Instalación de macOS y Linux**

```
git clone https://github.com/PrismML-Eng/Bonsai-demo.git
cd Bonsai-demo

# (Optional) Choose a model size: 27B (default), 8B, 4B, or 1.7B
export BONSAI_MODEL=27B

# Set your HuggingFace token (only required for 27B while its repos are private)
export BONSAI_TOKEN="hf_your_token_here"

# One command does everything: installs deps, downloads models + binaries
./setup.sh
```

## Ejecución

**Iniciando el servidor local**

```
./scripts/start_llama_server.sh    # http://localhost:8080

# Serve a different model size
BONSAI_MODEL=4B ./scripts/start_llama_server.sh
```

## Si no programa

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero ejecutar modelos de IA en mi dispositivo local usando el proyecto bonsai-demo. Después de clonar el repositorio git requerido para la instalación, necesito definir la información de mi token HuggingFace y descargar las dependencias y modelos con el comando ./setup.sh. Luego, usando el comando ./scripts/start_llama_server.sh, puedo activar el servidor local e interactuar con la IA a través del puerto 8080 a través de mi navegador.

## Términos relacionados del glosario

- [Machine Learning](https://trescout.com/es/dictionary/machine-learning/)
- [Shell](https://trescout.com/es/dictionary/shell/)
- [Token](https://trescout.com/es/dictionary/token/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Es adecuado para desarrolladores que desean ejecutar modelos de IA de alto rendimiento en su hardware nativo.
- **Licencia:** Apache-2.0

## Enlaces

- [Repositorio en GitHub →](https://github.com/PrismML-Eng/Bonsai-demo)
- [Leer en turco →](https://trescout.com/discover/bonsai-demo/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-07-17: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/bonsai-demo/
