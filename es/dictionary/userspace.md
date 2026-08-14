# ¿Qué es Userspace?

Un área segura donde se ejecutan las aplicaciones del usuario sin interferir con el kernel de la computadora.

## Definición
Los sistemas operativos se dividen en dos partes principales: kernel y espacio de usuario. El espacio de usuario es donde se ejecuta el navegador, el reproductor de música o los editores de código que utiliza. Un error aquí no bloqueará toda la computadora, solo afectará a esa aplicación.

## Cómo funciona
Las aplicaciones solicitan permiso del kernel para acceder a los recursos subyacentes del sistema. De esta forma, el resto del sistema queda protegido.

## Dónde se usa
Es un concepto fundamental en el desarrollo de software, seguridad y arquitectura de sistemas.

## Suele confundirse con
Se confunde con el espacio del núcleo; El kernel domina todo el sistema, mientras que el espacio de usuario es limitado.

## Preguntas frecuentes
**¿Por qué existe esta distinción?**
Por seguridad y estabilidad; Para evitar que las aplicaciones corrompan el sistema.

**¿Dónde se ejecuta el código que escribí?**
La mayoría de las aplicaciones y el código se ejecutan dentro del espacio de usuario.


## Términos relacionados
- [Runtime](/es/dictionary/runtime/)
- [Containers](/es/dictionary/containers/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/userspace/
