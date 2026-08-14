# ¿Qué es Secrets?

Estas son las contraseñas, claves API y códigos de acceso que las aplicaciones de software necesitan para funcionar de forma segura.

## Definición
Los secretos son información secreta que utiliza un programa para autenticarse cuando se conecta a otro sistema. A menudo pueden ser contraseñas de bases de datos, claves privadas o tokens de acceso a servicios. Dado que incorporar esta información en el código supone un riesgo para la seguridad, normalmente se almacena en sistemas de bóvedas especiales.

## Cómo funciona
En lugar de escribir esta información confidencial en archivos de código, los desarrolladores la definen de forma segura en la aplicación mediante variables de entorno o herramientas de gestión confidencial.

## Dónde se usa
Se utiliza en servicios en la nube, conexiones de bases de datos y procesos de autenticación de aplicaciones.

## Suele confundirse con
Puede confundirse con las contraseñas de usuario habituales, pero se trata de identidades digitales diseñadas para máquinas, no para personas.

## Preguntas frecuentes
**¿Por qué no se guardan secretos dentro del código?**
Cuando compartes tu código o lo subes accidentalmente a Internet, cualquiera puede obtener estas claves e infiltrarse en tus sistemas.

**¿Qué debo hacer si me roban Secrets?**
Debes cancelar inmediatamente esa clave, crear una nueva y comprobar si hay alguna infiltración en tu sistema.


## Términos relacionados
- [API](/es/dictionary/api/)
- [Self-hosting](/es/dictionary/self-hosting/)
- [Observability](/es/dictionary/observability/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/secrets/
