# Ferramenta de monitoramento de sistemas e serviços prometheus

O Prometheus é uma ferramenta de monitoramento que fornece operações de monitoramento de sistemas e serviços e gerenciamento de banco de dados de séries temporais (time series database). Coletando métricas de alvos em intervalos definidos, o sistema avalia regras para exibir resultados e pode gerar alertas sob condições definidas.

- ★ 67.226
- Go
- GitHub Trending · 2026-11-07

## Atualizações

- **7 de novembro de 2026:** Estrelas 67,225 → 67,226, versão mais recente v3.16.0 (5 de novembro de 2026).

## O que você ganha

- coleta métricas de alvos em intervalos definidos
- avalia regras e exibe os resultados
- pode gerar alertas sob condições definidas

## Instalação

**executar com docker**

```
docker run --name prometheus -d -p 127.0.0.1:9090:9090 prom/prometheus
```

## Execução

**compilar a partir do código-fonte e executar**

```
make build
./prometheus --config.file=your_config.yml
```

## Se você não programa

Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero iniciar a aplicação Prometheus, ferramenta de monitoramento de sistemas e serviços, usando o Docker. Para isso, execute o comando docker run --name prometheus -d -p 127.0.0.1:9090:9090 prom/prometheus.

Repositório: https://github.com/prometheus/prometheus. Baseie-se nas instruções oficiais no arquivo README deste repositório para a instalação e execução.

Antes de começar, verifique em qual sistema operacional estamos e se as ferramentas necessárias (ex: Python, Node.js, Git, Docker) estão instaladas. Instale as que faltarem passo a passo de acordo com este sistema.

Crie uma pasta nova e vazia para trabalhar. Não toque em arquivos fora desta pasta e não exclua nada. Antes de executar cada comando, diga o que você vai fazer em uma frase.

Diga-me o que devo ver na tela ao final de cada etapa. Se ocorrer um erro, colarei a mensagem de erro para você exatamente como ela é, e vamos corrigi-la juntos.

## Termos relacionados do glossário

- [Time Series Database](https://trescout.com/pt/dictionary/time-series-database/)
- [Database](https://trescout.com/pt/dictionary/database/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** desenvolvedores e administradores de sistemas que desejam monitorar o status de seus sistemas e serviços
- **Licença:** Apache-2.0

## Links

- [Repositório no GitHub →](https://github.com/prometheus/prometheus)
- [Ler em turco →](https://trescout.com/discover/prometheus/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-11-07: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. O texto de apresentação foi preparado com IA a partir da própria documentação do repositório e esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/prometheus/
