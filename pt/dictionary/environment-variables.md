# O que é Environment Variables?

*Glossário · Dev · Última atualização: 22 de setembro de 2026*

Variáveis de ambiente são identificadores que mantêm as configurações fora do código.

## Definição e origem da palavra

"Meio Ambiente" significa meio ambiente. Password and address do not stay in the code, they stay in the system. The same code behaves differently in different environment.

***Analogia:** É como um cartão inserido e substituível em vez de uma configuração embutida no dispositivo.*

## Como conhecer e usar no dia a dia?

**Apresentador:** Strings de conexão.
**Aplicação:** Seleção de modo.
**CI:** Chaves secretas.

## Profundidade Técnica e Arquitetura

Layout:

**.env:** Arquivo local, não entra no repositório.
**Prioridade:** O sistema de ambiente sobrescreve o arquivo.
**Esquema:** Lista de nomes necessários.

Valor de exemplo:

```
DATABASE_URL=postgres://kullanici:parola@localhost:5432/db
```

Regra: O valor real não é escrito no exemplo, coloca-se um marcador de posição. A chave vazada é cancelada.

## Coisas frequentemente misturadas

É considerado um valor fixo. O fixo permanece no código, a variável fica fora. Um é uma tatuagem, o outro é um distintivo.

## Use em diferentes disciplinas

**Cartão:** Cartão de configuração variável.
**Bateria do controle:** Energia plug-and-play.
**Chaveiro:** Acesso portátil.

## Perguntas Frequentes

**Por que é mantido em segredo?**

Se compartilhado, pode ser capturado e a conta pode ser aberta. Se permanecer privado, o risco diminui.

**O que é .env?**

É um arquivo de valores locais. Não entra no repositório, apenas o exemplo entra.

**O que acontece se vazar?**

A chave é revogada e os registros são auditados. O atraso é grande.

**Qual é a prioridade?**

O ambiente do sistema sobrescreve o arquivo. O valor de produção vem do sistema.

## Termos relacionados

- [Secrets](https://trescout.com/pt/dictionary/secrets/)
- [Runtime](https://trescout.com/pt/dictionary/runtime/)
- [API](https://trescout.com/pt/dictionary/api/)

## Ferramentas relacionadas

- [Mise](https://trescout.com/pt/discover/mise/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/environment-variables/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/environment-variables/
