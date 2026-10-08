# Configurar saídas de IA

A biblioteca Outlines permite que as respostas de grandes modelos de linguagem sejam apresentadas como saídas estruturadas de acordo com esquemas predefinidos. Com esta ferramenta baseada em Python, os desenvolvedores protegem a integridade dos dados restringindo as saídas do modelo com expressões regulares ou regras gramaticais livres de contexto.

- ★ 15.525
- Python
- GitHub Trending · 2026-07-22

## Atualizações

- **7 de agosto de 2026:** Estrelas 15,477 → 15,525, versão mais recente 1.3.3 (6 de agosto de 2026).
- **2 de agosto de 2026:** Estrelas 14,917 → 15,477, versão mais recente 1.3.2 (20 de julho de 2026).

## O que você ganha

- Restringe as saídas do modelo de acordo com esquemas predefinidos
- Totalmente compatível com tipos de dados JSON ou Python
- Elimina a necessidade de depurar saídas erradas

## Instalação

**Instale a biblioteca**

```
pip install outlines
```

## Execução

**Conecte o modelo**

```
import outlines
from transformers import AutoTokenizer, AutoModelForCausalLM


MODEL_NAME = "microsoft/Phi-3-mini-4k-instruct"
model = outlines.from_transformers(
    AutoModelForCausalLM.from_pretrained(MODEL_NAME, device_map="auto"),
    AutoTokenizer.from_pretrained(MODEL_NAME)
)
```

## Se você não programa

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero restringir a resposta de um modelo de IA a uma estrutura de dados Pydantic específica ou tipo Python (por exemplo, int ou Literal) usando a biblioteca Outlines. Como posso usar a função model(request, output_type) depois de definir o objeto do modelo para garantir que a saída do modelo sempre esteja em conformidade com o esquema desejado? Explique com um exemplo como definir o modelo Pydantic para objetos complexos e aplicar essa estrutura à saída do modelo.

## Termos relacionados do glossário

- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** É para desenvolvedores que desejam converter saídas de texto irregulares de modelos de IA em dados estruturados que podem ser usados ​​diretamente em processos de software.
- **Licença:** Apache-2.0

## Links

- [Repositório no GitHub →](https://github.com/dottxt-ai/outlines)
- [Ler em turco →](https://trescout.com/discover/outlines/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-07-22: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/outlines/
