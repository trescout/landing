# Automatize seu acervo de séries e streaming doméstico

O Sonarr é um gravador de vídeo pessoal (PVR) e gerenciador de automação de mídia de código aberto desenvolvido para usuários de Usenet e BitTorrent. Criado em C# e .NET, ele acompanha novos episódios, envia comandos aos clientes de download e organiza arquivos automaticamente para o Plex e Jellyfin.

- ★ 16.274
- C#
- GitHub Trending · 2026-09-12

## Atualizações
- 17 de setembro de 2026: Estrelas 16.274, versão estável v4.0.20.3014 (otimizações no runtime do .NET 8 e melhorias na pontuação de Custom Formats).

## O que você ganha
- Rastreamento automático e calendário de episódios: Acompanha datas de exibição em um calendário integrado e baixa episódios assim que são lançados.
- Atualizações inteligentes de qualidade: Substitui automaticamente arquivos de qualidade inicial por versões superiores (1080p / 4K HDR) com o passar do tempo.
- Suporte a links rígidos (Hardlinks): Mantém o seeding em torrents sem duplicar o espaço ocupado no disco rígido.
- Compatibilidade com clientes e indexadores: Integração perfeita com qBittorrent, Transmission, Deluge, SABnzbd e NZBGet.
- Organização e renomeação padronizada: Padroniza nomes de episódios e pastas de temporadas conforme as exigências do Plex, Jellyfin e Emby.

## Opções de instalação: Docker e serviço local

**Configuração com Docker Compose**

```yaml
services:
  sonarr:
    image: lscr.io/linuxserver/sonarr:latest
    container_name: sonarr
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=America/Sao_Paulo
    volumes:
      - /opt/sonarr/data:/config
      - /mnt/storage/media/tv:/tv
      - /mnt/storage/downloads:/downloads
    ports:
      - 8989:8989
    restart: unless-stopped
```

## Execução e configuração inicial

**Iniciar o contêiner**

```
docker compose up -d
```

**Acessar interface web**

```
http://localhost:8989
```

## Arquitetura técnica e princípio de funcionamento

O Sonarr opera como a central de automação de um ecossistema de mídia auto-hospedado:
- Ponte de protocolos Torznab e Newznab: Conecta-se a indexadores por meio do Prowlarr ou Jackett utilizando endpoints REST em XML e JSON.
- Operações atômicas de arquivo e Hardlinks: Vincula os inodes do sistema de arquivos sem duplicar arquivos pesados de vídeo, poupando a vida útil do disco.
- Motor de pontuação de formatos customizados: Atribui pontos a codecs de áudio (Atmos, DTS), codecs de vídeo (HEVC, AV1) e grupos de release para escolher a melhor versão.

## Integração com ecossistema de mídia (Plex, Jellyfin, Prowlarr)

Para um servidor doméstico completo, o Sonarr se integra perfeitamente a outras ferramentas:
- Sincronização de indexadores com Prowlarr: Centralize o cadastro de rastreadores e envie tudo automaticamente para o Sonarr.
- Controle de download com qBittorrent / SABnzbd: Defina limites de taxa de upload e categorias específicas para cada série.
- Aviso instantâneo aos servidores de mídia: Dispara varredura automática no Plex ou Jellyfin no segundo em que o arquivo é importado.

## Se você não programa
🤖 Se você não programa
Quero configurar o Sonarr, qBittorrent, Prowlarr e Jellyfin no Docker. Você pode me fornecer um arquivo docker-compose.yml completo com os pontos de montagem configurados para que os hardlinks funcionem sem gastar o dobro de espaço no disco, além de me explicar os primeiros passos no painel do Sonarr?

- **Para quem:** Usuários de homelab, colecionadores de mídia e quem quer automatizar o catálogo de séries sem trabalho manual.
- **Licença:** GPL-3.0 (Licença de código aberto)
- **Tecnologia:** Aplicação web desenvolvida em C# e .NET
- **Porta Web:** Padrão 8989

## Perguntas frequentes
- O Sonarr baixa os episódios diretamente? Não. O Sonarr não é um cliente de download; ele é o cérebro que localiza os arquivos, passa as tarefas para o qBittorrent ou SABnzbd e organiza os arquivos concluídos na sua biblioteca.
- O que é hardlink e ele consome o dobro de espaço? Não. Um hardlink é apenas um segundo atalho que aponta para os mesmos blocos físicos no disco. Ele aparece nas duas pastas gastando exatamente o espaço de um único arquivo.
- Qual a diferença entre Sonarr e Radarr? O Sonarr é especializado em séries de televisão e temporadas, enquanto o Radarr utiliza os mesmos padrões para gerenciar filmes.
- É obrigatório rodar o Sonarr com VPN? O Sonarr apenas faz consultas de metadados e não exige VPN. No entanto, é altamente recomendável passar o cliente de torrent (qBittorrent) por um túnel VPN.

## Links
- [GitHub →](https://github.com/Sonarr/Sonarr)

## Termos relacionados do glossário
Self-Hosted Offline Open Source Local

---
Source: TreScout Discover · https://trescout.com/pt/discover/sonarr/
