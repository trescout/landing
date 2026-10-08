# O que é Full Text Search?

*Glossário · Data · Última atualização: 22 de setembro de 2026*

A busca de texto completo (conhecida em turco como tam metin arama) é o método de busca que encontra palavras presentes em todo o conteúdo dos documentos.

## Definição e origem da palavra

Enquanto a busca simples analisa o nome do arquivo, a busca de texto completo examina cada frase dentro do documento. É a maneira mais eficaz de acessar informações em grandes arquivos. Sua infraestrutura moderna baseia-se em uma estrutura chamada índice invertido (inverted index).

***Analogia:** É como procurar a frase desejada folheando todas as páginas de um livro, em vez de olhar apenas para o sumário.*

## Como conhecer e usar no dia a dia?

**Pesquisa no site:** Buscar um tópico no blog.
**E-mail:** Encontrar uma mensagem de anos atrás.
**Código:** Procurar uma função no repositório.
**Direito:** Pesquisar no arquivo de jurisprudência.

## Profundidade Técnica e Arquitetura

A linha é a seguinte:

**Tokenização:** O texto é dividido em palavras, os sufixos são reduzidos à raiz.
**Índice invertido:** O documento em que cada palavra aparece é regist(r)ado antecipadamente.
**Ranqueamento:** Algoritmos como o BM25 ranqueiam com base no peso do título e da frequência.

Exemplo com o Postgres:

```
SELECT baslik FROM yazilar
WHERE to_tsvector('turkish', icerik) @@ to_tsquery('turkish', 'yapay & zeka');
```

Quando a semelhança semântica (por exemplo, digitar "automóvel" e aparecer "carro") é necessária, a busca vetorial é exigida. Ambos também são usados juntos: primeiro a palavra-chave restringe, depois o vetor ranqueia.

## Coisas frequentemente misturadas

Pode ser confundido com a busca de metadados. A busca de metadados analisa as informações do arquivo (nome, data, tamanho), enquanto a busca de texto completo analisa o conteúdo. Já a busca vetorial analisa o significado, não a palavra.

## Use em diferentes disciplinas

**Biblioteca:** Varredura de texto completo em vez de catálogo de fichas.
**Livro:** A seção de índice no final.
**Arquivo:** Pesquisar um assunto em uma coleção de recortes de jornal.

## Perguntas Frequentes

**Não vai correr muito devagar?**

Fornece resultados em segundos graças ao índice pré-criado. A pesquisa sem índice é lenta, por isso o índice é essencial.

**Funciona em todos os tipos de arquivos?**

Sim, em arquivos onde o texto pode ser extraído. Em documentos digitalizados, o texto é obtido primeiro por OCR.

**Os sufixos em turco causam problemas?**

Na análise qualificada, os sufixos são reduzidos à raiz. A precisão cai em um motor com suporte a idiomas fraco; é necessária uma configuração com suporte ao turco.

**Quando a pesquisa vetorial é necessária?**

Ao procurar sinônimos e conceitos. Se a palavra-chave não for encontrada, o vetor entra em ação; ambos juntos são poderosos.

## Termos relacionados

- [RAG](https://trescout.com/pt/dictionary/rag/)
- [Vector Index](https://trescout.com/pt/dictionary/vector-index/)
- [Document Parsing](https://trescout.com/pt/dictionary/document-parsing/)

## Ferramentas relacionadas

- [Karakeep](https://trescout.com/pt/discover/karakeep/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/full-text-search/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/full-text-search/
