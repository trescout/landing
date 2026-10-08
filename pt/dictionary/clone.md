# O que é Clone?

*Glossário · Dev · Última atualização: 22 de setembro de 2026*

O clone (com o equivalente em turco klonlama) é o processo de criar uma cópia local de um repositório Git remoto, juntamente com todo o seu histórico.

## Definição e origem da palavra

Clone, em inglês, significa cópia exata. No mundo do Git, é usado com o comando git clone: você baixa não apenas os arquivos atuais, mas todo o histórico de commits, branches e tags do projeto.

***Analogia:** É como tirar uma foto de apenas uma página de um livro da biblioteca, mas sim pegar uma cópia inteira do livro para a sua própria prateleira.*

## Como conhecer e usar no dia a dia?

Quando você quer examinar ou contribuir para um projeto de código aberto, o primeiro passo geralmente é clonar:

```
git clone https://github.com/kullanici/proje.git
```

Quando o comando é executado, a pasta do projeto é criada no diretório atual. Se o repositório for muito grande, usa-se um clone raso para obter apenas uma parte do histórico:

```
git clone --depth 1 https://github.com/kullanici/proje.git
```

## Profundidade Técnica e Arquitetura

O diretório .git dentro da pasta clonada é a memória do repositório: todos os objetos de commit, ponteiros de ramificação e endereços remotos ficam aqui. Após o clone:

git fetch baixa as alterações remotas, sem mexer nos seus arquivos.
git pull faz o download e mescla com a sua branch atual.
git push envia seus commits para o repositório remoto (se você tiver permissão).
um fork cria uma cópia no lado do servidor. O clone descarrega essa cópia ou o repositório original para o seu computador. São dois conceitos diferentes.

## Use em diferentes disciplinas

**Biologia:** Uma cópia genética de um organismo vivo. Já o clone no software é uma cópia de dados, não tem relação com seres vivos.
**Mídia:** Trajes sobressalentes para trabalhar enquanto o original está guardado.
**Virtualização:** Criação de uma nova máquina a partir de um modelo pronto.

## Perguntas Frequentes

**Posso alterar o projeto após a clonagem?**

Sim. Você faz as alterações que quiser na sua própria cópia. O repositório original não é afetado. Se quiser propor sua alteração para o projeto, você abre um pull request.

**Qual é a diferença entre fork e clone?**

O fork cria uma cópia no servidor (na sua conta), o clone baixa essa cópia para o seu computador. O fluxo de contribuição geralmente é um fork, seguido por um clone.

**O que devo fazer se o repositório for muito grande?**

Faça um clone raso com --depth 1 ou baixe apenas uma única ramificação (--single-branch). Se precisar do histórico, você poderá aprofundá-lo depois.

**Vou manter o clone atualizado?**

Sim. Basta executar git pull dentro da pasta. Se você tiver alterações, primeiro precisará fazê-las commit ou guardá-las (git stash).

## Termos relacionados

- [CLI](https://trescout.com/pt/dictionary/cli/)
- [Open Source](https://trescout.com/pt/dictionary/open-source/)
- [Self-Hosting](https://trescout.com/pt/dictionary/self-hosting/)

## Ferramentas relacionadas

- [MoneyPrinterTurbo](https://trescout.com/pt/discover/moneyprinterturbo/)
- [VoxCPM](https://trescout.com/pt/discover/voxcpm/)
- [Clone-Wars](https://trescout.com/pt/discover/clone-wars/)
- [Univer](https://trescout.com/pt/discover/univer/)
- [OpenStock](https://trescout.com/pt/discover/openstock/)
- [Hermes WebUI](https://trescout.com/pt/discover/hermes-webui/)
- [Production Agentic RAG Course](https://trescout.com/pt/discover/production-agentic-rag-course/)
- [Flowsint](https://trescout.com/pt/discover/flowsint/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/clone/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/clone/
