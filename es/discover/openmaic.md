# Simulación interactiva de aula con múltiples agentes de IA

OpenMAIC, desarrollado por investigadores de la Universidad de Tsinghua, reúne múltiples agentes de inteligencia artificial en los roles de profesor, estudiante y observador en un entorno de aula interactivo.

- ★ 41.041
- TypeScript
- GitHub Trending · 2026-08-31

## Actualizaciones

- **19 de octubre de 2026:** Estrellas 40,871 → 41,041, última versión v1.2.1 (18 de octubre de 2026).
- **16 de octubre de 2026:** Estrellas 40,363 → 40,871, última versión v1.2.0 (16 de octubre de 2026).
- **11 de octubre de 2026:** Estrellas 39,969 → 40,363, última versión v1.1.4 (11 de octubre de 2026).
- **5 de octubre de 2026:** Estrellas 39,351 → 39,969, última versión v1.1.3 (5 de octubre de 2026).

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

Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero simular un entorno de discusión socrático cargando mis propios apuntes de clase en la plataforma OpenMAIC. ¿Puedes explicar paso a paso cómo definir los roles de los agentes (maestro, estudiante curioso, interrogador crítico) y cómo plantear esta clase con un modelo local de Ollama?

Repositorio: https://github.com/THU-MAIC/OpenMAIC. Sigue las instrucciones oficiales del archivo README de este repositorio para la instalación y ejecución.

Antes de empezar, comprueba en qué sistema operativo estamos y si las herramientas necesarias (ej. Python, Node.js, Git, Docker) están instaladas. Instala las que falten paso a paso según este sistema.

Crea una carpeta nueva y vacía para trabajar. No toques ningún archivo fuera de esta carpeta y no borres nada. Antes de ejecutar cada comando, dime qué vas a hacer en una frase.

Dime qué debería ver en la pantalla al final de cada paso. Si ocurre un error, te pegaré el mensaje de error tal cual y lo solucionaremos juntos.

## Preguntas frecuentes

- ¿Se requiere una GPU para usar OpenMAIC? Si va a ejecutar su propio modelo nativo (Ollama/vLLM), se recomienda GPU; pero se puede utilizar directamente con una computadora estándar a través de API en la nube (OpenAI, Gemini, Groq).
- ¿Puede el usuario participar en la simulación por voz? Sí. Gracias a WebRTC y al módulo de reconocimiento de voz, el usuario puede participar en los debates de clase hablando con su micrófono.
- ¿Cuántos agentes pueden estar en el aula al mismo tiempo? La configuración predeterminada proporciona una interacción ideal entre 3 y 8 agentes; Se pueden diseñar clases más concurridas de acuerdo con los recursos del sistema.
- ¿En qué formatos se puede subir el contenido del curso? Los documentos de texto sin formato, Markdown y PDF se pueden importar directamente a la base de conocimientos del sistema.

## Términos relacionados del glosario

- [Markdown](https://trescout.com/es/dictionary/markdown/)
- [GPU](https://trescout.com/es/dictionary/gpu/)
- [PDF](https://trescout.com/es/dictionary/pdf/)
- [LLM](https://trescout.com/es/dictionary/llm/)
- [Open Source](https://trescout.com/es/dictionary/open-source/)
- [API](https://trescout.com/es/dictionary/api/)

- **Para quién es:** Educadores, investigadores de IA, emprendedores de tecnología educativa y estudiantes.
- **Licencia:** Apache-2.0 (licencia de código abierto)
- **Marco:** Simulador de agentes múltiples TypeScript y Next.js
- **Plataformas:** Navegador web, Linux, macOS, Windows

## Enlaces

- [Repositorio en GitHub →](https://github.com/THU-MAIC/OpenMAIC)
- [Leer en turco →](https://trescout.com/discover/openmaic/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-08-31: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. El texto de presentación se preparó con IA a partir de la propia documentación del repositorio y esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/openmaic/
