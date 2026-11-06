# ¿Qué es Password Authentication?

*Desarrollo · Última actualización: 6 de noviembre de 2026*

Es el proceso de utilizar una contraseña para verificar la identidad del usuario al iniciar sesión en el sistema.

## Definición

La autenticación por contraseña es un método para verificar la contraseña secreta establecida por un usuario con el fin de determinar si tiene derecho a acceder a un sistema digital. El sistema le pide al usuario que demuestre que es quien dice ser. La contraseña introducida se compara con su equivalente cifrado y almacenado de forma segura en la base de datos.

***Analogía:** Es similar a introducir y girar una llave en la cerradura de una puerta para entrar a una casa. Si la llave es correcta, la puerta se abre; si es incorrecta, te quedas afuera.*

## Cómo funciona

El nombre de usuario y la contraseña se escriben en la pantalla correspondiente y se envían. El software del lado del servidor no almacena la contraseña directamente como texto plano; en su lugar, la procesa a través de funciones hash matemáticas seguras. Si el hash de la contraseña recibida coincide con el hash en la base de datos, se concede el acceso.

## Dónde se usa

Se utiliza como capa de seguridad básica en inicios de sesión de sitios web, pantallas de inicio de sesión de computadoras, paneles de gestión de servidores en la nube y accesos a redes corporativas.

## Suele confundirse con

Se puede confundir con la autorización. La autenticación por contraseña demuestra quién eres, mientras que la autorización determina a qué puedes acceder una vez que ingresas al sistema.

## Preguntas y respuestas

**¿Cómo se almacenan las contraseñas en la base de datos?**

Por razones de seguridad, nunca se almacenan como texto plano. Se cifran de forma irreversible utilizando algoritmos de hash especiales y técnicas de salting (salado).

**¿Es suficientemente segura por sí sola?**

Hoy en día, dado que es fácil de robar o adivinar, generalmente se complementa con medidas adicionales como la verificación en dos pasos.

## Términos relacionados

- [SSO](https://trescout.com/es/dictionary/sso/)
- [OIDC](https://trescout.com/es/dictionary/oidc/)
- [RBAC](https://trescout.com/es/dictionary/rbac/)
- [Security Scanner](https://trescout.com/es/dictionary/security-scanner/)

Esta explicación se redactó en lenguaje sencillo para TreScout con IA y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/password-authentication/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/password-authentication/
