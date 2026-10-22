# Inferência eficiente de IA no processador

Desenvolvido pela Microsoft, o BitNet oferece um framework de inferência oficial para grandes modelos de linguagem (LLMs) de 1 bit. Escrita em C++, esta ferramenta tem como objetivo otimizar a execução de modelos de baixa precisão de bits.

- ★ 40.731
- C++
- GitHub Trending · 2026-10-12

## O que você ganha

- Executa modelos de inteligência artificial em processadores de computador padrão com alta velocidade e baixo consumo de energia.
- Permite utilizar modelos de linguagem de 1 bit comprimidos no seu dispositivo local sem perda de qualidade.
- Graças ao suporte ao modo de diálogo, oferece a possibilidade de conversar diretamente com os modelos baixados.

## Instalação

**Baixe o código-fonte**

```
git clone --recursive https://github.com/microsoft/BitNet.git
cd BitNet
```

**Prepare o ambiente e instale as dependências**

```
# (Recommended) Create a new conda environment
conda create -n bitnet-cpp python=3.10
conda activate bitnet-cpp

pip install -r requirements.txt
```

## Execução

**Baixe o modelo e configure o ambiente**

```
# Manually download the model and run with local path
huggingface-cli download microsoft/BitNet-b1.58-2B-4T-gguf --local-dir models/BitNet-b1.58-2B-4T
python setup_env.py -md models/BitNet-b1.58-2B-4T -q i2_s
```

**Execute o modelo no modo de conversa**

```
# Run inference with the quantized model
python run_inference.py -m models/BitNet-b1.58-2B-4T/ggml-model-i2_s.gguf -p "You are a helpful assistant" -cnv
```

## Se você não programa

Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero executar um modelo de inteligência artificial de 1 bit no meu computador usando a infraestrutura do BitNet. Em primeiro lugar, oriente-me nos passos para clonar o projeto com o comando 'git clone --recursive https://github.com/microsoft/BitNet.git' e entrar na pasta, criar um ambiente Python 3.10 com o gerenciador de pacotes Conda e instalar as dependências. Em seguida, explique passo a passo, de forma simples e acessível para quem não sabe programar, como baixar o modelo microsoft/BitNet-b1.58-2B-4T-gguf pela plataforma de modelos de código aberto Hugging Face, prepará-lo com o 'setup_env.py' e, por fim, iniciar o modo de chat com o script 'run_inference.py'.

Repositório: https://github.com/microsoft/BitNet. Baseie-se nas instruções oficiais no arquivo README deste repositório para a instalação e execução.

Antes de começar, verifique em qual sistema operacional estamos e se as ferramentas necessárias (ex: Python, Node.js, Git, Docker) estão instaladas. Instale as que faltarem passo a passo de acordo com este sistema.

Crie uma pasta nova e vazia para trabalhar. Não toque em arquivos fora desta pasta e não exclua nada. Antes de executar cada comando, diga o que você vai fazer em uma frase.

Diga-me o que devo ver na tela ao final de cada etapa. Se ocorrer um erro, colarei a mensagem de erro para você exatamente como ela é, e vamos corrigi-la juntos.

## Termos relacionados do glossário

- [Inference Framework](https://trescout.com/pt/dictionary/inference-framework/)
- [Inference](https://trescout.com/pt/dictionary/inference/)
- [Clone](https://trescout.com/pt/dictionary/clone/)
- [Framework](https://trescout.com/pt/dictionary/framework/)
- [Open Source](https://trescout.com/pt/dictionary/open-source/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** Destina-se a usuários que desejam executar modelos de linguagem rápidos e leves no próprio processador do computador, sem a necessidade de placas de vídeo potentes.
- **Licença:** MIT

## Links

- [Repositório no GitHub →](https://github.com/microsoft/BitNet)
- [Ler em turco →](https://trescout.com/discover/bitnet/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-10-12: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. O texto de apresentação foi preparado com IA a partir da própria documentação do repositório e esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/bitnet/
