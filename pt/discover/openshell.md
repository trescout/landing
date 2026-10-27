# Ambiente seguro para agentes de inteligência artificial

Desenvolvido pela NVIDIA, o OpenShell oferece um ambiente de tempo de execução seguro e focado em privacidade para agentes autônomos de inteligência artificial. Escrita em Rust, esta infraestrutura visa criar uma área de execução segura ao isolar o acesso dos agentes aos recursos do sistema.

- ★ 20.243
- Rust
- GitHub Trending · 2026-09-29

## Atualizações

- **27 de outubro de 2026:** Estrelas 19,581 → 20,243, versão mais recente v0.1.6 (27 de outubro de 2026).
- **25 de outubro de 2026:** Estrelas 18,169 → 19,581, versão mais recente v0.1.5 (20 de outubro de 2026).
- **23 de outubro de 2026:** Estrelas 16,850 → 18,169, versão mais recente v0.1.5 (20 de outubro de 2026).
- **21 de outubro de 2026:** Estrelas 16,170 → 16,850, versão mais recente v0.1.5 (20 de outubro de 2026).

## O que você ganha

- Executa agentes de IA em um ambiente isolado (sandbox)
- Limita o acesso a arquivos e rede com regras
- Aumenta a segurança ocultando credenciais

## Instalação

**Instalar a ferramenta e criar ambiente de demonstração**

```
curl -LsSf https://raw.githubusercontent.com/NVIDIA/OpenShell/main/install.sh | sh
openshell sandbox create --name demo
```

## Execução

**Adicionar recursos**

```
npx skills add NVIDIA/OpenShell
```

## Se você não programa

Cole isto no seu agente (Claude Code · Codex · Antigravity)

Para instalar e testar a ferramenta OpenShell, você pode usar os seguintes comandos: curl -LsSf https://raw.githubusercontent.com/NVIDIA/OpenShell/main/install.sh | sh e, em seguida, executar o comando openshell sandbox create --name demo para criar um ambiente de demonstração.

Repositório: https://github.com/NVIDIA/OpenShell. Baseie-se nas instruções oficiais no arquivo README deste repositório para a instalação e execução.

Antes de começar, verifique em qual sistema operacional estamos e se as ferramentas necessárias (ex: Python, Node.js, Git, Docker) estão instaladas. Instale as que faltarem passo a passo de acordo com este sistema.

Crie uma pasta nova e vazia para trabalhar. Não toque em arquivos fora desta pasta e não exclua nada. Antes de executar cada comando, diga o que você vai fazer em uma frase.

Diga-me o que devo ver na tela ao final de cada etapa. Se ocorrer um erro, colarei a mensagem de erro para você exatamente como ela é, e vamos corrigi-la juntos.

## Termos relacionados do glossário

- [Sandbox](https://trescout.com/pt/dictionary/sandbox/)
- [Runtime](https://trescout.com/pt/dictionary/runtime/)
- [Rust](https://trescout.com/pt/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** Desenvolvedores que desejam executar agentes de inteligência artificial em um ambiente seguro e isolado, sem conceder acesso total a todos os recursos do sistema.
- **Licença:** Apache-2.0

## Links

- [Repositório no GitHub →](https://github.com/NVIDIA/OpenShell)
- [Ler em turco →](https://trescout.com/discover/openshell/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-09-29: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. O texto de apresentação foi preparado com IA a partir da própria documentação do repositório e esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/openshell/
