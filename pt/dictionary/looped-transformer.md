# O que é Looped Transformer?

É uma arquitetura de inteligência artificial que reduz o uso de memória ao utilizar as mesmas camadas de processamento repetidamente.

## Definição
Enquanto modelos tradicionais exigem uma unidade de processamento separada para cada camada, esta arquitetura utiliza a mesma camada repetidamente em um loop. Isso reduz o tamanho do modelo e consome menos memória. O objetivo é executar modelos grandes em dispositivos menores sem sacrificar o desempenho.

## Como funciona
Os dados entram no modelo e passam pelo mesmo bloco de camadas várias vezes. A cada passagem, os dados são processados um pouco mais até que o resultado final seja alcançado.

## Onde é usado
É preferível em dispositivos com poucos recursos ou em aplicações de inteligência artificial móvel.

## Costuma ser confundido com
Pode ser confundido com a arquitetura transformer padrão, mas aqui o número de camadas é fisicamente menor.

## Perguntas frequentes
**Funciona de forma mais lenta?**
Como reutiliza as camadas, pode exigir um pouco mais de tempo de processamento, mas proporciona economia de memória.

**Por que nem todo modelo é assim?**
Para algumas tarefas complexas, é melhor que cada camada seja especializada para obter melhores resultados.


## Termos relacionados
- [Transformer](/pt/dictionary/transformer/)
- [Quantization](/pt/dictionary/quantization/)
- [SLM](/pt/dictionary/slm/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/looped-transformer/
