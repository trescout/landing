# Sensing sem fio com sinais WiFi

RuView é uma plataforma de sensing que usa Channel State Information (CSI) do WiFi para estudar mudanças no ambiente. Ela pode funcionar com hardware ESP32 ou NIC de pesquisa, enquanto dados simulados permitem avaliação sem hardware.

- ★ 91.805
- GitHub Trending · 2026-05-30

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
- Prepare o ambiente seguindo o caminho Docker ou código-fonte dos guias oficiais.
- Sem hardware, comece examinando o caminho de avaliação com dados simulados.
- Execute a verificação determinística descrita no build guide com `./verify`.
- Escolha o caminho RSSI-only ou CSI completo de acordo com seu hardware.

## Início seguro

## Primeiro prompt
Como posso avaliar um cenário simples de detecção de movimento usando dados CSI simulados do WiFi?

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Repositório GitHub oficial do RuView →
- Guia do usuário do RuView →
- Guia de build do RuView →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/ruview/
