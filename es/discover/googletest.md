# Pruebas unitarias estándar de la industria en proyectos C++

GoogleTest y GoogleMock son marcos de prueba de código abierto estándar de la industria que le permiten ejecutar pruebas unitarias, simulacros y pruebas paramétricas en proyectos C++ modernos.

- ★ 39.588
- C++
- GitHub Trending · 2026-08-27

## Qué aporta
- Ricas macros de aserción: diagnóstico claro de errores con las macros ASSERT_* (error crítico, finaliza la prueba) y EXPECT_* (registra el error, continúa el flujo de la prueba).
- Infraestructura de Mock avanzada (GoogleMock): Capacidad para simular fácilmente interfaces con MOCK_METHOD para aislar dependencias y definir expectativas de llamadas.
- Capacidad de prueba paramétrica: La capacidad de repetir automáticamente la misma lógica de prueba en decenas de entradas y conjuntos de datos diferentes con una sola plantilla.
- Multiplataforma y seguridad de hilos: arquitectura segura para hilos en entornos Linux, macOS y Windows, y validación de escenarios de bloqueo mediante pruebas de muerte (death tests).
- Integración de CI/CD y generación de informes: integración perfecta con las canalizaciones de GitHub Actions, Jenkins y GitLab CI mediante formatos de salida XML y JSON compatibles con JUnit.

## Instalación
**Agregar al proyecto con CMake FetchContent**

```
include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/refs/tags/v1.15.2.tar.gz
)
FetchContent_MakeAvailable(googletest)
```


## Ejecución
**Compile la prueba y ejecútela con CTest**

```
cmake -B build -S .
cmake --build build
ctest --test-dir build --output-on-failure
```


## Arquitectura técnica y principio de funcionamiento
- Gestión de fixtures y ciclo de vida: Mediante los procedimientos SetUp y TearDown, los recursos de memoria se gestionan de forma segura antes y después de cada prueba.
- Aislamiento de procesos para pruebas de muerte (Death Tests): Captura el bloqueo inesperado del programa o la generación de aserciones en procesos secundarios aislados mediante un mecanismo de bifurcación (fork).
- Plantillas de pruebas parametrizadas por tipos: Ofrece una infraestructura de pruebas parametrizadas por tipos para probar clases con plantillas (C++ templates) con diferentes tipos de datos de una sola vez.

## Casos de prueba e integración de GoogleMock
- Abstracción de Base de Datos y Llamadas de Red: Simule respuestas de API esperadas y latencias sin establecer conexiones de red reales utilizando MOCK_METHOD.
- Número de llamadas y validación de parámetros: compruebe cuántas veces, con qué argumentos y en qué orden se llama a una función mediante la macro EXPECT_CALL.
- Análisis de escenarios de lanzamiento de errores: garantice la solidez probando los bloques de código que lanzan excepciones (throw) con macros EXPECT_THROW.

## Si no programa
Quiero escribir pruebas unitarias para una clase de analizador de datos usando GoogleTest y GoogleMock en un proyecto moderno de C++. ¿Puede explicar con ejemplos de código cómo estructurar mi archivo CMakeLists.txt, un dispositivo de prueba TEST_F de muestra y cómo crear un objeto simulado con MOCK_METHOD y validar las expectativas de llamada?

## Preguntas frecuentes
- ¿Cuál es la forma más moderna de incluir GoogleTest en un proyecto? En los proyectos modernos de CMake, el mecanismo FetchContent es el enfoque más recomendado. Descarga el código fuente y lo vincula al proceso de compilación de destino sin necesidad de un administrador de paquetes externo.
- ¿Cuál es la diferencia fundamental entre EXPECT_* y ASSERT_*? Los macros EXPECT_* registran el error cuando fallan, pero permiten que el resto de la función siga ejecutándose. Por su parte, ASSERT_* sale inmediatamente de la función de prueba actual en caso de error.
- ¿Es GoogleMock una biblioteca independiente? GoogleMock era originalmente un proyecto independiente, pero lleva mucho tiempo integrado bajo el mismo techo que el repositorio de GoogleTest; ambos se instalan y utilizan juntos.
- ¿Ofrece seguridad de hilos? Sí. GoogleTest funciona de forma segura para hilos (thread-safe) en sistemas que admiten pthreads y en Windows; sincroniza correctamente las notificaciones simultáneas provenientes de múltiples hilos.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/googletest/
