# ¿Qué es QA?

*Glosario · Dev · Última actualización: 19 de septiembre de 2026*

> Quality Assurance

QA (Quality Assurance - Garantía de Calidad) es una disciplina sistemática de gestión de calidad que tiene como objetivo prevenir errores antes de que aparezcan en cada etapa del ciclo de vida del desarrollo de software, establecer estándares de ingeniería y garantizar la confiabilidad del producto final.

## Origen conceptual: Del ciclo de Deming y las líneas de producción al software

El concepto de Aseguramiento de la Calidad nació mucho antes del software, a mediados del siglo XX en la producción industrial. La Gestión de Calidad Total (TQM) y el ciclo PDCA (Planificar-Hacer-Verificar-Actuar), sentados sus cimientos por W. Edwards Deming y Walter Shewhart, sostienen que la calidad no puede inspeccionarse a posteriori, sino que debe construirse dentro del propio producto. El principio Jidoka del Sistema de Producción Toyota (detener la línea inmediatamente cuando se produce un producto defectuoso) es también el ancestro de la moderna filosofía de integración continua (CI) y QA actual.

En el mundo del software, la famosa investigación "Economía de la Ingeniería de Software" de Barry Boehm demostró que, mientras que el costo de corregir un error detectado en la fase de diseño es de 1 unidad, el costo de corregirlo después de pasar a producción puede multiplicarse por 100. QA existe para prevenir este costo masivo y la pérdida de reputación.

***Analogía:** Depurar (debugging) es intervenir en la mesa de operaciones, mientras que realizar pruebas de software es tomar análisis de laboratorio. Por otro lado, el control de calidad (QA) es el protocolo de salud pública y medicina preventiva: su objetivo es eliminar el riesgo de enfermedad desde el principio mediante la creación de guías de alimentación saludable, calendarios de vacunación y normas de higiene.*

## Distinción crítica: QA vs QC vs Testing

Aunque estos tres conceptos se utilizan a menudo indistintamente, existen límites metodológicos claros entre ellos:

**Pruebas (Testing):** Es la ejecución de escenarios para encontrar errores concretos (bugs) en una versión específica del software (está centrado en el producto y es reactivo).

**Control de Calidad (QC - Quality Control):** Es la puerta de auditoría que verifica si el producto cumple con las especificaciones técnicas determinadas y los criterios de aceptación antes de su lanzamiento (está centrado en el producto y es reactivo).

**Garantía de Calidad (QA - Quality Assurance):** Es la disciplina paraguas que diseña las metodologías de desarrollo, la infraestructura de pruebas, los estándares de arquitectura y los procesos de CI/CD para evitar que los errores aparezcan (está orientada a procesos y es proactiva).

## Paradigma moderno de QA: Shift-Left y Shift-Right

En el modelo tradicional en cascada (waterfall), los desarrolladores escribían el código y luego lo "lanzaban por encima de la pared" al departamento de QA para que lo probara. En el mundo moderno de Agile y DevOps, este enfoque ha dado paso a dos direcciones complementarias:

**1. Shift-Left (Desplazamiento hacia la izquierda):** Traslada el control de calidad al principio del desarrollo. Mientras el desarrollador escribe código, aplica análisis estático (ESLint, SonarQube), control de tipos (TypeScript), pruebas unitarias (Jest, pytest) y TDD (Test-Driven Development). Aquí, el ingeniero de QA no es quien ejecuta las pruebas, sino un arquitecto de plataformas que construye la infraestructura y los marcos de pruebas (frameworks).

**2. Shift-Right (Desplazamiento hacia la derecha):** Es la preservación de la calidad una vez que el código ha pasado a producción. La experiencia real del usuario se supervisa mediante monitoreo sintético, despliegues canary, seguimiento de errores (Sentry), ingeniería del caos (Chaos Engineering) y análisis de tráfico en vivo.

## Pirámide de pruebas y capas de automatización

Una arquitectura de QA sólida se basa en el principio de la Pirámide de Pruebas de Mike Cohn:

**Pruebas unitarias (Unit Tests):** Forman la base; prueban funciones independientes de forma aislada, se ejecutan en milisegundos y tienen el menor coste.

**Pruebas de integración y de contrato (Integration & Contract Tests):** Verifica las bases de données, la caché y los contratos de API entre microservicios (por ej. Pact).

**Pruebas de extremo a extremo (E2E Tests):** Simula los pasos de un usuario real en el navegador con herramientas como Cypress o Playwright; su alcance es amplio pero su mantenimiento es más costoso.

**Pruebas no funcionales:** Incluye pruebas de carga y estrés (k6, Locust), análisis de vulnerabilidades (SAST/DAST) y auditorías de accesibilidad (WCAG / a11y).

## QA en la era de la inteligencia artificial y los LLM

Con la proliferación de sistemas probabilísticos (non-deterministic) como los grandes modelos de lenguaje (LLM), la disciplina de QA ha entrado en una nueva fase:

**Evaluaciones de LLM (Evals):** Auditorías automáticas que califican las respuestas del modelo en cuanto a alucinaciones, precisión, toxicidad y relevancia (DeepEval, Ragas).

**Pruebas de regresión semántica:** Conjuntos de evaluación (benchmarks) que miden si un cambio realizado en las plantillas de prompts ha empeorado la calidad de las respuestas anteriores.

**Generación de Pruebas Asistida por Inteligencia Artificial:** Detección automática de casos de prueba y diferencias de regresión de la interfaz visual mediante modelos de inteligencia artificial.

## Preguntas frecuentes

**¿Qué significa QA y cuál es su desarrollo?**

Es la abreviatura de Quality Assurance; en español significa Garantía de Calidad. Es la disciplina de ingeniería que garantiza que los procesos de software funcionen sin errores de principio a fin.

**¿Cuál es la diferencia entre QA, QC (Control de Calidad) y Testing?**

El testing y QC son pasos reactivos enfocados en encontrar errores en el código existente. QA, por otro lado, es un proceso proactivo que diseña los procesos de desarrollo, estándares y herramientas para evitar que los errores ocurran desde el principio.

**¿Qué significan los enfoques de prueba Shift-Left y Shift-Right?**

Shift-Left se refiere a adelantar los procesos de prueba al inicio del desarrollo (el momento de escribir el código); Shift-Right se refiere a monitorear en tiempo real la salud del sistema y el comportamiento del usuario en el entorno de producción.

**¿Cómo se realiza el QA en aplicaciones basadas en inteligencia artificial y LLM?**

Además de las pruebas tradicionales, se utilizan marcos de evaluación (evals) especiales que miden las tasas de alucinación, la similitud semántica, la regresión de prompts y las métricas de precisión de RAG.

## Términos relacionados

- [Unit Testing](https://trescout.com/es/dictionary/unit-testing/)
- [End-to-End Testing](https://trescout.com/es/dictionary/end-to-end-testing/)
- [Testing Framework](https://trescout.com/es/dictionary/testing-framework/)
- [Production Pipeline](https://trescout.com/es/dictionary/production-pipeline/)
- [Benchmarks](https://trescout.com/es/dictionary/benchmark/)
- [Runtime](https://trescout.com/es/dictionary/runtime/)

## Herramientas relacionadas

- [Gstack](https://trescout.com/es/discover/gstack/)

Esta explicación se redactó en lenguaje sencillo para TreScout y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/qa/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/qa/
