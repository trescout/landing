# Biblioteca rápida de registros para proyectos C++

spdlog es una biblioteca de registro (logging) ultrarrápida para C++, disponible como biblioteca de solo encabezados (header-only) o precompilada. Desarrollada con estándares C++ modernos, proporciona salidas sin latencia y con máximo rendimiento.

- ★ 29.437
- C++
- GitHub Trending · 2026-08-05

## Actualizaciones
- 6 de agosto de 2026: Estrellas 29.402 → 29.437, última versión v1.17.0 (4 de enero de 2026).

## Qué aporta
- Rendimiento de millones de líneas por segundo: Arquitectura sin asignaciones dinámicas para una latencia de microsegundos en el hilo principal.
- Cola circular asíncrona sin bloqueos: Transfiere la escritura a un grupo de hilos de fondo, protegiendo las rutas críticas de cuellos de botella de E/S.
- Múltiples destinos (sinks): Salida simultánea a consola con colores, archivos rotativos por tamaño, registros diarios y syslog.
- Potencia de formato {fmt} integrada: Usa la biblioteca {fmt} (estandarizada en C++20) para un formateo seguro, rápido y expresivo.
- Flexibilidad header-only o compilada: Intégrala copiando una carpeta en tu proyecto o enlázala estáticamente para compilaciones más rápidas.

## Instalación

**macOS (Homebrew)**

```
brew install spdlog
```

**Gestor vcpkg**

```
vcpkg install spdlog
```

**Integración CMake FetchContent**

```
include(FetchContent)
FetchContent_Declare(
  spdlog
  GIT_REPOSITORY https://github.com/gabime/spdlog.git
  GIT_TAG v1.17.0
)
FetchContent_MakeAvailable(spdlog)
target_link_libraries(mi_proyecto PRIVATE spdlog::spdlog)
```

Source: Fórmula de Homebrew

## Cómo empezar y uso básico

Comenzar a usar spdlog no requiere esfuerzo. Tras incluir la cabecera, llama a funciones globales o crea instancias de loggers específicos:

**Ejemplo básico en C++**

```
#include "spdlog/spdlog.h"
#include "spdlog/sinks/rotating_file_sink.h"

int main() {
    // Registro estandar en consola
    spdlog::info("spdlog iniciado correctamente.");
    spdlog::warn("Atencion: ¡el uso de memoria esta subiendo!");
    spdlog::error("Codigo de error: {:d}, mensaje: {}", 404, "Pagina no encontrada");

    // Logger de archivo rotativo (max 5MB, 3 archivos)
    auto file_logger = spdlog::rotating_logger_mt("file_logger", "logs/app.txt", 1024 * 1024 * 5, 3);
    file_logger->info("Este mensaje es seguro entre hilos y se archiva automaticamente.");

    return 0;
}
```

## Arquitectura técnica y funcionamiento interno

La excepcional velocidad de spdlog se apoya en un diseño modular con cero sobrecoste:
- Separación entre Logger y Sink: El logger filtra por nivel (trace, debug, info, warn, err, critical) y pasa el registro a uno o varios destinos.
- Seguridad de hilos (_mt vs _st): Clases sink disponibles con sincronización mutex (_mt) o versiones mono-hilo sin bloqueo (_st).
- Búfer circular asíncrono: El pool de hilos en background procesa los registros sin ralentizar la lógica del programa.
- Vaciado inteligente (Flush): Los datos se almacenan en búfer y se fuerzan a disco automáticamente ante errores críticos.

## Si no programas
🤖 Si no programas
Quiero configurar spdlog en un proyecto moderno de C++ con CMake en modo asíncrono. ¿Podrías darme una función de inicialización y un archivo CMakeLists.txt con salida en color por consola, archivo rotativo de 10MB y vaciado inmediato ante errores?

- **Para quién:** Desarrolladores C++, creadores de motores de videojuegos y sistemas embebidos que requieren mínima latencia.
- **Licencia:** MIT (Licencia de código abierto permisiva)
- **Integración:** Solo encabezados o biblioteca precompilada
- **Estándares:** C++11, C++14, C++17, C++20

## Preguntas frecuentes
- ¿Por qué elegir spdlog frente a printf o std::cout? spdlog es inmensamente más rápido, seguro entre hilos, ofrece niveles estructurados y soporte asíncrono con {fmt}.
- ¿Se pueden registrar clases personalizadas? Sí, sobrecargando el operator<< o especializando fmt::formatter para tus tipos.
- ¿Es adecuado para videojuegos y trading de alta frecuencia? Sí, gracias a los búferes asíncronos y sinks lock-free, los registros toman nanosegundos sin pausar el hilo gráfico.
- ¿Admite formato JSON estructurado? Sí, puedes configurar patrones personalizados para generar logs en JSON compatibles con Datadog o Grafana Loki.

## Enlaces
- [GitHub →](https://github.com/gabime/spdlog)
- [Read in Turkish →](https://trescout.com/discover/spdlog/)

## Términos relacionados del glosario
Logging Logs Runtime Memory Management

---
Source: TreScout Discover · https://trescout.com/es/discover/spdlog/
