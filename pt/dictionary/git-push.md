# O que é Git Push?

> Inglês: Git Push · Etimologia: gíria britânica git + latim pulsare (empurrar, impulsionar)

**Categoria:** Dev  
**Última atualização:** 2026-09-19

Git Push é o comando central de controle de versão que transfere os commits, revisões de código e histórico salvos localmente para um repositório remoto, sincronizando as branches entre a equipe.

## Por analogia
É como redigir os capítulos de uma tese na pasta privada do seu computador e, ao terminar, enviá-los para a central da gráfica para que todos os revisores acessem a versão atualizada.

## 1. Definição e o modelo de 4 camadas do Git
O Git opera sob uma arquitetura distribuída (DVCS) com quatro áreas : o Diretório de Trabalho, a Área de Preparação (Index/Staging), o Repositório Local (.git) e o Repositório Remoto (GitHub, GitLab). O comando <code>git commit</code> cria um instantâneo no seu computador pessoal; é o <code>git push</code> que faz o envio de rede dos objetos binários para o servidor compartilhado.

## 2. Comandos mais utilizados no dia a dia
Instruções frequentes de trabalho :
- **Publicação Inicial de Branch:** <code>git push -u origin minha-branch</code> (vincula a branch local à remota).- **Push de Rotina:** <code>git push</code> (atualiza o ramo rastreado).- **Envio de Tags:** <code>git push origin --tags</code> (disponibiliza marcações de versões de release).- **Exclusão de Ramo Remoto:** <code>git push origin --delete branch-antiga</code>.- **Sobrescrita Segura:** <code>git push --force-with-lease</code> (substitui o histórico remoto apenas se ninguém enviou commits no intervalo).

## 3. Erros comuns e soluções práticas
Como destravar erros comuns de push :
- **fatal: [rejected - non-fast-forward]:** O servidor contém commits que você ainda não baixou. Solução: execute <code>git pull --rebase origin main</code>, resolva pendências e tente o push novamente.- **fatal: The current branch has no upstream branch:** Use a opção <code>-u</code> para definir o upstream remoto.- **Bloqueio por Arquivos Pesados:** Arquivos com mais de 100MB são rejeitados; adote Git LFS para mídias pesadas.

## Perguntas frequentes

**Qual a diferença entre 'git commit' e 'git push'?**  
O commit salva o pacote de modificações no seu disco local; o push transmite esses pacotes pela internet para o servidor da equipe.

**Por que '--force-with-lease' é preferível a '--force'?**  
Porque o --force comum apaga commits de colegas sem aviso; o --force-with-lease cancela a ação caso outro desenvolvedor tenha feito envios recentes.

**O que fazem os ganchos (hooks) pre-push?**  
Executam rotinas de testes e verificações de formatação no seu computador antes de permitir a transmissão pela rede.

**Posso enviar commits para dois servidores remotos simultaneamente?**  
Sim, associando mais de uma URL de envio ao mesmo repositório remoto no arquivo de configuração .git/config.

## Termos relacionados
- [CLI](/pt/dictionary/cli/)
- [Code Snippets](/pt/dictionary/code-snippets/)
- [Checkout](/pt/dictionary/checkout/)

## Ferramentas relacionadas
- [No Mistakes](/pt/discover/no-mistakes/)

---
Fonte: Dicionário Técnico TreScout · https://trescout.com/pt/dictionary/git-push/
