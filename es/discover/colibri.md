# Ejecute modelos de inteligencia artificial masivos localmente

Colibri es un motor basado en el lenguaje C que permite ejecutar modelos de mezcla de expertos (Mixture of Experts) a gran escala en computadoras locales con bajos requisitos de hardware. Al procesar capas de expertos mediante transmisión desde el disco, hace posible ejecutar modelos de IA de alta capacidad en hardware limitado.

- ★ 40.157
- C
- GitHub Trending · 2026-09-11

## Actualizaciones

- **7 de octubre de 2026:** Estrellas 39,698 → 40,157, última versión v2.0.0 (6 de octubre de 2026).
- **5 de octubre de 2026:** Estrellas 37,791 → 39,698, última versión v1.12.1 (24 de septiembre de 2026).
- **27 de septiembre de 2026:** Estrellas 36,260 → 37,791, última versión v1.12.1 (24 de septiembre de 2026).
- **19 de septiembre de 2026:** Estrellas 34,474 → 36,260, última versión v1.11.0 (13 de septiembre de 2026).

## Qué aporta

- Ejecuta modelos de alta capacidad en hardware limitado
- Gestiona VRAM, RAM y memoria de disco como una sola capa
- Proporciona eficiencia mediante el procesamiento de capas de expertos por transmisión

## Instalación

**Compilando desde el código fuente**

```
git clone https://github.com/JustVugg/colibri && cd colibri/c
./setup.sh                                # checks gcc/OpenMP, builds, self-tests
```

## Ejecución

**Iniciar interfaz de chat**

```
cd c
make deepseek-v4
python ./coli chat --model /path/to/DeepSeek-V4-Flash --ram 32
# also: coli run / coli serve / coli web
# Windows CUDA tier: make cuda-dsv4-dll CUDA_ARCH=portable  (+ make cuda-dsv4-dg-dll on RTX 50)
```

## Si no programa

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero ejecutar modelos de inteligencia artificial a gran escala en mi computadora local utilizando el motor Colibri. Ayúdame a configurarlo para utilizar mis recursos de hardware (VRAM, RAM y disco NVMe) de la manera más eficiente posible. Explica paso a paso cómo puedo optimizar y ejecutar modelos como GLM o DeepSeek según la capacidad de memoria de mi sistema.

## Términos relacionados del glosario

- [Mixture of Experts](https://trescout.com/es/dictionary/mixture-of-experts/)
- [VRAM](https://trescout.com/es/dictionary/vram/)
- [RAM](https://trescout.com/es/dictionary/ram/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Está destinado a investigadores y desarrolladores que deseen ejecutar modelos de lenguaje grandes en su propia computadora con recursos de hardware limitados.
- **Licencia:** Apache-2.0

## Enlaces

- [Repositorio en GitHub →](https://github.com/JustVugg/colibri)
- [Leer en turco →](https://trescout.com/discover/colibri/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-09-11: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/colibri/
