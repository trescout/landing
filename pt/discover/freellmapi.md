# Combine 34 provedores de LLM gratuitos em uma API

FreeLLMAPI fornece roteamento inteligente e tolerância a falhas agregando 34 diferentes provedores de modelos de linguagem gratuitos em uma única API REST no formato OpenAI.

- ★ 38.660
- TypeScript
- GitHub Trending · 2026-08-28

## Atualizações

- **21 de outubro de 2026:** Estrelas 38,000 → 38,660, versão mais recente v0.16.7 (21 de outubro de 2026).
- **20 de outubro de 2026:** Estrelas 37,418 → 38,000, versão mais recente v0.16.6 (20 de outubro de 2026).
- **19 de outubro de 2026:** Estrelas 37,306 → 37,418, versão mais recente v0.16.5 (19 de outubro de 2026).
- **19 de outubro de 2026:** Estrelas 36,776 → 37,306, versão mais recente v0.16.4 (19 de outubro de 2026).

## O que você ganha

- 34 provedores de modelos gratuitos: acesso completo a dezenas de provedores gratuitos, incluindo Google Gemini, Groq, Cloudflare Workers AI e Hugging Face.
- Compatibilidade da API REST OpenAI: trabalhe com LangChain, LlamaIndex e aplicativos de IA existentes sem alterar o código, graças ao endpoint /v1/chat/completions.
- Roteamento inteligente e recuperação de falhas: Mude automaticamente para um provedor alternativo quando um provedor atingir o limite de taxa ou falhar.
- Suporte a streaming (eventos enviados pelo servidor): Possibilidade de receber saídas do modelo como um fluxo palavra por palavra em tempo real.
- Leve e fácil de implantar: Arquitetura que pode ser implantada em um computador ou servidor local em segundos com Docker ou Node.js.

## Instalação

**Clonando o repositório e instalando dependências**

```
git clone https://github.com/tashfeenahmed/freellmapi.git
cd freellmapi
npm install
```

## Execução

**Iniciando o serviço e consultando o modelo**

```
npm start
# OpenAI uyumlu istek:
curl http://localhost:3000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"gpt-4o-mini","messages":[{"role":"user","content":"Merhaba!"}]}'
```

## Arquitetura técnica e princípio de funcionamento

- Camada de adaptador de provedor: arquitetura extensível que normaliza diferentes APIs REST e WebSocket em um formato de resposta JSON comum.
- Balanceamento de carga dinâmico e monitoramento de cotas: Monitorando os limites de velocidade atuais de cada provedor e direcionando as solicitações para o modelo ativo de resposta mais rápida.
- Cache integrado e gerenciamento de erros: cache de consultas repetidas e mecanismo de nova tentativa automática em caso de tempo limite.

## Roteamento de modelo e mecanismo de tolerância a falhas

- Comparação de vários modelos: meça a qualidade e a latência da resposta enviando a mesma entrada do usuário para diferentes modelos de código aberto.
- Economize em desenvolvimento e prototipagem: coloque rapidamente protótipos baseados em IA e projetos MVP em funcionamento sem definir chaves de API pagas.
- Estratégia de backup (pipeline de fallback): certifique-se de que seu sistema redirecione para modelos secundários sem interrupção quando o provedor primário ficar inativo.

## Se você não programa

Cole isto no seu agente (Claude Code · Codex · Antigravity)

Você pode explicar com exemplos de código como executar a ferramenta FreeLLMAPI em meu servidor local com Docker, como apontar o SDK OpenAI Node.js para este endpoint local e como habilitar o uso de um modelo de fallback automático quando um provedor falha?

Repositório: https://github.com/tashfeenahmed/freellmapi. Baseie-se nas instruções oficiais no arquivo README deste repositório para a instalação e execução.

Antes de começar, verifique em qual sistema operacional estamos e se as ferramentas necessárias (ex: Python, Node.js, Git, Docker) estão instaladas. Instale as que faltarem passo a passo de acordo com este sistema.

Crie uma pasta nova e vazia para trabalhar. Não toque em arquivos fora desta pasta e não exclua nada. Antes de executar cada comando, diga o que você vai fazer em uma frase.

Diga-me o que devo ver na tela ao final de cada etapa. Se ocorrer um erro, colarei a mensagem de erro para você exatamente como ela é, e vamos corrigi-la juntos.

## Perguntas frequentes

- Preciso adquirir uma chave API para usar o FreeLLMAPI? Não. O sistema combina 34 modelos de IA que oferecem níveis gratuitos ou inferência gratuita disponível ao público.
- Quais principais modelos de linguagem são suportados? São suportados modelos abertos como Llama 3, Mistral, Gemma, Claude e modelos populares como o nível gratuito do Google Gemini.
- É adequado para privacidade corporativa? FreeLLMAPI é de código aberto e roda em sua rede local, mas os provedores gratuitos por trás deles têm seus próprios termos de uso e políticas de privacidade.
- É compatível com LangChain ou CrewAI? Sim. Como fornece uma emulação completa da API REST OpenAI, pode ser usado diretamente com todas as estruturas LLM, definindo o endereço baseURL como localhost:3000/v1.

## Termos relacionados do glossário

- [Pipeline](https://trescout.com/pt/dictionary/pipeline/)
- [Proxy](https://trescout.com/pt/dictionary/proxy/)
- [Localhost](https://trescout.com/pt/dictionary/localhost/)
- [SDK](https://trescout.com/pt/dictionary/sdk/)
- [LLM](https://trescout.com/pt/dictionary/llm/)
- [Open Source](https://trescout.com/pt/dictionary/open-source/)

- **Para quem é:** Desenvolvedores de inteligência artificial, pesquisadores de código aberto, engenheiros full-stack e desenvolvedores de protótipos.
- **Licença:** MIT (Özgür açık kaynak lisansı)
- **Framework:** Proxy reverso TypeScript/Node.js
- **Plataformas:** Docker, Linux, macOS, Windows

## Links

- [Repositório no GitHub →](https://github.com/tashfeenahmed/freellmapi)
- [Ler em turco →](https://trescout.com/discover/freellmapi/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-08-28: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. O texto de apresentação foi preparado com IA a partir da própria documentação do repositório e esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/freellmapi/
