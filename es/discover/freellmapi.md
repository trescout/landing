# Combine 34 proveedores de LLM gratuitos en una sola API

FreeLLMAPI proporciona enrutamiento inteligente y tolerancia a fallas al agregar 34 proveedores principales de modelos de lenguaje gratuitos diferentes en una única API REST en formato OpenAI.

- ★ 29.808
- TypeScript
- GitHub Trending · 2026-08-28

## Qué aporta
- 34 proveedores de modelos gratuitos: acceso integral a docenas de proveedores gratuitos, incluidos Google Gemini, Groq, Cloudflare Workers AI y HuggingFace.
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
¿Puede explicar con ejemplos de código cómo ejecutar la herramienta FreeLLMAPI en mi servidor local con Docker, cómo apuntar el SDK de OpenAI Node.js a este punto final local y cómo habilitar el uso de un modelo de respaldo automático cuando falla un proveedor?

## Preguntas frecuentes
- ¿Necesito comprar una clave API para usar FreeLLMAPI? No. El sistema combina 34 modelos de IA que ofrecen niveles gratuitos o proporcionan inferencias gratuitas disponibles públicamente.
- ¿Qué modelos de lenguaje principales son compatibles? Se admiten modelos abiertos como Llama 3, Mistral, Gemma, Claude y modelos populares como el nivel gratuito de Google Gemini.
- ¿Es adecuado para la privacidad corporativa? FreeLLMAPI es de código abierto y se ejecuta en su red local, pero los proveedores gratuitos que lo respaldan tienen sus propios términos de uso y políticas de privacidad.
- ¿Es compatible con LangChain o CrewAI? Sí. Dado que proporciona una emulación completa de API REST de OpenAI, se puede utilizar directamente con todos los marcos LLM configurando la dirección baseURL en localhost:3000/v1.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/freellmapi/
