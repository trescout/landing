# Cálculo matricial rápido para inteligencia artificial

DeepGEMM, desarrollado por DeepSeek, es una biblioteca de subprogramas de álgebra lineal básica (BLAS) de código abierto que acelera las operaciones de multiplicación de matrices en unidades de procesamiento gráfico (GPU). El software ofrece núcleos (kernels) optimizados para modelos de inteligencia artificial que requieren computación de alto rendimiento.

- ★ 8.528
- Cuda
- GitHub Trending · 2026-10-06

## Actualizaciones

- **6 de octubre de 2026:** Estrellas 8,522 → 8,528, última versión v2.1.1.post3 (15 de octubre de 2025).

## Qué aporta

- Reduce los tiempos de ejecución de los modelos de lenguaje grandes al acelerar las multiplicaciones de matrices.
- Compila automáticamente los núcleos en tiempo de ejecución sin esperar a la compilación de CUDA durante la instalación.
- Reduce las pérdidas de comunicación de la tarjeta gráfica al combinar diferentes modelos de expertos en una sola operación.

## Instalación

**Clonar el repositorio y el entorno de desarrollo h**

```
# Submodule must be cloned
git clone --recursive git@github.com:deepseek-ai/DeepGEMM.git
cd DeepGEMM

# Link some essential includes and build the C++ extension
cat develop.sh
./develop.sh
```

**Instalación de la biblioteca**

```
cat install.sh
./install.sh
```

## Si no programa

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero instalar la biblioteca DeepGEMM en mi hardware con arquitectura NVIDIA SM90 o SM100. Primero, ejecute los comandos '# Submodule must be cloned\ngit clone --recursive git@github.com:deepseek-ai/DeepGEMM.git\ncd DeepGEMM\n\n# Link some essential includes and build the C++ extension\ncat develop.sh\n./develop.sh' para clonar el repositorio con sus submódulos y preparar el entorno de desarrollo. Luego, aplique el comando 'cat install.sh\n./install.sh' para completar la instalación y deje la biblioteca lista para usar en el entorno de Python con el comando 'import deep_gemm'.

## Términos relacionados del glosario

- [BLAS](https://trescout.com/es/dictionary/blas/)
- [Kernels](https://trescout.com/es/dictionary/kernels/)
- [Clone](https://trescout.com/es/dictionary/clone/)
- [GPU](https://trescout.com/es/dictionary/gpu/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Está destinado a desarrolladores e investigadores que desean ejecutar grandes modelos de inteligencia artificial con el máximo rendimiento en unidades de procesamiento gráfico modernas de NVIDIA.
- **Licencia:** MIT

## Enlaces

- [Repositorio en GitHub →](https://github.com/deepseek-ai/DeepGEMM)
- [Leer en turco →](https://trescout.com/discover/deepgemm/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-10-06: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/deepgemm/
