# Tools: Herramientas de desarrollo, Function Calling y MCP


**Categoría:** Dev  

**Última actualización:** 2026-09-19


Tools (herramientas) engloba dos conceptos esenciales en tecnología: las utilidades que potencian el trabajo de los desarrolladores y las interfaces que facultan a la inteligencia artificial para ejecutar acciones y consultar APIs.


## Etimología y la Metáfora de la Herramienta en Computación
La palabra inglesa *tool* proviene del inglés antiguo *tol* (utensilio para obrar). En software, la filosofía Unix sentó las bases modernas: construir programas específicos y minimalistas que colaboren entre sí mediante tuberías de texto estandarizadas.

## 1. Herramientas para Desarrolladores (DevTools)
El desarrollo de software contemporáneo se sostiene sobre herramientas de precisión :
- **Compiladores y Sistemas de Construcción:** GCC, Clang, rustc y Vite transforman el código fuente en binarios nativos optimizados.
- **Depuradores y Analizadores de Rendimiento:** GDB, LLDB y las DevTools del navegador rastrean el uso de memoria y las peticiones HTTP al vuelo.
- **Linters y Análisis Estático:** ESLint, Ruff y SonarQube detectan inconsistencias y riesgos de seguridad antes de compilar.

## 2. El Gran Hito en IA: Tool Use y Function Calling
Los modelos de lenguaje son motores probabilísticos de texto. La adopción de herramientas solventa cuatro barreras fundamentales :
1. **Información en Tiempo Real:** Acceso a bases de datos y APIs web vivas sin depender del corte de entrenamiento.
2. **Precisión de Cálculo:** Delegación de operaciones algebraicas en intérpretes como Python.
3. **Capacidad de Acción:** Ejecución de órdenes reales como enviar correos o modificar registros en bases de datos.
4. **Inspección de Sistemas:** Lectura de archivos locales y árboles de código Git.

## 3. Model Context Protocol (MCP) como Estándar Abierto
La proliferación de formatos propietarios dificultaba la integración de herramientas. Anthropic propuso el **Model Context Protocol (MCP)**, un estándar abierto inspirado en el protocolo LSP de los IDEs que unifica la comunicación cliente-servidor mediante JSON-RPC.

## 4. Herramientas de Doble Uso en Ciberseguridad
En el campo de la seguridad digital, las herramientas tienen un doble filo evidente :
- **Auditoría y Pruebas de Penetración:** Nmap, Wireshark y Burp Suite permiten a los equipos defensivos neutralizar brechas antes de que cibercriminales las descubran.
- **Fuzzing de Seguridad:** Soluciones automáticas como AFL++ prueban interfaces con datos arbitrarios para destapar corrupciones de memoria.

## Por analogía
Un modelo de IA sin herramientas es como un erudito brillante encerrado en una habitación cerrada; dotarle de herramientas equivale a darle manos, un teléfono y una calculadora para interactuar con la realidad.

## Preguntas frecuentes

**¿Qué es una tool en inteligencia artificial?**  
Es una función o servicio externo que el modelo puede invocar mediante parámetros JSON estructurados para obtener datos o ejecutar tareas.

**¿Para qué sirve el estándar Model Context Protocol (MCP)?**  
Permite conectar modelos de IA con fuentes de datos y utilidades locales mediante un protocolo universal y abierto.

**¿Cómo decide un LLM qué herramienta emplear?**  
Analiza el propósito de la consulta frente a las descripciones y esquemas de parámetros definidos para cada herramienta.

## Términos relacionados
- [MCP](/es/dictionary/mcp/)
- [AI Agent](/es/dictionary/ai-agent/)
- [Plugin](/es/dictionary/plugin/)
- [SDK](/es/dictionary/sdk/)

## Herramientas relacionadas
- [ECC](/es/discover/ecc/)
- [System Prompts and Models of AI Tools](/es/discover/system-prompts-and-models-of-ai-tools/)
- [Claude Plugins Official](/es/discover/claude-plugins-official/)

---
Fuente: Glosario técnico TreScout · https://trescout.com/es/dictionary/tools/
