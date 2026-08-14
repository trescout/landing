# O que é Prefix Cache?

Método de aceleração que evita que a inteligência artificial repita as mesmas operações, mantendo na memória o início do texto que processou anteriormente.

## Definição
Os modelos de inteligência artificial podem ler desde o início sempre que processam textos longos. O cache de prefixo salva a parte inicial imutável deste texto na memória. Assim, o modelo usa as informações literais em vez de reler essa parte na próxima solicitação.

## Como funciona
O sistema armazena em cache os prefixos dos textos processados ​​pelo modelo. Quando uma consulta semelhante chega, o sistema usa imediatamente essa parte do cache e processa apenas as partes recém-adicionadas.

## Onde é usado
É usado em serviços LLM, conversas que exigem contexto longo e aplicações de inteligência artificial de alto tráfego.

## Costuma ser confundido com
Pode ser confundido com cache KV; Enquanto o cache KV mantém o estado interno do modelo, o cache de prefixo contém blocos de texto.

## Perguntas frequentes
**Quanta velocidade ele fornece?**
Reduz significativamente o tempo de resposta, especialmente ao trabalhar com documentos longos.

**Está sempre disponível?**
Sim, mas como ocupa espaço na memória, deve ser gerenciado de acordo com a capacidade do sistema.


## Termos relacionados
- [KV Cache](/pt/dictionary/kv-cache/)
- [Context Window](/pt/dictionary/context-window/)
- [Inference](/pt/dictionary/inference/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/prefix-cache/
