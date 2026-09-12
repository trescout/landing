# Tunelamento TCP para tráfego de rede

Desenvolvido na linguagem Go, o OpenFlux é uma ferramenta de tunelamento TCP projetada para pesquisas na pilha de rede (network stack). Graças ao suporte a transportes conectáveis (pluggable transports), oferece possibilidades flexíveis de análise e gerenciamento sobre o tráfego de rede.

- ★ 1.241
- Go
- GitHub Trending · 2026-09-12

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
Desejo criar um túnel TCP usando a ferramenta OpenFlux. Explique passo a passo as etapas de compilação necessárias para executar o cliente no meu computador desktop e, em seguida, como configurar as definições de proxy SOCKS5 no navegador. Além disso, ao configurar um nó de saída (exit node) em um servidor Linux, especifique com detalhes técnicos por que é necessário bloquear pacotes RST com iptables e qual o impacto dessa operação na segurança da rede.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/openflux/
