# Inteligencia artificial de código abierto en la atención sanitaria

OpenMed es una plataforma que reúne modelos de inteligencia artificial de código abierto y conjuntos de datos utilizados en la atención sanitaria. Desarrollada para aplicaciones orientadas a la medicina, esta biblioteca basada en Python tiene como objetivo estandarizar los procesos de procesamiento de datos de salud.

- ★ 5.715
- Python
- GitHub Trending · 2026-06-10

## Actualizaciones

- **27 de octubre de 2026:** Estrellas 5,457 → 5,715, última versión v3.1.0 (26 de octubre de 2026).
- **8 de octubre de 2026:** Estrellas 5,329 → 5,457, última versión v3.0.0 (7 de octubre de 2026).
- **16 de septiembre de 2026:** Estrellas 5,217 → 5,329, última versión v2.5.0 (15 de septiembre de 2026).
- **5 de septiembre de 2026:** Estrellas 5,076 → 5,217, última versión v2.3.0 (4 de septiembre de 2026).

## Qué aporta

- Extrae conocimientos médicos estructurados de textos clínicos.
- Anonimiza los datos de salud personales en el dispositivo.
- Ejecuta más de 1000 modelos médicos de IA sin conexión.

## Instalación

**Configuración básica**

```
pip install "openmed[hf]"
```

**Compatibilidad con Apple Silicon (MLX)**

```
pip install "openmed[mlx]"
```

## Ejecución

**Análisis simple con Python**

```
python -c "from openmed import extract_pii; print([(e.label, e.text) for e in extract_pii('Dr. Pedro Almeida, CPF: 123.456.789-09, email: pedro@hospital.pt', lang='pt').entities])"
```

## Si no programa

Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero analizar textos médicos usando la biblioteca OpenMed. Tengo Python instalado en mi dispositivo. En primer lugar, completé la instalación con el comando pip install "openmed[hf]". Ahora bien, ¿qué funciones debo llamar en mi código Python para analizar mis notas clínicas y detectar términos médicos o datos personales (PII) en ellas? Créame un bloque de código de muestra simple sobre la selección del modelo y la impresión de los resultados.

Repositorio: https://github.com/maziyarpanahi/openmed. Sigue las instrucciones oficiales del archivo README de este repositorio para la instalación y ejecución.

Antes de empezar, comprueba en qué sistema operativo estamos y si las herramientas necesarias (ej. Python, Node.js, Git, Docker) están instaladas. Instala las que falten paso a paso según este sistema.

Crea una carpeta nueva y vacía para trabajar. No toques ningún archivo fuera de esta carpeta y no borres nada. Antes de ejecutar cada comando, dime qué vas a hacer en una frase.

Dime qué debería ver en la pantalla al final de cada paso. Si ocurre un error, te pegaré el mensaje de error tal cual y lo solucionaremos juntos.

## Términos relacionados del glosario

- [Apple Silicon](https://trescout.com/es/dictionary/apple-silicon/)
- [Open Source](https://trescout.com/es/dictionary/open-source/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Está dirigido a profesionales de la salud y desarrolladores de software que desean realizar análisis orientados a la privacidad en su propio hardware sin enviar sus datos médicos a servicios en la nube.
- **Licencia:** Apache-2.0

## Enlaces

- [Repositorio en GitHub →](https://github.com/maziyarpanahi/openmed)
- [Leer en turco →](https://trescout.com/discover/openmed/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-06-10: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. El texto de presentación se preparó con IA a partir de la propia documentación del repositorio y esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/openmed/
