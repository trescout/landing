# O que é Repository Checkout?

*Glossário · Dev · Última atualização: 22 de setembro de 2026*

Check-out do repositório é o processo de download de uma versão específica do repositório para o seu espaço de trabalho.

## Definição e origem da palavra

Você obtém a versão atual do projeto do servidor e a leva para sua mesa. É como pegar um livro emprestado na biblioteca: a fonte permanece, você trabalha com a cópia. As informações de histórico e versão acompanham a cópia.

***Analogia:** É como pegar um livro emprestado na biblioteca, levá-lo até a mesa e começar a ler as páginas uma por uma.*

## Como conhecer e usar no dia a dia?

**Novo projeto:** Baixando o repositório pela primeira vez.
**Migração de versão:** Não volte para a tag antiga e examine o erro.
**Experimente o ramo:** Não abra a filial do seu amigo localmente.

## Profundidade Técnica e Arquitetura

O fluxo é o seguinte:

```
git clone https://github.com/ornek/proje.git
cd proje
git checkout v2.0.0
```

Distinções:

**Clone:** Baixando todo o repositório pela primeira vez.
**Confira:** Alterando versão ou branch no repositório baixado.
**Trocar/Restaurar:** Ramificação e recuperação de comandos no Git moderno.
**Escasso:** Baixando apenas a pasta necessária no enorme repositório.

Regra: Não passe enquanto tiver o trabalho salvo, confirme ou salve-o primeiro.

## Use em diferentes disciplinas

**Biblioteca:** Não tire o livro da estante e leve-o para a mesa.
**Arquivo:** Remova a pasta do armazenamento e examine-a.
**Fotografia:** Não aceite pressão do negativo.

## Perguntas Frequentes

**Ele só baixa arquivos?**

Não. Informações sobre histórico e versão também estão incluídas, para que você possa reverter para a versão antiga.

**Qual é a diferença com Clone?**

Clone é o download inicial, checkout é a passagem pelo repositório baixado. A ordem é nessa direção.

**Como reverter para a versão antiga?**

É passado com uma tag ou hash de commit. Se houver um trabalho salvo, ele será armazenado primeiro.

**O que é mudar?**

É o comando moderno para ramificar. Como o checkout dá muito trabalho, o Git o divide em dois: mudar para o branch, restaurar para o arquivo.

## Termos relacionados

- [Git Push](https://trescout.com/pt/dictionary/git-push/)
- [Tech Stack](https://trescout.com/pt/dictionary/tech-stack/)
- [Cloning](https://trescout.com/pt/dictionary/cloning/)

## Ferramentas relacionadas

- [Checkout](https://trescout.com/pt/discover/checkout/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/repository-checkout/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/repository-checkout/
