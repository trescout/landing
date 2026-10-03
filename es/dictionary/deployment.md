# ¿Qué es Deployment?

La implementación (deployment / puesta en producción) es el proceso mediante el cual un componente de software desarrollado y probado en un entorno local se compila, se instala en servidores de destino o en una infraestructura en la nube, y se pone a disposición de los usuarios finales.

## Marco conceptual, etimología y transformación histórica
Etimológicamente, el término deployment tiene su origen en la terminología militar; se refiere al envío de tropas, municiones o equipos a posiciones de combate estratégicas para prepararlos para la operación ("to deploy"). En la ingeniería de software, comenzó en las décadas de 1970 y 1980 con la carga de tarjetas perforadas o cintas magnéticas en mainframes; evolucionó en los años 90 a transferencias de archivos FTP/SSH ejecutadas manualmente, y hoy en día se ha transformado en pipelines en la nube completamente declarativos y automatizados (GitOps).

## Estrategias de implementación sin interrupción (Zero-Downtime)
Los principales patrones de implementación desarrollados para garantizar que los usuarios no experimenten interrupciones en el servicio mientras las aplicaciones se actualizan son los siguientes:

## Canalización CI/CD, GitOps y migraciones de bases de datos
Una arquitectura de despliegue exitosa se construye sobre tres pilares de ingeniería críticos:

## Gestión de errores, observabilidad y arquitectura de reversión (Rollback)
Incluso en los entornos de prueba más avanzados, existen dos salvavidas fundamentales para los errores de producción que pasan desapercibidos:

## Suele confundirse con

## Preguntas frecuentes
**¿Qué significa deployment y cuál es su equivalente en español?**
Es una palabra de origen inglés que significa 'despliegue' o 'puesta en producción'. Es el proceso mediante el cual se compila el paquete de software y se pone en funcionamiento en los servidores de destino o en el entorno en la nube.

**¿Cuál es la diferencia entre deployment y release?**
El despliegue (Deployment) es la instalación técnica y ejecución del código en el servidor. El lanzamiento (Release), en cambio, es la apertura oficial de la característica al acceso del usuario final mediante un Feature Flag o pasos de marketing.

**¿Cuál es la diferencia principal entre el despliegue Azul-Verde (Blue-Green) y el Canary?**
En el despliegue Azul-Verde hay dos entornos idénticos y el tráfico se transfiere al 100% al nuevo entorno en un solo instante mediante un equilibrador de carga. En el despliegue Canary, por el contrario, la nueva versión se ofrece gradualmente primero a una pequeña porción de usuarios del 1-5% y la proporción se incrementa observando las métricas.

**¿Cómo se gestionan los cambios en el esquema de la base de datos en el despliegue sin interrupciones (Zero-Downtime)?**
Se gestionan con el patrón Expand-Contract (Ampliar y Contraer). Primero se añaden nuevos campos compatibles con versiones anteriores; una vez que todos los servidores del sistema pasan al nuevo código y el flujo de datos está asegurado, se limpian los campos antiguos.


## Términos relacionados
- [Runtime](/es/dictionary/runtime/)
- [Compile-time](/es/dictionary/compile-time/)
- [Cloud Computing](/es/dictionary/cloud-computing/)
- [Production Pipeline](/es/dictionary/production-pipeline/)
- [Tech Stack](/es/dictionary/tech-stack/)
- [Git Push](/es/dictionary/git-push/)

## Herramientas relacionadas
- [Rocket.Chat](/es/discover/rocket-chat/)
- [Chatwoot](/es/discover/chatwoot/)
- [Argo Cd](/es/discover/argo-cd/)
- [Openship](/es/discover/openship/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/deployment/
