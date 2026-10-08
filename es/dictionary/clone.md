# ¿Qué es Clone?

*Glosario · Dev · Última actualización: 22 de septiembre de 2026*

El clonado (en turco "Clone") es el proceso de crear una copia local de un repositorio Git remoto junto con todo su historial.

## Definición y origen de la palabra

Clone en inglés significa copia exacta. En el mundo de Git se usa con el comando git clone: descargas no solo los archivos actuales, sino también todo el historial de commits, ramas y etiquetas del proyecto.

***Analogía:** Es como no solo tomar una foto de una sola página de un libro en la biblioteca, sino llevarse una copia completa del libro a su propio estante.*

## ¿Cómo saberlo y utilizarlo en la vida diaria?

Cuando deseas examinar o contribuir a un proyecto de código abierto, el primer paso suele ser clonarlo:

```
git clone https://github.com/kullanici/proje.git
```

Al ejecutar el comando, se crea la carpeta del proyecto en el directorio actual. Si el repositorio es muy grande, se utiliza un clon superficial para obtener solo una parte del historial:

```
git clone --depth 1 https://github.com/kullanici/proje.git
```

## Profundidad técnica y arquitectura

El directorio .git dentro de la carpeta clonada es la memoria del repositorio: todos los objetos de commit, los punteros de rama y las direcciones remotas residen aquí. Después del clon:

git fetch descarga los cambios remotos y no toca tus archivos.
git pull descarga los cambios y los fusiona en tu rama actual.
git push envía tus commits al repositorio remoto (si tienes permisos).
un fork crea una copia en el lado del servidor. Un clon descarga esa copia o el repositorio original en su ordenador. Son dos conceptos diferentes.

## Uso en diferentes disciplinas

**Biología:** Una copia genética del ser vivo. En cambio, el clon en el software es una copia de datos, no tiene relación con un ser vivo.
**Medios:** Vestuarios de repuesto con los que trabajar mientras el original está ocupado.
**Virtualización:** Creación de una nueva máquina a partir de una plantilla predefinida.

## Preguntas frecuentes

**¿Puedo cambiar el proyecto después de la clonación?**

Sí. Puedes hacer los cambios que quieras en tu propia copia. El repositorio original no se ve afectado. Si quieres proponer tu cambio al proyecto, abres un pull request.

**¿Cuál es la diferencia entre fork y clone?**

Fork crea una copia en el servidor (en tu cuenta), clone descarga esa copia en tu ordenador. El flujo de contribución suele ser fork y luego clone.

**¿Qué debo hacer si el repositorio es muy grande?**

Realiza un clon superficial con --depth 1 o descarga solo una rama (--single-branch). Si necesitas el historial, puedes profundizar más adelante.

**¿Mantendré el clon actualizado?**

Sí. Solo necesitas ejecutar git pull dentro de la carpeta. Si tienes cambios, primero debes hacer commit o guardarlos (git stash).

## Términos relacionados

- [CLI](https://trescout.com/es/dictionary/cli/)
- [Open Source](https://trescout.com/es/dictionary/open-source/)
- [Self-Hosting](https://trescout.com/es/dictionary/self-hosting/)

## Herramientas relacionadas

- [MoneyPrinterTurbo](https://trescout.com/es/discover/moneyprinterturbo/)
- [VoxCPM](https://trescout.com/es/discover/voxcpm/)
- [Clone-Wars](https://trescout.com/es/discover/clone-wars/)
- [Univer](https://trescout.com/es/discover/univer/)
- [OpenStock](https://trescout.com/es/discover/openstock/)
- [Hermes WebUI](https://trescout.com/es/discover/hermes-webui/)
- [Production Agentic RAG Course](https://trescout.com/es/discover/production-agentic-rag-course/)
- [Flowsint](https://trescout.com/es/discover/flowsint/)

Esta explicación se redactó en lenguaje sencillo para TreScout y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/clone/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/clone/
