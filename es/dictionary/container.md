# ¿Qué es Container?

Un contenedor es una única aplicación empaquetada con su código y dependencias, diseñada para ejecutarse de la misma manera en cualquier entorno.

## Definición y origen de la palabra
Los contenedores agrupan el código, las bibliotecas y la configuración de una aplicación en un solo paquete. Funciona en el servidor exactamente igual que en tu ordenador. La idea es antigua (chroot, LXC), se popularizó después de 2013 con Docker y hoy en día se define mediante el estándar OCI.

## ¿Cómo saberlo y utilizarlo en la vida diaria?
Distribución: El mismo paquete desde el desarrollo hasta producción.Microservicio: Cada servicio con su propia caja.CI: Que cada prueba se ejecute en una caja limpia.

## Profundidad técnica y arquitectura
Conceptos:

## Cosas frecuentemente mezcladas
Se confunde con una máquina virtual. La máquina lleva un sistema operativo completo, el contenedor solo lleva la aplicación. El aislamiento es fuerte en la máquina y suficiente en el contenedor; la elección se hace según la carga.

## Uso en diferentes disciplinas
Transporte: Compatibilidad con barcos, trenes y camiones mediante contenedores de tamaño estándar.Cocina: Una fiambrera con sus ingredientes listos dentro.Campamento: Un kit de acampada transportado ordenadamente en su bolsa.

## Preguntas frecuentes
**¿Por qué el contenedor es tan popular?**
Debido a que garantiza el mismo funcionamiento y una instalación rápida en cualquier entorno. Se ha convertido en el estándar junto con los microservicios y la orquestación en la nube.

**¿Cuál es la diferencia entre un contenedor y una máquina virtual?**
La máquina lleva su propio sistema operativo, el contenedor comparte el núcleo principal. El contenedor es ligero y rápido, la máquina es fuerte en aislamiento.

**¿Es seguro el contenedor?**
Dado que se comparte el núcleo, no está tan aislado como una máquina. Debes descargar las imágenes de una fuente confiable y mantenerlas actualizadas.

**¿Cuándo se prefiere una máquina virtual?**
Cuando se requiere un sistema operativo diferente o un aislamiento fuerte. Para la mayoría de las demás cargas de trabajo, el contenedor es suficiente.


## Términos relacionados
- [Containers](/es/dictionary/containers/)
- [Virtual Machines](/es/dictionary/virtual-machines/)
- [Deployment](/es/dictionary/deployment/)

## Herramientas relacionadas
- [N8n](/es/discover/n8n/)
- [Stirling-PDF](/es/discover/stirling-pdf/)
- [Core](/es/discover/core/)
- [Container](/es/discover/container/)
- [Mattermost](/es/discover/mattermost/)
- [Keycloak](/es/discover/keycloak/)
- [Trivy](/es/discover/trivy/)
- [PPF Contact Solver](/es/discover/ppf-contact-solver/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/container/
