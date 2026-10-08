# ¿Qué es Amazon Web Services?

*Glosario · Dev · Última actualización: 22 de septiembre de 2026*

> Amazon Web Services

AWS (Amazon Web Services) es una plataforma en la nube donde se alquilan servicios de TI como servidores, almacenamiento y bases de datos desde Internet.

## Definición y origen de la palabra

En lugar de construir su propio servidor físico, alquila los centros de datos de Amazon. Cuando aumenta la necesidad, aumenta la capacidad y cuando se completa el trabajo, disminuye. Funciona con el modelo de pago que aumenta a medida que lo utilizas. Casi todas las aplicaciones modernas tienen este tipo de infraestructura en la nube en segundo plano.

***Analogía:** Es como comprar electricidad de la red en lugar de construir su propia central eléctrica; Sólo pagas por lo que usas.*

## ¿Cómo saberlo y utilizarlo en la vida diaria?

**Sitio web:** Servidores que crecen según el tráfico.
**Respaldo:** Una bóveda de archivos aparentemente interminable.
**Video:** Contenido distribuido a medida que se ve.
**Startup:** No salga al aire sin configurar una sala de servidores.

## Profundidad técnica y arquitectura

Servicios básicos:

**EC2:** Alquiler de servidor virtual.
**P3:** Almacenamiento de objetos, respaldo y bóveda de archivos estáticos.
**RDS:** Base de datos relacional administrada.
**lambda:** Función sin servidor que se ejecuta cuando ocurre un evento.

Conceptos:

**Región y zona de acceso:** Ubicación física de datos y redundancia.
**Responsabilidad compartida:** La seguridad de la nube es responsabilidad de Amazon, la seguridad de los datos que contiene es suya.
**Nivel gratuito:** Uso gratuito limitado para cuentas nuevas.

Para enumerar los servidores en ejecución:

```
aws ec2 describe-instances --query "Reservations[].Instances[].State.Name"
```

Se recomienda configurar una alarma de presupuesto para evitar sorpresas en las facturas, porque se siguen cobrando recursos abiertos y olvidados.

## Cosas frecuentemente mezcladas

Se cree que es sólo un servicio de alojamiento de sitios. Sin embargo, es una plataforma de infraestructura completa que cubre bases de datos, inteligencia artificial, redes y capas de seguridad con más de 200 servicios.

## Uso en diferentes disciplinas

**Red eléctrica:** Desconectar en lugar de instalar una centralita.
**Bodega en alquiler:** Alquiler de tantas estanterías como sean necesarias.
**Taxi:** Viajar sin vehículo propio.

## Preguntas frecuentes

**¿Por qué debería utilizar AWS?**

Tiene acceso instantáneo a la infraestructura corporativa sin realizar ninguna inversión en hardware. Si el tráfico fluctúa, los servicios escalables y listos para usar ahorran tiempo.

**¿Puedo empezar gratis?**

Sí. Los términos del plan gratuito, el crédito y los plazos para cuentas nuevas pueden cambiar con el tiempo; Antes de comenzar, debe verificar los límites actuales en la página de la capa gratuita de AWS.

**¿Dónde se guardan mis datos?**

Se conserva en la región que elijas. Para regulaciones como KVKK, debe seleccionar la región y el cifrado de acuerdo con su política.

**¿Cómo mantener la factura bajo control?**

Con alertas de presupuesto, limpieza de recursos no utilizados y ajuste de tamaño. La disciplina de etiquetado es esencial en equipos pequeños.

## Términos relacionados

- [Cloud Computing](https://trescout.com/es/dictionary/cloud-computing/)
- [IaaS](https://trescout.com/es/dictionary/iaas/)
- [PaaS](https://trescout.com/es/dictionary/paas/)

Esta explicación se redactó en lenguaje sencillo para TreScout y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/aws/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/aws/
