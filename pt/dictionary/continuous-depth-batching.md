# O que é Continuous Depth Batching?

Um método que permite que modelos de inteligência artificial processem um grande número de solicitações simultâneas de forma contínua e rápida, sem a necessidade de espera.

## Definição
As solicitações externas feitas aos modelos de inteligência artificial são colocadas em uma fila. Este método gerencia de forma inteligente a profundidade e o tempo de processamento das solicitações recebidas dentro do modelo, evitando que o sistema fique ocioso. Assim, os recursos de hardware são utilizados da maneira mais eficiente e os tempos de resposta são reduzidos.

## Como funciona
Fragmentos de texto ou cargas de computação recebidos são agrupados dinamicamente de acordo com a capacidade instantânea do modelo. Graças ao gerenciamento de filas, cada dado cujo processamento é concluído é imediatamente substituído por um novo.

## Onde é usado
É utilizado para aumentar o desempenho em infraestruturas de servidor que hospedam grandes modelos de linguagem e em serviços de inteligência artificial baseados em nuvem.

## Costuma ser confundido com
Diferente dos métodos clássicos de processamento em lote, ele não espera que as solicitações sejam concluídas, alimentando o fluxo instantaneamente.

## Perguntas frequentes
**Reduz os custos de servidor?**
Sim, otimiza o custo ao permitir que mais usuários sejam atendidos simultaneamente no mesmo hardware.


## Termos relacionados
- [Continuous Batching](/pt/dictionary/continuous-batching/)
- [Inference Server](/pt/dictionary/inference-server/)
- [GPU](/pt/dictionary/gpu/)
- [LLM Inference](/pt/dictionary/llm-inference/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/continuous-depth-batching/
