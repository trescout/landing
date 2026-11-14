# Motor de inteligência artificial local TensorFold

O ashhart/TensorFold oferece um mecanismo de inferência compatível com Metal, CUDA e Vulkan para modelos de linguagem grande (LLMs). Desenvolvido em Zig, esta ferramenta permite executar modelos diretamente em processadores gráficos Apple Silicon e NVIDIA, sem a necessidade de instalação de Python ou MLX.

- ★ 2.080
- Zig
- GitHub Trending · 2026-11-13

## Atualizações

- **14 de novembro de 2026:** Estrelas 1,998 → 2,080, versão mais recente v1.2.8 (13 de novembro de 2026).
- **13 de novembro de 2026:** Estrelas 1,996 → 1,998, versão mais recente v1.2.7 (11 de novembro de 2026).

## O que você ganha

- Executa modelos de linguagem grande diretamente em processadores gráficos Apple Silicon e NVIDIA.
- Fornece serviço através de arquivo binário sem a necessidade de instalação de Python ou MLX.
- Permite selecionar modelos e conversar através de um aplicativo web local.

## Instalação

**Instalação no Mac**

```
brew install ashhart/tensorfold/tensorfold
tensorfold pull mlx-community/Qwen3.5-2B-MLX-4bit@93760be4f1f69842a46bc13dbdc0f19e291392a3
tensorfold serve mlx-community/Qwen3.5-2B-MLX-4bit --name local-model --context 8192 --no-thinking
```

## Execução

**Enviando Solicitação**

```
curl -fsS http://127.0.0.1:8080/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{"model":"local-model","messages":[{"role":"user","content":"Say hello in one sentence."}],"max_tokens":128,"temperature":0}'
```

## Se você não programa

Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero instalar a ferramenta TensorFold no meu Mac com chip Apple Silicon, baixar o modelo Qwen3.5-2B e iniciar o servidor. Para isso, você precisa executar os seguintes comandos em ordem:

brew install ashhart/tensorfold/tensorfold
tensorfold pull mlx-community/Qwen3.5-2B-MLX-4bit@93760be4f1f69842a46bc13dbdc0f19e291392a3
tensorfold serve mlx-community/Qwen3.5-2B-MLX-4bit --name local-model --context 8192 --no-thinking

Em seguida, para verificar se o servidor está funcionando, você pode enviar uma solicitação com o seguinte comando:

curl -fsS http://127.0.0.1:8080/v1/chat/completions \
-H 'Content-Type: application/json' \
-d '{"model":"local-model","messages":[{"role":"user","content":"Say hello in one sentence."}],"max_tokens":128,"temperature":0}'

Repositório: https://github.com/ashhart/TensorFold. Baseie-se nas instruções oficiais no arquivo README deste repositório para a instalação e execução.

Antes de começar, verifique em qual sistema operacional estamos e se as ferramentas necessárias (ex: Python, Node.js, Git, Docker) estão instaladas. Instale as que faltarem passo a passo de acordo com este sistema.

Crie uma pasta nova e vazia para trabalhar. Não toque em arquivos fora desta pasta e não exclua nada. Antes de executar cada comando, diga o que você vai fazer em uma frase.

Diga-me o que devo ver na tela ao final de cada etapa. Se ocorrer um erro, colarei a mensagem de erro para você exatamente como ela é, e vamos corrigi-la juntos.

## Termos relacionados do glossário

- [Temperature](https://trescout.com/pt/dictionary/temperature/)
- [Application](https://trescout.com/pt/dictionary/application/)
- [Inference Engine](https://trescout.com/pt/dictionary/inference-engine/)
- [Apple Silicon](https://trescout.com/pt/dictionary/apple-silicon/)
- [Inference](https://trescout.com/pt/dictionary/inference/)
- [LLM](https://trescout.com/pt/dictionary/llm/)

- **Para quem é:** Destinado a desenvolvedores que desejam executar modelos de linguagem grande em processadores gráficos Apple Silicon ou NVIDIA sem instalar o Python.
- **Licença:** Apache-2.0

## Links

- [Repositório no GitHub →](https://github.com/ashhart/TensorFold)
- [Ler em turco →](https://trescout.com/discover/tensorfold/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-11-13: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. O texto de apresentação foi preparado com IA a partir da própria documentação do repositório e esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/tensorfold/
