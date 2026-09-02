# Descarga vídeos de Internet en tu propio servidor

Reclip, desarrollado por Averygan, es una herramienta ligera y autohospedable para descargar vídeos de casi cualquier sitio web de Internet. Permite guardar archivos multimedia en tu dispositivo local a través de una interfaz web sencilla.

- ★ 7.951
- HTML
- GitHub Trending · 2026-09-02

## Qué aporta
- Descarga archivos de vídeo y audio de más de 1000 sitios, como YouTube e Instagram.
- Guarda los archivos descargados en formato de vídeo MP4 o audio MP3.
- Ofrece una interfaz sencilla y rápida que funciona a través del navegador web.

## Instalación
**Instalación estándar**

```
brew install yt-dlp ffmpeg    # or apt install ffmpeg && pip install yt-dlp
git clone https://github.com/averygan/reclip.git
cd reclip
./reclip.sh
```

**Instalación con Docker**

```
docker build -t reclip . && docker run -p 8899:8899 reclip
```


## Ejecución
**Acceso a la interfaz**

```
http://localhost:8899
```


## Si no programa
Quiero usar la herramienta Reclip para descargar enlaces de vídeo de Internet en formato MP4 o MP3 a mi dispositivo local. Para iniciar el proceso de descarga, debo pegar los enlaces en el cuadro de entrada, seleccionar el formato, hacer clic en el botón Fetch para cargar la información del vídeo y luego usar el botón Download. En este proceso, puedo realizar descargas masivas y ajustar la resolución del vídeo según mis preferencias.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/reclip/
