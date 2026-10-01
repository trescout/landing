# Combine 34 provedores de LLM gratuitos em uma API

FreeLLMAPI fornece roteamento inteligente e tolerância a falhas agregando 34 diferentes provedores de modelos de linguagem gratuitos em uma única API REST no formato OpenAI.

- ★ 29.808
- TypeScript
- GitHub Trending · 2026-08-28

## O que você ganha
- 34 provedores de modelos gratuitos: acesso completo a dezenas de provedores gratuitos, incluindo Google Gemini, Groq, Cloudflare Workers AI e HuggingFace.
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
Você pode explicar com exemplos de código como executar a ferramenta FreeLLMAPI em meu servidor local com Docker, como apontar o SDK OpenAI Node.js para este endpoint local e como habilitar o uso de um modelo de fallback automático quando um provedor falha?

## Perguntas frequentes
- Preciso adquirir uma chave API para usar o FreeLLMAPI? Não. O sistema combina 34 modelos de IA que oferecem níveis gratuitos ou inferência gratuita disponível ao público.
- Quais principais modelos de linguagem são suportados? São suportados modelos abertos como Llama 3, Mistral, Gemma, Claude e modelos populares como o nível gratuito do Google Gemini.
- É adequado para privacidade corporativa? FreeLLMAPI é de código aberto e roda em sua rede local, mas os provedores gratuitos por trás deles têm seus próprios termos de uso e políticas de privacidade.
- É compatível com LangChain ou CrewAI? Sim. Como fornece uma emulação completa da API REST OpenAI, pode ser usado diretamente com todas as estruturas LLM, definindo o endereço baseURL como localhost:3000/v1.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/freellmapi/
