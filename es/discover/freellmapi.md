# Combine 34 proveedores de LLM gratuitos en una sola API

FreeLLMAPI proporciona enrutamiento inteligente y tolerancia a fallas al agregar 34 proveedores principales de modelos de lenguaje gratuitos diferentes en una única API REST en formato OpenAI.

- ★ 42.614
- TypeScript
- GitHub Trending · 2026-08-28

## Actualizaciones

- **27 de octubre de 2026:** Estrellas 41,667 → 42,614, última versión v0.16.11 (27 de octubre de 2026).
- **26 de octubre de 2026:** Estrellas 40,353 → 41,667, última versión v0.16.10 (25 de octubre de 2026).
- **24 de octubre de 2026:** Estrellas 39,822 → 40,353, última versión v0.16.9 (23 de octubre de 2026).
- **23 de octubre de 2026:** Estrellas 38,660 → 39,822, última versión v0.16.8 (23 de octubre de 2026).

## Qué aporta

- 34 proveedores de modelos gratuitos: acceso integral a docenas de proveedores gratuitos, incluidos Google Gemini, Groq, Cloudflare Workers AI y Hugging Face.
- Compatibilidad con OpenAI REST API: trabaje con LangChain, LlamaIndex y aplicaciones de IA existentes sin cambiar el código, gracias al punto final /v1/chat/completions.
- Enrutamiento inteligente y recuperación de fallas: cambie automáticamente a un proveedor alternativo cuando un proveedor alcance el límite de velocidad o falle.
- Compatibilidad con streaming (eventos enviados por el servidor): posibilidad de recibir resultados del modelo como un flujo palabra por palabra en tiempo real.
- Liviana y fácil de implementar: Arquitectura que se puede implementar en una computadora o servidor local en segundos con Docker o Node.js.

## Instalación

**Clonando el repositorio e instalando dependencias**

```
git clone https://github.com/tashfeenahmed/freellmapi.git
cd freellmapi
npm install
```

## Ejecución

**Iniciar el servicio y consultar el modelo.**

```
npm start
# OpenAI uyumlu istek:
curl http://localhost:3000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"gpt-4o-mini","messages":[{"role":"user","content":"Merhaba!"}]}'
```

## Arquitectura técnica y principio de funcionamiento

- Capa de adaptador de proveedor: arquitectura extensible que normaliza diferentes API REST y WebSocket en un formato de respuesta JSON común.
- Equilibrio de carga dinámico y monitoreo de cuotas: monitorear los límites de velocidad actuales de cada proveedor y dirigir las solicitudes al modelo activo de respuesta más rápida.
- Gestión de errores y caché integrada: almacenamiento en caché de consultas repetidas y mecanismo de reintento automático en caso de tiempos de espera.

## Mecanismo de enrutamiento del modelo y tolerancia a fallas.

- Comparación de varios modelos: mida la calidad de la respuesta y la latencia enviando la misma entrada del usuario a diferentes modelos de código abierto.
- Ahorre en desarrollo y creación de prototipos: ponga en marcha rápidamente prototipos impulsados ​​por IA y proyectos MVP sin definir claves API pagas.
- Estrategia de respaldo (canalización de respaldo): asegúrese de que su sistema redirija a modelos secundarios sin interrupción cuando el proveedor principal deje de funcionar.

## Si no programa

Pegue esto en su agente (Claude Code · Codex · Antigravity)

¿Puede explicar con ejemplos de código cómo ejecutar la herramienta FreeLLMAPI en mi servidor local con Docker, cómo apuntar el SDK de OpenAI Node.js a este punto final local y cómo habilitar el uso de un modelo de respaldo automático cuando falla un proveedor?

Repositorio: https://github.com/tashfeenahmed/freellmapi. Sigue las instrucciones oficiales del archivo README de este repositorio para la instalación y ejecución.

Antes de empezar, comprueba en qué sistema operativo estamos y si las herramientas necesarias (ej. Python, Node.js, Git, Docker) están instaladas. Instala las que falten paso a paso según este sistema.

Crea una carpeta nueva y vacía para trabajar. No toques ningún archivo fuera de esta carpeta y no borres nada. Antes de ejecutar cada comando, dime qué vas a hacer en una frase.

Dime qué debería ver en la pantalla al final de cada paso. Si ocurre un error, te pegaré el mensaje de error tal cual y lo solucionaremos juntos.

## Preguntas frecuentes

- ¿Necesito comprar una clave API para usar FreeLLMAPI? No. El sistema combina 34 modelos de IA que ofrecen niveles gratuitos o proporcionan inferencias gratuitas disponibles públicamente.
- ¿Qué modelos de lenguaje principales son compatibles? Se admiten modelos abiertos como Llama 3, Mistral, Gemma, Claude y modelos populares como el nivel gratuito de Google Gemini.
- ¿Es adecuado para la privacidad corporativa? FreeLLMAPI es de código abierto y se ejecuta en su red local, pero los proveedores gratuitos que lo respaldan tienen sus propios términos de uso y políticas de privacidad.
- ¿Es compatible con LangChain o CrewAI? Sí. Dado que proporciona una emulación completa de API REST de OpenAI, se puede utilizar directamente con todos los marcos LLM configurando la dirección baseURL en localhost:3000/v1.

## Términos relacionados del glosario

- [Full-stack](https://trescout.com/es/dictionary/full-stack/)
- [Pipeline](https://trescout.com/es/dictionary/pipeline/)
- [Proxy](https://trescout.com/es/dictionary/proxy/)
- [Localhost](https://trescout.com/es/dictionary/localhost/)
- [SDK](https://trescout.com/es/dictionary/sdk/)
- [LLM](https://trescout.com/es/dictionary/llm/)

- **Para quién es:** Desarrolladores de inteligencia artificial, investigadores de código abierto, ingenieros completos y desarrolladores de prototipos.
- **Licencia:** MIT (Licencia de código abierto libre)
- **Marco:** Proxy inverso TypeScript / Node.js
- **Plataformas:** Docker, Linux, macOS, Windows

## Enlaces

- [Repositorio en GitHub →](https://github.com/tashfeenahmed/freellmapi)
- [Leer en turco →](https://trescout.com/discover/freellmapi/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-08-28: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. El texto de presentación se preparó con IA a partir de la propia documentación del repositorio y esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/freellmapi/
