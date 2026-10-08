# O que é Git Push?

*Glossário · Dev · Última atualização: 19 de setembro de 2026*

O Git Push é o comando essencial do Git que transfere blocos de código com commit, o histórico de commits e objetos do seu ambiente de desenvolvimento local para um servidor Git remoto, atualizando o branch remoto.

## 1. Definição e o modelo de dados de 4 camadas do Git

O Git é um sistema de controle de versão distribuído (DVCS). Nesta arquitetura, as alterações de código passam por 4 áreas de trabalho diferentes até chegarem a um servidor remoto:

```
[Çalışma Dizini] ──git add──> [Staging / Index] ──git commit──> [Yerel Depo] ──git push──> [Uzak Depo]
(Working Directory)            (Hazırlık Alanı)                 (.git veritabanı)            (GitHub/GitLab)
```

1. Diretório de Trabalho (Working Directory): A área de código ativa onde você edita os arquivos.
2. Staging Area / Index (Área de Preparação / Índice): as alterações que você selecionou com o comando git add para serem incluídas no próximo commit.
3. Repositório Local (Yerel Depo): pontos de verificação selados permanentemente no diretório .git do seu próprio disco com o git commit.
4. Remote Repository (Repositório Remoto): o servidor centralizado que, por meio do comando git push, pode ser visto pelos membros da sua equipe e aciona os pipelines de CI/CD.

Quando se executa git push, não são enviados apenas os diffs de texto; os objetos Commit, Tree e Blob do banco de objetos do Git são transferidos para o servidor remoto em um arquivo de pacote compactado (packfile) e a referência da branch remota é avançada.

***Analogia:** É como salvar os capítulos de um livro que você escreveu no seu computador em sua pasta de rascunhos local e, em seguida, entregá-los por mensageiro ao centro de impressão compartilhado da gráfica dizendo: "carregue estes capítulos para o arquivo oficial e coloque-os na fila de impressão".*

## 2. Modelos de comandos mais utilizados (Cheatsheet)

```
git push -u origin feature/auth
```

O sinalizador -u ou --set-upstream vincula permanentemente sua ramificação local à ramificação remota. Após esse mapeamento, basta digitar apenas git push ou git pull quando estiver na mesma ramificação.

```
git push --force-with-lease
```

Quando o push padrão é rejeitado após git commit --amend ou git rebase, usar git push -f pode apagar os commits dos seus colegas de equipe no servidor. Já o --force-with-lease é uma trava de segurança que só permite a sobrescrita se mais ninguém tiver enviado commits para essa ramificação depois de você.

```
git push origin --delete eski-ozellik-dali
git push origin --tags
```

## 3. Erros mais comuns do Git Push e suas soluções

- fatal: [rejeitado - non-fast-forward]: Há commits no branch remoto que ainda não estão no seu repositório local. Para resolver, execute git pull --rebase origin \<branch> e depois git push.
- fatal: The current branch has no upstream branch: O ramo atual não tem um ramo upstream. Solução: git push -u origin HEAD.
- remote rejected: pre-receive hook declined: Bloqueado por regra de branch protegida ou falta de permissão; em vez de push direto, deve ser aberto um Pull Request (PR).

## Perguntas frequentes

**O que significa Git push e para que serve?**

O Git Push é o comando essencial que sincroniza os repositórios remotos com o estado local, carregando os commits concluídos no seu computador local para servidores remotos como GitHub, GitLab ou Bitbucket.

**O que significa o -u no comando git push -u origin main?**

A flag -u (--set-upstream) estabelece uma conexão de rastreamento (tracking) entre a branch local e a branch remota. Assim, nas próximas vezes, você pode simplesmente digitar git push sem especificar o destino.

**Por que --force-with-lease deve ser usado em vez de git push -f?**

O git push -f exclui permanentemente as alterações feitas por outras pessoas no repositório remoto sem verificar. Já o --force-with-lease protege o código dos colegas de equipe, permitindo a sobrescrita apenas se a branch estiver no estado que você puxou por último.

**Como o erro non-fast-forward é resolvido?**

Ele ocorre porque os novos commits no repositório remoto ainda não estão no seu ambiente local. Para resolver, os commits devem ser atualizados executando git pull --rebase origin \<branch> e, em seguida, o git push deve ser feito novamente.

## Termos relacionados

- [CLI](https://trescout.com/pt/dictionary/cli/)
- [Deployment](https://trescout.com/pt/dictionary/deployment/)
- [Production Pipeline](https://trescout.com/pt/dictionary/production-pipeline/)
- [Patch](https://trescout.com/pt/dictionary/patch/)
- [Tech Stack](https://trescout.com/pt/dictionary/tech-stack/)

## Ferramentas relacionadas

- [No Mistakes](https://trescout.com/pt/discover/no-mistakes/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/git-push/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/git-push/
