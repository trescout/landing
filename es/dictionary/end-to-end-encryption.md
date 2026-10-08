# ¿Qué es End-to-End Encryption?

*Glosario · Dev · Última actualización: 22 de septiembre de 2026*

> E2EE

El cifrado de extremo a extremo (end-to-end encryption) es un sistema de seguridad que solo permite la lectura a los extremos.

## Definición y origen de la palabra

Los datos se bloquean en el dispositivo y se desbloquean en el destino. El transportista y el servidor no pueden ver el contenido. Es el escudo fundamental de la privacidad. WhatsApp y Signal son ejemplos conocidos.

***Analogía:** Es similar a intercambiar cartas con una caja cuya llave solo tienen ustedes dos.*

## ¿Cómo saberlo y utilizarlo en la vida diaria?

**Mensaje:** Chats privados.
**Archivo:** Transferencia segura.
**Respaldo:** Copia cifrada.

## Profundidad técnica y arquitectura

Diseño:

**Par de claves:** Clave pública y privada.
**Verificación:** Identidad de la otra parte.
**Secreto de transmisión:** La clave de sesión se actualiza.

Regla: La copia de seguridad se mantiene cifrada, la clave se guarda por separado. En caso de pérdida del dispositivo, se requiere un código de recuperación.

## Cosas frecuentemente mezcladas

Se confunde con TLS. TLS protege en tránsito, el servidor puede ver el contenido. En el cifrado de extremo a extremo, ni siquiera el servidor puede verlo. Uno es como una armadura de mensajero, el otro es un sobre sellado.

## Uso en diferentes disciplinas

**Caja cerrada con llave:** El transportista no puede ver el contenido.
**Sello:** Un sobre que se nota si ha sido abierto.
**Circuito cerrado:** Línea cerrada al exterior.

## Preguntas frecuentes

**¿Se puede leer si es robado?**

No. La clave está en los extremos, lo robado es un montón de datos sin sentido.

**¿Está disponible en todas las aplicaciones?**

No. Se verifica en la configuración, no se hacen suposiciones.

**¿Cómo se realiza la copia de seguridad?**

Se requiere una copia de seguridad cifrada y un código de recuperación. No hay forma de restaurar sin el código.

**¿Es adecuado para empresas?**

Se equilibra con la necesidad de registro y auditoría. Se establece la política.

## Términos relacionados

- [Security Scanner](https://trescout.com/es/dictionary/security-scanner/)
- [Linux Server Security](https://trescout.com/es/dictionary/linux-server-security/)
- [SSO](https://trescout.com/es/dictionary/sso/)

## Herramientas relacionadas

- [Croc](https://trescout.com/es/discover/croc/)

Esta explicación se redactó en lenguaje sencillo para TreScout y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/end-to-end-encryption/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/end-to-end-encryption/
