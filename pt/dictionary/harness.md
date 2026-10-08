# O que é Harness?

*Glossário · Dev · Última atualização: 22 de setembro de 2026*

Harness (em português, conjunto de testes) é uma estrutura que testa o código automaticamente.

## Definição e origem da palavra

Harness significa arreios. Sempre que o código é atualizado, os testes são executados e emitem um alerta em caso de falha. É uma rede de segurança que realiza a verificação da integridade do sistema.

***Analogia:** É como uma linha de controle automático na fábrica que inspeciona os freios e faróis de cada veículo.*

## Como conhecer e usar no dia a dia?

**Desenvolvimento:** Teste após cada commit.
**CI:** Porta automática na linha.
**Qualidade:** Varredura pré-lançamento.

## Profundidade Técnica e Arquitetura

Peças:

**Cenário de teste:** Definição de comportamento esperado.
**Fixture:** Dados de teste prontos.
**Mock:** Simulação de serviço externo.
**Relatório:** Lista de aprovados e reprovados.

Exemplo:

```
def test_toplama():
    assert topla(2, 3) == 5
```

Regra: Testes rápidos rodam a cada commit, os lentos rodam à noite. A meta de cobertura é definida pela equipe.

## Coisas frequentemente misturadas

Pensa-se que é o próprio software. No entanto, o harness não é o código, mas o ambiente que audita o código. Um é o jogador, o outro é o árbitro.

## Use em diferentes disciplinas

**Linha de fábrica:** Inspeção de freios e faróis de cada veículo.
**Cinto de segurança:** Mecanismo que retém em caso de colisão.
**Treinamento:** Pista de medição de desempenho.

## Perguntas Frequentes

**Por que é necessário?**

Reduz o erro humano e detecta falhas a cada alteração.

**É obrigatório em todo software?**

É um padrão em trabalhos profissionais. Em códigos de teste, pode ser um exagero.

**Quando deve ser escrito?**

Junto com o código, preferencialmente antes. Testes deixados para depois ficam incompletos.

**Qual é a meta de cobertura?**

Definido pela equipe. Mantido alto no caminho crítico e baixo nas partes periféricas.

## Termos relacionados

- [Testing Framework](https://trescout.com/pt/dictionary/testing-framework/)
- [Unit Testing](https://trescout.com/pt/dictionary/unit-testing/)
- [QA](https://trescout.com/pt/dictionary/qa/)

## Ferramentas relacionadas

- [Jcode](https://trescout.com/pt/discover/jcode/)
- [Harness SDK](https://trescout.com/pt/discover/harness-sdk/)
- [Harness · Ajan Ekip Fabrikası](https://trescout.com/pt/discover/harness/)
- [Munder Difflin](https://trescout.com/pt/discover/munder-difflin/)
- [Claude Code Harness](https://trescout.com/pt/discover/claude-code-harness/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/harness/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/harness/
