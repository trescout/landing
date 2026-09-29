# E-mail temporário gratuito na Cloudflare

Cloudflare Temp Email é uma plataforma de código aberto que permite configurar um serviço de e-mail temporário (disposable email) totalmente gratuito, sem servidor (serverless) e que funciona com seu próprio domínio, utilizando a infraestrutura do Cloudflare Workers, Pages e banco de dados D1/KV. Protege sua privacidade pessoal com gerenciamento de caixa de entrada, armazenamento de anexos, integração com bot do Telegram e mecanismos de limpeza automática.

- ★ 11.734
- TypeScript
- GitHub Trending · 2026-07-23

## O que você ganha
- Custo zero de servidor e operação: funciona sem a necessidade de alugar um servidor externo, aproveitando o generoso plano gratuito da Cloudflare (100.000 solicitações de Workers por dia, Email Routing gratuito e hospedagem de Pages).
- Nome de domínio personalizado e endereços impossíveis de bloquear: ao contrário dos serviços de e-mail temporário genéricos, gera endereços descartáveis com seu próprio domínio que não são bloqueados pelas listas negras dos sites.
- Análise rápida de e-mail com Rust e WASM: Processa e-mails complexos com conteúdo MIME, multipart e HTML em milissegundos graças a um módulo WebAssembly compilado com Rust.
- Bot do Telegram e notificações instantâneas: receba notificações diretamente pelo Telegram quando um novo e-mail chegar, leia o conteúdo da mensagem ou crie novos endereços instantaneamente com comandos do bot.
- Limpeza automática e acesso seguro: limpa automaticamente mensagens e anexos antigos após um período definido; impede o acesso não autorizado com uma senha de administrador.

## Como começar e opções de instalação
- Guia oficial de instalação →
- Interface de demonstração ao vivo →

## Arquitetura técnica e princípio de funcionamento
- Integração do Cloudflare Email Routing: Todo o tráfego MX destinado ao seu domínio é recebido na infraestrutura da Cloudflare e, por meio de uma regra catch-all, direcionado diretamente para a função Worker de captura.
- Edge Worker e analisador Rust WASM: O fluxo de e-mail recebido (raw stream) é transferido para um motor Rust WASM otimizado que roda dentro do Worker, permitindo a análise rápida de cabeçalhos, corpo, HTML e anexos.
- Armazenamento Cloudflare D1 e R2: Os textos e metadados de e-mail são armazenados no Cloudflare D1, um banco de dados SQLite de borda. Os anexos de arquivos são gravados opcionalmente no armazenamento de objetos Cloudflare R2.
- Aplicativo de página única (SPA) moderno: interface web amigável servida com latência zero através da rede CDN global do Cloudflare Pages.
- API REST e integrações externas: Oferece a possibilidade de derivar novos endereços de e-mail e consultar a caixa de entrada por meio de endpoints de API REST para testes automatizados ou softwares de terceiros.

## Instalação e implantação de exemplo
**Passos de Implantação com Wrangler CLI**

```
# 1. Depoyu klonlayin ve bagimliliklari kurun
git clone https://github.com/dreamhunter2333/cloudflare_temp_email.git
cd cloudflare_temp_email
pnpm install

# 2. Cloudflare D1 veritabanini olusturun
npx wrangler d1 create temp_email_db

# 3. Veritabani semasini calistirin ve yayinlayin
npx wrangler d1 execute temp_email_db --file=./db/schema.sql
pnpm run deploy
```


## Se você não programa
Quero configurar o projeto de e-mail temporário de código aberto dreamhunter2333/cloudflare_temp_email, que roda no Cloudflare, com meu próprio domínio. Tenho uma conta Cloudflare e um domínio conectado ao Cloudflare DNS. Você poderia explicar passo a passo como configurar o roteamento de e-mail (Email Routing), o banco de dados D1 e a interface do Cloudflare Pages a partir do zero através do painel do Cloudflare? Além disso, quais etapas de configuração devo seguir para encaminhar os e-mails recebidos para o meu bot do Telegram?

## Perguntas frequentes
- O plano gratuito da Cloudflare é suficiente para uso pessoal? Sim. O plano gratuito da Cloudflare oferece 100.000 solicitações de Worker por dia, além de Email Routing gratuito e uma cota para o banco de dados D1. Para uso pessoal e pequenas equipes, é quase impossível exceder esses limites; o sistema funciona com custo zero.
- É obrigatório ter um domínio personalizado (custom domain) para usar o serviço? Sim. Para receber e-mails, você precisa ter um domínio (ou subdomínio, por exemplo: mail.seudominio.com) gerenciado no Cloudflare DNS. Dessa forma, você pode contornar facilmente sites que bloqueiam serviços de e-mail temporário genéricos.
- Os e-mails recebidos são armazenados permanentemente? Não, este é um serviço de e-mail temporário. Como administrador do sistema, você pode definir o tempo de retenção dos e-mails pelo painel (por exemplo, 1 hora, 24 horas ou 7 dias); os registros que expirarem serão excluídos automaticamente do armazenamento D1 e R2.
- É possível enviar respostas de e-mail para o exterior através do serviço? Sim. Embora o Cloudflare Email Routing suporte apenas o recebimento de e-mails, quando o projeto é conectado a uma API do Resend, Brevo ou a um servidor SMTP personalizado, ele também passa a suportar operações de envio e resposta de e-mails para o mundo exterior a partir do painel web.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/cloudflare-temp-email/
