# Núcleos de alto rendimiento para algunos Delta Atención

Desarrollado por Moonshot AI, FlashKDA ofrece núcleos de alto rendimiento para el mecanismo Some Delta Attention. Esta tecnología basada en CUDA tiene como objetivo acelerar los cálculos de atención en modelos de lenguaje grandes.

- ★ 1.043
- Cuda
- GitHub Trending · 2026-07-30

## Qué aporta
- Cálculos de atención acelerada basados en CUDA
- Trabajar de manera eficiente en modelos de lenguaje grandes
- Estructura del kernel optimizada con CUTLASS

## Instalación
**Configuración básica**

```
git clone https://github.com/MoonshotAI/FlashKDA.git flash-kda
cd flash-kda
git submodule update --init --recursive
pip install -v --no-build-isolation .
```

**Construido para todas las arquitecturas**

```
FLASH_KDA_CUDA_ARCHS=all pip install -v --no-build-isolation .
```


## Ejecución
**Usando FLA como backend**

```
pip install -U flash-linear-attention
```


## Si no programa
Quiero acelerar algunos cálculos de Delta Attention usando la herramienta FlashKDA. ¿Cómo puedo optimizar el mecanismo de atención de mi modelo utilizando la función chunk_kda en torch.inference_mode(), integrada con la biblioteca flash-linear-attention? Cree un ejemplo de aplicación, teniendo en cuenta los parámetros necesarios y los requisitos de hardware a los que debo prestar atención.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/flashkda/
