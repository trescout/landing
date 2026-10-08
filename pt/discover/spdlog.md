# Registro rápido para projetos C++

spdlog é uma biblioteca de log ultrarrápida desenvolvida para a linguagem de programação C++, que pode ser usada apenas como cabeçalho ou como uma biblioteca compilada. Ele oferece gerenciamento de saída de alto desempenho e sem atrasos em projetos de software usando padrões C++ modernos.

- ★ 29.437
- C++
- GitHub Trending · 2026-08-05

## Atualizações

- **6 de agosto de 2026:** Estrelas 29,402 → 29,437, versão mais recente v1.17.0 (4 de janeiro de 2026).

## O que você ganha

- Desempenho de registro de milhões de linhas por segundo: Cria latência em nível de microssegundos no thread principal do aplicativo com uma abordagem de alocação zero de memória e otimizações de tempo de compilação.
- Fila em anel assíncrona e sem bloqueio: isola completamente gargalos de E/S de arquivo ou rede do pipeline de chamada, descarregando gravações de log no pool de segundo plano.
- Rica variedade de alvos: saída colorida do console, arquivos girando por tamanho, arquivos com datas diárias, gravação simultânea em syslog e alvos de logcat do Android.
- Poder de formatação fmt integrado: fornece formatação de texto segura, rápida e flexível no estilo Python usando a biblioteca {fmt}, que é a base do padrão de formatação C++20.
- Flexibilidade de uso somente de cabeçalho ou compilado: você pode incluí-lo em seu projeto copiando um único diretório ou vinculá-lo como uma biblioteca estática para reduzir o tempo de compilação.

## Instalação

**macOS (Homebrew)**

```
brew install spdlog
```

## Como começar e uso básico

Começar a usar a biblioteca spdlog é extremamente fácil. Depois de incluir o arquivo de cabeçalho em seu projeto, você pode chamar funções de registro global diretamente ou criar objetos de registro personalizados:

## Arquitetura técnica e princípio de funcionamento

- Distinção entre Logger e Sink: O objeto Logger filtra o log de entrada (rastreamento, depuração, informação, aviso, erro, crítico). As mensagens aceitas são transferidas para um ou mais objetos Sink. Por exemplo, um único criador de logs pode gravar no arquivo no formato JSON e, ao mesmo tempo, imprimir cores no console.
- Thread-safe (_mt vs _st): spdlog provides all sink classes in two forms: multi-thread-safe mutex-locking (_mt) and single-thread-specific lock-free (_st) versions. No modo single-threaded, o custo do mutex é completamente zero.
- Fila de anel assíncrona (Ring Buffer): O bloco de memória alocado com spdlog::init_thread_pool é consumido pelo thread em execução em segundo plano. A aplicação principal deixa o log na fila e segue seu caminho imediatamente.
- Liberação inteligente de buffer (Flush): Os dados são mantidos no buffer do sistema operacional para desempenho; No entanto, o mecanismo spdlog::flush_on(spdlog::level::err) pode ser acionado para evitar perda de dados em momentos de erro críticos.

## Se você não programa

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero configurar a biblioteca spdlog com arquitetura assíncrona usando CMake em um projeto C++ moderno. Você pode preparar o arquivo CMakeLists.txt com uma função de inicialização C++ de amostra que gira o arquivo quando o log atinge 10 MB de tamanho, também fornece saída colorida para o console e o libera no disco imediatamente após o nível de erro?

## Perguntas frequentes

- O spdlog deve ser usado apenas no cabeçalho ou compilado? Em projetos de pequeno e médio porte, utilizar header-only adicionando apenas o diretório include proporciona grande praticidade. No entanto, em grandes projetos C++ que consistem em centenas de arquivos de origem, é recomendável compilar e vincular a biblioteca ao sinalizador SPDLOG_COMPILED para otimizar o tempo de compilação.
- O registro afeta a velocidade de execução do aplicativo principal? Executando no nível de microssegundos, mesmo no modo síncrono, o spdlog reduz a carga de E/S no thread principal a quase zero ao usar a arquitetura do logger assíncrono. A mensagem é copiada para a fila e a gravação no disco ocorre em segundo plano.
- Como funciona o mecanismo de rotação de arquivos? Quando o tamanho máximo de arquivo especificado (por exemplo, 10 MB) for atingido, o arquivo ativo será arquivado (application.1.txt, application.2.txt) e um novo arquivo será aberto do zero. Quando o número máximo de arquivos especificado for excedido, o arquivo de log mais antigo será automaticamente apagado.
- Haverá um conflito com a biblioteca fmt externa? Não. O spdlog usa a versão empacotada internamente do fmt por padrão. Se desejar, você pode integrar diretamente a biblioteca fmt independente existente em seu sistema com spdlog definindo a macro SPDLOG_FMT_EXTERNAL.

## Termos relacionados do glossário

- [Logging](https://trescout.com/pt/dictionary/logging/)
- [Open Source](https://trescout.com/pt/dictionary/open-source/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** Para desenvolvedores C++, arquitetos de mecanismos de jogos e sistemas embarcados que desejam acelerar a depuração, o monitoramento e a verificação de projetos de software com latência zero.
- **Licença:** MIT Lisansı (Ticari ve açık kaynak projelerde tamamen serbest)
- **Padrão:** Compatível com C++11, C++14, C++17, C++20 e C++23
- **Tipo de biblioteca:** Vinculação estática/dinâmica somente de cabeçalho ou compilada

## Links

- [Repositório no GitHub →](https://github.com/gabime/spdlog)
- [Ler em turco →](https://trescout.com/discover/spdlog/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-08-05: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/spdlog/
