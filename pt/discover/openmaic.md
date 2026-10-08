# Simulação de sala de aula interativa com múltiplos agentes de inteligência artificial

O OpenMAIC, desenvolvido por pesquisadores da Universidade Tsinghua, reúne múltiplos agentes de IA nos papéis de professor, aluno e observador em um ambiente de sala de aula interativo.

- ★ 39.969
- TypeScript
- GitHub Trending · 2026-08-31

## Atualizações

- **5 de outubro de 2026:** Estrelas 39,351 → 39,969, versão mais recente v1.1.3 (5 de outubro de 2026).
- **28 de setembro de 2026:** Estrelas 39,156 → 39,351, versão mais recente v1.1.2 (28 de setembro de 2026).
- **27 de setembro de 2026:** Estrelas 25,572 → 39,156, versão mais recente v1.1.1 (26 de setembro de 2026).

## O que você ganha

- Arquitetura multiagente baseada em funções: interação dinâmica de agentes LLM nos papéis de professor, aluno que faz perguntas, debatedor e resumidor.
- Interface de sala de aula visual e de áudio: experiência pedagógica imersiva com lousa virtual, fluxo de perguntas e respostas em tempo real e síntese de voz (TTS).
- Currículo de curso personalizável: crie aulas interativas instantaneamente fazendo upload de seus próprios documentos PDF ou notas de aula em texto.
- Início de simulação com um clique: gerencie orquestrações complexas de agentes através de uma interface web moderna, sem necessidade de conhecimentos em programação técnica.
- Compatibilidade com modelos de pesos abertos: a liberdade de conectar o modelo de inteligência artificial que você desejar via Ollama, vLLM ou provedores de LLM em nuvem.

## Instalação

**Clonando o repositório e instalando dependências**

```
git clone https://github.com/THU-MAIC/OpenMAIC.git
cd OpenMAIC
pnpm install
```

## Execução

**Iniciando o servidor de desenvolvimento**

```
pnpm run dev
# Tarayıcıda http://localhost:3000 adresini açın
```

## Arquitetura técnica e princípio de funcionamento

- Motor de Orquestração de Conversa: O controlador central que gerencia qual agente falará, quando falará, a ordem dos turnos e o contexto da discussão.
- Gerenciamento de Memória e Contexto: Armazenar o conteúdo do quadro compartilhado e as perguntas dos alunos durante a aula na memória de curto/longo prazo.
- Transmissão em tempo real via WebSocket: envio de transcrições, expressões emocionais e animações para a interface de frontend sem latência.

## Dinâmicas de sala de aula com múltiplos agentes e simulações de papéis

- Ambientes de Discussão Socrática: Agentes com diferentes pontos de vista debatem um tema para estimular o pensamento crítico do usuário.
- Suporte Personalizado do Professor: Tutores de inteligência artificial dedicados que ajustam automaticamente o nível de dificuldade de acordo com a velocidade de compreensão do usuário.
- Pesquisas de Interação Social entre Agentes: Analisar como grandes modelos de linguagem colaboram e compartilham informações em ambientes de grupo.

## Se você não programa

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero simular um ambiente de discussão socrática na plataforma OpenMAIC carregando minhas próprias notas de aula. Você poderia explicar passo a passo como definir os papéis dos agentes (professor, aluno curioso, questionador crítico) e como configurar essa classe com um modelo Ollama local?

## Perguntas frequentes

- É necessário uma GPU para usar o OpenMAIC? Se você for executar seu próprio modelo local (Ollama/vLLM), uma GPU é recomendada; no entanto, ele pode ser usado diretamente com um computador padrão através de APIs em nuvem (OpenAI, Gemini, Groq).
- O usuário pode participar da simulação por voz? Sim. Graças ao WebRTC e ao módulo de reconhecimento de voz, o usuário pode participar das discussões em sala de aula falando através do microfone.
- Quantos agentes podem estar presentes na sala ao mesmo tempo? Na configuração padrão, a interação ideal é alcançada entre 3 e 8 agentes; turmas maiores podem ser configuradas dependendo dos recursos do sistema.
- Em quais formatos o conteúdo das aulas pode ser carregado? Documentos em texto simples, Markdown e PDF podem ser importados diretamente para a base de conhecimento do sistema.

## Termos relacionados do glossário

- [Markdown](https://trescout.com/pt/dictionary/markdown/)
- [GPU](https://trescout.com/pt/dictionary/gpu/)
- [PDF](https://trescout.com/pt/dictionary/pdf/)
- [LLM](https://trescout.com/pt/dictionary/llm/)
- [API](https://trescout.com/pt/dictionary/api/)
- [Open Source](https://trescout.com/pt/dictionary/open-source/)

- **Para quem é:** Educadores, pesquisadores de IA, empreendedores de edtech e estudantes.
- **Licença:** Apache-2.0 (Açık kaynak lisansı)
- **Framework:** Simulador Multiagente em TypeScript & Next.js
- **Plataformas:** Navegador web, Linux, macOS, Windows

## Links

- [Repositório no GitHub →](https://github.com/THU-MAIC/OpenMAIC)
- [Ler em turco →](https://trescout.com/discover/openmaic/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-08-31: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/openmaic/
