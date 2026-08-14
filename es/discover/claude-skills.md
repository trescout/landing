# Aportar experiencia a los agentes de codificación de IA

Desarrollada para Claude Code y varios agentes de codificación, esta biblioteca ofrece más de 330 paquetes de habilidades y más de 70 comandos especiales en diferentes campos, desde ingeniería hasta marketing. Este conjunto de herramientas basado en Python proporciona scripts personalizables para estandarizar los flujos de trabajo basados ​​en IA y aumentar la productividad.

- ★ 23.654
- Python
- GitHub Trending · 2026-07-05

## Actualizar
- 2 de agosto de 2026: Star 20,244 → 23,654, última versión v2.9.0 (28 de mayo de 2026).

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
Active los paquetes de habilidades en esta biblioteca para Claude Code o el agente de codificación que utilice. Estandarice mi flujo de trabajo y aumente mi productividad utilizando scripts especializados en campos como ingeniería, marketing o consultoría de nivel C. Integrar las capacidades específicas que necesito (por ejemplo, auditoría de seguridad o desarrollo de productos) en mi proyecto.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/claude-skills/
