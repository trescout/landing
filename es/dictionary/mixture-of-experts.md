# ¿Qué es Mixture of Experts?

> MoE

Es un sistema que resuelve tareas complejas dividiéndolas en subsecciones, cada una especializada en un tema diferente.

## Definición
En esta estructura, en lugar de que todo el modelo responda a cada pregunta, solo se activan las secciones (expertos) especializadas en esa consulta. Esto permite que el modelo, a pesar de tener un tamaño gigantesco, solo utilice la parte necesaria. Como resultado, se obtienen respuestas más inteligentes y rápidas.

## Cómo funciona
Cuando se hace una pregunta, un mecanismo de 'enrutamiento' determina a qué área de especialización pertenece. Solo esos expertos procesan la pregunta y generan la respuesta.

## Dónde se usa
Se utiliza en la mayoría de los modelos modernos de inteligencia artificial a gran escala para aumentar la eficiencia.

## Suele confundirse con
Podría confundirse con el procesamiento de todos los datos por parte de un único modelo.

## Preguntas frecuentes
**¿Cómo se seleccionan los expertos?**
Durante el entrenamiento, el modelo aprende qué expertos son mejores en qué temas.

**¿Este método ralentiza el modelo?**
Al contrario, es más rápido porque solo se ejecutan las partes relevantes.


## Términos relacionados
- [LLM](/es/dictionary/llm/)
- [AI Models](/es/dictionary/ai-models/)
- [Inference](/es/dictionary/inference/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/mixture-of-experts/
