# ¿Qué es Intermediate CA?

*Desarrollo · Última actualización: 21 de octubre de 2026*

> Intermediate Certificate Authority

Una entidad emisora intermedia ubicada entre el usuario final y el certificado raíz que verifica la identidad de los sitios web seguros.

## Definición

Una autoridad de certificación intermedia (CA intermedia) es una institución de confianza intermedia autorizada por la autoridad de certificación raíz que constituye la base de las conexiones HTTPS seguras en Internet. Dado que el uso del certificado raíz directamente en servidores expuestos a Internet crea un riesgo de seguridad, esta tarea se delega en los certificados intermedios. Por lo tanto, mientras se protege la cadena de confianza principal, los certificados de seguridad digital se pueden distribuir de forma segura a los sitios web.

***Analogía:** Es similar a que el gobierno, en lugar de emitir documentos de identidad directamente desde su oficina central, otorgue una autorización a la oficina del jefe de barrio (muhtar) para llevar a cabo los procesos de aprobación a través de ella.*

## Cómo funciona

Cuando su navegador accede a un sitio web, el servidor le presenta una cadena de certificados. Esta cadena comienza desde el certificado de usuario final, pasa por el certificado intermedio y llega hasta el certificado raíz principal preinstalado en su dispositivo, estableciendo así el vínculo de confianza.

## Dónde se usa

Participa activamente en la gestión de certificados SSL/TLS, las configuraciones de servidores web y las infraestructuras de seguridad empresarial.

## Suele confundirse con

No es el certificado raíz principal en sí mismo, sino el paso intermedio que actúa como un puente que transporta la confianza entre la raíz y el punto final.

## Preguntas y respuestas

**¿Por qué no se utiliza directamente el certificado raíz en lugar del certificado intermedio?**

Si la clave privada del certificado raíz se ve comprometida, toda la seguridad de Internet podría venirse abajo; por lo tanto, el riesgo se limita mediante el uso de certificados intermedios.

**¿Cómo verifican los navegadores el certificado intermedio?**

El servidor transmite los certificados intermedios faltantes al navegador y este completa la verificación utilizando la cadena de confianza integradas.

## Términos relacionados

- [End-to-End Encryption](https://trescout.com/es/dictionary/end-to-end-encryption/)
- [Identity Provider](https://trescout.com/es/dictionary/identity-provider/)
- [OIDC](https://trescout.com/es/dictionary/oidc/)
- [Vulnerability Scanning](https://trescout.com/es/dictionary/vulnerability-scanning/)

Esta explicación se redactó en lenguaje sencillo para TreScout con IA y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/intermediate-ca/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/intermediate-ca/
