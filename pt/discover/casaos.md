# Gerencie seu servidor em nuvem pessoal

O CasaOS é um sistema operativo de nuvem pessoal de código aberto, leve e elegante, que permite gerir aplicações baseadas em Docker com apenas um clique em servidores domésticos, mini PCs e dispositivos Raspberry Pi. Desenvolvido em linguagem Go, a plataforma permite-lhe estabelecer a sua própria soberania digital sem a necessidade de comandos de terminal complexos.

- ★ 36.953
- Go
- GitHub Trending · 2026-06-26

## Atualizações

- **2 de agosto de 2026:** Estrelas 34,992 → 36,953, versão mais recente v0.4.15 (19 de dezembro de 2024).

## O que você ganha

- Loja de aplicativos rica com um clique: instale o Nextcloud, Plex, Jellyfin, AdGuard Home, qBittorrent, Home Assistant e mais de 100 serviços populares auto-hospedados (self-hosted) em segundos.
- Painel de controle web elegante e intuitivo: monitore em tempo real a carga de CPU e RAM, as taxas de ocupação de disco, a atividade de rede e os contêineres em execução através de elegantes cartões de widgets.
- Armazenamento visual e gerenciamento de arquivos: Monte automaticamente discos rígidos externos e unidades USB, compartilhe suas pastas na rede local via protocolo Samba (SMB) com seus dispositivos Windows/Mac.
- Suporte a Docker Compose personalizado: Dê vida aos seus contêineres personalizados sem esforço, colando qualquer arquivo Docker Compose que não esteja na loja oficial diretamente na interface web.
- Núcleo Go leve e sobrecarga de sistema zero: com consumo mínimo de memória em segundo plano, ele oferece desempenho fluido mesmo nos Raspberry Pi 4/5 mais modestos ou em laptops antigos.

## Instalação

**comando de instalação**

```
curl -fsSL https://get.casaos.io | sudo bash
```

## Execução

**comando de atualização**

```
curl -fsSL https://get.casaos.io/update | sudo bash
```

## Arquitetura técnica e princípio de funcionamento

- Arquitetura de microsserviços em Go: O núcleo do CasaOS (CasaOS-Gateway, MessageBus, LocalStorage e UserService) consiste em serviços Go leves que funcionam de forma independente. A comunicação entre os serviços ocorre via REST e WebSocket.
- Abstração do ciclo de vida de contêineres: Comunica-se diretamente com o daemon do Docker para detectar automaticamente conflitos de portas, transformando variáveis de ambiente e caminhos de montagem de volumes persistentes em formulários fáceis de usar.
- Ecossistema ZimaOS e IceWhale: o projeto, apoiado pela IceWhale Technology · fabricante do hardware ZimaBoard e ZimaBlade ·, oferece total compatibilidade com hardwares de nuvem local.
- Agrupamento inteligente de discos: Combina discos rígidos de diferentes tamanhos em um único pool de armazenamento lógico, criando espaço flexível para mídia doméstica e backup.

## Guia passo a passo para configurar seu próprio servidor doméstico

- Instalação básica do Linux: instale uma versão limpa do Ubuntu Server ou Debian minimal no seu dispositivo e conecte-o à sua rede local com um cabo Ethernet.
- Instalação do CasaOS em uma única linha: execute o script de instalação oficial via terminal; o script configura o Docker e as dependências automaticamente.
- Acesso à interface pelo navegador: crie sua primeira conta de administrador digitando o endereço IP do seu servidor (por exemplo, http://192.168.1.100) no navegador a partir de qualquer computador na rede.
- Implantação de aplicativos: Acesse a aba App Store para instalar sua nuvem pessoal com o Nextcloud e sua biblioteca de filmes/séries com o Jellyfin com apenas um clique.

## Se você não programa

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

O CasaOS está instalado no meu servidor doméstico. Quero instalar e configurar os serviços AdGuard Home (bloqueador de anúncios), Jellyfin (transmissão de mídia) e Tailscale (acesso seguro fora de casa) para todos os dispositivos da minha casa. Poderia explicar passo a passo como instalar esses serviços a partir do painel web do CasaOS usando Docker Compose personalizado ou a loja de aplicativos, e como configurar o compartilhamento de disco?

## Perguntas frequentes

- O CasaOSapaga o meu sistema operativo Linux ou os meus dados actuais? Não. O CasaOS não apaga o seu sistema operativo atual; é instalado sobre o mesmo como uma camada de gestão de ambiente de trabalho e Docker. Os ficheiros existentes nos seus discos são preservados e tornam-se acessíveis através do painel.
- Como posso acessar meu servidor CasaOS com segurança quando estiver fora de casa? Em vez de fazer um encaminhamento de porta inseguro (port forwarding), você pode instalar o Tailscale ou o WireGuard no CasaOS com apenas um clique. Dessa forma, você pode acessar o painel de qualquer lugar do mundo por meio de um túnel VPN criptografado, como se estivesse na sua rede doméstica.
- Qual é a diferença entre o CasaOS e o TrueNAS ou o Unraid? O TrueNAS e o Unraid são sistemas operacionais independentes focados em gerenciamento avançado de armazenamento e configurações de RAID. Já o CasaOS oferece uma experiência de nuvem doméstica leve, extremamente fácil de usar e centrada em aplicativos.
- As aplicações instaladas iniciam automaticamente após uma falha de energia? Sim. Todos os contentores Docker no CasaOS são iniciados por predefinição com a política restart: unless-stopped. Quando o seu servidor é reiniciado, todos os seus serviços continuam a funcionar automaticamente a partir de onde pararam.

## Termos relacionados do glossário

- [VPN](https://trescout.com/pt/dictionary/vpn/)
- [RAM](https://trescout.com/pt/dictionary/ram/)
- [Self-hosted](https://trescout.com/pt/dictionary/self-hosted/)
- [CPU](https://trescout.com/pt/dictionary/cpu/)
- [Terminal](https://trescout.com/pt/dictionary/terminal/)
- [Open Source](https://trescout.com/pt/dictionary/open-source/)

- **Para quem é:** Destinado a usuários que desejam configurar um servidor doméstico (Homelab) ou nuvem pessoal, evitando a complexidade do terminal e visando gerenciar aplicativos Docker com um único clique.
- **Licença:** Apache-2.0 (Geniş özgürlük sunan açık kaynak lisansı)
- **Desenvolvedor:** IceWhale Technology e Comunidade de Código Aberto
- **Sistemas Suportados:** Ubuntu, Debian, Raspberry Pi OS, Armbian (x86_64, aarch64, armv7)

## Links

- [Repositório no GitHub →](https://github.com/IceWhaleTech/CasaOS)
- [Ler em turco →](https://trescout.com/discover/casaos/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-06-26: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/casaos/
