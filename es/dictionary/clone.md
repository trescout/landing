# ¿Qué es Clone?

El clonado (en turco "Clone") es el proceso de crear una copia local de un repositorio Git remoto junto con todo su historial.

## Definición y origen de la palabra
Clone en inglés significa copia exacta. En el mundo de Git se usa con el comando git clone: descargas no solo los archivos actuales, sino también todo el historial de commits, ramas y etiquetas del proyecto.

## ¿Cómo saberlo y utilizarlo en la vida diaria?
Cuando deseas examinar o contribuir a un proyecto de código abierto, el primer paso suele ser clonarlo:

## Profundidad técnica y arquitectura
El directorio .git dentro de la carpeta clonada es la memoria del repositorio: todos los objetos de commit, los punteros de rama y las direcciones remotas residen aquí. Después del clon:

## Uso en diferentes disciplinas
Biología: Una copia genética del ser vivo. En cambio, el clon en el software es una copia de datos, no tiene relación con un ser vivo.Medios: Vestuarios de repuesto con los que trabajar mientras el original está ocupado.Virtualización: Creación de una nueva máquina a partir de una plantilla predefinida.

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
- [CLI](/es/dictionary/cli/)
- [Open Source](/es/dictionary/open-source/)
- [Self-Hosting](/es/dictionary/self-hosting/)

## Herramientas relacionadas
- [MoneyPrinterTurbo](/es/discover/moneyprinterturbo/)
- [VoxCPM](/es/discover/voxcpm/)
- [Clone-Wars](/es/discover/clone-wars/)
- [Univer](/es/discover/univer/)
- [OpenStock](/es/discover/openstock/)
- [Hermes WebUI](/es/discover/hermes-webui/)
- [Production Agentic RAG Course](/es/discover/production-agentic-rag-course/)
- [Flowsint](/es/discover/flowsint/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/clone/
