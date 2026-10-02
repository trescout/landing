# Juego de estrategia ligero y de código abierto.

Unciv es una adaptación de Android y de escritorio de código abierto, minimalista y multiplataforma de Civilization V. Desarrollado con infraestructura Kotlin y LibGDX, el proyecto ofrece mecánicas de estrategia 4X originales sin carga de hardware y alto soporte de modificación.

- ★ 11.379
- Kotlin
- GitHub Trending · 2026-06-18

## Qué aporta
- Arquitectura de bajo hardware y compatible con batería: funciona sin calentamiento incluso en los dispositivos móviles más básicos mediante el uso de gráficos vectoriales y de píxeles 2D en lugar de pesados ​​motores de renderizado 3D.
- Mecánicas originales de Civilization V: la planificación urbana, el árbol tecnológico, las políticas sociales, la diplomacia y el sistema táctico de combate hexagonal se conservan por completo.
- Soporte multiplataforma para guardar y multijugador: puedes mover archivos guardados directamente entre el escritorio y Android o jugar partidas multijugador por turnos basadas en correo electrónico/servidor.
- Rico ecosistema de mods impulsado por la comunidad: se pueden instalar y activar nuevas civilizaciones, unidades, escenarios de fantasía y temas gráficos con un solo clic desde la interfaz del juego.
- Experiencia completamente gratuita y sin publicidad: Distribuido bajo licencia MPL-2.0; no contiene compras dentro de la aplicación, publicidad, seguimiento o recopilación de datos.

## Cómo empezar y opciones de instalación
- Página de Google Play Store →
- Repositorio de código abierto F-Droid →
- Versiones de escritorio de itch.io →

## Arquitectura técnica y principio de funcionamiento
- Motor de juego impulsado por el estado: cada casilla hexagonal, unidad, ciudad y relación diplomática en el tablero de juego se almacena como objetos JSON puros. Esta estructura mantiene el tamaño de los archivos de registro en sólo unos pocos cientos de kilobytes.
- Motor de modificación declarativo: las características de la civilización, los árboles tecnológicos y los costos de construcción se definen mediante archivos JSON sin tocar el código fuente. De esta forma, los desarrolladores de mods no necesitan un compilador externo.
- Cálculo de rondas determinista: los movimientos de la IA y los resultados de las batallas se calculan con algoritmos predecibles. Esto evita interrupciones en la sincronización en juegos multijugador asíncronos.
- Compilación multiplataforma: gracias a LibGDX, se incluye una única base de código Kotlin con rendimiento nativo para escritorio (JVM) y dispositivos móviles (tiempo de ejecución de Android).

## Estrategias de juego y dinámicas 4X.
- Exploración del mapa en las primeras rondas: distribuye tus unidades de guerreros y exploradores por el mapa temprano para recolectar artefactos antiguos, hacer el primer contacto con ciudades-estado y obtener ingresos en oro.
- Felicidad y equilibrio alimentario: al establecer nuevas ciudades, tenga cuidado de estar dentro del alcance de recursos de lujo. Cuando su tasa de felicidad cae a negativo, el crecimiento de la población y la producción se desaceleran significativamente.
- Hoja de ruta tecnológica: concéntrate en las fortalezas de tu civilización en lugar de en investigaciones aleatorias; Sigue los caminos de la herrería y la pólvora para la victoria militar, la filosofía y la educación para la victoria cultural.
- Aprovechar las ventajas del terreno: repele a grandes ejércitos con un pequeño número de unidades creando defensas junto al río, ventajas en las colinas y pasos estrechos.

## Si no programa
Quiero preparar una estructura mod JSON válida para el juego Unciv. ¿Puedes crear una plantilla de mod Unciv de muestra que incluya una unidad de caballería especial y un edificio de biblioteca especial que otorgue una bonificación a la producción científica y cultural como habilidad de líder? ¿Puedes explicar paso a paso qué archivos JSON debo guardar en qué estructura de carpetas y cómo puedo probar esto desde la interfaz de Mod Manager del juego?

## Preguntas frecuentes
- ¿Qué tan similar es Unciv a Civilization V? La mecánica del juego, las estadísticas de las unidades, el árbol tecnológico y las condiciones de victoria son en gran medida compatibles con los complementos Civilization V Gods and Kings y Brave New World. La diferencia es básicamente el uso de un diseño visual 2D simple en lugar de gráficos 3D.
- ¿Se requiere una conexión a Internet para jugar? No. Unciv se puede jugar completamente sin conexión. No se requiere conexión de red para jugar contra oponentes de IA en el modo para un jugador. Sólo las descargas de mods y las partidas multijugador requieren una conexión.
- ¿Cómo instalar modificaciones Unciv? Al ir a la pestaña Mods en el menú principal, puedes enumerar cientos de mods cargados por la comunidad y descargarlos a tu dispositivo con un solo clic. También puedes instalarlo directamente agregando un enlace a cualquier repositorio de mods en GitHub.
- ¿Se pueden transferir archivos de grabación entre el escritorio y el teléfono? Sí. Puedes copiar el archivo guardado al portapapeles desde el menú de grabación del juego, enviarlo a tu otro dispositivo por correo electrónico o mensaje en formato de texto y continuar donde lo dejaste con la carga desde la opción del portapapeles allí.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/unciv/
