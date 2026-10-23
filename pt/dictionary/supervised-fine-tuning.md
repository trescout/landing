# O que é Supervised Fine-Tuning?

*Inteligência artificial · Última atualização: 23 de outubro de 2026*

> SFT

É o processo de adaptação de um modelo de inteligência artificial pré-treinado para uma tarefa específica utilizando pares de dados rotulados.

## Definição

O ajuste fino supervisionado (Supervised Fine-Tuning) permite que modelos base, que adquiriram habilidades gerais de linguagem por meio de grandes conjuntos de dados, sejam direcionados a uma área de especialização específica. Nesse processo, são fornecidos ao modelo dados de exemplo diretos preparados na forma de perguntas e respostas ideais. O modelo aprende a gerar respostas corretas para as instruções fornecidas analisando esses pares de dados rotulados.

***Analogia:** É semelhante a um médico com formação médica geral que se especializa em um determinado tipo de doença ao examinar casos documentados.*

## Como funciona

Os pesos do modelo são atualizados em pequenas proporções com base nos padrões de entrada e saída do conjunto de dados preparado. Ao calcular a taxa de erro, garante-se que as respostas produzidas pelo modelo se aproximem das respostas-alvo. Esse processo ajuda a alinhar o modelo ao formato desejado sem sofrer de sobreajuste (overfitting).

## Onde é usado

É utilizado para garantir que os bots de atendimento ao cliente respondam de acordo com os documentos internos da empresa e para que os assistentes de programação produzam saídas dentro de determinados padrões.

## Costuma ser confundido com

Pode ser confundido com o conceito geral de Fine-Tuning. Enquanto o Fine-Tuning é um guarda-chuva geral de adaptação, o Supervised Fine-Tuning representa a etapa específica realizada com pares de instruções e respostas rotuladas.

## Perguntas e respostas

**De quantos dados se precisa para o Supervised Fine-Tuning?**

Dependendo da complexidade da tarefa que você vai desenvolver, geralmente entre algumas centenas e alguns milhares de pares de dados de qualidade são suficientes.

**O processo de SFT faz com que o modelo esqueça suas habilidades gerais?**

Em processos de treinamento mal configurados ou prolongados em excesso, o modelo pode correr o risco de perder sua base de conhecimento geral.

## Termos relacionados

- [Fine-tuning](https://trescout.com/pt/dictionary/fine-tuning/)
- [Post-training](https://trescout.com/pt/dictionary/post-training/)
- [RLHF](https://trescout.com/pt/dictionary/rlhf/)
- [Foundation Model](https://trescout.com/pt/dictionary/foundation-model/)

Esta explicação foi escrita em linguagem simples para a TreScout com IA e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/supervised-fine-tuning/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/supervised-fine-tuning/
