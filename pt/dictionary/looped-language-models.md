# O que é Looped Language Models?

São modelos de inteligência artificial cíclicos que realizam raciocínio passo a passo usando suas próprias saídas geradas como entrada novamente.

## Definição
Diferente dos modelos de linguagem tradicionais de passagem única, os modelos de linguagem em loop são estruturas que reprocessam sua saída entre camadas ou em um processo circular. Ao resolver um problema complexo, em vez de fornecer a resposta de uma só vez, o modelo melhora o rascunho inicial que ele mesmo gerou, passo a passo. Essa abordagem aprofunda a capacidade de raciocínio sem aumentar o custo computacional.

## Como funciona
No primeiro passo, o modelo gera uma resposta provisória e alimenta essa resposta de volta à camada de entrada do modelo por meio de uma memória interna ou mecanismo de loop. Esse processo continua até que o número de ciclos definido ou o limite de confiança seja atingido.

## Onde é usado
São usados especialmente na resolução de problemas matemáticos complexos, análise de quebra-cabeças lógicos e processos de depuração de código. Também são preferidos em agentes de inteligência artificial que exigem raciocínio profundo.

## Costuma ser confundido com
Não devem ser confundidos com redes neurais recorrentes tradicionais. Enquanto as redes neurais recorrentes processam dados ao longo de uma série temporal, esses modelos executam a arquitetura transformer novamente com uma lógica cíclica.

## Perguntas frequentes
**Esses modelos funcionam de forma mais lenta?**
Sim. Como o mesmo modelo executa vários ciclos, o tempo de geração da resposta pode ser um pouco maior.

**O número de ciclos pode ser infinito?**
Não. Nos sistemas, um limite máximo de ciclos é definido para evitar o consumo excessivo de recursos.


## Termos relacionados
- [Transformer](/pt/dictionary/transformer/)
- [LLM](/pt/dictionary/llm/)
- [Looped Transformer](/pt/dictionary/looped-transformer/)
- [Inference](/pt/dictionary/inference/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/looped-language-models/
