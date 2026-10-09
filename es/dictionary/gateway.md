# ¿Qué es Gateway?

*Glosario · Dev · Última actualización: 22 de septiembre de 2026*

Gateway es el punto de conexión que gestiona el tráfico entre diferentes redes.

## Definición y origen de la palabra

"Puerta" significa puerta y "camino" significa camino. Es el puente que permite que dos redes se comuniquen entre sí: el dispositivo que conecta Internet en su hogar con el mundo exterior es un ejemplo típico. Examina los datos entrantes y decide a qué red irá.

***Analogía:** Es como la puerta fronteriza de un país; Controla las llegadas y garantiza que vayan en la dirección correcta.*

## ¿Cómo saberlo y utilizarlo en la vida diaria?

**Módem doméstico:** Conecta tu hogar a la red del proveedor.
**Inicio de sesión corporativo:** Punto de control del tráfico de oficinas.
**Nube:** La puerta de entrada de las redes virtuales entre sí.

## Profundidad técnica y arquitectura

Obras de la puerta:

**Traducción de direcciones (NAT):** Extrae direcciones internas de una sola dirección.
**Filtración:** Mantiene el tráfico no deseado en la puerta.
**Orientación:** Entrega el paquete a la red correcta.

La información de ruta predeterminada es:

```
default via 192.168.1.1 dev eth0
```

Esta línea le indica que el destino no reconocido se enviará a través del módem. La puerta de enlace API se encuentra en una capa diferente: gestiona las solicitudes de servicio, no la red.

## Cosas frecuentemente mezcladas

Se puede confundir con API Gateway. API Gateway gestiona los servicios de software, la puerta de enlace opera a nivel de red. Una es la puerta de la aplicación y la otra es la puerta de la ruta.

## Uso en diferentes disciplinas

**Puerta fronteriza:** Supervisión y orientación de llegadas.
**Puerto:** Buques que pasan por la aduana.
**Recepción:** Dirigir al visitante al piso correcto.

## Preguntas frecuentes

**¿Puedo acceder a Internet sin una puerta de enlace?**

No. La red local no se puede conectar con el mundo exterior, permanece aislada.

**¿Cuál es la diferencia con la puerta de enlace API?**

La puerta de enlace transporta el paquete, la puerta de enlace API maneja la solicitud. Uno es la ruta y el otro es la capa de aplicación.

**¿Cuál se usa en casa?**

La puerta de enlace dentro de su módem funcionará. No se requieren configuraciones adicionales, la dirección se distribuye automáticamente.

**¿Se pueden mantener separadas las dos redes?**

Sí. Con reglas de firewall, el acceso está cerrado y las redes operan aisladas.

## Términos relacionados

- [API Gateway](https://trescout.com/es/dictionary/api-gateway/)
- [Network Stack](https://trescout.com/es/dictionary/network-stack/)
- [Proxy](https://trescout.com/es/dictionary/proxy/)

## Herramientas relacionadas

- [OmniRoute](https://trescout.com/es/discover/omniroute/)
- [Litellm](https://trescout.com/es/discover/litellm/)
- [Fanqiang](https://trescout.com/es/discover/fanqiang/)
- [Gitdiagram](https://trescout.com/es/discover/gitdiagram/)
- [OpenWA](https://trescout.com/es/discover/openwa/)
- [Grok2api](https://trescout.com/es/discover/grok2api/)

Esta explicación se redactó en lenguaje sencillo para TreScout y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/gateway/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/gateway/
