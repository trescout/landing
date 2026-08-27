# Backup de fotos e vídeos no seu próprio servidor

O Immich é uma solução de alto desempenho projetada para você fazer backup de suas fotos e vídeos pessoais, que pode ser hospedada diretamente no seu próprio servidor.

- ★ 109.538
- GitHub Trending · 2026-07-05

## O que esta ferramenta faz?
O Immich é uma solução de alto desempenho projetada para você fazer backup de suas fotos e vídeos pessoais, que pode ser hospedada diretamente no seu próprio servidor. Ele permite que você gerencie sua biblioteca de mídia por meio de aplicativos móveis e web.

## Para quem é?
Para aqueles que desejam armazenar e gerenciar suas fotos e vídeos em seu próprio hardware, em vez de usar serviços de nuvem de terceiros.

## O que não esperar
Usuários que não desejam gerenciar seu próprio servidor ou lidar com processos de instalação técnica.

## Destaques
- Faz backup de fotos e vídeos na qualidade original.
- Oferece acesso por meio de aplicativos web e móveis.
- Garante a privacidade dos dados ao ser hospedado em seu próprio hardware.
- Suporte multiusuário para criar espaços para membros da família ou equipes.

## Primeiro fluxo de uso
- Certifique-se de atender aos requisitos de hardware especificados na documentação oficial.
- Inicie os contêineres do Immich usando Docker e Docker Compose.
- Baixe o aplicativo móvel no seu dispositivo e conecte-se inserindo o endereço do seu servidor.
- Crie a conta de administrador inicial e inicie o processo de backup.

## Início seguro

## Primeiro prompt
Como adicionar um novo usuário na instalação do Immich?

## Instalação
**Baixe a configuração do Docker Compose**

```
mkdir immich-app && cd immich-app
wget -O docker-compose.yml https://github.com/immich-app/immich/releases/latest/download/docker-compose.yml
wget -O .env https://github.com/immich-app/immich/releases/latest/download/example.env
```


## Execução
**Iniciar serviços Docker**

```
docker compose up -d
```


## Links
- Repositório no GitHub →
- README oficial do Immich →
- Site oficial do Immich →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/immich/
