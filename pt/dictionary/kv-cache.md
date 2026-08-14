# O que é KV Cache?

> Key-Value Cache

É um método de aceleração que evita que a inteligência artificial repita as mesmas operações, mantendo na memória as palavras que processou anteriormente.

## Definição
Ao produzir um texto, em vez de pensar do zero em cada palavra, a inteligência artificial armazena as informações previamente processadas em um cache como valores de ‘Chave’ e ‘Valor’. Este sistema permite que o modelo recupere rapidamente o passado sem ter que recalculá-lo ao prever a próxima palavra. Assim, a carga de processamento é reduzida e os tempos de resposta são significativamente reduzidos.

## Como funciona
Enquanto o modelo está em execução, ele é criado automaticamente em segundo plano e mantido na memória. Esse cache começa a ficar cheio quando o usuário inicia uma longa conversa. Quando a memória fica cheia, o sistema desenvolve estratégias para limpar informações antigas ou abrir espaço para novos dados.

## Onde é usado
É utilizado nos processos de trabalho de LLMs e principalmente em interfaces de chat onde são produzidos textos longos.

## Costuma ser confundido com
Pode ser confundido com Janela de Contexto, mas este não é um limite de capacidade, mas um método de utilização eficiente desta capacidade.

## Perguntas frequentes
**Por que o cache KV é importante?**
Ao evitar que a inteligência artificial calcule a mesma frase repetidamente, reduz a carga do processador e acelera a resposta.

**O que acontece se a memória ficar cheia?**
O sistema pode tornar-se incapaz de processar novos dados ou começar a esquecer informações antigas.


## Termos relacionados
- [LLM](/pt/dictionary/llm/)
- [Context Window](/pt/dictionary/context-window/)
- [Inference](/pt/dictionary/inference/)
- [Memory Management](/pt/dictionary/memory-management/)

## Ferramentas relacionadas
- [LMCache](/pt/discover/lmcache/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/kv-cache/
