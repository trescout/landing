# O que é Clean Code?

*Glossário · Dev · Última atualização: 22 de setembro de 2026*

Código limpo é o código que pode ser lido por humanos.

## Definição e origem da palavra

A máquina executa todos os códigos, um ser humano não consegue ler todos os códigos. Nome significativo, função pequena e fluxo simples trazem legibilidade. Robert Martin é o nome de referência desta disciplina.

***Analogia:** É como ter estantes de biblioteca organizadas por gênero e autor.*

## Como conhecer e usar no dia a dia?

**Equipe:** Base de código comum.
**Revisão:** Verificação de legibilidade.
**Cuidados:** Revertendo para o código antigo.

## Profundidade Técnica e Arquitetura

Princípios:

**Nome:** O nome que expressa a intenção.
**Dimensão:** Função de trabalho único.
**De novo:** A peça comum está em um só lugar.

Exemplo:

```
# önce
def h(a, b):
    return a + a*b
# sonra
def indirimli_fiyat(fiyat, oran):
    return fiyat + fiyat * oran
```

Regra: Executar o código é a primeira etapa, ler o código é a segunda etapa.

## Use em diferentes disciplinas

**Mesa:** Área de trabalho arrumada.
**Prateleiras:** Classificado por gênero e autor.
**Jardim:** Arranjo de galhos podados.

## Perguntas Frequentes

**Não é suficiente trabalhar?**

Não é suficiente. O código funcional salva hoje, o código lido salva amanhã.

**Desacelera?**

No começo sim, na manutenção não. Ganha dinheiro no total.

**Como é medido?**

Com tempo de revisão e taxa de erro. O número por si só não é suficiente.

**Por onde começar?**

Do nome e da função. O código tocado é apagado.

## Termos relacionados

- [Refactoring](https://trescout.com/pt/dictionary/refactoring/)
- [Unit Testing](https://trescout.com/pt/dictionary/unit-testing/)
- [Engineering Skills](https://trescout.com/pt/dictionary/engineering-skills/)

## Ferramentas relacionadas

- [Clean Code Javascript](https://trescout.com/pt/discover/clean-code-javascript/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/clean-code/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/clean-code/
