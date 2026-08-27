# Gestiona archivos de office con inteligencia artificial

OfficeCLI ofrece una suite ofimática de código abierto que permite a los agentes de IA leer, editar y automatizar directamente archivos de Word, Excel y PowerPoint. Desarrollada con C#, esta herramienta permite realizar operaciones a través de un único archivo binario sin necesidad de instalar ningún software ofimático.

- ★ 29.368
- C#
- GitHub Trending · 2026-07-08

## Qué aporta
- Edite archivos de Word, Excel y PowerPoint con código
- Realice transacciones directamente sin instalar software de oficina
- Brinde a los agentes de IA la capacidad de crear documentos

## Instalación
**Instalación en macOS o Linux**

```
curl -fsSL https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.sh | bash
```

**Instalación en Windows**

```
irm https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.ps1 | iex
```


## Ejecución
**Crear una presentación en blanco**

```
officecli create deck.pptx
```

**Agregar diapositivas a una presentación**

```
officecli add deck.pptx / --type slide --prop title="Hello, World!"
```


## Si no programa
Puede administrar archivos de Word, Excel y PowerPoint con la herramienta OfficeCLI preparada para usted. Para utilizar esta herramienta, instale el archivo de habilidades requerido ejecutando el siguiente comando: curl -fsSL https://officecli.ai/SKILL.md. Después de este proceso, podrá leer, editar y crear documentos de Office a través de la línea de comando.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/officecli/
