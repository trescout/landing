# Crea videos largos de manera coherente

Desarrollado por Meituan, LongCat-Video es un marco de trabajo (framework) de generación de video utilizado para crear videos largos de manera coherente. Esta herramienta permite producir contenidos de video de mayor duración y alta calidad manteniendo la coherencia de la imagen.

- ★ 8.892
- Python
- GitHub Trending · 2026-10-04

## Qué aporta
- Puedes generar nuevos contenidos de larga duración a partir de texto, imágenes o videos existentes.
- Puedes obtener resultados en videos de varios minutos de duración sin pérdida de calidad ni desviación de color.
- Puedes crear animaciones de personajes sincronizadas con el audio utilizando archivos de sonido.

## Instalación
**Descarga del repositorio de código en el ordenador**

```
git clone --single-branch --branch main https://github.com/meituan-longcat/LongCat-Video
cd LongCat-Video
```

**Descarga de los pesos del modelo**

```
pip install "huggingface_hub[cli]"
huggingface-cli download meituan-longcat/LongCat-Video --local-dir ./weights/LongCat-Video
huggingface-cli download meituan-longcat/LongCat-Video-Avatar --local-dir ./weights/LongCat-Video-Avatar
huggingface-cli download meituan-longcat/LongCat-Video-Avatar-1.5 --local-dir ./weights/LongCat-Video-Avatar-1.5
```


## Si no programa
Quiero instalar el proyecto LongCat-Video en mi sistema. Por favor, guíame paso a paso para descargar el código fuente con los comandos 'git clone --single-branch --branch main https://github.com/meituan-longcat/LongCat-Video' y 'cd LongCat-Video', y luego ejecutar los comandos de descarga con 'pip install "huggingface_hub[cli]"' para acceder a los archivos necesarios a través de la biblioteca de modelos Hugging Face.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/longcat-video/
