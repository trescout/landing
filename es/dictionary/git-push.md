# ¿Qué es Git Push?

> Inglés: Git Push · Etimología: argot británico git + latín pulsare (empujar, impulsar)

**Categoría:** Dev  
**Última actualización:** 2026-09-19

Git Push es la instrucción fundamental de control de versiones que sube las confirmaciones de código (commits), ramas e historiales locales hacia un repositorio remoto para sincronizar el trabajo con el equipo.

## Por analogía
Es como redactar capítulos de una obra en un borrador privado en tu ordenador y, cuando están listos, enviarlos por mensajería a la editorial central para que todo el equipo disponga de la misma edición.

## 1. Definición y el modelo de 4 capas de Git
Git es un sistema de control de versiones distribuido (DVCS) estructurado en cuatro espacios de trabajo : el Directorio de Trabajo, el Área de Preparación (Staging/Index), el Repositorio Local (.git) y el Repositorio Remoto (GitHub, GitLab). Mientras que <code>git commit</code> guarda un punto de restauración en tu máquina, <code>git push</code> es el proceso que transfiere esos objetos por red al servidor centralizado.

## 2. Comandos más habituales (Chuleta)
Sintaxis frecuentes en el día a día del desarrollador :
- **Publicar Rama por Primera Vez:** <code>git push -u origin mi-rama</code> (establece el seguimiento con el servidor).- **Empuje Estándar:** <code>git push</code> (actualiza la rama aguas arriba activa).- **Enviar Etiquetas:** <code>git push origin --tags</code> (sincroniza versiones etiquetadas).- **Eliminar Rama Remota:** <code>git push origin --delete rama-obsoleta</code>.- **Sobrescritura Segura:** <code>git push --force-with-lease</code> (reescribe el remoto solo si ningún compañero ha subido cambios entretanto).

## 3. Errores habituales de push y soluciones
Resolución de bloqueos comunes :
- **fatal: [rejected - non-fast-forward]:** Hay cambios en el servidor que no tienes en local. Solución: ejecuta <code>git pull --rebase origin main</code>, soluciona conflictos y vuelve a empujar.- **fatal: The current branch has no upstream branch:** Añade el parámetro <code>-u</code> para fijar la rama remota de referencia.- **Rechazo por Archivos Grandes:** Ficheros superiores a 100 MB son rechazados por GitHub; utiliza la extensión Git LFS.

## Preguntas frecuentes

**¿Qué diferencia hay entre 'git commit' y 'git push'?**  
Commit guarda un punto de control en tu disco local; push transmite ese conjunto de cambios al servidor compartido en la red.

**¿Por qué es más recomendable '--force-with-lease' frente a '--force'?**  
Porque --force destruye el trabajo que otros hayan subido al servidor; --force-with-lease aborta si detecta que otra persona ha actualizado la rama.

**¿Qué función tienen los hooks pre-push?**  
Ejecutan pruebas de calidad y formateo en tu ordenador antes de autorizar la salida de los paquetes hacia el servidor remoto.

**¿Se puede hacer push a dos servidores distintos a la vez?**  
Sí, configurando múltiples direcciones URL de empuje para un mismo alias en el archivo .git/config.

## Términos relacionados
- [CLI](/es/dictionary/cli/)
- [Code Snippets](/es/dictionary/code-snippets/)
- [Checkout](/es/dictionary/checkout/)

## Herramientas relacionadas
- [No Mistakes](/es/discover/no-mistakes/)

---
Fuente: Diccionario Tecnológico TreScout · https://trescout.com/es/dictionary/git-push/
