# E-mail temporário gratuito na Cloudflare

O Cloudflare Temp Email é uma plataforma de código aberto para criar um serviço de e-mail temporário (descartável) totalmente gratuito, serverless e com seu próprio domínio usando Cloudflare Workers, Pages e D1/KV. Ele protege a privacidade com gerenciamento de caixa de entrada, suporte a anexos, bot do Telegram e limpeza automática.

- ★ 11.734
- TypeScript
- GitHub Trending · 2026-07-23

## Atualizações
- 13 de setembro de 2026: Estrelas 11.391 → 11.734, versão mais recente v1.12.0 (13 de setembro de 2026).
- 23 de agosto de 2026: Estrelas 11.332 → 11.391, versão mais recente v1.11.1 (22 de agosto de 2026).
- 19 de agosto de 2026: Estrelas 11.156 → 11.332, versão mais recente v1.11.0 (19 de agosto de 2026).
- 2 de agosto de 2026: Estrelas 10.884 → 11.156, versão mais recente v1.10.0 (31 de julho de 2026).

## O que você ganha
- Custo zero de servidor e operação: Executa no generoso plano gratuito da Cloudflare (100.000 requisições Workers/dia, Email Routing e Pages gratuitos) sem alugar servidores externos.
- Domínio personalizado e endereços não bloqueáveis: Gera endereços descartáveis usando seu próprio domínio, contornando listas de bloqueio aplicadas a serviços públicos de e-mail temporário.
- Análise rápida de e-mails com Rust e WASM: Processa e-mails complexos (MIME, multipart, HTML) em milissegundos através de um módulo WebAssembly compilado em Rust.
- Bot no Telegram e notificações instantâneas: Receba avisos de novos e-mails diretamente no Telegram, leia conteúdos ou crie novos endereços com comandos práticos.
- Limpeza automática e acesso seguro: Remove automaticamente mensagens e anexos expirados após o período configurado e restringe a administração com senha.

## Como começar e opções de implantação

A implantação requer apenas uma conta na Cloudflare e um domínio gerenciado no Cloudflare DNS. Você pode implantar com um clique pelo Cloudflare Pages vinculando o repositório do GitHub ou configurar o banco D1 e os Workers localmente através do Wrangler CLI.
- [Guia oficial de instalação →](https://temp-mail-docs.awsl.uk)
- [Interface de demonstração ao vivo →](https://mail.awsl.uk)

## Arquitetura técnica e funcionamento interno

O Cloudflare Temp Email elimina a sobrecarga de gerenciar servidores SMTP legados (Postfix, Dovecot) adotando uma arquitetura serverless moderna:
- Roteamento de e-mails da Cloudflare (Email Routing): O tráfego MX de entrada é recebido pela infraestrutura da Cloudflare e encaminhado para o Worker receptor (catch-all).
- Edge Worker e analisador Rust WASM: O fluxo bruto de e-mail é processado pelo módulo Rust WASM otimizado para extrair cabeçalhos, corpo, HTML e anexos.
- Armazenamento Cloudflare D1 e R2: Textos e metadados são salvos no banco SQLite de borda Cloudflare D1, enquanto anexos podem ser transferidos para o Cloudflare R2.
- Aplicação de página única (SPA) moderna: A interface web é servida com latência quase nula pela rede CDN global do Cloudflare Pages.
- API REST e integrações externas: Endpoints programáveis permitem que testes automatizados ou pipelines de CI/CD gerem e-mails descartáveis e capturem códigos de verificação.

## Instalação e exemplo de implantação

```bash
# 1. Clonar o repositorio e instalar dependencias
git clone https://github.com/dreamhunter2333/cloudflare_temp_email.git
cd cloudflare_temp_email
pnpm install

# 2. Criar banco de dados Cloudflare D1
npx wrangler d1 create temp_email_db

# 3. Executar o schema e implantar
npx wrangler d1 execute temp_email_db --file=./db/schema.sql
pnpm run deploy
```

## Se você não programa
🤖 Cole no seu agente de IA (Claude Code · Codex · Antigravity) 
Quero implantar o projeto de código aberto dreamhunter2333/cloudflare_temp_email na Cloudflare usando meu próprio domínio. Possuo uma conta na Cloudflare e um domínio configurado no Cloudflare DNS. Você pode me explicar passo a passo como configurar as regras de encaminhamento do Email Routing (catch-all), criar o banco D1 e publicar a interface no Cloudflare Pages? Além disso, quais variáveis de ambiente devo preencher para ativar as notificações no meu bot do Telegram?

- **Para quem:** Desenvolvedores, engenheiros de QA e usuários focados em privacidade que desejam hospedar gratuitamente um serviço de e-mail descartável com domínio próprio. 
- **Licença:** MIT (Código aberto) 
- **Infraestrutura:** Cloudflare Workers, Pages, D1 (SQLite) e Email Routing 
- **Linguagens e Ferramentas:** TypeScript, Rust (WASM), Vue 3, Wrangler 

## Perguntas frequentes
- O plano gratuito da Cloudflare é suficiente para uso pessoal? Sim. O plano gratuito oferece 100.000 requisições Workers por dia, além de cotas gratuitas para Email Routing e banco D1. Para uso individual ou pequenas equipes, ultrapassar esses limites é quase impossível; o serviço roda com custo zero.
- É obrigatório possuir um domínio personalizado? Sim. Para receber mensagens, você precisa de um domínio ou subdomínio gerenciado no Cloudflare DNS. Isso também garante que seus e-mails não sejam rejeitados por plataformas da web.
- Os e-mails recebidos ficam salvos para sempre? Não, este é um serviço descartável. O administrador pode definir um tempo de retenção (como 1 hora, 24 horas ou 7 dias); itens expirados são apagados automaticamente do armazenamento.
- É possível enviar respostas externas pelo serviço? Sim. Embora o Cloudflare Email Routing gerencie apenas a entrada, o projeto suporta o envio e respostas de e-mails quando integrado com APIs como Resend, Brevo ou um servidor SMTP externo.

## Links
- [Repositório no GitHub →](https://github.com/dreamhunter2333/cloudflare_temp_email)
- [Ler em turco →](https://trescout.com/discover/cloudflare-temp-email/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e resumimos em português. Esta página descreve o repositório em 2026-07-23.

## Termos relacionados do glossário
Self-Hosted Cloud Computing Digital Privacy Open Source API Rust

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/cloudflare-temp-email/
