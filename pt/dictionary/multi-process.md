# O que é Multi-process?

*Glossário · Dev · Última atualização: 7 de outubro de 2026*

É um método em que um programa de computador é executado simultaneamente, dividindo suas tarefas em vários subprocessos completamente independentes, cada um com seu próprio espaço de memória dedicado.

## Definição

Na programação tradicional, uma aplicação geralmente é executada sequencialmente em um único fluxo. Na abordagem de multi-process (ou múltiplos processos), o sistema operacional cria uma área de trabalho separada para cada tarefa. Graças a esse método, que você encontrará frequentemente no glossário do TreScout, se um dos processos encontrar um erro e travar, os outros processos continuam funcionando sem serem afetados por essa situação.

***Analogia:** Você pode comparar isso a cozinheiros independentes que trabalham na mesma cozinha, mas têm suas próprias bancadas, suas próprias facas e seus próprios ingredientes. Mesmo que um dos cozinheiros corte o dedo e pare de trabalhar, os outros cozinheiros continuam cozinhando com segurança em suas próprias bancadas.*

## Como funciona

Ao nível do sistema operacional, um endereço de memória separado é alocado para cada processo. O programa gera novos subprocessos a partir de um processo principal, e esses processos compartilham tarefas comunicando-se entre si por meio de canais de comunicação especiais.

## Onde é usado

É frequentemente utilizado, em especial, para executar cada aba como um processo separado em navegadores de internet, em sistemas de processamento de big data e em aplicações de servidor que realizam cálculos pesados em segundo plano.

## Costuma ser confundido com

É frequentemente confundido com o conceito de multi-threading. Enquanto no método multi-threading as tarefas são realizadas com threads leves que compartilham o mesmo espaço de memória, no método multi-process cada tarefa possui seu próprio espaço de memória totalmente isolado.

## Perguntas frequentes

**O uso de multi-process sobrecarrega o computador?**

Sim, como memória e recursos separados são alocados para cada processo, ele pode consumir mais recursos do computador em comparação com outros métodos.

**Em quais situações o multi-process deve ser preferido?**

Deve ser preferido em tarefas pesadas onde a segurança e a estabilidade são fundamentais, e onde você não quer que um processo seja afetado pelo travamento do outro.

## Termos relacionados

- [Concurrency](https://trescout.com/pt/dictionary/concurrency/)
- [Runtime](https://trescout.com/pt/dictionary/runtime/)
- [Thread-safety](https://trescout.com/pt/dictionary/thread-safety/)
- [Distributed](https://trescout.com/pt/dictionary/distributed/)

## Ferramentas relacionadas

- [Raddebugger](https://trescout.com/pt/discover/raddebugger/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/multi-process/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/multi-process/
