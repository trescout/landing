# Sensing sem fio com sinais WiFi

RuView é uma plataforma de sensing que usa Channel State Information (CSI) do WiFi para estudar mudanças no ambiente. Ela pode funcionar com hardware ESP32 ou NIC de pesquisa, enquanto dados simulados permitem avaliação sem hardware.

- ★ 96.773
- GitHub Trending · 2026-05-30

## Atualizações

- **7 de outubro de 2026:** Estrelas 96,651 → 96,773, versão mais recente v3067 (6 de outubro de 2026).
- **6 de outubro de 2026:** Estrelas 96,464 → 96,651, versão mais recente v3060 (5 de outubro de 2026).
- **5 de outubro de 2026:** Estrelas 95,926 → 96,464, versão mais recente v3037 (4 de outubro de 2026).
- **2 de outubro de 2026:** Estrelas 95,751 → 95,926, versão mais recente v2975 (2 de outubro de 2026).

## Instalação

**Baixe a imagem Docker**

```
docker pull ruvnet/wifi-densepose:latest
```

**Clone o código-fonte**

```
git clone https://github.com/ruvnet/RuView.git
```

## Execução

**Servidor de demonstração sem hardware**

```
docker run -p 3000:3000 ruvnet/wifi-densepose:latest
```

**Verificação determinística**

```
./verify
```

## O que esta ferramenta faz?

RuView é uma plataforma com licença MIT para experimentos de sensing usando Channel State Information do WiFi. Pode ser instalada com Docker ou a partir do código-fonte e avaliada com dados simulados sem hardware. As capacidades dependem do modo de hardware: o sensing RSSI-only em laptops serve para presença e movimento grosseiros, enquanto o sensing avançado exige hardware com CSI completo.

## Para quem é?

Pesquisadores e desenvolvedores que querem experimentar presença, movimento ou mudanças ambientais a partir de sinais WiFi.

## O que não esperar

Monitoramento médico ou expectativas de estimativa de pose em um laptop comum no modo RSSI-only.

## Destaques

- Oferece caminhos de sensing com CSI usando ESP32 e NICs de pesquisa.
- Pode ser avaliada com dados simulados sem hardware.
- Documenta uma verificação determinística com sinal de referência usando `./verify`.
- Distingue o que o modo RSSI-only de um laptop oferece do hardware com CSI completo.

## Primeiro fluxo de uso

1. Prepare o ambiente seguindo o caminho Docker ou código-fonte dos guias oficiais.
2. Sem hardware, comece examinando o caminho de avaliação com dados simulados.
3. Execute a verificação determinística descrita no build guide com `./verify`.
4. Escolha o caminho RSSI-only ou CSI completo de acordo com seu hardware.

## Início seguro

O modo RSSI-only em laptop serve para detecção grosseira de presença e movimento e não oferece pose. Pose e alguns benchmarks são documentados como experimentais, de primeira versão ou limitados; avalie os resultados de acordo com o modo de hardware usado.

## Primeiro prompt

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Como posso avaliar um cenário simples de detecção de movimento usando dados CSI simulados do WiFi?

## Termos relacionados do glossário

- [WiFi](https://trescout.com/pt/dictionary/wifi/)
- [Benchmark](https://trescout.com/pt/dictionary/benchmark/)

## Links

- [Repositório no GitHub →](https://github.com/ruvnet/RuView)
- [Repositório GitHub oficial do RuView →](https://github.com/ruvnet/RuView)
- [Guia do usuário do RuView →](https://github.com/ruvnet/RuView/blob/main/docs/user-guide.md)
- [Guia de build do RuView →](https://github.com/ruvnet/RuView/blob/main/docs/build-guide.md)
- [Ler em turco →](https://trescout.com/discover/ruview/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-05-30: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/ruview/
