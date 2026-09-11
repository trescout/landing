# Ejecute modelos de inteligencia artificial masivos localmente

Colibri es un motor basado en el lenguaje C que permite ejecutar modelos de mezcla de expertos (Mixture of Experts) a gran escala en computadoras locales con bajos requisitos de hardware. Al procesar capas de expertos mediante transmisión desde el disco, hace posible ejecutar modelos de IA de alta capacidad en hardware limitado.

- ★ 27.610
- C
- GitHub Trending · 2026-09-11

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
Quiero ejecutar modelos de inteligencia artificial a gran escala en mi computadora local utilizando el motor Colibri. Ayúdame a configurarlo para utilizar mis recursos de hardware (VRAM, RAM y disco NVMe) de la manera más eficiente posible. Explica paso a paso cómo puedo optimizar y ejecutar modelos como GLM o DeepSeek según la capacidad de memoria de mi sistema.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/colibri/
