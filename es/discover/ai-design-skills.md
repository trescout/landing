# Reglas de diseño listas para asistentes de código

elayadesign/ai-design-skills ofrece una colección de habilidades de diseño formada por archivos de reglas en markdown que las herramientas de programación con IA (Claude Code, Cursor, Codex, Windsurf) pueden leer. Este proyecto proporciona un recurso a modo de guía orientado a herramientas impulsadas por IA para estandarizar los procesos de diseño.

- ★ 12.378
- GitHub Trending · 2026-10-28

## Actualizaciones

- **30 de octubre de 2026:** Estrellas 11,349 → 12,378.
- **29 de octubre de 2026:** Estrellas 9,826 → 11,349.

## Qué aporta

- Permite que las herramientas de IA generen desde cero páginas de destino coherentes y sistemas visuales
- Reúne estándares de diseño como tipografía, color, espaciado y animación en un solo archivo
- Hace posible que los asistentes de código escriban interfaces más consistentes con reglas específicas para el proyecto

## Instalación

**Añadir a la carpeta de reglas de Claude Code**

```
mkdir -p .claude/skills
git clone https://github.com/elayadesign/ai-design-skills.git /tmp/ai-design-skills
cp -r /tmp/ai-design-skills/skills/<skill-name> .claude/skills/
```

**Instalar para Cursor, el editor de código con IA**

```
mkdir -p .cursor/rules
curl -o .cursor/rules/<skill-name>.md \
  https://raw.githubusercontent.com/elayadesign/ai-design-skills/main/skills/<skill-name>/SKILL.md
```

## Si no programa

Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero enseñarle las reglas de diseño a mi herramienta de codificación de inteligencia artificial. Para descargar el archivo de reglas necesario para el editor de código Cursor, ejecuta los siguientes comandos en orden: `mkdirp .cursor/rules` y luego `curl -o .cursor/rules/\<skill-name>.md \ https://raw.githubusercontent.com/elayadesign/ai-design-skills/main/skills/\<skill-name>/SKILL.md`. No olvides reemplazar la parte `\<skill-name>` aquí con `landing-page-design`, que es la regla que queremos descargar.

Repositorio: https://github.com/elayadesign/ai-design-skills. Sigue las instrucciones oficiales del archivo README de este repositorio para la instalación y ejecución.

Antes de empezar, comprueba en qué sistema operativo estamos y si las herramientas necesarias (ej. Python, Node.js, Git, Docker) están instaladas. Instala las que falten paso a paso según este sistema.

Crea una carpeta nueva y vacía para trabajar. No toques ningún archivo fuera de esta carpeta y no borres nada. Antes de ejecutar cada comando, dime qué vas a hacer en una frase.

Dime qué debería ver en la pantalla al final de cada paso. Si ocurre un error, te pegaré el mensaje de error tal cual y lo solucionaremos juntos.

## Términos relacionados del glosario

- [Skill](https://trescout.com/es/dictionary/skill/)
- [Markdown](https://trescout.com/es/dictionary/markdown/)
- [AI Skills](https://trescout.com/es/dictionary/ai-skills/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Está destinado a propietarios de productos y desarrolladores que desean crear interfaces web estéticas y coherentes con editores de código impulsados por inteligencia artificial.
- **Licencia:** MIT

## Enlaces

- [Repositorio en GitHub →](https://github.com/elayadesign/ai-design-skills)
- [Leer en turco →](https://trescout.com/discover/ai-design-skills/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-10-28: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. El texto de presentación se preparó con IA a partir de la propia documentación del repositorio y esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/ai-design-skills/
