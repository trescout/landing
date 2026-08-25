# Sistema de información local para Claude Code

Organiza contenido de investigación en un vault de Obsidian enlazando fuentes y aplicando cambios aprobados mediante transacciones reversibles. Diseñado para priorizar el funcionamiento local y minimizar la dependencia de la nube.

- ★ 12.404
- Python
- GitHub Trending · 2026-08-25

## ¿Qué hace esta herramienta?
Organiza el contenido de investigación con libros de fuentes y de reclamaciones, páginas enlazadas y mapas de conocimiento. Agentes paralelos generan borradores y un orquestador aplica los cambios aprobados mediante una operación reversible.

## ¿Para quién es?
Quienes quieran construir una base de conocimiento local y citada en Obsidian para uso con Claude Code.

## Qué no esperar
No es adecuado como sistema de registro automático de transcripciones, para sincronización en la nube, como garantía de exactitud ni como sustituto de copias de seguridad o control de versiones.

## Aspectos destacados
- Diseñado para funcionar por defecto de forma local y con un enfoque de salida de red explícita
- Genera páginas enlazadas que citan fuentes mediante libros de fuentes y de reclamaciones
- Aplica cambios aprobados mediante operaciones que pueden revertirse

## Primer flujo de uso
- Clona el repositorio y prepara un entorno con Python 3.11 o superior
- Crea el plan inicial para un vault separado y revisa el plan JSON
- Comprueba el valor approved_plan_sha256 y confirma el proceso completo
- Abre el vault en Obsidian y ejecuta Claude Code con el plugin local
- Inicia el flujo wiki y usa los pasos de agregar fuentes, consultar y guardar explícitamente

## Inicio seguro

## Primer prompt
Inicia un flujo wiki local en Obsidian asociando las fuentes con libros de fuentes y de reclamaciones.

## Instalación
**Agregar el marketplace de Claude Code**

```
claude plugin marketplace add AgriciDaniel/claude-obsidian
```

**Instalar el plugin claude-obsidian**

```
claude plugin install claude-obsidian@agricidaniel-claude-obsidian
```

**Crear el plan para un vault separado**

```
python3 scripts/claude-obsidian.py init <new-vault> --generated-at <ISO-UTC> --operation-id init-reviewed
```


## Ejecución
**Verificar la instalación del plugin**

```
claude plugin list
```

**Iniciar el flujo wiki**

```
/claude-obsidian:wiki
```


## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Guía de instalación →
- README oficial →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/claude-obsidian/
