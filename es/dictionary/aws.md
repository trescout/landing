# ¿Qué es AWS?

> Amazon Web Services

**Categoría:** Dev  
**Última actualización:** 2026-09-22

AWS (Amazon Web Services) es la plataforma de computación en la nube de Amazon que proporciona servidores bajo demanda, bases de datos gestionadas, almacenamiento masivo y servicios analíticos a través de internet.

## Definición y etimología
En lugar de adquirir racks y servidores físicos en centros de datos locales, las organizaciones alquilan capacidad de computación elástica en las instalaciones de Amazon. La infraestructura escala con la demanda y reduce su tamaño en períodos de inactividad, operando bajo el modelo de pago por uso.

## Contexto cotidiano y uso práctico
- **Portales y Apps Móviles:** Clústeres que se autoescalan para soportar picos de usuarios simultáneos.
- **Copias de Seguridad:** Almacenamiento seguro e inmutable para preservación histórica de datos.
- **Redes de Medios:** Servidores de distribución perimetral para streaming sin cortes.
- **Empresas Emergentes:** Despliegue de servicios globales desde el primer día sin presupuesto de hardware.

## Profundidad técnica y arquitectura
Servicios Fundamentales de la Plataforma:- **EC2:** Servidores virtuales configurables con sistemas operativos Linux o Windows.
- **S3:** Almacenamiento de objetos de durabilidad extrema para archivos y copias.
- **RDS:** Motores de bases de datos relacionales administrados por completo.
- **Lambda:** Entorno de ejecución serverless que procesa código en respuesta a eventos puntuales.

La infraestructura global se divide en Regiones y Zonas de Disponibilidad (AZ). El Modelo de Responsabilidad Compartida delimita que Amazon protege la seguridad de la nube, mientras que el usuario gestiona la seguridad en la nube (cifrado, parches y credenciales).<div class="disc-cmd"><div class="disc-cmd-head"><span>Listar servidores activos con AWS CLI</span></div><pre><code>aws ec2 describe-instances --query "Reservations[].Instances[].State.Name"</code></pre></div>

## Suele confundirse con
Suele confundirse con un servicio tradicional de alojamiento web. Mientras un hosting básico alberga páginas estáticas en servidores fijos, AWS es una plataforma de infraestructura integral que abarca desde redes neuronales hasta computación cuántica.

## Perspectivas interdisciplinares
- **Red Eléctrica:** Conectar electrodomésticos a la pared en lugar de instalar un generador propio.
- **Almacenes de Alquiler:** Contratar metros cuadrados conforme crece el inventario.
- **Vehículos Compartidos:** Desplazarse pagando por minutos sin comprar un automóvil.

## Por analogía
Es como conectarse a la red eléctrica municipal en lugar de construir una central eléctrica propia: consume la energía que necesita y paga exactamente por lo medido.

## Preguntas frecuentes

**¿Por qué las empresas eligen AWS?**  
Elimina la inversión inicial en hardware, permite expandirse internacionalmente en minutos y flexibiliza los gastos de infraestructura.

**¿Se puede comenzar a utilizar sin coste?**  
Sí. La capa gratuita de AWS (Free Tier) ofrece niveles de servicio sin coste mensual para familiarizarse con las tecnologías clave.

**¿Dónde residen físicamente los datos?**  
En la Región geográfica elegida por el cliente, lo que facilita el cumplimiento de normativas de soberanía de datos como el RGPD.

**¿Cómo prevenir costes imprevistos?**  
Configurando alarmas de presupuesto en AWS Budgets, eliminando discos sin asignar y aplicando etiquetas estrictas a cada proyecto.

## Términos relacionados
- [Computación en la Nube](/es/dictionary/cloud-computing/)
- [IaaS](/es/dictionary/iaas/)
- [PaaS](/es/dictionary/paas/)

---
Fuente: Diccionario Tecnológico TreScout · https://trescout.com/es/dictionary/aws/
