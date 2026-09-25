# Gerencie seu servidor de nuvem pessoal

O CasaOS é um sistema operacional de nuvem pessoal de código aberto, leve e elegante, feito para gerenciar aplicativos Docker com um clique em servidores caseiros, mini PCs e Raspberry Pi. Desenvolvido em Go, ele permite construir sua soberania digital sem precisar lidar com comandos complicados de terminal.

- ★ 36.953
- Go
- GitHub Trending · 2026-06-26

## Atualizações
- 2 de agosto de 2026: Estrelas 34.992 → 36.953, versão mais recente v0.4.15 (19 de dezembro de 2024).

## O que você ganha
- Loja rica de aplicativos em um clique: Instale Nextcloud, Plex, Jellyfin, AdGuard Home, qBittorrent, Home Assistant e mais de 100 serviços auto-hospedados em segundos.
- Painel web elegante e intuitivo: Acompanhe uso de CPU, RAM, armazenamento, atividade de rede e contêineres ativos por meio de cartões e widgets informativos.
- Armazenamento visual e gerenciamento de arquivos: Monte discos rígidos externos e unidades USB automaticamente e compartilhe pastas via protocolo Samba (SMB).
- Suporte a Docker Compose personalizado: Suba contêineres que não estejam na loja colando o arquivo Docker Compose diretamente na interface web.
- Núcleo leve em Go com consumo mínimo: Funciona com altíssima eficiência e quase zero sobrecarga até mesmo em Raspberry Pi 4/5 ou notebooks antigos.

## Instalação

**Comando de instalação**

```
curl -fsSL https://get.casaos.io | sudo bash
```

## Execução

**Comando de atualização**

```
curl -fsSL https://get.casaos.io/update | sudo bash
```

## Arquitetura técnica e princípio de funcionamento

Em vez de criar um novo kernel Linux, o CasaOS opera como uma camada moderna de orquestração Docker sobre a sua distribuição Debian, Ubuntu ou Raspberry Pi OS existente. Essa abordagem preserva os drivers do hardware enquanto estrutura o sistema em microsserviços modulares:
- Arquitetura de microsserviços em Go: O núcleo do CasaOS (Gateway, MessageBus, LocalStorage e UserService) roda como microsserviços Go independentes via REST e WebSockets.
- Abstração do ciclo de vida dos contêineres: Comunica-se com o Docker daemon para detectar portas ocupadas e traduzir variáveis de ambiente e volumes em formulários amigáveis.
- Ecossistema ZimaOS e IceWhale: Apoiado pela IceWhale Technology (fabricante do ZimaBoard e ZimaBlade), o sistema oferece perfeita integração com hardware de nuvem local.
- Fusão inteligente de unidades de disco: Combina discos de tamanhos variados em um único pool lógico para facilitar backups e reprodução de mídia.

## Guia passo a passo para montar seu servidor caseiro

Para transformar um computador antigo ou mini PC em uma nuvem pessoal completa, siga estes passos fundamentais:
- Instalação do Linux: Instale uma cópia limpa do Ubuntu Server ou Debian minimal no dispositivo e conecte-o ao roteador via cabo de rede.
- Instalação em linha única do CasaOS: Execute o script oficial no terminal; ele providencia e configura o Docker e todas as dependências automaticamente.
- Acesso ao painel pelo navegador: Em qualquer computador da rede, digite o IP local do servidor (por exemplo, http://192.168.1.100) e crie seu login de administrador.
- Implantação de aplicativos: Abra a App Store para instalar o Nextcloud para arquivos ou o Jellyfin para filmes e séries com apenas um clique.

## Se você não programa
🤖 Se você não programa
Instalei o CasaOS no meu servidor doméstico. Quero configurar o AdGuard Home (bloqueador de anúncios), o Jellyfin (streaming de mídia) e o Tailscale (acesso remoto seguro) para todos os dispositivos de casa. Você pode me explicar passo a passo como instalar esses serviços pela loja do CasaOS ou por Docker Compose e como compartilhar meus discos rígidos?

- **Para quem:** Usuários e entusiastas de homelab que desejam montar nuvens pessoais e gerenciar apps Docker sem complicações de terminal.
- **Licença:** Apache-2.0 (Licença permissiva de código aberto)
- **Desenvolvedor:** IceWhale Technology e Comunidade Open Source
- **Sistemas Suportados:** Ubuntu, Debian, Raspberry Pi OS, Armbian (x86_64, aarch64, armv7)

## Perguntas frequentes
- O CasaOS apaga o meu Linux ou os arquivos do computador? Não. O CasaOS não formata nem remove seu sistema operacional; ele é instalado como uma camada de gerenciamento e Docker sobre o Linux. Todos os seus arquivos permanecem intactos.
- Como acessar o CasaOS com segurança fora de casa? Em vez de abrir portas no roteador, instale o Tailscale ou WireGuard no CasaOS. Assim você ganha uma conexão VPN criptografada para acessar o painel de qualquer lugar do mundo.
- Qual é a diferença entre CasaOS, TrueNAS e Unraid? TrueNAS e Unraid são sistemas dedicados com foco profundo em arranjos de discos complexos e ZFS. O CasaOS foca em simplicidade, leveza e facilidade de uso orientada a aplicativos domésticos.
- Os aplicativos voltam a funcionar sozinhos após uma queda de energia? Sim. Todos os contêineres Docker do CasaOS rodam com a política <code>restart: unless-stopped</code>, reiniciando automaticamente assim que o servidor ligar de novo.

## Links
- [GitHub →](https://github.com/IceWhaleTech/CasaOS)

## Termos relacionados do glossário
Self-Hosted Offline Open Source Local

---
Source: TreScout Discover · https://trescout.com/pt/discover/casaos/
