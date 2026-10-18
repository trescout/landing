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

Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero instalar el proyecto LongCat-Video en mi sistema. Por favor, guíame paso a paso para descargar el código fuente con los comandos 'git clone --single-branch --branch main https://github.com/meituan-longcat/LongCat-Video' y 'cd LongCat-Video', y luego ejecutar los comandos de descarga con 'pip install "huggingface_hub[cli]"' para acceder a los archivos necesarios a través de la biblioteca de modelos Hugging Face.

Repositorio: https://github.com/meituan-longcat/LongCat-Video. Sigue las instrucciones oficiales del archivo README de este repositorio para la instalación y ejecución.

Antes de empezar, comprueba en qué sistema operativo estamos y si las herramientas necesarias (ej. Python, Node.js, Git, Docker) están instaladas. Instala las que falten paso a paso según este sistema.

Crea una carpeta nueva y vacía para trabajar. No toques ningún archivo fuera de esta carpeta y no borres nada. Antes de ejecutar cada comando, dime qué vas a hacer en una frase.

Dime qué debería ver en la pantalla al final de cada paso. Si ocurre un error, te pegaré el mensaje de error tal cual y lo solucionaremos juntos.

## Términos relacionados del glosario

- [Clone](https://trescout.com/es/dictionary/clone/)
- [Framework](https://trescout.com/es/dictionary/framework/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Está dirigido a desarrolladores y creadores de contenido que desean generar videos de alta calidad y larga duración a partir de entradas de texto, imágenes o audio con la ayuda de la inteligencia artificial.
- **Licencia:** MIT

## Enlaces

- [Repositorio en GitHub →](https://github.com/meituan-longcat/LongCat-Video)
- [Leer en turco →](https://trescout.com/discover/longcat-video/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-10-04: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. El texto de presentación se preparó con IA a partir de la propia documentación del repositorio y esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/longcat-video/
