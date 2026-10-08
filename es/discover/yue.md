# Composición editable con inteligencia artificial en la producción musical

YuE es un sistema de generación musical equipado con capacidades como planificación simbólica y generación de covers de disparo cero (zero-shot). Este modelo de IA, que automatiza los procesos de edición musical, le permite gestionar composiciones complejas mediante flujos de trabajo agénticos.

- ★ 10.749
- Python
- GitHub Trending · 2026-09-13

## Actualizaciones

- **3 de octubre de 2026:** Estrellas 9,749 → 10,749, última versión yue2-v0.1.6 (9 de septiembre de 2026).
- **19 de septiembre de 2026:** Estrellas 8,744 → 9,749, última versión yue2-v0.1.6 (9 de septiembre de 2026).
- **15 de septiembre de 2026:** Estrellas 7,463 → 8,744, última versión yue2-v0.1.6 (9 de septiembre de 2026).
- **13 de septiembre de 2026:** Estrellas 7,459 → 7,463, última versión yue2-v0.1.6 (9 de septiembre de 2026).

## Qué aporta

- Generación de planes de melodía y acordes a partir de letras y entradas de estilo
- Capacidad de editar notas musicales antes de convertirlas en archivos de audio
- Reinterpretación y edición de canciones existentes en diferentes estilos

## Instalación

**Descarga e instalación del proyecto**

```
git clone https://github.com/multimodal-art-projection/YuE.git
cd YuE
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install .
python examples/generate.py --output outputs/first-song
```

## Ejecución

**Creación de canciones con notas editadas**

```
python examples/generate.py --request examples/song.json \
  --abc-file edited.abc --cot full --output outputs/edited
```

## Si no programa

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero crear una canción usando YuE2. Por favor, prepárame un plan de melodía y acordes editable basado en la letra y el estilo musical que deseo. Luego, utiliza este plan para producir una grabación completa de la canción que incluya voces y acompañamiento instrumental. Si tengo un archivo de notación, permíteme usarlo para realizar ediciones.

## Términos relacionados del glosario

- [Zero-shot](https://trescout.com/es/dictionary/zero-shot/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Es adecuado para músicos y creadores de contenido que deseen planificar sus composiciones musicales con la ayuda de inteligencia artificial, realizar cambios en las partituras y producir canciones originales.
- **Licencia:** Apache-2.0

## Enlaces

- [Repositorio en GitHub →](https://github.com/multimodal-art-projection/YuE)
- [Leer en turco →](https://trescout.com/discover/yue/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-09-13: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/yue/
