# Registro rápido para proyectos C++

spdlog es una biblioteca de registro ultrarrápida desarrollada para el lenguaje de programación C++, que puede usarse solo como encabezado o como una biblioteca compilada. Ofrece gestión de salida de alto rendimiento y sin demoras en proyectos de software que utilizan estándares C++ modernos.

- ★ 29.437
- C++
- GitHub Trending · 2026-08-05

## Qué aporta
- Rendimiento de registro de millones de líneas por segundo: crea una latencia de nivel de microsegundos en el subproceso principal de la aplicación con un enfoque de asignación de memoria cero y optimizaciones en tiempo de compilación.
- Cola de anillo asincrónica y sin bloqueos: aísla completamente los cuellos de botella de E/S de red o archivos de la canalización de llamadas mediante la descarga de escrituras de registros al grupo en segundo plano.
- Amplia variedad de objetivos: salida de consola colorida, archivos que rotan por tamaño, archivos con fechas diarias, escritura simultánea en objetivos syslog y logcat de Android.
- Potencia de formato fmt integrada: proporciona formato de texto estilo Python seguro, rápido y flexible utilizando la biblioteca {fmt}, que es la base del estándar de formato C++20.
- Flexibilidad de uso compilado o solo de encabezado: puede incluirlo en su proyecto copiando un único directorio o vinculándolo como una biblioteca estática para reducir los tiempos de compilación.

## Instalación
**macOS (Homebrew)**

```
brew install spdlog
```


## Cómo empezar y uso básico
Comenzar a utilizar la biblioteca spdlog es muy sencillo. Una vez que incluya el archivo de encabezado en su proyecto, puede llamar a funciones de registro globales directamente o crear objetos de registro personalizados:

## Arquitectura técnica y principio de funcionamiento
- Distinción de registrador y receptor: el objeto Logger filtra el registro entrante (rastreo, depuración, información, advertencia, error, crítico). Los mensajes aceptados se transfieren a uno o más objetos Sink. Por ejemplo, un único registrador puede escribir en el archivo en formato JSON y al mismo tiempo imprimir en color en la consola.
- Seguro para subprocesos (_mt vs _st): spdlog proporciona todas las clases de receptores en dos formas: versiones con bloqueo mutex seguro para múltiples subprocesos (_mt) y versiones sin bloqueo específicas de un solo subproceso (_st). En el modo de un solo subproceso, el costo del mutex es completamente cero.
- Cola de anillo asíncrona (Ring Buffer): el bloque de memoria asignado con spdlog::init_thread_pool es consumido por el subproceso que se ejecuta en segundo plano. La aplicación principal deja el registro en la cola y continúa su camino inmediatamente.
- Vaciado inteligente del búfer (Flush): los datos se guardan en el búfer del sistema operativo para mejorar el rendimiento; Sin embargo, el mecanismo spdlog::flush_on(spdlog::level::err) se puede activar para evitar la pérdida de datos en momentos críticos de error.

## Si no programa
Quiero configurar la biblioteca spdlog con arquitectura asincrónica usando CMake en un proyecto moderno de C++. ¿Puede preparar el archivo CMakeLists.txt con una función de inicialización de C++ de muestra que rota el archivo cuando el registro alcanza los 10 MB de tamaño, también proporciona salida en color a la consola y lo descarga en el disco inmediatamente después del nivel de error?

## Preguntas frecuentes
- ¿Debería usarse spdlog solo con encabezado o compilarse? En proyectos pequeños y medianos, usar solo encabezado agregando solo el directorio de inclusión proporciona una gran practicidad. Sin embargo, en proyectos grandes de C++ que constan de cientos de archivos fuente, se recomienda compilar y vincular la biblioteca con el indicador SPDLOG_COMPILED para optimizar el tiempo de compilación.
- ¿El registro afecta la velocidad de ejecución de la aplicación principal? Al ejecutarse a nivel de microsegundos incluso en modo síncrono, spdlog reduce la carga de E/S en el subproceso principal a casi cero cuando se utiliza una arquitectura de registrador asíncrono. El mensaje se copia en la cola y la escritura en el disco se produce en segundo plano.
- ¿Cómo funciona el mecanismo de archivo giratorio? Cuando se alcanza el tamaño máximo de archivo especificado (por ejemplo, 10 MB), el archivo activo se archiva (application.1.txt, application.2.txt) y se abre un archivo nuevo desde cero. Cuando se excede el número máximo de archivos especificado, el archivo de registro más antiguo se borra automáticamente.
- ¿Habrá algún conflicto con la biblioteca fmt externa? No. spdlog utiliza la versión empaquetada internamente de fmt de forma predeterminada. Si lo desea, puede integrar directamente la biblioteca fmt independiente existente en su sistema con spdlog definiendo la macro SPDLOG_FMT_EXTERNAL.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/spdlog/
