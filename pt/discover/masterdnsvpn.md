# Ignore bloqueios de censura com tunelamento DNS

MasterDnsVPN é uma solução de rede privada virtual (VPN) de túnel de sistema de nomes de domínio de baixa carga (túnel DNS) desenvolvida para contornar barreiras de censura. Escrita na linguagem Go, a ferramenta oferece alta estabilidade de perda de pacotes e recursos de balanceamento de carga do resolvedor na transmissão de dados.

- ★ 6.870
- Go
- GitHub Trending · 2026-06-11

## O que você ganha
- Ele fornece transmissão de dados em redes censuradas através do método de tunelamento DNS.
- Oferece multipathing e balanceamento de carga para baixa perda de pacotes e alta velocidade.
- Otimizado para conexão estável mesmo sob condições de rede restritas.

## Instalação
**Configuração automática de servidor**

```
bash <(curl -Ls https://raw.githubusercontent.com/masterking32/MasterDnsVPN/main/server_linux_install.sh)
```

**Executando com Docker**

```
docker run -d \
  --name masterdnsvpn \
  --restart unless-stopped \
  -e DOMAIN=v.example.com \
  -v $(pwd)/data:/data \
  -p 53:53/tcp \
  -p 53:53/udp \
  ghcr.io/masterking32/masterdnsvpn:latest
```


## Se você não programa
Quero estabelecer uma conexão segura via túnel DNS em uma rede censurada usando a ferramenta MasterDnsVPN. Como posso configurar o lado do servidor usando o script de instalação automática compartilhado e quais etapas básicas devo seguir para garantir a conexão no lado do cliente? Detalhe os requisitos de rede aos quais devo prestar atenção durante o processo de instalação e o método de execução via Docker.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/masterdnsvpn/
