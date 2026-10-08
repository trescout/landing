# Tunelamento TCP para tráfego de rede

Desenvolvido na linguagem Go, o OpenFlux é uma ferramenta de tunelamento TCP projetada para pesquisas na pilha de rede (network stack). Graças ao suporte a transportes conectáveis (pluggable transports), oferece possibilidades flexíveis de análise e gerenciamento sobre o tráfego de rede.

- ★ 2.027
- Go
- GitHub Trending · 2026-09-12

## Atualizações

- **8 de outubro de 2026:** Estrelas 2,019 → 2,027, versão mais recente v0.4.2 (7 de outubro de 2026).
- **7 de outubro de 2026:** Estrelas 1,910 → 2,019, versão mais recente v0.4.1 (7 de outubro de 2026).
- **1 de outubro de 2026:** Estrelas 1,896 → 1,910, versão mais recente v0.3.0 (30 de setembro de 2026).
- **29 de setembro de 2026:** Estrelas 1,884 → 1,896, versão mais recente v0.2.0 (28 de setembro de 2026).

## O que você ganha

- Gerenciamento de rede flexível com transportes conectáveis
- Encaminhamento de tráfego de rede local com suporte a proxy SOCKS5
- Transmissão de dados via Yandex Docs e WebRTC

## Instalação

**Compilação de cliente desktop e nó de saída**

```
go mod tidy
go build -o universal-bypass-tool .
```

**Compilação de cliente Android**

```
export ANDROID_NDK_HOME=<your Android NDK path>
./build_android.sh
```

## Execução

**Iniciando o cliente desktop**

```
./universal-bypass-tool --client --url "YOUR_YANDEX_DOC_URL" --socks5 :1080 --debug
```

## Se você não programa

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Desejo criar um túnel TCP usando a ferramenta OpenFlux. Explique passo a passo as etapas de compilação necessárias para executar o cliente no meu computador desktop e, em seguida, como configurar as definições de proxy SOCKS5 no navegador. Além disso, ao configurar um nó de saída (exit node) em um servidor Linux, especifique com detalhes técnicos por que é necessário bloquear pacotes RST com iptables e qual o impacto dessa operação na segurança da rede.

## Termos relacionados do glossário

- [Pluggable Transports](https://trescout.com/pt/dictionary/pluggable-transports/)
- [Network Stack](https://trescout.com/pt/dictionary/network-stack/)
- [Proxy](https://trescout.com/pt/dictionary/proxy/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** Destina-se a utilizadores que realizam pesquisas sobre pilhas de rede e que pretendem tunelar tráfego TCP através de diferentes protocolos de transporte.
- **Licença:** GPL-3.0

## Links

- [Repositório no GitHub →](https://github.com/p1neappleXpress/OpenFlux)
- [Ler em turco →](https://trescout.com/discover/openflux/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-09-12: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/openflux/
