# Testes unitários padrão da indústria para projetos em C++

O GoogleTest e o GoogleMock são a estrutura de teste de código aberto padrão da indústria que permite executar testes unitários, objetos falsos (mocks) e testes parametrizados em projetos modernos em C++.

- ★ 39.588
- C++
- GitHub Trending · 2026-08-27

## O que você ganha
- Ricas de Asserções: Diagnóstico claro de erros com as macros ASSERT_* (erro crítico, encerra o teste) e EXPECT_* (registra o erro, continua o fluxo de testes).
- Infraestrutura avançada de Mock (GoogleMock): Capacidade de simular facilmente interfaces com MOCK_METHOD para isolar dependências e definir expectativas de chamadas.
- Capacidade de teste paramétrico: A capacidade de repetir automaticamente a mesma lógica de teste em dezenas de entradas e conjuntos de dados diferentes com um único modelo.
- Multiplataforma e segurança de threads: arquitetura thread-safe em ambientes Linux, macOS e Windows e validação de cenários de falha com testes de morte (death tests).
- Integração de CI/CD e relatórios: integração perfeita com pipelines do GitHub Actions, Jenkins e GitLab CI usando formatos de saída XML e JSON compatíveis com JUnit.

## Instalação
**Adição ao projeto com CMake FetchContent**

```
include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/refs/tags/v1.15.2.tar.gz
)
FetchContent_MakeAvailable(googletest)
```


## Execução
**Compilação do teste e execução com CTest**

```
cmake -B build -S .
cmake --build build
ctest --test-dir build --output-on-failure
```


## Arquitetura técnica e princípio de funcionamento
- Gerenciamento de Test Fixture e Ciclo de Vida: Os procedimentos SetUp e TearDown gerenciam com segurança os recursos de memória antes e depois de cada teste.
- Isolamento de Processos para Testes de Morte (Death Tests): Captura o encerramento inesperado do programa ou a geração de asserts em processos filhos isolados por meio de um mecanismo de fork.
- Modelos de Testes Parametrizados por Tipo: Oferece infraestrutura de testes Type-Parameterized para testar classes com gabarito (templates C++) com diferentes tipos de dados de uma só vez.

## Cenários de teste e integração com o GoogleMock
- Abstração de Chamadas de Banco de Dados e de Rede: Simule respostas de API esperadas e latências sem estabelecer conexões de rede reais usando MOCK_METHOD.
- Contagem de Chamadas e Validação de Parâmetros: Verifique quantas vezes, com quais argumentos e em que ordem uma função é chamada usando a macro EXPECT_CALL.
- Análise de Cenários de Lançamento de Erros: garanta a resiliência testando blocos de código que lançam exceções (throw) com as macros EXPECT_THROW.

## Se você não programa
Gostaria de escrever testes unitários para uma classe de analisador (parser) de dados usando GoogleTest e GoogleMock em um projeto C++ moderno. Poderia explicar com exemplos de código como configurar meu arquivo CMakeLists.txt, um exemplo de fixture de teste TEST_F e como criar um objeto mock com MOCK_METHOD e validar expectativas de chamada?

## Perguntas frequentes
- Qual é a maneira mais moderna de incluir o GoogleTest em um projeto? Em projetos CMake modernos, o mecanismo FetchContent é a abordagem mais recomendada. Ele baixa o código-fonte e o integra ao processo de compilação de destino sem a necessidade de um gerenciador de pacotes externo.
- Qual é a principal diferença entre EXPECT_* e ASSERT_*? As macros EXPECT_* registram o erro quando falham, mas permitem que o restante da função continue sendo executado. Já a ASSERT_* sai imediatamente da função de teste atual em caso de erro.
- O GoogleMock é uma biblioteca separada? O GoogleMock era originalmente um projeto separado, mas há muito tempo foi integrado sob o mesmo teto com o repositório do GoogleTest; ambos são instalados e usados juntos.
- Oferece segurança de thread? Sim. O GoogleTest é executado de forma thread-safe em sistemas que suportam pthreads e no Windows; ele sincroniza corretamente notificações simultâneas vindas de múltiplas threads.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/googletest/
