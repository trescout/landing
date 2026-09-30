# Simulación interactiva de aula con múltiples agentes de IA

OpenMAIC, desarrollado por investigadores de la Universidad de Tsinghua, reúne múltiples agentes de inteligencia artificial en los roles de profesor, estudiante y observador en un entorno de aula interactivo.

- ★ 39.351
- TypeScript
- GitHub Trending · 2026-08-31

## Qué aporta
- Arquitectura de múltiples agentes basada en roles: interacción dinámica de agentes de LLM en los roles de maestro, estudiante interrogador, comentarista y resumidor.
- Interfaz visual y de audio en el aula: experiencia pedagógica inmersiva con pizarra virtual, flujo instantáneo de preguntas y respuestas y síntesis de voz (TTS).
- Plan de estudios del curso personalizable: cree instantáneamente cursos interactivos cargando sus propios documentos PDF o notas de clase de texto.
- Lanzamiento de simulación con un solo clic: administre la orquestación compleja de agentes a través de una interfaz web moderna sin conocimientos de codificación técnica.
- Compatibilidad de modelos ponderados abiertos: Libertad para conectar cualquier modelo de IA a través de Ollama, vLLM o proveedores de LLM en la nube.

## Instalación
**Clonando el repositorio e instalando dependencias**

```
git clone https://github.com/THU-MAIC/OpenMAIC.git
cd OpenMAIC
pnpm install
```


## Ejecución
**Iniciando el servidor de desarrollo**

```
pnpm run dev
# Tarayıcıda http://localhost:3000 adresini açın
```


## Arquitectura técnica y principio de funcionamiento
- Motor de orquestación de conversaciones: el controlador central que gestiona qué agente habla y cuándo, el orden de la conversación y el contexto de la discusión.
- Gestión de la memoria y el contexto: almacenar en la memoria a corto y largo plazo el contenido común del tablero y las preguntas de los estudiantes compartidas a lo largo de la lección.
- Transmisión en tiempo real a través de WebSocket: transmisión de textos hablados, expresiones emocionales y animaciones a la interfaz frontal sin demora.

## Dinámica de clases multiagente y simulaciones de roles.
- Entornos de discusión socráticos: agentes con diferentes perspectivas discuten un tema y desencadenan el pensamiento crítico del usuario.
- Soporte de tutor personalizado: tutores de IA dedicados que ajustan automáticamente el nivel de dificultad según la velocidad de comprensión del usuario.
- Estudios de interacción social interagente: análisis de cómo grandes modelos lingüísticos colaboran y comparten información en entornos de grupos grandes.

## Si no programa
Quiero simular un entorno de discusión socrático cargando mis propios apuntes de clase en la plataforma OpenMAIC. ¿Puedes explicar paso a paso cómo definir los roles de los agentes (maestro, estudiante curioso, interrogador crítico) y cómo plantear esta clase con un modelo local de Ollama?

## Preguntas frecuentes
- ¿Se requiere una GPU para usar OpenMAIC? Si va a ejecutar su propio modelo nativo (Ollama/vLLM), se recomienda GPU; pero se puede utilizar directamente con una computadora estándar a través de API en la nube (OpenAI, Gemini, Groq).
- ¿Puede el usuario participar en la simulación por voz? Sí. Gracias a WebRTC y al módulo de reconocimiento de voz, el usuario puede participar en los debates de clase hablando con su micrófono.
- ¿Cuántos agentes pueden estar en el aula al mismo tiempo? La configuración predeterminada proporciona una interacción ideal entre 3 y 8 agentes; Se pueden diseñar clases más concurridas de acuerdo con los recursos del sistema.
- ¿En qué formatos se puede subir el contenido del curso? Los documentos de texto sin formato, Markdown y PDF se pueden importar directamente a la base de conocimientos del sistema.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/openmaic/
