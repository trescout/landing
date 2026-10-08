# Tunelamento Netcat seguro em redes Tailscale

Tailcat traz a funcionalidade clássica do netcat para a camada de malha Tailscale VPN, fornecendo transferência segura de dados sem a necessidade de um plano de controle ou porta aberta.

- ★ 7.746
- Go
- GitHub Trending · 2026-08-28

## Atualizações

- **27 de setembro de 2026:** Estrelas 2,435 → 7,746, versão mais recente v0.7.0 (20 de setembro de 2026).

## O que você ganha

- Encaminhamento de porta zero (Port Forwarding): Comunicação direta entre dispositivos atrás de NAT ou firewall restrita sem abrir portas abertas.
- Criptografia WireGuard ponta a ponta: Criptografe automaticamente todas as transferências TCP e de dados brutos com autenticação Tailscale e WireGuard.
- Biblioteca tsnet incorporada: Trabalhando como um nó Tailscale independente sem a necessidade de instalar um cliente Tailscale no nível do sistema operacional.
- Transferência rápida de arquivos e pipeline: fluxo de comandos tar, gzip ou dd entre máquinas por meio de pipes de entrada/saída padrão (stdin/stdout).
- Depuração e diagnóstico de rede: teste de acessibilidade de porta entre microsserviços e máquinas remotas com comandos práticos como o netcat tradicional.

## Instalação

**Instalação direta com Go**

```
go install tailscale.com/cmd/tailcat@latest
```

## Execução

**Iniciando o modo de escuta e conectando um cliente**

```
# Sunucu düğümde dinle:
tailcat -l 8080
# İstemci düğümden bağlan:
tailcat hedef-node 8080
```

## Arquitetura técnica e princípio de funcionamento

- Rede de área de usuário tsnet: Cria uma sessão VPN diretamente no aplicativo, sem a necessidade de privilégios de root ou de um dispositivo TUN virtual.
- Resolução de nó MagicDNS: Capacidade de conectar-se instantaneamente a nomes de máquinas Tailscale, como 'nó de servidor', em vez de endereços IP.
- Suporte a relé DERP: Retomando a transferência de dados por meio de relés DERP Tailscale em redes extremamente restritivas onde a conexão P2P direta não é possível.

## Tunelamento de rede seguro e cenários de ponta a ponta

- Transferência rápida e segura de arquivos: transferência de configuração zero com `tailcat -l 9000 > backup.tar.gz` no destinatário e `tailcat destination 9000 \< backup.tar.gz` no remetente.
- Compartilhamento temporário de serviço HTTP: Abrindo o servidor web local em desenvolvimento para seus colegas na rede tailnet com um único comando.
- Dispositivo incorporado e acesso Raspberry Pi: Envie dados remotamente com segurança para dispositivos IoT restritos com IP dinâmico e na rede doméstica.

## Se você não programa

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Desejo configurar um túnel de transferência de arquivos criptografados entre dois servidores diferentes na rede mesh Tailscale usando a ferramenta Tailcat. Você pode explicar como iniciar o ouvinte no lado do servidor, como transmitir o arquivo tar da saída padrão no lado do cliente e como gerenciar a autenticação tsnet?

## Perguntas frequentes

- Preciso de um cliente Tailscale instalado em minha máquina? Não. Tailcat tem o mecanismo tsnet integrado; Ele lança seu próprio link Tailscale como um binário independente.
- O tráfego é realmente criptografado de ponta a ponta? Sim. Tailcat usa o protocolo WireGuard no núcleo da rede Tailscale; os dados são criptografados diretamente entre dispositivos.
- Suporta tráfego UDP? Tailcat é otimizado principalmente para fluxos TCP e tunelamento de soquete; Ele protege os recursos TCP do netcat clássico.
- Como autenticar para conexão? Quando o Tailcat é executado pela primeira vez, ele fornece um link de login do Tailscale no terminal ou autentica automaticamente com a variável de ambiente TAILSCALE_AUTHKEY.

## Termos relacionados do glossário

- [Root](https://trescout.com/pt/dictionary/root/)
- [VPN](https://trescout.com/pt/dictionary/vpn/)
- [Mesh](https://trescout.com/pt/dictionary/mesh/)
- [Open Source](https://trescout.com/pt/dictionary/open-source/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** Administradores de sistemas, engenheiros de DevOps, especialistas em redes e arquitetos de nuvem.
- **Licença:** BSD 3-Clause (Esnek açık kaynak lisansı)
- **Framework:** Biblioteca tsnet Go e Tailscale
- **Plataformas:** Linux, macOS, Windows

## Links

- [Repositório no GitHub →](https://github.com/tailscale/tailcat)
- [Ler em turco →](https://trescout.com/discover/tailcat/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-08-28: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/tailcat/
