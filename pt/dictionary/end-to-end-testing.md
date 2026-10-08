# O que é End-to-End Testing?

*Glossário · Dev · Última atualização: 22 de setembro de 2026*

> E2E Testing

O teste de ponta a ponta (ou E2E, para abreviar) consiste em testar a aplicação do princípio ao fim, exatamente como um usuário faria.

## Definição e origem da palavra

De ponta a ponta significa de ponta a ponta. Testa-se o todo, não as partes: faz-se o login, prime-se o botão, os dados são enviados, o resultado retorna. É a porta de conformidade antes da publicação.

***Analogia:** É como tentar ligar a chave e pegar a estrada, em vez do motor.*

## Como conhecer e usar no dia a dia?

**Lançamento:** Turnê pré-versão.
**Loja:** Caminho de compra.
**Formulário:** Fluxo de cadastro.

## Profundidade Técnica e Arquitetura

Layout:

**Caminho crítico:** Fluxo que gera receita primeiro.
**Automação:** Ferramenta que controla o navegador.
**Dados:** Conta de teste e reinicialização.

Exemplo:

```
test("giriş", async () => {
  await sayfa.goto("/giris");
  await bekle("#panel");
});
```

Motivo da lentidão: O navegador real é aberto. O caminho crítico é selecionado, nem tudo é testado.

## Coisas frequentemente misturadas

Confundido com teste unitário. Aquele olha para a peça, este olha para o todo. Um é o teste do parafuso, o outro do test-drive.

## Use em diferentes disciplinas

**Carro:** Partindo da chave.
**Ensaio:** Revisão geral.
**Final:** Ensaio de transmissão.

## Perguntas Frequentes

**Por que apenas isso não é feito?**

É lento, a localização da falha é vaga. É usado junto com a unidade.

**Com que frequência roda?**

Antes da transmissão e à noite. O subconjunto crítico é executado em cada commit.

**Quem escreve?**

O desenvolvedor e o testador escrevem juntos. O proprietário é definido.

**É frágil?**

Quebra quando a interface muda. É escrito de forma seletiva e durável.

## Termos relacionados

- [Unit Testing](https://trescout.com/pt/dictionary/unit-testing/)
- [Testing Framework](https://trescout.com/pt/dictionary/testing-framework/)
- [Web Interface](https://trescout.com/pt/dictionary/web-interface/)

## Ferramentas relacionadas

- [Cypress](https://trescout.com/pt/discover/cypress/)
- [E2e](https://trescout.com/pt/discover/e2e/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/end-to-end-testing/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/end-to-end-testing/
