# Transforme o seu computador pessoal num servidor de inteligência artificial local

O Osmantic/ODS de código aberto permite-lhe configurar inferência de grandes modelos de linguagem locais, pipelines de RAG baseados em pesquisa vetorial e fluxos de trabalho de agentes autónomos executados no seu próprio hardware.

- ★ 6.854
- Python
- GitHub Trending · 2026-08-31

## O que você ganha
- Privacidade total de dados e execução local: operação segura de inteligência artificial em GPU e CPU locais, sem enviar seus dados para servidores em nuvem externos.
- RAG integrado (Search Aided Generation): vetorize suas notas pessoais, documentos da empresa e repositórios de código para pesquisas semânticas instantâneas.
- Capacidades multimodais: reunir geração de texto, reconhecimento de fala (Whisper), síntese de voz e geração de imagens sob o mesmo teto.
- API local compatível com OpenAI: redirecione seus clientes e ferramentas de IA existentes para seu servidor ODS local com apenas uma alteração de URL.
- Orquestração abrangente de agentes: cadeias de agentes inteligentes que invocam ferramentas locais e resolvem tarefas de várias etapas de forma autônoma.

## Instalação
**Clonar o repositório e configurar o ambiente**

```
git clone https://github.com/Osmantic/ODS.git
cd ODS
pip install -e .
```


## Execução
**Iniciar o servidor de IA local**

```
python -m ods.server --port 8000
# Web paneline http://localhost:8000 adresinden erişin
```


## Arquitetura técnica e princípio de funcionamento
- Núcleo de Inferência Local (llama.cpp e vLLM): Carregamento e execução rápidos de modelos em formatos GGUF e GPU puro com o mínimo de uso de memória.
- Banco de Dados Vetorial Embutido: Fragmentação (chunking) e indexação de documentos com armazenamento vetorial leve baseado em ChromaDB e SQLite.
- Fila de Tarefas e Máquina de Estados do Agente: Processadores assíncronos que gerenciam consultas de várias etapas e fluxos de chamada de ferramentas (tool calling).

## Fluxos de trabalho RAG locais e pipelines de agentes personalizados
- Trabalhando com Documentos Confidenciais da Empresa: Consulte contratos, demonstrativos financeiros e comunicações internas com RAG local, sem enviá-los para a nuvem.
- Assistente de Desenvolvimento e Análise de Código Local: Indexe seus projetos de software personalizados para obter preenchimento de código com IA local no VS Code ou Cursor.
- Agentes de Processamento de Dados Autônomos: Defina tarefas em segundo plano que leem, resumem e convertem o formato de relatórios no sistema de arquivos local.

## Se você não programa
Você poderia explicar, com código e passos de terminal, como configurar o servidor ODS no meu computador pessoal para transferir os documentos PDF da minha empresa para um banco de dados vetorial local e, em seguida, realizar consultas de perguntas e respostas RAG baseadas nesses documentos através de um modelo Llama 3 local?

## Perguntas frequentes
- Funciona totalmente offline sem conexão com a internet? Sim. Após o download dos pesos do modelo necessários, o ODS pode operar em ambientes totalmente offline (air-gapped) sem a necessidade de qualquer conexão de rede.
- Quais formatos de modelo são suportados? Suporta todos os modelos abertos no formato GGUF (Llama 3, Mistral, Qwen, DeepSeek) e pesos puros do HuggingFace.
- Existe uma interface web? Sim. O ODS vem com um painel web integrado; você pode gerenciar modelos, fazer upload de arquivos e iniciar sessões de chat.
- Funciona apenas com CPU, sem GPU? Sim. Graças ao kernel llama.cpp, ele também pode rodar com alta eficiência apenas na CPU, utilizando os conjuntos de instruções AVX2/AVX-512.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/ods/
