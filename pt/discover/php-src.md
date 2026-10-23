# Linguagem de script para sites

O PHP é usado como uma linguagem de script de propósito geral projetada especificamente para processos de desenvolvimento web. Escrito em C, este interpretador forma a infraestrutura de muitos sites em todo o mundo.

- ★ 41.410
- C
- GitHub Trending · 2026-10-23

## Atualizações

- **23 de outubro de 2026:** Estrelas 41,391 → 41,410, versão mais recente php-8.5.12 (21 de outubro de 2026).

## O que você ganha

- Permite executar sites dinâmicos e aplicações web.
- Oferece a oportunidade de testar a versão mais recente compilando diretamente a partir do código-fonte.
- Ajuda a medir a estabilidade do sistema com ferramentas de teste integradas e abrangentes.

## Instalação

**Instalar ferramentas de compilação para o Ubuntu**

```
sudo apt install -y pkg-config build-essential autoconf bison re2c libxml2-dev libsqlite3-dev
```

**Instalar ferramentas de compilação para o Fedora**

```
sudo dnf install re2c bison autoconf make ccache libxml2-devel sqlite-devel
```

## Execução

**Compilar o código-fonte**

```
make -j4
```

**Executar os testes**

```
make TEST_PHP_ARGS=-j4 test
```

## Se você não programa

Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero compilar o interpretador PHP a partir do código-fonte e testá-lo. Se eu estiver usando o Ubuntu, execute o comando sudo apt install -y pkg-config build-essential autoconf bison re2c libxml2-dev libsqlite3-dev para instalar as ferramentas de compilação necessárias através do gerenciador de pacotes. Se eu estiver usando o Fedora, execute o comando sudo dnf install re2c bison autoconf make ccache libxml2-devel sqlite-devel e, se eu estiver usando o macOS, use o gerenciador de pacotes Homebrew com o comando brew install autoconf bison re2c libiconv libxml2 sqlite. Em seguida, execute o comando make -j4 para compilar o projeto. Após a conclusão da compilação, aplique o comando make TEST_PHP_ARGS=-j4 test para executar os testes concorrentemente ou make TESTS=tests/lang/ test para executar os testes de linguagem.

Repositório: https://github.com/php/php-src. Baseie-se nas instruções oficiais no arquivo README deste repositório para a instalação e execução.

Antes de começar, verifique em qual sistema operacional estamos e se as ferramentas necessárias (ex: Python, Node.js, Git, Docker) estão instaladas. Instale as que faltarem passo a passo de acordo com este sistema.

Crie uma pasta nova e vazia para trabalhar. Não toque em arquivos fora desta pasta e não exclua nada. Antes de executar cada comando, diga o que você vai fazer em uma frase.

Diga-me o que devo ver na tela ao final de cada etapa. Se ocorrer um erro, colarei a mensagem de erro para você exatamente como ela é, e vamos corrigi-la juntos.

## Termos relacionados do glossário

- [Scripting Language](https://trescout.com/pt/dictionary/scripting-language/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** Destinado a desenvolvedores que criam aplicações web e desenvolvedores que desejam inspecionar o código principal do PHP e compilá-lo diretamente a partir da fonte.
- **Licença:** BSD-3-Clause

## Links

- [Repositório no GitHub →](https://github.com/php/php-src)
- [Ler em turco →](https://trescout.com/discover/php-src/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-10-23: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. O texto de apresentação foi preparado com IA a partir da própria documentação do repositório e esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/php-src/
