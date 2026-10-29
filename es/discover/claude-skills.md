# Aportar experiencia a los agentes de codificación de IA

Desarrollada para Claude Code y varios agentes de codificación, esta biblioteca ofrece más de 330 paquetes de habilidades y más de 70 comandos especiales en diferentes campos, desde ingeniería hasta marketing. Este conjunto de herramientas basado en Python proporciona scripts personalizables para estandarizar los flujos de trabajo basados ​​en IA y aumentar la productividad.

- ★ 28.939
- Python
- GitHub Trending · 2026-07-05

## Actualizaciones

- **29 de octubre de 2026:** Estrellas 28,795 → 28,939, última versión v2.14.3 (29 de octubre de 2026).
- **27 de octubre de 2026:** Estrellas 28,584 → 28,795, última versión v2.14.2 (26 de octubre de 2026).
- **23 de octubre de 2026:** Estrellas 28,525 → 28,584, última versión v2.14.1 (23 de octubre de 2026).
- **22 de octubre de 2026:** Estrellas 28,485 → 28,525, última versión v2.14.0 (21 de octubre de 2026).

## Qué aporta

- Más de 350 paquetes de habilidades ya preparados
- Amplia experiencia desde ingeniería hasta marketing.
- Compatible con 13 herramientas de codificación diferentes

## Instalación

**Instalación de la CLI de Géminis**

```
# Clone the repository
git clone https://github.com/alirezarezvani/claude-skills.git
cd claude-skills

# Run the setup script
./scripts/gemini-install.sh

# Start using skills
> activate_skill(name="senior-architect")
```

**Instalación de OpenClaw**

```
bash <(curl -s https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/scripts/openclaw-install.sh)
```

## Ejecución

**Convertir capacidades para el cursor**

```
# 1. Convert all skills to all tools (takes ~15 seconds)
./scripts/convert.sh --tool all

# 2. Install into your project (with confirmation)
./scripts/install.sh --tool cursor --target /path/to/project

# Or use --force to skip confirmation:
./scripts/install.sh --tool aider --target . --force

# 3. Verify
find .cursor/rules -name "*.mdc" | wc -l  # Should show 346
```

## Si no programa

Pegue esto en su agente (Claude Code · Codex · Antigravity)

Active los paquetes de habilidades en esta biblioteca para Claude Code o el agente de codificación que utilice. Estandarice mi flujo de trabajo y aumente mi productividad utilizando scripts especializados en campos como ingeniería, marketing o consultoría de nivel C. Integrar las capacidades específicas que necesito (por ejemplo, auditoría de seguridad o desarrollo de productos) en mi proyecto.

Repositorio: https://github.com/alirezarezvani/claude-skills. Sigue las instrucciones oficiales del archivo README de este repositorio para la instalación y ejecución.

Antes de empezar, comprueba en qué sistema operativo estamos y si las herramientas necesarias (ej. Python, Node.js, Git, Docker) están instaladas. Instala las que falten paso a paso según este sistema.

Crea una carpeta nueva y vacía para trabajar. No toques ningún archivo fuera de esta carpeta y no borres nada. Antes de ejecutar cada comando, dime qué vas a hacer en una frase.

Dime qué debería ver en la pantalla al final de cada paso. Si ocurre un error, te pegaré el mensaje de error tal cual y lo solucionaremos juntos.

## Términos relacionados del glosario

- [AI Skills](https://trescout.com/es/dictionary/ai-skills/)
- [CLI](https://trescout.com/es/dictionary/cli/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Es para desarrolladores de software y equipos técnicos que desean utilizar herramientas de codificación respaldadas por inteligencia artificial de manera más eficiente y experta en sus flujos de trabajo profesionales.
- **Licencia:** MIT

## Enlaces

- [Repositorio en GitHub →](https://github.com/alirezarezvani/claude-skills)
- [Leer en turco →](https://trescout.com/discover/claude-skills/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-07-05: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. El texto de presentación se preparó con IA a partir de la propia documentación del repositorio y esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/claude-skills/
