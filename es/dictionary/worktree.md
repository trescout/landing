# ¿Qué es Worktree?

Es una estructura que le permite trabajar en diferentes versiones del proyecto simultáneamente sin cambiar la carpeta del proyecto original.

## Definición
Worktree le permite abrir diferentes ramas (branch) del proyecto en carpetas separadas sin interrumpir su espacio de trabajo principal mientras desarrolla software. Por ejemplo, mientras desarrolla una funcionalidad en el proyecto principal, puede corregir un error antiguo en otra carpeta al mismo tiempo. Esto elimina la pérdida de tiempo y la confusión causadas por cambiar constantemente de rama.

## Cómo funciona
Añade un nuevo worktree a través de sistemas de control de versiones como Git. El sistema vincula una copia del proyecto a un directorio diferente para usted y usted continúa trabajando allí sin tocar el directorio principal.

## Dónde se usa
Se utiliza en proyectos de software complejos cuando es necesario realizar correcciones de errores urgentes durante el desarrollo de funcionalidades que requieren mucho tiempo.

## Suele confundirse con
No es lo mismo que simplemente copiar carpetas; los worktrees están vinculados al mismo repositorio de Git y funcionan sincronizados entre sí.

## Preguntas frecuentes
**¿Por qué no copiamos carpetas por separado?**
Copiar desperdicia espacio en disco y dificulta la gestión del historial de Git; el worktree es mucho más eficiente.

**¿Funciona en todos los proyectos de Git?**
Sí, esta función es compatible con todas las versiones modernas de Git.


## Términos relacionados
- [Source Control](/es/dictionary/source-control/)
- [Git Push](/es/dictionary/git-push/)
- [Repository Checkout](/es/dictionary/repository-checkout/)

## Herramientas relacionadas
- [Worktrunk](/es/discover/worktrunk/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/worktree/
