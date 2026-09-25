# Suíte de engenharia reversa e análise de software

O Ghidra é uma suíte abrangente de engenharia reversa de software (SRE) de código aberto desenvolvida e lançada pela National Security Agency (NSA). Desenvolvido em Java com um descompilador de alto desempenho em C++, ele converte binários compilados em código compreensível e viabiliza análises de segurança profundas em dezenas de arquiteturas.

- ★ 78.142
- Java
- GitHub Trending · 2026-08-28

## Atualizações
- 17 de setembro de 2026: Estrelas 78.142, versão mais recente Ghidra_12.1.3_build (suporte a Java 21, melhorias no descompilador RISC-V e ARM64).

## O que você ganha
- Descompilador C integrado e avançado: Transforma código de máquina e instruções assembly em pseudocódigo legível em C.
- Suporte abrangente a processadores: Compatível com x86, ARM, AArch64, MIPS, PowerPC, RISC-V, SPARC e centenas de microcontroladores.
- Trabalho colaborativo multiusuário: Equipes podem trabalhar no mesmo binário de forma simultânea com anotações e controle de versão via Ghidra Server.
- Análise headless automatizada: Execute varreduras de malware e auditorias em massa pela linha de comando sem abrir a interface gráfica.
- Extensibilidade via Java e Python: Desenvolva scripts personalizados, desempacotadores automáticos e analisadores de tipos de dados.

## Instalação e requisitos de sistema

**Instalação do JDK 21 e Ghidra**

```
# No macOS via Homebrew:
brew install --cask ghidra

# Linux / Windows (Início manual do arquivo de release):
# Exige JDK 21 64-bit instalado.
./ghidraRun          # Linux / macOS
ghidraRun.bat        # Windows
```

## Execução e análise headless por linha de comando

**Iniciar interface gráfica**

```
./ghidraRun
```

**Executar análise headless automatizada**

```
analyzeHeadless /diretorio/projeto NomeProjeto -import executavel.bin -postScript Auditoria.py
```

## Arquitetura técnica: Sleigh e motor descompilador

Os componentes fundamentais que transformaram o Ghidra em referência internacional incluem:
- Linguagem de especificação Sleigh: Linguagem descritiva usada para definir novos conjuntos de instruções e registradores de processadores.
- Representação intermediária P-Code: Normaliza todas as instruções em uma linguagem comum, permitindo analisar fluxos de dados sem depender da arquitetura.
- Motor descompilador nativo em C++: Elimina código morto, estrutura fluxos de controle e reconstrói tipos de variáveis de forma extremamente rápida.

## Fluxos de trabalho em engenharia reversa e análise de vulnerabilidades

O Ghidra é uma estação de trabalho indispensável para segurança ofensiva e defensiva:
- Análise de malwares (Malware Triage): Inspecione executáveis suspeitos para descobrir strings ofuscadas, servidores C2 e chamadas de API ocultas.
- Comparação de binários (Program Diff): Compare binários antes e depois de atualizações de segurança para entender a falha corrigida.
- Engenharia reversa de firmware: Mapeie dumps de memória flash de dispositivos IoT para inspecionar bootloaders e rotinas de sistema.

## Se você não programa
🤖 Se você não programa
Quero inspecionar um arquivo binário suspeito usando o Ghidra. Você pode me explicar passo a passo como criar um projeto, importar o arquivo, rodar o Auto Analysis, navegar pela janela do Decompiler e identificar chamadas a funções perigosas?

- **Para quem:** Analistas de malware, pesquisadores de vulnerabilidades, especialistas em engenharia reversa e desenvolvedores de firmware.
- **Licença:** Apache-2.0 (Licença permissiva de código aberto)
- **Desenvolvedor:** National Security Agency (NSA) e Comunidade Open Source
- **Requisitos:** Java Development Kit (JDK) 21 64-bit

## Perguntas frequentes
- Quais são as principais diferenças entre Ghidra e IDA Pro? Enquanto o IDA Pro é um software comercial com licenças caras por arquitetura, o Ghidra é totalmente gratuito, de código aberto, inclui descompiladores para todas as arquiteturas e conta com servidor colaborativo nativo.
- O Ghidra é seguro ao analisar códigos maliciosos? Sim, a análise estática apenas lê e desmonta os bytes sem executar o binário. Ainda assim, executar a análise dentro de uma máquina virtual isolada é uma prática recomendada.
- Como funciona o Ghidra Server? O script svrAdmin incluído no pacote permite configurar um servidor de colaboração local em poucos minutos, gerenciando acessos e repositórios da equipe.
- É possível usar scripts em Python 3 no Ghidra? Embora o Ghidra venha historicamente com Jython (Python 2.7), a extensão PyGhidra permite executar scripts nativos em Python 3 com acesso a bibliotecas externas como NumPy e Capstone.

## Links
- [GitHub →](https://github.com/NationalSecurityAgency/ghidra)

## Termos relacionados do glossário
Binary Open Source Local Offline

---
Source: TreScout Discover · https://trescout.com/pt/discover/ghidra/
