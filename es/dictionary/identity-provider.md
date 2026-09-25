# ¿Qué es un Identity Provider?

> Proveedor de Identidad Digital

**Categoría:** Dev  
**Última actualización:** 2026-09-22

Un Identity Provider (IdP / Proveedor de Identidad) es un servicio centralizado que gestiona, autentica y valida las identidades digitales de los usuarios en múltiples aplicaciones y plataformas.

## Definición y etimología
En el desarrollo de software moderno, las aplicaciones individuales no deben almacenar contraseñas por separado. El IdP independiza la autenticación del código de negocio, facilitando el inicio de sesión único (Single Sign-On / SSO) seguro para múltiples servicios independientes.

## Contexto cotidiano e uso práctico
- **Acceso Social:** Botones de 'Iniciar sesión con Google o GitHub' en aplicaciones web y móviles.
- **Seguridad Corporativa:** Administración centralizada de permisos y políticas MFA con Okta o Microsoft Entra ID.
- **Entornos Autohospedados:** Despliegue de Keycloak o Authentik para orquestar la seguridad en arquitecturas de microservicios.

## Profundidad técnica y arquitectura
Estándares y Mecanismos Criptográficos:- **OpenID Connect (OIDC):** Protocolo de identidad sobre OAuth 2.0 que transmite tokens JWT firmados digitalmente.
- **SAML 2.0:** Estándar federado basado en esquemas XML común en administraciones y grandes corporaciones.
- **Autenticación Multifactor (MFA):** Protección añadida con llaves FIDO2/WebAuthn y aplicaciones de códigos TOTP.

## Suele confundirse con
Suele confundirse con un Service Provider (SP) o servidor de autorización. El IdP responde a '¿Quién eres?' (autenticación); la autorización define '¿A qué funciones tienes acceso?' (permisos).

## Perspectivas interdisciplinares
- **Trámites:** El ministerio que emite un pasaporte nacional vs el control aduanero que revisa el visado.
- **Alojamientos:** La recepción del hotel comprobando la identidad y entregando la tarjeta llave vs la puerta de la habitación.
- **Edificios:** La entrada principal emitiendo una acreditación vs los accesos a salas de reuniones privadas.

## Por analogía
Funciona exactamente como la recepción de un hotel: entrega su pasaporte una sola vez al registrarse, recibe una tarjeta de acceso electrónica y entra en su habitación sin necesidad de identificarse ante cada puerta.

## Preguntas frecuentes

**¿Cuál es la principal ventaja de utilizar un IdP?**  
Centraliza la seguridad de las credenciales, previene filtraciones en múltiples bases de datos y habilita inicio de sesión único (SSO).

**¿Cómo confirma el IdP la identidad a las aplicaciones?**  
Emitiendo tokens criptográficos firmados con atributos verificados del usuario.

**¿Existen alternativas de código abierto para desplegar un IdP propio?**  
Sí, suites consolidadas como Keycloak, Authentik y Authelia se pueden autohospedar de forma íntegra.

**¿Qué impacto tiene una caída del servicio de IdP?**  
Impide que los usuarios puedan autenticarse en los servicios dependientes; la redundancia de infraestructura resulta prioritaria.

## Términos relacionados
- [Cloud Computing](/es/dictionary/cloud-computing/)
- [Endpoint](/es/dictionary/endpoint/)
- [Application](/es/dictionary/application/)

---
Fuente: Diccionario Tecnológico TreScout · https://trescout.com/es/dictionary/identity-provider/
