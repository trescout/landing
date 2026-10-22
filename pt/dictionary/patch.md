# O que é Patch?

*Desenvolvimento · Última atualização: 19 de setembro de 2026*

Patch (Türkçe karşılığıyla yama), bir yazılımdaki hataları düzeltmek, güvenlik açıklarını kapatmak veya mevcut işlevleri geliştirmek amacıyla yayınlanan kod ve dosya güncellemesidir.

Um patch é uma atualização de código e arquivos lançada com o objetivo de corrigir erros em um software, fechar vulnerabilidades de segurança ou aprimorar funcionalidades existentes.

## 1. Patch no Mundo do Software e dos Jogos

Tradicionalmente, quando ocorre um erro em um programa, baixar e instalar todo o software do zero é ineficiente em termos de largura de banda e tempo. Um patch aplica ao sistema de destino apenas os bytes ou arquivos que foram alterados.

- Patches de Segurança: Distribuídos em caráter de urgência para corrigir vulnerabilidades críticas de segurança (CVE) e falhas de dia zero (zero-day).
- Correções de Erros (Bug Fixes): Resolve erros lógicos que comprometem a estabilidade ou causam travamentos inesperados.
- Patches e Balanceamentos de Jogos: São atualizações em jogos multijogador online que equilibram as habilidades dos personagens, adicionam novos conteúdos e otimizam o desempenho. Geralmente são apresentados com "Notas de Atualização" (Patch Notes) detalhadas.
- Hotfix: Correção de escopo restrito publicada com urgência para apagar um incêndio no ambiente de produção sem aguardar o ciclo de testes.

***Analogia:** É como costurar um pedaço de tecido adequado sobre um pequeno rasgo em sua roupa, em vez de jogar a peça inteira no lixo. Ele substitui apenas as partes defeituosas sem precisar baixar todo o software novamente.*

## 2. Patch em Ferramentas de Desenvolvimento: UNIX patch e Git

No mundo do código aberto e nos sistemas de controle de versão, um patch é um documento de texto simples que representa a diferença (diff) entre dois arquivos ou commits.

### O Comando UNIX patch e seu Histórico

Baseado na metáfora de cobrir furos em cartões perfurados com fita ou reparar tiras de papel, o termo "patch" foi padronizado em 1985 pelo comando patch, escrito por Larry Wall. O patch gerado com o comando diff -u antigo.c novo.c > correcao.patch pode ser aplicado diretamente ao código-fonte no outro lado com patch \< correcao.patch.

### Uso de Patch no Ambiente Git

O Git oferece ferramentas avançadas para transportar patches via listas de e-mail ou canais offline:

- git format-patch: Converte commits específicos em arquivos .patch compatíveis com e-mail, incluindo informações do autor, mensagem de commit e as diferenças de código.
- git apply: Aplica um arquivo de patch diretamente no diretório de trabalho sem criar um commit.
- git am: Lê patches em formato de e-mail e cria commits automaticamente com as informações originais de autor e data (é o padrão, especialmente no desenvolvimento do kernel Linux).

## 3. Arquitetura Web e HTTP PATCH em APIs REST

Ao atualizar dados em serviços RESTful, os métodos PUT e PATCH são frequentemente comparados:

- PUT (Substituição Completa): Reenvia o recurso completo. Campos não especificados geralmente retornam ao padrão ou são excluídos. A operação PUT é idempotente (enviar a mesma solicitação várias vezes produz o mesmo resultado).
- PATCH (Atualização Parcial - RFC 5789): Envia um corpo contendo apenas os campos que se deseja alterar. Por exemplo, para atualizar apenas o endereço de e-mail de um usuário, basta transmitir o campo correspondente em vez de enviar todo o objeto de perfil.
- JSON Patch (RFC 6902): É uma estrutura que define sequências de operações atômicas, como add, remove, replace, move, copy e test, para padronizar alterações.

## Resumo Comparativo: "Patch" em Diferentes Contextos

| Contexto | O que significa? | Objetivo Principal | Exemplo Típico |
|---|---|---|---|
| Software & Sistema Operacional | Pacote de Atualização | Correção de vulnerabilidades de segurança, estabilidade | Patch KB do Windows Update, patch de dia zero |
| Mundo dos Jogos | Atualização de Conteúdo e Balanceamento | Balanceamento de jogabilidade, desempenho, mudança de meta | Patch de temporada (Patch 14.2), atualização de balanceamento |
| Git & Controle de Versão | Arquivo de Alteração Baseado em Linhas | Compartilhamento de código, revisão de código, contribuição | git format-patch HEAD~1, linux-kernel.patch |
| Web API / HTTP | Método de Atualização Parcial | Economia de rede, alteração parcial no recurso | PATCH /api/users/42 corpo: {"status": "ativo"} |

## Perguntas e respostas

**O que significa "patch" e qual é a sua tradução para o português?**

A tradução para o português é "correção" ou "pacote de correção". Refere-se a trechos de código que reparam ou atualizam uma parte específica de um sistema ou software sem alterar o todo.

**Qual é a diferença entre Hotfix e Patch?**

O patch é geralmente lançado com versões planejadas (por exemplo, boletins de segurança mensais) após testes abrangentes. O hotfix, por outro lado, é um patch de intervenção rápida e não planejado, preparado para interromper imediatamente uma falha crítica ou vulnerabilidade de segurança que surge no ambiente de produção.

**Qual é a principal diferença entre HTTP PUT e HTTP PATCH?**

O PUT visa a substituição total do recurso (replace) e produz o mesmo resultado se a mesma solicitação for repetida (idempotente). O PATCH, por sua vez, altera apenas os campos especificados do recurso parcialmente (partial update) e não precisa ser necessariamente idempotente em todos os cenários.

**Por que arquivos de patch ainda são usados quando existe o PR (Pull Request) no ambiente Git?**

O kernel do Linux, o próprio processo de desenvolvimento do Git e projetos de código aberto estabelecidos, como o Postgres, mantêm o fluxo de trabalho de patches baseado em e-mail para não depender de plataformas web centralizadas (como o GitHub, etc.).

**O que é a Patch Tuesday?**

É o nome dado ao calendário setorial em que a Microsoft distribui regularmente patches de segurança cumulativos para o Windows e seus produtos corporativos na segunda terça-feira de cada mês.

## Termos relacionados

- [Vulnerability Scanning](https://trescout.com/pt/dictionary/vulnerability-scanning/)
- [Security Scanner](https://trescout.com/pt/dictionary/security-scanner/)
- [Deployment](https://trescout.com/pt/dictionary/deployment/)
- [Git Push](https://trescout.com/pt/dictionary/git-push/)

## Ferramentas relacionadas

- [PLFM RADAR](https://trescout.com/pt/discover/plfm-radar/)
- [PhotoGIMP](https://trescout.com/pt/discover/photogimp/)

Esta explicação foi escrita em linguagem simples para a TreScout com IA e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/patch/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/patch/
