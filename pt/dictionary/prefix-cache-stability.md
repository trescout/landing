# O que é Prefix Cache Stability?

É uma técnica que permite à inteligência artificial responder às mesmas perguntas com muito mais rapidez e consistência, mantendo na memória as informações que processou anteriormente.

## Definição
Em vez de pensar sempre do zero, os modelos de inteligência artificial armazenam em cache informações importantes (prefixo) no início da conversa. Desta forma, o modelo não precisa ler o contexto repetidamente e o tempo de resposta é reduzido.

## Como funciona
O sistema bloqueia as informações que o modelo utiliza com mais frequência ou fornece inicialmente na memória e as utiliza diretamente em outras consultas.

## Onde é usado
É usado em aplicativos de inteligência artificial de alto tráfego e bots de bate-papo.

## Costuma ser confundido com
Pode ser confundido com cache KV; O cache KV é a memória do modelo em tempo de execução e esta é uma estratégia que garante que a memória permaneça estável.

## Perguntas frequentes
**Este método aumenta a precisão?**
Sim, porque o modelo parte de uma base fixa em vez de interpretar a mesma informação de forma diferente a cada vez.


## Termos relacionados
- [KV Cache](/pt/dictionary/kv-cache/)
- [Inference Engine](/pt/dictionary/inference-engine/)
- [Context Window](/pt/dictionary/context-window/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/prefix-cache-stability/
