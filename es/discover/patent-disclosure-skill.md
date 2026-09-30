# Automatizar las divulgaciones de invenciones de patentes con IA

Patent Disclosure Skill basada en Python analiza borradores de invenciones técnicas y produce descripciones técnicas, reivindicaciones y comparaciones de la técnica anterior de acuerdo con el formato oficial de patentes.

- ★ 10.360
- Python
- GitHub Trending · 2026-08-31

## Qué aporta
- Producción estructurada de texto de patente: creación de las secciones de campo técnico, antecedentes, resumen y descripción detallada de la invención de acuerdo con las normas estándar de patentes.
- Árbol de reivindicaciones independientes y dependientes: formulación automática de listas jerárquicas de reivindicaciones de patentes que maximizan el alcance de la protección legal.
- Análisis de diferencias del arte previo: Destacando claramente las diferencias técnicas y la etapa de innovación entre las tecnologías existentes y la invención.
- Acelerar la colaboración con los abogados de patentes: ahorro de costos y tiempo al convertir los borradores de los ingenieros en documentos técnicos simplificados listos para los abogados de patentes.
- Soporte de terminología de patentes multilingüe: Compatibilidad con terminología en inglés, turco e instituciones internacionales de patentes (OMPI, EPO, USPTO).

## Instalación
**Clonando el repositorio e instalando dependencias**

```
git clone https://github.com/handsomestWei/patent-disclosure-skill.git
cd patent-disclosure-skill
pip install -r requirements.txt
```


## Ejecución
**Iniciar el análisis de patentes y la producción de divulgación**

```
python run_skill.py --input bulus_taslagi.txt --output patent_disclosure.md
```


## Arquitectura técnica y principio de funcionamiento
- Motor de análisis de descubrimiento técnico: detecta entradas, salidas y metodologías clave en software, hardware o descripciones de procesos químicos.
- Verificador de sintaxis de reclamos: analizador de lenguaje legal que busca expresiones vagas y errores formales en los reclamos.
- Exportación de plantilla y Markdown: guardar el documento en formato Markdown segmentado estándar para su uso en solicitudes de patente formales.

## Flujos de trabajo de análisis de patentes y preparación de reclamaciones
- Traducir algoritmos de software a una forma patentable: derivar descripciones de métodos y sistemas aceptables para las autoridades de patentes a partir de diagramas de código y arquitectura.
- Defensa contra acciones de la oficina: creación de borradores de respuesta que enumeren las características distintivas de la invención contra las objeciones de los examinadores de patentes.
- Auditoría de cartera de propiedad intelectual: mapeo temprano de los pasos de invención potencial de patentes de proyectos tecnológicos internos.

## Si no programa
Me gustaría preparar un texto formal de divulgación de invenciones utilizando la habilidad de divulgación de patentes para un algoritmo de almacenamiento en caché de bases de datos distribuidas que he desarrollado. ¿Puede darnos el flujo del algoritmo como entrada y explicar paso a paso cómo generar reivindicaciones independientes, el campo técnico de la invención y las diferencias con el estado de la técnica?

## Preguntas frecuentes
- ¿Esta herramienta reemplaza a un abogado de patentes formal? No. Patent Disclosure Skill es una herramienta de preparación y productividad que ayuda a los ingenieros a organizar borradores de invenciones y prepararlos para los abogados; Las solicitudes legales deben realizarse a través de un abogado.
- ¿Con qué modelos LLM funciona? Claude 3.5 Sonnet se puede configurar para funcionar con GPT-4o o modelos nativos abiertos (Qwen, Llama 3).
- ¿Mis secretos técnicos confidenciales se filtrarán a Internet? Cuando se ejecuta con un LLM local (Ollama o vLLM), todo el análisis de patentes se realiza íntegramente en su computadora local, no se envían datos.
- ¿Puede interpretar dibujos y diagramas de flujo de patentes? Cuando se conectan modelos multimodales, se pueden analizar y transcribir la arquitectura del sistema y los diagramas de bloques.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/patent-disclosure-skill/
