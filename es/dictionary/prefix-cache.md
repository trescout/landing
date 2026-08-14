# ¿Qué es Prefix Cache?

Un método de aceleración que evita que la inteligencia artificial repita las mismas operaciones manteniendo en la memoria los inicios del texto que ha procesado previamente.

## Definición
Los modelos de inteligencia artificial pueden leer desde el principio cada vez que procesan textos largos. La caché de prefijos guarda la parte inicial inalterable de este texto en la memoria. Así, el modelo utiliza la información literal en lugar de releer esa parte en su siguiente solicitud.

## Cómo funciona
El sistema almacena en caché los prefijos de los textos procesados ​​por el modelo. Cuando llega una consulta similar, el sistema utiliza inmediatamente esta parte del caché y procesa solo las partes recién agregadas.

## Dónde se usa
Se utiliza en servicios LLM, conversaciones que requieren un contexto extenso y aplicaciones de inteligencia artificial de alto tráfico.

## Suele confundirse con
Se puede confundir con la caché KV; Mientras que la caché KV contiene el estado interno del modelo, la caché de prefijo contiene bloques de texto.

## Preguntas frecuentes
**¿Cuánta velocidad proporciona?**
Reduce significativamente el tiempo de respuesta, especialmente cuando se trabaja con documentos largos.

**¿Está siempre disponible?**
Sí, pero como ocupa espacio en la memoria hay que gestionarlo según la capacidad del sistema.


## Términos relacionados
- [KV Cache](/es/dictionary/kv-cache/)
- [Context Window](/es/dictionary/context-window/)
- [Inference](/es/dictionary/inference/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/prefix-cache/
