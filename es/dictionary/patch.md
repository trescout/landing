# ¿Qué es Patch?

*Desarrollo · Última actualización: 19 de septiembre de 2026*

Un parche es una actualización de código y archivos que se publica con el fin de corregir errores en un software, cerrar vulnerabilidades de seguridad o mejorar las funciones existentes.

## 1. Patch en el mundo del software y los juegos

Tradicionalmente, cuando ocurre un error en un programa, descargar e instalar todo el software desde cero es ineficiente en términos de ancho de banda y tiempo. Un parche aplica al sistema de destino solo los bytes o archivos que han cambiado.

- Parches de seguridad: Se distribuyen de forma urgente para corregir vulnerabilidades críticas (CVE) y fallos de día cero (zero-day).
- Parches de corrección de errores (Bug Fixes): Corrige errores lógicos que afectan a la estabilidad o provocan cierres inesperados.
- Parches y ajustes de juego: Son actualizaciones que equilibran las habilidades de los personajes, añaden contenido nuevo y optimizan el rendimiento en juegos multijugador en línea. Por lo general, se presentan junto con notas del parche detalladas.
- Hotfix: Un parche de alcance limitado publicado con urgencia para apagar un incendio en el entorno de producción sin esperar al ciclo de pruebas.

***Analogía:** Es como coser un trozo de tela adecuado sobre un pequeño desgarro en tu ropa en lugar de tirar toda la prenda a la basura. Reemplaza solo las partes defectuosas sin tener que descargar todo el software desde cero.*

## 2. Parches en herramientas de desarrollo: UNIX patch y Git

En el mundo del código abierto y los sistemas de control de versiones, un parche es un documento de texto plano que representa la diferencia (diff) entre dos archivos o commits.

### El comando UNIX patch y su historia

El término "patch", basado en la metáfora de tapar agujeros en tarjetas perforadas con cinta o reparar tiras de papel, se estandarizó en 1985 con el comando patch escrito por Larry Wall. El parche generado con el comando diff -u antiguo.c nuevo.c > correccion.patch puede aplicarse directamente al código fuente en el otro extremo mediante patch \< correccion.patch.

### Uso de parches en el entorno Git

Git ofrece herramientas avanzadas para transportar parches a través de listas de correo o canales fuera de línea:

- git format-patch: Convierte commits específicos en archivos .patch aptos para correo electrónico, incluyendo la información del autor, el mensaje de commit y las diferencias de código.
- git apply: Aplica un archivo de parche directamente al directorio de trabajo sin crear un commit.
- git am: Lee parches en formato de correo electrónico y crea commits automáticamente manteniendo la información del autor original y la fecha (es el estándar, especialmente en el desarrollo del kernel de Linux).

## 3. Arquitectura Web y HTTP PATCH en APIs REST

En los servicios RESTful, los métodos PUT y PATCH se comparan frecuentemente al actualizar datos:

- PUT (Reemplazo completo): Envía el recurso completo de nuevo. Los campos no especificados generalmente vuelven a su valor predeterminado o se eliminan. La operación PUT es idempotente (enviar la misma solicitud varias veces produce el mismo resultado).
- PATCH (Actualización parcial - RFC 5789): Envía un cuerpo que contiene solo los campos que se desea cambiar. Por ejemplo, para actualizar solo la dirección de correo electrónico de un usuario, basta con enviar el campo correspondiente en lugar de todo el objeto del perfil.
- JSON Patch (RFC 6902): es una estructura que define secuencias de operaciones atómicas como add, remove, replace, move, copy y test para estandarizar los cambios.

## Resumen comparativo: "Patch" en diferentes contextos

| Contexto | ¿Qué significa? | Objetivo principal | Ejemplo típico |
|---|---|---|---|
| Software y sistema operativo | Paquete de actualización | Corrección de vulnerabilidades de seguridad, estabilidad | Parche KB de Windows Update, parche de día cero |
| Mundo de los videojuegos | Actualización de contenido y equilibrio | Equilibrio de juego, rendimiento, cambio de meta | Parche de temporada (Parche 14.2), actualización de equilibrio |
| Git y control de versiones | Archivo de cambios basado en líneas | Compartir código, revisión de código, contribución | git format-patch HEAD~1, linux-kernel.patch |
| Web API / HTTP | Método de actualización parcial | Ahorro de red, cambio parcial en el recurso | PATCH /api/users/42 cuerpo: {"status": "active"} |

## Preguntas y respuestas

**¿Qué significa 'patch' y cuál es su equivalente en español?**

Su equivalente en español es "parche" o "corrección de errores". Se refiere a fragmentos de código que reparan o actualizan una parte específica de un sistema o software sin necesidad de reemplazarlo por completo.

**¿Cuál es la diferencia entre un 'hotfix' y un 'patch'?**

Un 'patch' generalmente se publica con versiones planificadas (por ejemplo, boletines de seguridad mensuales) después de pruebas exhaustivas. Un 'hotfix', en cambio, es un parche de intervención rápida y no planificado, preparado para detener inmediatamente un bloqueo crítico o una vulnerabilidad de seguridad que surge en el entorno de producción.

**¿Cuál es la diferencia fundamental entre HTTP PUT y HTTP PATCH?**

PUT tiene como objetivo el reemplazo total del recurso y produce el mismo resultado si se repite la misma solicitud (idempotente). PATCH, por otro lado, modifica solo los campos especificados del recurso de forma parcial (actualización parcial) y no tiene que ser necesariamente idempotente en todos los escenarios.

**¿Por qué se siguen utilizando archivos de parche (patch) en el entorno Git cuando existen los PR (Pull Request)?**

El kernel de Linux, el propio proceso de desarrollo de Git y proyectos de código abierto consolidados como Postgres mantienen el flujo de trabajo de parches basado en correo electrónico para no depender de plataformas web centralizadas (como GitHub, etc.).

**¿Qué es el 'Patch Tuesday'?**

Es el nombre dado al calendario sectorial en el que Microsoft distribuye regularmente parches de seguridad acumulativos para Windows y sus productos empresariales el segundo martes de cada mes.

## Términos relacionados

- [Vulnerability Scanning](https://trescout.com/es/dictionary/vulnerability-scanning/)
- [Security Scanner](https://trescout.com/es/dictionary/security-scanner/)
- [Deployment](https://trescout.com/es/dictionary/deployment/)
- [Git Push](https://trescout.com/es/dictionary/git-push/)

## Herramientas relacionadas

- [PLFM RADAR](https://trescout.com/es/discover/plfm-radar/)
- [PhotoGIMP](https://trescout.com/es/discover/photogimp/)

Esta explicación se redactó en lenguaje sencillo para TreScout con IA y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/patch/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/patch/
