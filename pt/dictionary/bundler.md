# O que é Bundler?

Bundler (empacotador de módulos) é uma ferramenta de desenvolvimento que analisa códigos-fonte divididos em centenas de partes independentes (JavaScript, TypeScript, CSS, HTML, ativos de fontes e imagens) e dependências de bibliotecas externas no ecossistema moderno de desenvolvimento web e de software, transformando esses ativos em pacotes de arquivos otimizados (bundles) que os navegadores podem executar da maneira mais rápida e eficiente.

## O que é um Bundler e por que ele surgiu?
Nos primeiros anos da web, os sites consistiam em apenas algumas tags <script> adicionadas sequencialmente ao HTML. No entanto, à medida que as aplicações web se tornaram tão complexas quanto os softwares de desktop e se transformaram em bases de código gigantescas compostas por milhares de módulos, surgiram sérios obstáculos estruturais:

## Como Funciona um Bundler? Arquitetura Profunda
O funcionamento de um empacotador moderno consiste fundamentalmente em três fases:

## Técnicas Críticas de Otimização

## Comparação do Ecossistema de Empacotadores
As ferramentas de destaque que respondem a diferentes necessidades no ecossistema web são as seguintes:

## Perguntas frequentes
**O que é um Bundler e por que ele é obrigatório no desenvolvimento web moderno?**
Bundler é a ferramenta que transforma centenas de arquivos-fonte modulares, imagens e arquivos de estilo escritos pelo desenvolvedor em pacotes que o navegador pode processar de forma única e otimizada. É considerado obrigatório em projetos modernos para otimização do tamanho do arquivo, redução de requisições de rede e compatibilidade com o navegador.

**Qual é a principal diferença entre Webpack e Vite?**
O Webpack compila todo o projeto mesmo no ambiente de desenvolvimento e cria um único pacote na memória; à medida que o projeto cresce, o tempo de inicialização aumenta. O Vite, por outro lado, utiliza o suporte nativo a Módulos ES (Native ESM) do navegador no ambiente de desenvolvimento e compila os arquivos instantaneamente apenas quando o navegador os solicita, abrindo assim de forma imediata, independentemente do tamanho do projeto.

**O que é Tree-shaking e por que ele funciona apenas em Módulos ES?**
Tree-shaking é a remoção de funções e blocos de código nunca utilizados no projeto do pacote final. Este processo só pode ser realizado com segurança no formato ESM, que possui sintaxe estática como import e export; a análise completa de códigos CommonJS (require()) chamados dinamicamente não é possível na fase de compilação.

**Qual é a diferença entre um Transpiler (Babel, SWC) e um Bundler?**
Um Transpiler apenas transforma a sintaxe do código (por exemplo, converte código TypeScript moderno ou ES6+ para ES5). Já o Bundler une esses arquivos independentes transformados, resolvendo as relações de dependência entre eles e empacotando-os sob uma única estrutura.

**Para que serve o Code splitting (divisão de código)?**
Permite que o código da aplicação seja dividido em arquivos fragmentados em vez de um único arquivo grande. O usuário baixa apenas o código da página que está visualizando no momento, o que reduz significativamente o tempo de carregamento inicial e melhora a experiência do usuário.


## Termos relacionados
- [Bundling](/pt/dictionary/bundling/)
- [Compilation](/pt/dictionary/compilation/)
- [Frontend Stack](/pt/dictionary/frontend-stack/)
- [Runtime](/pt/dictionary/runtime/)

## Ferramentas relacionadas
- [Webpack](/pt/discover/webpack/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/bundler/
