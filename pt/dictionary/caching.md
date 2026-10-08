# O que é Caching?

*Glossário · Data · Última atualização: 22 de setembro de 2026*

Caching (em português, armazenamento em cache) é a cópia de dados frequentes para uma camada rápida.

## Definição e origem da palavra

Cache significa armazenamento em cache. O sistema fornece os dados a partir de uma cópia em vez de recalculá-los. O tempo de resposta diminui e a carga é aliviada. Funciona em todas as camadas, do navegador ao data center.

***Analogia:** É como carregar o livro favorito na bolsa; não é preciso ir à biblioteca todas as vezes.*

## Como conhecer e usar no dia a dia?

**Navegador:** Armazenamento de páginas e imagens.
**Aplicação:** Cópia offline.
**Apresentador:** Armazenamento de resultados de consultas.

## Profundidade Técnica e Arquitetura

Estratégias:

**LRU:** Remove o menos recentemente utilizado.
**TTL:** O que expira, cai.
**Cache-aside:** A aplicação gerencia.

Diretiva do navegador:

```
Cache-Control: public, max-age=3600
```

Esta linha diz que a cópia é válida por uma hora. Há um custo de consistência: quando a fonte muda, a cópia torna-se obsoleta; para dados críticos, o tempo é mantido curto.

## Coisas frequentemente misturadas

Pensa-se que é o banco de dados. O banco de dados é persistente e vasto, o cache é temporário e rápido. Um é o cofre, o outro é a carteira de bolso.

## Use em diferentes disciplinas

**Bolsa:** Livro frequente à mão.
**Geladeira:** Comida diária na frente.
**Despensa:** Estoque em massa no fundo.

## Perguntas Frequentes

**O que acontece se o cache ficar cheio?**

O antigo e pouco usado é descartado, o novo é escrito. A política gerencia isso.

**Quando é limpo?**

Quando o tempo expira, a capacidade é excedida ou manualmente. Dados críticos são mantidos por pouco tempo.

**Pode haver inconsistência?**

Pode. Quando a fonte muda, a cópia fica obsoleta; é necessária disciplina de versão e tempo.

**Onde é mantido?**

Na memória, no disco ou na borda da CDN. É escolhido de acordo com o equilíbrio entre velocidade e capacidade.

## Termos relacionados

- [KV Cache](https://trescout.com/pt/dictionary/kv-cache/)
- [Prefix Cache](https://trescout.com/pt/dictionary/prefix-cache/)
- [Database](https://trescout.com/pt/dictionary/database/)

## Ferramentas relacionadas

- [Free for Dev](https://trescout.com/pt/discover/free-for-dev/)
- [OmniRoute](https://trescout.com/pt/discover/omniroute/)
- [Guava](https://trescout.com/pt/discover/guava/)
- [Omlx](https://trescout.com/pt/discover/omlx/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/caching/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/caching/
