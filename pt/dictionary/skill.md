# O que é Skill?

*Glossário · AI · Última atualização: 22 de setembro de 2026*

Skill (com a equivalência em turco de yetenek), é uma unidade definida que permite a um assistente de inteligência artificial realizar tarefas utilizando uma ferramenta externa.

## Definição e origem da palavra

A conversa geral do assistente não é suficiente; às vezes ele precisa ler arquivos ou fazer pesquisas. Cada uma dessas funções especiais é definida como uma skill. O conceito passou da era dos assistentes de voz para a era dos agentes: das habilidades da Alexa às atuais capacidades dos agentes.

***Analogia:** É como as diferentes ferramentas nas mãos de um chef; o chef é único e escolhe a ferramenta certa para cada trabalho.*

## Como conhecer e usar no dia a dia?

**Arquivo:** Leitura e resumo de documentos.
**Calendário:** Agendamento de reuniões.
**Pesquisa:** Recuperação de informações atualizadas.

## Profundidade Técnica e Arquitetura

A habilidade é escrita a partir de três partes:

**Nome:** O nome curto que o modelo chamará.
**Descrição:** Descrição de quando deve ser usado. O modelo baseia a seleção nisso.
**Esquema de parâmetros:** Formato de entrada.

Definição de exemplo:

```
{
  "name": "hava-durumu",
  "description": "Belirtilen şehrin güncel havasını verir",
  "parameters": { "sehir": "string" }
}
```

Fluxo: O usuário faz um pedido, o modelo seleciona a capacidade apropriada, preenche o parâmetro, a ferramenta é executada e o resultado retorna ao modelo. A aprovação do usuário é solicitada para capacidades com privilégios de gravação.

## Coisas frequentemente misturadas

Pensa-se que seja uma capacidade geral do modelo. No entanto, o que se quer dizer aqui é a habilidade do assistente de usar ferramentas externas. O modelo entende a linguagem, a skill executa o trabalho.

## Use em diferentes disciplinas

**Culinária:** A faca e as técnicas de molho nas mãos do chef.
**Broca:** Função que varia de acordo com a ponta.
**Telefone:** Cada aplicativo instalado.

## Perguntas Frequentes

**Cada modelo tem uma habilidade?**

Não. Os modelos básicos geram texto, a habilidade é adquirida quando uma ferramenta externa é adicionada ao assistente.

**Como desenvolver habilidades?**

É definido por uma conexão de API ou bloco de código. A descrição é escrita claramente e o modelo escolhe corretamente.

**É seguro?**

As habilidades de leitura têm baixo risco. Em operações como escrita e pagamento, a aprovação e a limitação de escopo são essenciais.

**Quem escreve as habilidades?**

Os desenvolvedores escrevem, as plataformas distribuem na loja. Escrever uma boa descrição é metade do trabalho.

## Termos relacionados

- [AI Agent](https://trescout.com/pt/dictionary/ai-agent/)
- [AI Skill](https://trescout.com/pt/dictionary/ai-skills/)
- [Agent Skills](https://trescout.com/pt/dictionary/agent-skills/)
- [Tools](https://trescout.com/pt/dictionary/tools/)
- [AI Capabilities](https://trescout.com/pt/dictionary/ai-capabilities/)

## Ferramentas relacionadas

- [Anthropic Skills](https://trescout.com/pt/discover/anthropic-skills/)
- [Taste Skill](https://trescout.com/pt/discover/taste-skill/)
- [Archify](https://trescout.com/pt/discover/archify/)
- [Awesome Claude Skills](https://trescout.com/pt/discover/awesome-claude-skills/)
- [Last30days Skill](https://trescout.com/pt/discover/last30days-skill/)
- [I Have Adhd](https://trescout.com/pt/discover/i-have-adhd/)
- [Reverse Skill](https://trescout.com/pt/discover/reverse-skill/)
- [Book to Skill](https://trescout.com/pt/discover/book-to-skill/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/skill/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/skill/
