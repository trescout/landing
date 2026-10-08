# ¿Qué es Cloud Computing?

*Glosario · Dev · Última actualización: 19 de septiembre de 2026*

La computación en la nube (cloud computing) es la prestación de recursos informáticos como servidores, almacenamiento, bases de datos, redes y software a través de Internet desde centros de datos remotos bajo demanda, en lugar de utilizar infraestructuras físicas locales.

## Definición, origen etimológico y nacimiento conceptual

La computación en la nube (Cloud Computing) es el modelo de computación moderno que permite a las empresas y a los ingenieros alquilar potencia de cálculo, memoria, espacio de almacenamiento y clústeres de GPU para inteligencia artificial en cuestión de segundos a través de Internet, en lugar de construir sus propias salas de servidores y comprar hardware físico.

Conceptualmente, sus raíces se remontan a 1961, al discurso de John McCarthy, uno de los padres de la inteligencia artificial, en el MIT. McCarthy predijo que la potencia informática se ofrecería en el futuro como un servicio público (utility), al igual que la electricidad y el agua. La adopción del término "nube" en este sector se basa en la ingeniería de telecomunicaciones y redes: en la década de 1990, los arquitectos de sistemas solían representar las complejas centrales telefónicas y la infraestructura de Internet, cuyos detalles querían abstraer, dibujando un "icono de nube" en sus diagramas. Con el lanzamiento de los servicios Simple Storage Service (S3) y Elastic Compute Cloud (EC2) de Amazon en 2006, el modelo de compra de servidores basado en gastos de capital (CapEx) fue reemplazado por el principio de pago por uso (OpEx).

***Analogía:** Es como conectarse directamente a la red eléctrica nacional en lugar de instalar una central hidroeléctrica o un generador privado en el jardín de su propia fábrica o casa. En el momento en que enchufa el dispositivo, la electricidad fluye; usted solo paga por el consumo realizado a fin de mes según la potencia que su máquina haya utilizado, sin tener que preocuparse por averías del generador, combustible o mantenimiento del transformador.*

## Modelos básicos de servicio y distribución (IaaS, PaaS, SaaS, Serverless)

La arquitectura de la computación en la nube se divide en cuatro modelos de servicio principales según los niveles de abstracción:

1. IaaS (Infrastructure as a Service · Infraestructura como Servicio): Es el nivel más bajo, compuesto por máquinas virtuales sin procesar, discos de almacenamiento en bloque y topologías de red virtual. AWS EC2, Google Compute Engine y Azure VM pertenecen a esta categoría. El proveedor de la nube gestiona el hardware y la capa de virtualización, mientras que el desarrollador es responsable de la instalación del sistema operativo, los parches de seguridad y la pila de software.
2. PaaS (Platform as a Service · Plataforma como servicio): Son plataformas que liberan al desarrollador de las preocupaciones sobre la configuración del servidor, el sistema operativo y el entorno de ejecución (runtime). Vercel, Heroku y AWS Elastic Beanstalk pueden citarse como ejemplos. El ingeniero solo envía el código fuente; el escalado, los certificados SSL y el balanceo de carga se gestionan automáticamente en segundo plano.
3. SaaS (Software as a Service · Software as a Service): Son el usuario accede directamente a través de un navegador web o una API, y cuyo mantenimiento corre totalmente a cargo del fabricante; son soluciones de software llave en mano. Google Workspace, Slack, Salesforce y Figma son los ejemplos más conocidos de este modelo.
4. Serverless (FaaS · Función como Servicio): Es una arquitectura orientada a eventos que abstrae completamente el concepto de servidor. El código escrito en AWS Lambda o Cloudflare Workers se activa solo cuando llega una solicitud HTTP o un evento de base de datos, se ejecuta en milisegundos y se cierra. No genera costos cuando no hay tráfico.

Los modelos de despliegue se definen según dónde se alojen los datos:

- Nube pública: Estructura en la que los recursos se comparten de forma multiinquilino (multi-tenant) en los centros de datos globales de grandes proveedores.
- Nube Privada: Entorno aislado que sectores regulados como el financiero, el de defensa y el sanitario operan en centros de datos dedicados exclusivamente a ellos.
- Nube híbrida: Estructura mixta en la que los datos confidenciales de los clientes se alojan en servidores locales (on-premise), mientras que la capa web, que requiere un alto volumen de procesamiento, se ejecuta en la nube pública.
- Multi-Cloud: Para evitar la dependencia de un único proveedor (vendor lock-in), los sistemas se configuran de forma distribuida entre AWS, Google Cloud y Azure.

## Ciencias de la computación y arquitectura de sistemas: Hipervisor, contenedor y CAP

El milagro técnico que subyace a la computación en la nube es la abstracción del hardware mediante software (virtualización):

- Capa de hipervisor: Es el software central que divide los recursos de procesador y memoria RAM de un único servidor físico para distribuirlos entre decenas de máquinas virtuales (VM) independientes. Los hipervisores de tipo 1 (bare-metal), que se ejecutan directamente sobre el hardware (KVM, VMware ESXi), constituyen la columna vertebral del rendimiento de los proveedores de servicios en la nube.
- Contenedores y orquestación: Los contenedores Docker nacieron utilizando las capacidades de cgroups (limitación de recursos) y namespaces (aislamiento de procesos) del kernel de Linux para superar la carga de replicación del sistema operativo de las máquinas virtuales. El despliegue automático y la autorreparación (self-healing) de miles de contenedores se logran mediante clústeres de Kubernetes.
- Teorema CAP y resiliencia distribuida: Las infraestructuras de nube global operan dentro de los límites del Teorema CAP de Eric Brewer. En caso de una partición de red (Network Partition), el sistema debe priorizar la consistencia de los datos (Consistency) o la disponibilidad ininterrumpida (Availability). Los arquitectos de la nube implementan escenarios de recuperación ante desastres mediante arquitecturas geográficamente redundantes (Multi-Region / Availability Zone).
- Modelo de Responsabilidad Compartida: La seguridad en la nube se divide en dos. El proveedor es responsable de la seguridad de los centros de datos físicos, los servidores, el hipervisor y los cables de red ("Seguridad DE la nube"). Por su parte, el cliente es responsable de las actualizaciones del sistema operativo, el cifrado, los roles de IAM (gestión de acceso) y las vulnerabilidades del código de la aplicación ("Seguridad EN la nube").

## Dimensión económica, ecológica y geopolítica

La computación en la nube no es solo una revolución técnica, sino también una ruptura masiva en la asignación de recursos globales:

- Paradoja de Jevons: El principio que el economista del siglo XIX William Stanley Jevons estableció para el consumo de carbón también se aplica a la nube: a medida que el acceso a la potencia informática se vuelve más barato y sencillo, el consumo total no disminuye, sino que aumenta exponencialmente. Hoy en día, la capacidad de entrenar modelos de inteligencia artificial con cientos de miles de millones de parámetros es una consecuencia directa de las economías de escala que ofrece la computación en la nube.
- Consumo de energía y agua: Los centros de datos de hiperescala consumen aproximadamente entre el 1% y el 2% de la electricidad mundial, y se utilizan millones de metros cúbicos de agua pura para refrigerar los enormes clústeres de GPU. Esta situación ha hecho obligatorio que los centros de datos se instalen cerca de fuentes de energía renovable y en climas fríos.
- Soberanía digital y regímenes jurídicos: dónde reside físicamente el dato es una cuestión geopolítica. Mientras que la ley CLOUD Act de EE. UU. otorga autoridad a las empresas estadounidenses para intervenir en sus servidores en el extranjero, la Unión Europea, a través del RGPD y la iniciativa GAIA-X, y Turquía, mediante la normativa KVKK, fomentan que los datos críticos permanezcan dentro de las fronteras nacionales.

## Suele confundirse con

- Almacenamiento en la nube frente a computación en la nube: Google Drive, iCloud o Dropbox son solo servicios de almacenamiento; la computación en la nube, por otro lado, es un ecosistema masivo que, además del almacenamiento, incluye potencia de procesamiento dinámica, entrenamiento de inteligencia artificial, gestión de redes y orquestación de bases de datos.
- Serverless (sin servidor) frente a "realmente sin servidor": en la arquitectura serverless, por supuesto, existen servidores físicos; el término "sin servidor" indica que el desarrollador ya no tiene que preocuparse por configurar, actualizar o supervisar un servidor, ya que la gestión del mismo se vuelve invisible gracias al proveedor.

## Preguntas frecuentes

**¿Qué significa cloud computing y cuál es su equivalente en turco?**

En turco significa 'bulut bilişim'. Es un modelo en el que la potencia de procesamiento, los servidores y los recursos de almacenamiento se alquilan instantáneamente según la necesidad a través de la columna vertebral de Internet en lugar de utilizar computadoras locales.

**¿Cuál es la diferencia fundamental entre los 3 modelos de servicio principales de la computación en la nube (IaaS, PaaS, SaaS)?**

IaaS es el alquiler de hardware básico y servidores virtuales (AWS EC2), PaaS es un entorno de ejecución y alojamiento de código directo (Vercel), y SaaS es software llave en mano ofrecido al usuario final a través de la web (Google Docs).

**¿Qué significa el Modelo de Responsabilidad Compartida (Shared Responsibility Model)?**

Es una división de seguridad donde el proveedor de la nube es responsable de proteger la infraestructura física, el centro de datos y el hardware; mientras que el usuario es responsable de la seguridad de su propia aplicación, los permisos de usuario (IAM) y el cifrado de datos.

**¿Cómo se evita la dependencia del proveedor de la nube (Vendor Lock-in)?**

Utilizando estándares de código abierto (contenedores Docker, Kubernetes), motores de bases de datos independientes (PostgreSQL) y herramientas de Infraestructura como Código (Terraform / OpenTofu), el software se aísla de las API propietarias específicas del proveedor.

## Términos relacionados

- [SaaS](https://trescout.com/es/dictionary/saas/)
- [PaaS](https://trescout.com/es/dictionary/paas/)
- [IaaS](https://trescout.com/es/dictionary/iaas/)
- [Personal Cloud](https://trescout.com/es/dictionary/personal-cloud/)
- [Runtime](https://trescout.com/es/dictionary/runtime/)
- [Network Stack](https://trescout.com/es/dictionary/network-stack/)
- [Memory Management](https://trescout.com/es/dictionary/memory-management/)

## Herramientas relacionadas

- [DevOps-Interview-Guide](https://trescout.com/es/discover/devops-interview-guide/)

Esta explicación se redactó en lenguaje sencillo para TreScout y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/cloud-computing/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/cloud-computing/
