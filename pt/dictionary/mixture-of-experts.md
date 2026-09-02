# O que é Mixture of Experts?

> MoE

É um sistema que resolve tarefas complexas dividindo-as em subseções, cada uma especializada em um assunto diferente.

## Definição
Nesta estrutura, em vez de todo o modelo responder a cada pergunta, apenas as seções (especialistas) relevantes para essa pergunta são ativadas. Isso permite que o modelo, apesar de ter dimensões gigantescas, utilize apenas a parte necessária. Como resultado, obtêm-se respostas mais inteligentes e mais rápidas.

## Como funciona
Quando uma pergunta é feita, um mecanismo de 'roteamento' determina em qual área de especialização a pergunta se enquadra. Apenas esses especialistas processam a pergunta e geram a resposta.

## Onde é usado
É utilizado na maioria dos modelos modernos de inteligência artificial de grande escala para aumentar a eficiência.

## Costuma ser confundido com
Pode ser confundido com o processamento de todos os dados por um único modelo.

## Perguntas frequentes
**Como os especialistas são escolhidos?**
Durante o treinamento, o modelo aprende quais especialistas são melhores em quais assuntos.

**Este método torna o modelo mais lento?**
Pelo contrário, é mais rápido porque apenas as partes relevantes são executadas.


## Termos relacionados
- [LLM](/pt/dictionary/llm/)
- [AI Models](/pt/dictionary/ai-models/)
- [Inference](/pt/dictionary/inference/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/mixture-of-experts/
