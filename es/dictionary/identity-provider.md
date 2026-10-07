# ¿Qué es Identity Provider?

Un proveedor de identidad (identity provider) es el servicio central que verifica los inicios de sesión.

## Definición y origen de la palabra
En lugar de una contraseña separada para cada aplicación, se realiza un inicio de sesión desde un centro único. La aplicación pregunta al servicio quién es usted y recibe la confirmación. Su contraseña no se distribuye a las aplicaciones, permanece en el centro.

## ¿Cómo saberlo y utilizarlo en la vida diaria?
Compañía: Todos los sistemas con un solo inicio de sesión.Web: Inicio de sesión con cuenta social.Institucional: Ciclo de vida del empleado.

## Profundidad técnica y arquitectura
Flujo:

## Cosas frecuentemente mezcladas
Se confunde con un gestor de contraseñas. Aquel guarda la contraseña, este confirma la identidad. Uno es una caja fuerte, el otro es un notario.

## Uso en diferentes disciplinas
Recepción: Pasaporte frente a tarjeta llave.Notario: Certificación de identidad.Control de pasaportes: Acceso mediante sello.

## Preguntas frecuentes
**¿Es seguro?**
Sí. Como la contraseña no se distribuye a cada aplicación, la superficie de ataque se reduce.

**¿Qué pasa si el sistema falla?**
Las aplicaciones conectadas se ven afectadas. La redundancia y un plan de acceso de emergencia son obligatorios.

**¿Cuál es la diferencia con SSO?**
SSO es una experiencia de inicio de sesión único, es la infraestructura del proveedor. Uno es la cara, el otro es la columna vertebral.

**¿Puedo instalarlo yo mismo?**
Sí, existen opciones de código abierto. La disciplina de parches y copias de seguridad depende de usted.


## Términos relacionados
- [SSO](/es/dictionary/sso/)
- [OIDC](/es/dictionary/oidc/)
- [RBAC](/es/dictionary/rbac/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/identity-provider/
