# O que é Tokenizer?

O tokenizador (ou conversor em tokens) é o componente fundamental de processamento de dados que transforma textos em linguagem natural em tokens numéricos (IDs de tokens) que os grandes modelos de linguagem (LLMs) e redes neurais podem processar matematicamente.

## 1. Definição e o problema fundamental: Por que não usar palavras diretamente?
Grandes modelos de linguagem (GPT-4, Claude, Llama, etc.) não leem textos letra por letra ou palavra por palavra como os humanos. As redes neurais só conseguem operar com matrizes, tensores e números. Portanto, o texto deve primeiro ser convertido em números.

## 2. Algoritmos de tokenização e suas lógicas matemáticas
Os principais algoritmos de tokenização no coração dos modelos de linguagem modernos são os seguintes:

## 3. O "Imposto do Tokenizador" (The Tokenizer Tax) em Turco
Mais de 85% dos dados de treinamento dos grandes modelos de linguagem estão em inglês. Isso faz com que o vocabulário do tokenizador seja preenchido predominantemente com raízes e palavras em inglês.

## 4. Segurança e Casos Limite: Glitch Tokens
Tokens especiais que estão presentes no vocabulário do tokenizador, mas que aparecem raramente ou em contextos sem sentido no corpus de texto durante o pré-treinamento do modelo, são chamados de Glitch Tokens.

## Perguntas frequentes
**O que significa tokenizador, qual é a tradução em turco?**
Em turco, é chamado de "jetonlaştırıcı" ou "simgeleştirici". É o software que divide os textos em linguagem natural nos menores índices numéricos (tokens) que o modelo de inteligência artificial conseguirá entender.

**A quantas palavras ou letras equivale 1 token?**
Em textos em inglês, 1 token equivale em média a 4 caracteres ou 0,75 palavras (100 palavras são cerca de 130 tokens). Em línguas aglutinantes como o turco, devido à divisão de sufixos, 1 palavra pode corresponder em média a 2 a 3 tokens.

**Como funciona o BPE (Byte Pair Encoding)?**
É um algoritmo estatístico que começa com os caracteres mais básicos e constrói um vocabulário de subpalavras de tamanho fixo, combinando passo a passo os pares de caracteres que aparecem com mais frequência lado a lado no conjunto de treinamento.

**Modelos sem tokenizador (tokenizer-free) são possíveis?**
Sim; as arquiteturas de redes neurais de nova geração desenvolvidas recentemente, como MambaByte e MegaByte, têm como objetivo eliminar completamente a camada de tokenizador e processar diretamente os bytes brutos (bytes), eliminando assim a desigualdade linguística.


## Termos relacionados
- [Token](/pt/dictionary/token/)
- [NLP](/pt/dictionary/nlp/)
- [Tokenizer-free](/pt/dictionary/tokenizer-free/)
- [Prompt Engineering](/pt/dictionary/prompt-engineering/)
- [Context](/pt/dictionary/context/)

## Ferramentas relacionadas
- [AI Engineering from Scratch](/pt/discover/ai-engineering-from-scratch/)
- [Minimind](/pt/discover/minimind/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/tokenizer/
