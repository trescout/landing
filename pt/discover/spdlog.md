# Biblioteca rápida de logging para projetos em C++

O spdlog é uma biblioteca de logging ultrarrápida para C++, disponível como biblioteca header-only ou pré-compilada. Projetada com padrões modernos de C++, garante registros de alto desempenho e latência zero.

- ★ 29.437
- C++
- GitHub Trending · 2026-08-05

## Atualizações
- 6 de agosto de 2026: Estrelas 29.402 → 29.437, versão mais recente v1.17.0 (4 de janeiro de 2026).

## O que você ganha
- Milhões de linhas por segundo de vazão: Arquitetura de alocação zero para gerar impacto quase nulo na thread chamadora.
- Fila circular assíncrona e lock-free: Transfere a gravação em disco para um pool de threads, evitando travamentos de I/O.
- Diversidade de destinos (sinks): Escreva simultaneamente no console colorido, arquivos rotativos por tamanho, syslog e Android logcat.
- Poder integrado da biblioteca {fmt}: Utiliza a base do C++20 format para interpolação segura, veloz e elegante de strings.
- Flexibilidade header-only ou compilada: Copie uma pasta para seu projeto ou compile estaticamente para acelerar builds.

## Instalação

**macOS (Homebrew)**

```
brew install spdlog
```

**Gerenciador vcpkg**

```
vcpkg install spdlog
```

**Integração CMake FetchContent**

```
include(FetchContent)
FetchContent_Declare(
  spdlog
  GIT_REPOSITORY https://github.com/gabime/spdlog.git
  GIT_TAG v1.17.0
)
FetchContent_MakeAvailable(spdlog)
target_link_libraries(meu_projeto PRIVATE spdlog::spdlog)
```

Source: Fórmula do Homebrew

## Como começar e uso básico

Começar a usar o spdlog é simples. Após incluir o cabeçalho, chame funções globais diretamente ou instancie loggers dedicados:

**Exemplo básico em C++**

```
#include "spdlog/spdlog.h"
#include "spdlog/sinks/rotating_file_sink.h"

int main() {
    // Logging padrão no console
    spdlog::info("spdlog inicializado com sucesso.");
    spdlog::warn("Aviso: consumo de memoria aumentando!");
    spdlog::error("Codigo de erro: {:d}, mensagem: {}", 404, "Pagina nao encontrada");

    // Logger com arquivo rotativo (max 5MB, 3 arquivos)
    auto file_logger = spdlog::rotating_logger_mt("file_logger", "logs/app.txt", 1024 * 1024 * 5, 3);
    file_logger->info("Esta mensagem e thread-safe e arquivada automaticamente.");

    return 0;
}
```

## Arquitetura técnica e funcionamento interno

A velocidade recorde do spdlog é fruto de um design modular com sobrecarga zero:
- Separação entre Logger e Sink: O logger filtra por severidade e encaminha para um ou múltiplos destinos de saída.
- Segurança entre threads (_mt vs _st): Classes sink possuem variantes com mutex (_mt) e lock-free monothread (_st).
- Buffer circular assíncrono: O pool de threads consome a fila em background sem travar a lógica do software.
- Descarga inteligente (Flush): Buffers do sistema são despejados imediatamente em caso de erro crítico via spdlog::flush_on.

## Se você não programa
🤖 Se você não programa
Quero configurar o spdlog em um projeto moderno de C++ com CMake usando arquitetura assíncrona. Você pode me fornecer uma função de inicialização e um CMakeLists.txt configurando saída colorida no console, arquivo rotativo de 10MB e flush imediato em erros?

- **Para quem:** Desenvolvedores C++, criadores de games e sistemas embarcados que exigem latência ultra baixa.
- **Licença:** MIT (Código aberto permissivo)
- **Integração:** Header-only ou biblioteca estática
- **Padrões:** C++11, C++14, C++17, C++20

## Perguntas frequentes
- Por que usar spdlog em vez de printf ou std::cout? O spdlog é ordens de grandeza mais veloz, thread-safe, oferece níveis de log estruturados e suporta I/O assíncrono.
- É possível registrar objetos de classes próprias? Sim, basta sobrecarregar o operator<< ou especializar o fmt::formatter para seus tipos.
- É adequado para jogos e trading de alta frequência? Sim, com sinks assíncronos a gravação de logs ocorre em nanossegundos sem engasgar o loop principal.
- Suporta saída estruturada em JSON? Sim, é possível configurar padrões de formatação JSON para exportar para Loki, Datadog ou Elasticsearch.

## Links
- [GitHub →](https://github.com/gabime/spdlog)
- [Read in Turkish →](https://trescout.com/discover/spdlog/)

## Termos relacionados do glossário
Logging Logs Runtime Memory Management

---
Source: TreScout Discover · https://trescout.com/pt/discover/spdlog/
