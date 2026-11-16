# Fluxos de trabalho gerenciáveis para seus agentes de codificação

Desenvolvido pela Tencent, o LoopForge é uma ferramenta de fluxo de trabalho auto-hospedada usada para gerenciar processos de entrega de agentes de codificação. Ele suporta processos locais de assistentes de codificação orquestrando softwares como CodeBuddy, Codex e Claude Code com scripts e mecanismos de aprovação humana.

- ★ 2.090
- Go
- GitHub Trending · 2026-11-15

## Atualizações

- **16 de novembro de 2026:** Estrelas 986 → 2,090, versão mais recente v0.3.8 (12 de novembro de 2026).
- **15 de novembro de 2026:** Estrelas 983 → 986, versão mais recente v0.3.8 (12 de novembro de 2026).

## O que você ganha

- Executa ferramentas de codificação de IA com segurança em áreas de trabalho isoladas.
- Garante entregas reproduzíveis com processos padronizados e etapas de aprovação humana.
- Atribui tarefas a funções a partir da interface de bate-papo ou executa fluxos de trabalho passo a passo.

## Instalação

**Clonar o repositório e iniciar o sistema**

```
git clone https://github.com/Tencent/LoopForge.git
cd LoopForge
./start.sh
```

**Iniciar com uma fonte de imagem alternativa**

```
MIRROR=ghcr.nju.edu.cn ./start.sh
```

## Execução

**Configurar o assistente de codificação dentro do projeto**

```
# Run inside your target project, e.g. for Claude Code
npx -y loopforge-cli@latest install claude
```

## Se você não programa

Cole isto no seu agente (Claude Code · Codex · Antigravity)

Para gerenciar os processos de entrega de agentes de codificação no meu próprio servidor, quero configurar o sistema LoopForge. Primeiro, clone o repositório e inicie o sistema executando a sequência de comandos `git clone https://github.com/Tencent/LoopForge.git
cd LoopForge
./start.sh`. Se ocorrer algum travamento durante a fase de download, use o comando `MIRROR=ghcr.nju.edu.cn ./start.sh` para puxar as imagens do servidor alternativo e concluir a inicialização. Para configurar o assistente de codificação dentro do seu projeto de destino, execute o comando `# Run inside your target project, e.g. for Claude Code
npx -y loopforge-cli@latest install claude`.

Repositório: https://github.com/Tencent/LoopForge. Baseie-se nas instruções oficiais no arquivo README deste repositório para a instalação e execução.

Antes de começar, verifique em qual sistema operacional estamos e se as ferramentas necessárias (ex: Python, Node.js, Git, Docker) estão instaladas. Instale as que faltarem passo a passo de acordo com este sistema.

Crie uma pasta nova e vazia para trabalhar. Não toque em arquivos fora desta pasta e não exclua nada. Antes de executar cada comando, diga o que você vai fazer em uma frase.

Diga-me o que devo ver na tela ao final de cada etapa. Se ocorrer um erro, colarei a mensagem de erro para você exatamente como ela é, e vamos corrigi-la juntos.

## Termos relacionados do glossário

- [Self-hosted](https://trescout.com/pt/dictionary/self-hosted/)
- [Clone](https://trescout.com/pt/dictionary/clone/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** É adequado para equipes que desejam gerenciar agentes de codificação impulsionados por inteligência artificial em sua própria infraestrutura, com aprovação humana e fluxos de trabalho padrão.

## Links

- [Repositório no GitHub →](https://github.com/Tencent/LoopForge)
- [Ler em turco →](https://trescout.com/discover/loopforge/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-11-15: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. O texto de apresentação foi preparado com IA a partir da própria documentação do repositório e esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/loopforge/
