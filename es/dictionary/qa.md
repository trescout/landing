# ¿Qué es QA?

> Quality Assurance

QA (Quality Assurance - Garantía de Calidad) es una disciplina sistemática de gestión de calidad que tiene como objetivo prevenir errores antes de que aparezcan en cada etapa del ciclo de vida del desarrollo de software, establecer estándares de ingeniería y garantizar la confiabilidad del producto final.

## Origen conceptual: Del ciclo de Deming y las líneas de producción al software
El concepto de Aseguramiento de la Calidad nació mucho antes del software, a mediados del siglo XX en la producción industrial. La Gestión de Calidad Total (TQM) y el ciclo PDCA (Planificar-Hacer-Verificar-Actuar), sentados sus cimientos por W. Edwards Deming y Walter Shewhart, sostienen que la calidad no puede inspeccionarse a posteriori, sino que debe construirse dentro del propio producto. El principio Jidoka del Sistema de Producción Toyota (detener la línea inmediatamente cuando se produce un producto defectuoso) es también el ancestro de la moderna filosofía de integración continua (CI) y QA actual.

## Distinción crítica: QA vs QC vs Testing
Aunque estos tres conceptos se utilizan a menudo indistintamente, existen límites metodológicos claros entre ellos:

## Paradigma moderno de QA: Shift-Left y Shift-Right
En el modelo tradicional en cascada (waterfall), los desarrolladores escribían el código y luego lo "lanzaban por encima de la pared" al departamento de QA para que lo probara. En el mundo moderno de Agile y DevOps, este enfoque ha dado paso a dos direcciones complementarias:

## Pirámide de pruebas y capas de automatización
Una arquitectura de QA sólida se basa en el principio de la Pirámide de Pruebas de Mike Cohn:

## QA en la era de la inteligencia artificial y los LLM
Con la proliferación de sistemas probabilísticos (non-deterministic) como los grandes modelos de lenguaje (LLM), la disciplina de QA ha entrado en una nueva fase:

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
- [Unit Testing](/es/dictionary/unit-testing/)
- [End-to-End Testing](/es/dictionary/end-to-end-testing/)
- [Testing Framework](/es/dictionary/testing-framework/)
- [Production Pipeline](/es/dictionary/production-pipeline/)
- [Benchmarks](/es/dictionary/benchmark/)
- [Runtime](/es/dictionary/runtime/)

## Herramientas relacionadas
- [Gstack](/es/discover/gstack/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/qa/
