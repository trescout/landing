# Workflows visuais e automação com IA

O n8n combina canvas visual, código personalizado, agentes de IA e workflows em uma plataforma de automação fair-code. Ele oferece implantação self-hosted ou cloud e pode incluir diferentes provedores de modelos nos workflows.

- ★ 203.105
- GitHub Trending · 2026-08-23

## Instalação
**Crie o volume de dados**

```
docker volume create n8n_data
```


## Execução
**Inicie o container Docker do n8n**

```
docker run -it --rm --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```


## O que esta ferramenta faz?
Com o n8n, você pode criar workflows em um canvas visual e estendê-los com JavaScript, Python e pacotes npm. As fontes oficiais listam flexibilidade de modelos entre OpenAI, Anthropic, Google e modelos de código aberto, além de aprovações humanas, observabilidade, acesso baseado em funções e trilhas de auditoria. A plataforma pode ser implantada de forma self-hosted ou na nuvem.

## Para quem é?
Equipes que querem combinar o desenho visual de workflows com código personalizado e agentes de IA.

## O que não esperar
Pessoas que procuram apenas produtos de licença proprietária ou não querem ampliar workflows com código ou configuração.

## Destaques
- Combina canvas visual, código personalizado e agentes de IA nos workflows.
- Pode ser estendido com JavaScript, Python e pacotes npm.
- Oferece implantação self-hosted e cloud.
- Lista aprovações humanas, observabilidade, acesso baseado em funções e trilhas de auditoria.

## Primeiro fluxo de uso
- Siga o início rápido oficial com Docker para executar o n8n.
- Abra o editor no navegador pela porta 5678.
- Crie seu primeiro workflow no canvas visual.
- Adicione código personalizado ou um provedor de modelos compatível conforme a sua necessidade.

## Início seguro

## Primeiro prompt
Ajude-me a criar no canvas visual um workflow que receba uma entrada, a processe com um modelo de IA e passe o resultado para a próxima etapa.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Repositório GitHub oficial do n8n →
- Documentação oficial do n8n →
- Repositório de documentação do n8n →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/n8n/
