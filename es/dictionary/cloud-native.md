# ¿Qué es Cloud Native?

Cloud native (o su traducción al turco bulut yerlisi), es un enfoque para diseñar aplicaciones de modo que aprovechen al máximo la flexibilidad y escalabilidad de la nube.

## Definición y origen de la palabra
El concepto lo engloba el paraguas de la CNCF (Cloud Native Computing Foundation). La distinción crítica aquí es esta: subir un software a la nube no lo hace nativo de la nube. Lo nativo de la nube es que la aplicación se construya desde el principio según la estructura dinámica de la nube, en piezas pequeñas e independientes.

## ¿Cómo saberlo y utilizarlo en la vida diaria?
Días de gran actividad: Aumento automático de la capacidad cuando el tráfico del día de campaña se multiplica.Momento de fallo: Traspaso silencioso del trabajo a otra copia cuando un servidor se cae.Actualización: Renovación de la aplicación por partes mientras está en ejecución, no cuando está cerrada.

## Profundidad técnica y arquitectura
Partes de la pila nativa de la nube:

## Uso en diferentes disciplinas
Estructura prefabricada: Una casa modular a la que se le pueden añadir habitaciones según las necesidades.Red eléctrica: Centrales que entran en funcionamiento según la demanda.Logística: Líneas de distribución que se abren y cierran según la densidad.

## Preguntas frecuentes
**¿Migrar la aplicación a la nube la hace nativa de la nube (cloud native)?**
No. Mover una aplicación heredada tal cual solo la reubica. Para ser nativa de la nube, la arquitectura debe dividirse en partes pequeñas y ser apta para la gestión automática.

**¿Es necesario para un proyecto pequeño?**
No siempre. Para un blog que funciona cómodamente en un solo servidor, esta configuración puede ser excesiva. Cobra sentido si el tráfico es volátil o el equipo está creciendo.

**¿Aumenta el coste?**
Tiene un coste de instalación y aprendizaje. A cambio, se reducen el tiempo de inactividad y los costes de escalado. Debes hacer el cálculo según tu carga de trabajo.

**¿Por dónde se debe empezar?**
Empieza por contenedorizar la aplicación. Luego, añade comprobaciones de salud (health check), registro de logs y despliegue automático. La orquestación es el último paso.


## Términos relacionados
- [Containers](/es/dictionary/containers/)
- [Virtual Machines](/es/dictionary/virtual-machines/)
- [Runtime](/es/dictionary/runtime/)

## Herramientas relacionadas
- [Meshery](/es/discover/meshery/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/cloud-native/
