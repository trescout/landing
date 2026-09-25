# ¿Qué es QA (Aseguramiento de la Calidad)?

**Categoría:** Desarrollo
**Última actualización:** 2026-09-19

QA (Quality Assurance - Aseguramiento de la Calidad) es la disciplina sistemática de la ingeniería de software enfocada en prevenir la aparición de defectos a lo largo del ciclo de vida de desarrollo (SDLC), fijando estándares de ingeniería y asegurando la fiabilidad del producto final.

## Orígenes conceptuales: Del ciclo de Deming a la ingeniería de software
El Aseguramiento de la Calidad nació a mediados del siglo XX en la manufactura industrial antes de la era informática. La Gestión de Calidad Total (TQM) y el ciclo PDCA (Plan-Do-Check-Act) de W. Edwards Deming y Walter Shewhart defendían que la calidad no se inspecciona al final; debe construirse dentro del propio proceso. El concepto Jidoka de Toyota (detener la cadena al detectar un fallo) es el antecedente directo de la integración continua (CI) moderna.En el software, las investigaciones de Barry Boehm demostraron que resolver un defecto detectado en la fase de diseño cuesta 1 unidad, mientras que repararlo tras llegar a producción puede costar hasta 100 veces más. QA existe para evitar este enorme impacto económico y de reputación.

## Diferencia crítica: QA vs QC vs Testing
Aunque a menudo se utilicen indistintamente, existen fronteras metodológicas nítidas entre estos términos:Pruebas (Testing): La ejecución de casos de prueba para descubrir errores concretos en una versión de software existente (enfoque en producto, reactivo).Control de Calidad (QC - Quality Control): El punto de control que valida si el producto terminado cumple con las especificaciones y criterios de aceptación antes del despliegue (enfoque en producto, reactivo).Aseguramiento de la Calidad (QA - Quality Assurance): La disciplina global que define las metodologías, la arquitectura de pruebas, los linters y las canalizaciones CI/CD para impedir que los errores lleguen a producirse (enfoque en proceso, proactivo).

## Paradigmas modernos de QA: Shift-Left y Shift-Right
En el antiguo modelo en cascada, los programadores escribían el código y 'lo tiraban por encima de la pared' al departamento de pruebas. En entornos ágiles y DevOps, este cuello de botella se sustituye por dos enfoques sincronizados:1. Shift-Left (Desplazamiento a la izquierda): Llevar la validación al inicio del ciclo de desarrollo. Desde que escribe código, el programador aplica análisis estático (SonarQube), tipado estricto, pruebas unitarias y TDD. El especialista en QA actúa como arquitecto facilitando frameworks e infraestructura.2. Shift-Right (Desplazamiento a la derecha): Salvaguardar la calidad en producción. Monitorización sintética, despliegues canario, seguimiento de excepciones (Sentry) e ingeniería del caos auditan el sistema con usuarios reales.

## Pirámide de pruebas y niveles de automatización
Una arquitectura de pruebas equilibrada se estructura según la Pirámide de Mike Cohn:Pruebas Unitarias: La base sólida; se ejecutan en milisegundos de forma aislada con mínimo coste de mantenimiento.Pruebas de Integración y Contrato: Verifican la interacción entre microservicios, bases de datos y contratos de API (e.g. Pact).Pruebas de Extremo a Extremo (E2E): Simulan la navegación del usuario en navegadores mediante Playwright o Cypress; aportan máxima certeza pero requieren mayor mantenimiento.Pruebas No Funcionales: Pruebas de carga y estrés (k6, Locust), análisis de seguridad (SAST/DAST) y auditorías de accesibilidad (WCAG).

## Analogia
Depurar código (debugging) es como una intervención de urgencia, y probar software es como hacer análisis clínicos. QA es la medicina preventiva y la salud pública: establece normas higiénicas y planes de vacunación para evitar que el paciente enferme.

## QA en la era de la Inteligencia Artificial y los LLM
La incorporación de sistemas no deterministas como los modelos grandes de lenguaje introduce retos inéditos:Evaluaciones de LLM (Evals): Frameworks de puntuación automatizada (DeepEval, Ragas) que miden tasas de alucinación, veracidad y relevancia.Pruebas de Regresión Semántica: Benchmarks que verifican que un cambio en los prompts no degrade la calidad de respuestas previas.Generación de Pruebas con IA: Creación de casos de prueba complejos y detección visual de regresiones de interfaz mediante visión artificial.

## Preguntas frecuentes

### ¿Qué significan las siglas QA en ingeniería de software?
QA significa Quality Assurance (Aseguramiento de la Calidad). Es la disciplina dedicada a planificar procesos, estándares y herramientas para asegurar la fiabilidad del software.

### ¿En qué se diferencian el QA y el testing de software?
El testing es una labor reactiva que busca bugs en código ya escrito. El QA es una estrategia proactiva que diseña los procesos para evitar que los fallos se cometan desde el inicio.

### ¿Qué son las estrategias Shift-Left y Shift-Right?
Shift-Left consiste en validar desde el inicio de la programación (pruebas unitarias, linting). Shift-Right monitoriza en tiempo real el comportamiento del sistema en producción.

### ¿Cómo se realiza el QA en aplicaciones basadas en LLM e IA?
Además de pruebas tradicionales, se usan suites de evaluación (evals) que miden objetivamente la precisión de recuperación (RAG), la fidelidad y las alucinaciones.

## Términos relacionados
- [Unit Testing](/es/dictionary/unit-testing/)
- [End-to-End Testing](/es/dictionary/end-to-end-testing/)
- [Testing Framework](/es/dictionary/testing-framework/)
- [Production Pipeline](/es/dictionary/production-pipeline/)
- [Benchmarks](/es/dictionary/benchmark/)
- [Runtime](/es/dictionary/runtime/)

## Herramientas relacionadas
- [Gstack](/es/discover/gstack/)

---
Source: TreScout Tech Dictionary · https://trescout.com/es/dictionary/qa/
