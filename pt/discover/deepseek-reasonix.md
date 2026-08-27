# Agente de codificação AI para terminal

DeepSeek-Reasonix é um agente de codificação de IA executado no terminal e baseado em modelos DeepSeek. Com foco na estabilidade do cache de prefixo, esta ferramenta garante que os desenvolvedores recebam suporte de codificação ininterrupto durante sessões longas.

- ★ 35.212
- Go
- GitHub Trending · 2026-08-03

## O que você ganha
- Fornece suporte de codificação ininterrupto de longo prazo com modelos DeepSeek.
- Oferece gerenciamento de sessão de baixo custo com seu recurso de cache de prefixo.
- Ele fornece uso flexível através do terminal com suporte de plug-in configurável.

## Instalação
**Instalação via NPM ou Homebrew**

```
npm i -g reasonix                  # any OS; pulls the prebuilt native binary
brew install esengine/reasonix/reasonix   # macOS
```

**Compilando a partir do código-fonte**

```
git clone https://github.com/esengine/DeepSeek-Reasonix.git
cd DeepSeek-Reasonix
make build      # -> bin/reasonix(.exe)
make cross      # -> dist/ (darwin|linux|windows × amd64|arm64)
```


## Execução
**Configuração e inicialização**

```
reasonix setup                      # configure a provider and model
reasonix                            # start an interactive session
reasonix run "implement the TODOs in main.go"
```


## Se você não programa
Ao trabalhar com este agente de codificação de inteligência artificial rodando no terminal, desenvolvo sugestões de código levando em consideração a estrutura atual e os objetivos do meu projeto. Concentre-se na produção de respostas consistentes e de baixo custo em nossas longas sessões usando estabilidade de cache de prefixo. Ao escrever ou depurar código, forneça soluções modulares e limpas que atendam às necessidades do projeto.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/deepseek-reasonix/
