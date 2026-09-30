# Gerencie automaticamente seu arquivo de séries

Sonarr é um gravador de vídeo pessoal inteligente (PVR) de código aberto e gerenciador de automação de mídia desenvolvido para usuários Usenet (grupos de notícias) e BitTorrent. Plataforma desenvolvida com infraestrutura C# e .NET; acompanha episódios recém-lançados, comunica-se com clientes de download, renomeia e transfere arquivos para bibliotecas Plex e Jellyfin regularmente.

- ★ 16.274
- C#
- GitHub Trending · 2026-09-12

## O que você ganha
- Rastreamento e calendário automático de episódios: acompanhe as datas de transmissão de suas séries favoritas por meio do calendário integrado e baixe automaticamente novos episódios assim que forem lançados.
- Atualizações de qualidade inteligentes: substitua automaticamente seções de resolução mais baixa (HDTV 720p) por versões de qualidade superior (1080p / 4K HDR WEB-DL) ao longo do tempo.
- Suporte a hardlinking: Manter os arquivos baixados no compartilhamento torrent e apresentá-los ao servidor de mídia no mesmo disco sem duplicá-los.
- Ampla integração de cliente e indexador: trabalho sem atrito com qBittorrent, Transmission, Deluge, SABnzbd e NZBGet.
- Nomeação de arquivos personalizável: Nomeação e pasta automática de arquivos de episódios de acordo com os padrões dos servidores de mídia (Plex, Jellyfin, Emby).

## Opções de instalação: Docker e serviço local
**Instalação com Docker Compose**

```
services:
  sonarr:
    image: lscr.io/linuxserver/sonarr:latest
    container_name: sonarr
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/Istanbul
    volumes:
      - /opt/sonarr/data:/config
      - /mnt/storage/media/tv:/tv
      - /mnt/storage/downloads:/downloads
    ports:
      - 8989:8989
    restart: unless-stopped
```


## Operação e configuração básica
**Iniciando o contêiner**

```
docker compose up -d
```

**Acesso à interface web**

```
http://localhost:8989
```


## Arquitetura técnica e princípio de funcionamento
- Ponte de protocolo Torznab e Newznab: comunica-se com indexadores (via Jackett ou Prowlarr) por meio da API XML/JSON padrão por meio de feeds RSS e consultas de pesquisa.
- Movimentação atômica de arquivos e Hardlink: Reduz a carga de gravação em disco e o desperdício de armazenamento a zero montando o inode do sistema de arquivos em vez de copiar o arquivo quando o download for concluído.
- Mecanismo de pontuação de formatos personalizados: seleciona a melhor versão pontuando codecs de áudio preferidos (Atmos, DTS-HD), formatos de vídeo (AV1, HEVC) e grupos de editores.

## Integração do ecossistema de mídia (Plex, Jellyfin, Prowlarr)
- Sincronização do indexador com Prowlarr: importe automaticamente rastreadores de torrent e indexadores Usenet para o Sonarr a partir de um único centro.
- Gerenciamento de download com qBittorrent / SABnzbd: controle a velocidade de download e a taxa de compartilhamento por meio de categorias designadas.
- Notificação da biblioteca Plex ou Jellyfin: Envie uma notificação instantânea ao servidor de mídia quando um novo episódio for gravado no disco e verifique a biblioteca.

## Se você não programa
Quero executar os serviços Sonarr, qBittorrent, Prowlarr e Jellyfin juntos no Docker em meu servidor doméstico. Você pode explicar passo a passo o arquivo docker-compose.yml completo contendo uma estrutura de montagem de volume único e as primeiras configurações que preciso fazer no painel da web do Sonarr para que os hardlinks funcionem sem problemas?

## Perguntas frequentes
- O Sonarr baixa o arquivo diretamente? Não. Sonarr não é um cliente de download; é um gerente. Ele pesquisa, envia o arquivo torrent/NZB para clientes como qBittorrent ou SABnzbd e move o arquivo baixado para a pasta de arquivo.
- O que é hardlink e ele preenche o disco duas vezes mais? Não. Hardlinking é colocar um segundo ponteiro de caminho para os dados físicos do arquivo no disco. Ele aparece nas pastas de downloads e tv, mas ocupa tanto espaço no disco quanto um único arquivo.
- Qual é a diferença entre Sonarr e Radarr? Enquanto Sonarr dirige séries de televisão, temporadas e episódios; Radarr oferece a mesma arquitetura para longas-metragens.
- É necessário usar uma VPN? Como o Sonarr faz apenas consultas RSS e metadados, geralmente não requer VPN; entretanto, é recomendado que o cliente de download de torrent (qBittorrent) seja executado atrás de um túnel VPN.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/sonarr/
