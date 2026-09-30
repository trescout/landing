# Análisis de usuarios OSINT en más de 465 plataformas

User-Scanner basado en Python realiza escaneo de inteligencia de código abierto (OSINT) en más de 465 redes sociales, foros y repositorios de código desde un único nombre de usuario o correo electrónico.

- ★ 5.007
- Python
- GitHub Trending · 2026-08-31

## Qué aporta
- Amplia cobertura de plataforma: verifique la presencia de la cuenta en GitHub, Reddit, Twitter, Steam, Telegram y más de 465 sitios de una sola vez.
- Escaneo asincrónico de alta velocidad: consulta en paralelo de cientos de objetivos en segundos con arquitectura basada en asyncio y aiohttp.
- Filtrado de falsos positivos: mecanismo de detección inteligente que verifica los textos de error en el cuerpo de la respuesta, así como los códigos de estado HTTP.
- Exportación de informes JSON y CSV: guardar los resultados del análisis en formatos configurados para su uso en informes forenses y de seguridad.
- Privacidad y ejecución local: Posibilidad de ejecutar cualquier consulta completamente desde la máquina local, sin enviarla a servidores de terceros.

## Instalación
**Clonando el repositorio e instalando dependencias**

```
git clone https://github.com/kaifcodec/user-scanner.git
cd user-scanner
pip install -r requirements.txt
```


## Ejecución
**Escanear nombre de usuario y correo electrónico de destino**

```
python3 user_scanner.py -u hedef_kullanici
# veya e-posta ile:
python3 user_scanner.py -e hedef@ornek.com
```


## Arquitectura técnica y principio de funcionamiento
- Plantillas de bases de datos (manifiestos de sitio JSON): configuración modular que contiene patrones de URL, códigos de error y expresiones regulares de perfil para más de 465 plataformas.
- Agrupación de solicitudes simultáneas: uso más eficiente del ancho de banda de la red mediante el almacenamiento en caché de resoluciones DNS y sockets TCP.
- Encabezados HTTP personalizados y rotación de agente de usuario: simulación realista de encabezados del navegador para evitar obstrucciones de límite de velocidad y WAF.

## Escenarios de investigación OSINT y análisis de datos.
- Seguimiento y violación de datos personales: mapee en qué canales sociales están activos los perfiles filtrados con la correlación del nombre de usuario.
- Auditorías de Seguridad Corporativa: Determinar si los empleados de la empresa abren cuentas en plataformas externas con sus direcciones de correo electrónico corporativas.
- Defensa de ingeniería social: identifique tempranamente cuentas de imitación no autorizadas contra ataques de phishing.

## Si no programa
¿Puedes explicar paso a paso cómo puedo escanear más de 465 plataformas usando un solo nombre de usuario usando la herramienta User-Scanner en una auditoría de seguridad, exportar los hallazgos en formato JSON y enumerar perfiles sospechosos?

## Preguntas frecuentes
- ¿Es legal utilizar User-Scanner? Sí. User-Scanner solo consulta el estado de presencia de la cuenta públicamente visible en páginas web públicas; No proporciona ningún acceso no autorizado al sistema ni descifra contraseñas.
- ¿Hay soporte para Tor o proxy? Sí. Puede enmascarar su dirección IP y evitar límites de velocidad enrutando solicitudes a través de SOCKS5 o cadenas de proxy HTTP.
- ¿Cuánto tiempo se tarda en completar los resultados? Gracias a su arquitectura asincrónica, el escaneo de más de 465 plataformas normalmente se completa en 20 a 45 segundos, dependiendo de su conexión a Internet.
- ¿Cómo funciona la búsqueda de correo electrónico? En el modo de correo electrónico, las señales de autenticación pública se examinan en los puntos finales de restablecimiento de contraseña o registro de cuenta de los servicios compatibles.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/user-scanner/
