# Juego de estrategia ligero y de código abierto

Unciv es una adaptación de código abierto, minimalista y multiplataforma de Civilization V para escritorio y Android. Desarrollado con Kotlin y LibGDX, el proyecto ofrece las mecánicas originales de estrategia 4X sin sobrecarga de hardware y con amplio soporte para mods.

- ★ 11.285
- Kotlin
- GitHub Trending · 2026-06-18

## Actualizaciones
- 18 de septiembre de 2026: Estrellas 11.276 → 11.285, última versión 4.22.1 (17 de septiembre de 2026).
- 15 de septiembre de 2026: Estrellas 11.257 → 11.276, última versión 4.22.0 (14 de septiembre de 2026).
- 10 de septiembre de 2026: Estrellas 11.241 → 11.257, última versión 4.21.19 (9 de septiembre de 2026).
- 8 de septiembre de 2026: Estrellas 11.223 → 11.241, última versión 4.21.18 (7 de septiembre de 2026).

## Qué aporta
- Arquitectura ligera y de bajo consumo: Emplea gráficos 2D para funcionar con fluidez incluso en dispositivos modestos sin calentamiento.
- Mecánicas originales de Civilization V: Planificación urbana, árbol tecnológico, políticas sociales y combates tácticos hexagonales.
- Partidas guardadas cruzadas y multijugador: Pasa tus partidas entre Android y PC o compite en partidas por turnos.
- Ecosistema de mods de la comunidad: Añade civilizaciones, unidades y escenarios con un solo clic desde el menú.
- Totalmente libre y sin anuncios: Licencia MPL-2.0, sin compras dentro de la app, seguimiento ni publicidad.

## Cómo empezar y opciones de instalación

Unciv está disponible en múltiples plataformas. En Android puedes instalarlo desde Google Play Store o F-Droid. En escritorio (Windows, Linux, macOS), puedes descargar los ejecutables, Flatpak o itch.io.
- [Página en Google Play Store →](https://play.google.com/store/apps/details?id=com.unciv.app)
- [Repositorio de código abierto en F-Droid →](https://f-droid.org/packages/com.unciv.app/)
- [Versiones de escritorio en itch.io →](https://yairm210.itch.io/unciv)

## Arquitectura técnica y funcionamiento interno

Unciv está desarrollado sobre LibGDX y Kotlin, organizando la lógica del juego sobre un estado ligero y determinista:
- Motor de juego basado en estado: Hexágonos, unidades y ciudades se guardan en JSON puro, produciendo archivos de guardado muy pequeños.
- Motor de mods declarativo: Reglas, costes y civilizaciones se definen en JSON sin necesidad de compilar código fuente.
- Cálculo de turnos determinista: Las decisiones de la IA y combates son predecibles para evitar desincronizaciones en multijugador.
- Compilación multiplataforma: Una única base de código Kotlin compila nativamente para escritorio (JVM) y Android.

## Estrategias de juego y dinámicas 4X

Unciv traslada a la perfección los cuatro pilares 4X: eXplore, eXpand, eXploit y eXterminate:
- Exploración en los primeros turnos: Envía guerreros y batidores a recoger ruinas antiguas y contactar con ciudades-estado.
- Equilibrio de felicidad y alimento: Funda ciudades cerca de recursos de lujo para no frenar el crecimiento de tu población.
- Hoja de ruta tecnológica: Enfoca tu investigación en las ventajas particulares de tu civilización.
- Aprovechamiento del terreno: Defiende tras ríos y sobre colinas para neutralizar ejércitos superiores con pocas unidades.

## Si no programas
🤖 Si no programas
Quiero crear un mod en formato JSON válido para Unciv. ¿Podrías crear una plantilla con un líder que dé bonificaciones de ciencia y cultura, una unidad de caballería personalizada y una biblioteca única? Explícame la estructura de carpetas y cómo probarlo desde el Mod Manager del juego.

- **Para quién:** Jugadores y creadores de mods que buscan estrategia 4X clásica en formato ligero y sin publicidad.
- **Licencia:** MPL-2.0 (Mozilla Public License 2.0)
- **Motor de juego:** LibGDX (Kotlin multiplataforma)
- **Plataformas:** Android, Windows, Linux, macOS

## Preguntas frecuentes
- ¿Cuánto se parece Unciv a Civilization V? Las mecánicas, tecnologías y unidades coinciden prácticamente al 100% con Civ V y sus expansiones, en formato 2D.
- ¿Requiere conexión a internet para jugar? No, Unciv es totalmente jugable sin conexión contra la IA. Solo hace falta internet para descargar mods o multijugador.
- ¿Cómo se instalan los mods? Desde el menú de Mods dentro del juego puedes explorar e instalar cientos de modificaciones con un solo clic.
- ¿Se pueden pasar partidas entre PC y móvil? Sí, puedes copiar la partida guardada al portapapeles desde el menú y cargarla en el otro dispositivo con un toque.

## Enlaces
- [GitHub →](https://github.com/yairm210/Unciv)
- [Read in Turkish →](https://trescout.com/discover/unciv/)

## Términos relacionados del glosario
Open Source Offline

---
Source: TreScout Discover · https://trescout.com/es/discover/unciv/
