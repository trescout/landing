# ¿Qué es Service Mesh?

*Glosario · Dev · Última actualización: 22 de septiembre de 2026*

Service mesh es la capa de infraestructura invisible que gestiona el tráfico de los microservicios.

## Definición y origen de la palabra

En sistemas fragmentados con cientos de piezas, es difícil que se encuentren entre sí y se comuniquen de forma segura. El service mesh gestiona la comunicación, regula el tráfico y garantiza la seguridad. Aplica políticas de red sin tocar el código.

***Analogía:** Es como la torre que gestiona el tráfico de vuelos en un aeropuerto grande; garantiza que los servicios se desplacen de forma segura sin chocar entre sí.*

## ¿Cómo saberlo y utilizarlo en la vida diaria?

**Nube:** Grandes aplicaciones basadas en microservicios.
**Banco:** Tráfico de servicios con seguridad estricta.
**Comercio electrónico:** Línea de pedidos bajo carga de campañas.

## Profundidad técnica y arquitectura

Regiones:

**Sidecar:** Pequeño proxy junto a cada servicio, por donde fluye el tráfico.
**Control plane:** El cerebro que distribuye las reglas.
**Data plane:** Los agentes que realizan el trabajo.
**mTLS:** Identidad cifrada entre servicios.
**Resiliencia:** Reintento y disyuntor.

Regla de reintento:

```
retries:
  attempts: 3
  perTryTimeout: 2s
```

Istio y Linkerd son implementaciones conocidas. En un sistema pequeño, el costo supera al beneficio.

## Uso en diferentes disciplinas

**Aeropuerto:** La torre que evita que los aviones colisionen.
**Tráfico:** La red de señales que regula el flujo.
**Correo:** El centro de distribución que separa el envío.

## Preguntas frecuentes

**¿Es necesario para cada proyecto?**

No. Aporta carga en un sistema con pocos servicios. Cobra sentido cuando la complejidad aumenta.

**¿Cuánto cuesta?**

Añade memoria y latencia por proxy. Se paga a cambio de una mayor observabilidad.

**¿Es Kubernetes obligatorio?**

No, pero a menudo se usan juntos. También hay versiones que se ejecutan en máquinas virtuales.

**¿Reemplaza al API gateway?**

No. El gateway es la puerta exterior, el mesh es el tráfico interno. Ambos trabajan juntos.

## Términos relacionados

- [Cloud Native](https://trescout.com/es/dictionary/cloud-native/)
- [API](https://trescout.com/es/dictionary/api/)
- [Proxy](https://trescout.com/es/dictionary/proxy/)

## Herramientas relacionadas

- [Meshery](https://trescout.com/es/discover/meshery/)

Esta explicación se redactó en lenguaje sencillo para TreScout y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/service-mesh/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/service-mesh/
