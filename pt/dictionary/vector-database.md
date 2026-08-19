# O que é Vector Database?

É um tipo especial de banco de dados onde a inteligência artificial armazena dados para que possa encontrá-los rapidamente com base no seu significado.

## Definição
Um banco de dados vetorial é um sistema de armazenamento especial que armazena dados como vetores numéricos que representam seu significado, em vez de linhas e colunas tradicionais. Essa estrutura permite que a inteligência artificial encontre os dados mais relevantes entre milhões de dados em milissegundos.

## Como funciona
Primeiro, os dados são convertidos em vetores numéricos usando o método de incorporação. Quando uma consulta é feita, o banco de dados mede a distância entre o vetor da consulta e os vetores dos dados. Aqueles com menor distância, ou seja, os mais próximos em significado, são retornados como resultados.

## Onde é usado
É usado em sistemas de busca inteligentes, mecanismos de recomendação e sistemas RAG onde a inteligência artificial cria memória de longo prazo.

## Costuma ser confundido com
É confundido com bancos de dados clássicos como SQL, mas os bancos de dados clássicos procuram correspondências exatas, enquanto os bancos de dados vetoriais procuram semelhanças.

## Perguntas frequentes
**É mais lento que os bancos de dados clássicos?**
Não, é muito mais rápido que os métodos clássicos para pesquisas de similaridade em conjuntos de dados muito grandes.

**Quais dados podem ser armazenados?**
Quaisquer dados cujo significado possa ser convertido em vetor, como texto, imagem, áudio ou vídeo, podem ser armazenados.


## Termos relacionados
- [Embedding](/pt/dictionary/embedding/)
- [RAG](/pt/dictionary/rag/)
- [Knowledge Graph](/pt/dictionary/knowledge-graph/)
- [Memory Engine](/pt/dictionary/memory-engine/)

## Ferramentas relacionadas
- [Turbovec](/pt/discover/turbovec/)
- [Zvec](/pt/discover/zvec/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/vector-database/
