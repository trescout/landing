# ¿Qué es Repository Checkout?

*Glosario · Dev · Última actualización: 22 de septiembre de 2026*

La compra del repositorio es el proceso de descargar una versión específica del repositorio a su espacio de trabajo.

## Definición y origen de la palabra

Obtienes la versión actual del proyecto del servidor y la llevas a tu escritorio. Es como pedir prestado un libro de la biblioteca: la fuente permanece, tú trabajas con la copia. La información del historial y la versión viene con la copia.

***Analogía:** Es como pedir prestado un libro de la biblioteca, llevarlo a tu escritorio y empezar a leer las páginas una por una.*

## ¿Cómo saberlo y utilizarlo en la vida diaria?

**Nuevo proyecto:** Descargando el repositorio por primera vez.
**Migración de versión:** No vuelva a la etiqueta anterior y examine el error.
**Pruebe la rama:** No abras la sucursal de tu amigo localmente.

## Profundidad técnica y arquitectura

El flujo es el siguiente:

```
git clone https://github.com/ornek/proje.git
cd proje
git checkout v2.0.0
```

Distinciones:

**Clon:** Descargando el repositorio completo por primera vez.
**Verificar:** Cambiando de versión o rama en el repositorio descargado.
**Cambiar/Restaurar:** Bifurcación y recuperación de comandos en Git moderno.
**Escaso:** Descargando solo la carpeta requerida en el enorme repositorio.

Regla: no pase mientras tenga el trabajo guardado, confírmelo o guárdelo primero.

## Uso en diferentes disciplinas

**Biblioteca:** No saques el libro del estante y lo lleves a la mesa.
**Archivo:** Retire la carpeta del almacenamiento y examínela.
**Fotografía:** No dejes que lo negativo te presione.

## Preguntas frecuentes

**¿Solo descarga archivos?**

No. También se incluye información sobre el historial y la versión, por lo que puedes volver a la versión anterior.

**¿Cuál es la diferencia con Clonar?**

Clonar es la descarga inicial, el pago es el paso por el repositorio descargado. El orden va en esta dirección.

**¿Cómo volver a la versión anterior?**

Se pasa con una etiqueta o un hash de confirmación. Si hay un trabajo guardado, se almacena primero.

**¿Qué es el interruptor?**

Es el comando moderno para bifurcar. Dado que el proceso de pago requiere mucho trabajo, Git lo divide en dos: cambiar a la rama y restaurar al archivo.

## Términos relacionados

- [Git Push](https://trescout.com/es/dictionary/git-push/)
- [Tech Stack](https://trescout.com/es/dictionary/tech-stack/)
- [Cloning](https://trescout.com/es/dictionary/cloning/)

## Herramientas relacionadas

- [Checkout](https://trescout.com/es/discover/checkout/)

Esta explicación se redactó en lenguaje sencillo para TreScout y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/repository-checkout/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/repository-checkout/
