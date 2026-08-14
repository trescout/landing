# O que é Data Layer?

É a camada intermediária que permite que seu aplicativo se comunique com o banco de dados e organize os dados.

## Definição
Ele atua como um tradutor entre o frontend do seu aplicativo (a tela que você vê) e o banco de dados por trás dele. Ele garante que os dados sejam transportados com segurança, precisão e rapidez. Usar essa camada em vez de acessar diretamente o banco de dados torna seu código mais limpo e seguro.

## Como funciona
Em vez de escrever consultas diretas ao banco de dados para acessar dados, os desenvolvedores de software chamam funções nesta camada. Portanto, mesmo que o banco de dados seja alterado, o restante do seu aplicativo não será afetado.

## Onde é usado
É o padrão na arquitetura de aplicações web e móveis, principalmente em grandes projetos.

## Costuma ser confundido com
Pode ser misturado com banco de dados; A camada de dados não é o banco de dados, mas o método de acesso ao banco de dados.

## Perguntas frequentes
**Por que não nos conectamos diretamente?**
Uma estrutura em camadas é preferida devido aos riscos de segurança e à complexidade do código.

**Isso afeta o desempenho?**
Quando projetado corretamente, melhora o desempenho porque pode armazenar dados em cache.


## Termos relacionados
- [Database](/pt/dictionary/database/)
- [API](/pt/dictionary/api/)
- [Tech Stack](/pt/dictionary/tech-stack/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/data-layer/
