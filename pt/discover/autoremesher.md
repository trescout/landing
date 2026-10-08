# Quadratura automática para modelos tridimensionais

Autoremesher é uma ferramenta que converte automaticamente estruturas de superfície irregulares em modelos tridimensionais em remalhamento quádruplo. Desenvolvido em linguagem C++, este software é otimizado para tornar geometrias complexas adequadas para processos de animação e modelagem.

- ★ 3.322
- C++
- GitHub Trending · 2026-07-09

## Atualizações

- **24 de agosto de 2026:** Estrelas 3,225 → 3,322, versão mais recente 1.2.0 (23 de agosto de 2026).
- **17 de agosto de 2026:** Estrelas 3,087 → 3,225, versão mais recente 1.1.0 (16 de agosto de 2026).
- **2 de agosto de 2026:** Estrelas 2,123 → 3,087, versão mais recente 1.0.0 (6 de julho de 2026).

## O que você ganha

- Transforma modelos complexos em malhas retangulares limpas
- Fornece topologia otimizada para processos de animação
- Oferece suporte para processamento em lote via linha de comando

## Instalação

**Compilando no Linux**

```
# Install Qt and build tools
sudo apt install build-essential qt5-qmake qtbase5-dev qttools5-dev-tools libqt5svg5-dev libqt5multimedia5-dev

# Install TBB and OpenGL
sudo apt install libtbb-dev libgl1-mesa-dev

# Clone and build
git clone https://github.com/huxingyi/autoremesher.git
cd autoremesher
qmake
make -j$(nproc)
```

**Crie no macOS**

```
# Install Xcode Command Line Tools
xcode-select --install

# Install dependencies via Homebrew
brew install qt@5 tbb cmake

# Build
export PATH="/usr/local/opt/qt@5/bin:$PATH"
git clone https://github.com/huxingyi/autoremesher.git
cd autoremesher
qmake CONFIG+=sdk_no_version_check
make -j$(sysctl -n hw.logicalcpu)
```

## Se você não programa

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero converter o arquivo do modelo 3D que possuo em uma estrutura de malha retangular. Como posso processar meu arquivo de entrada com um número alvo especificado de quadriláteros, escala de arestas e configurações de arestas vivas usando a ferramenta Autoremesher? Crie um exemplo de configuração que eu possa usar por meio da linha de comando.

## Termos relacionados do glossário

- [Quad Remeshing](https://trescout.com/pt/dictionary/quad-remeshing/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** Para artistas e desenvolvedores que necessitam de edição de topologia em processos de modelagem e animação 3D.
- **Licença:** MIT

## Links

- [Repositório no GitHub →](https://github.com/huxingyi/autoremesher)
- [Ler em turco →](https://trescout.com/discover/autoremesher/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-07-09: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/autoremesher/
