# Estrutura de análise para engenharia reversa de software

Ghidra é uma estrutura abrangente de engenharia reversa de software (SRE) desenvolvida pela Agência de Segurança Nacional (NSA) e compartilhada como código aberto. Plataforma desenvolvida com núcleo Java e C++; Ele converte arquivos binários compilados em código-fonte, oferecendo aos pesquisadores de segurança descompilação avançada, análise simbólica e suporte multiarquitetura.

- ★ 79.733
- Java
- GitHub Trending · 2026-08-28

## O que você ganha
- Poderosos descompiladores C integrados: Convertendo código de máquina e instruções de montagem em sintaxe legível e de alto nível semelhante a C.
- Ampla gama de processadores e arquiteturas: suporte para x86, ARM, AArch64, MIPS, PowerPC, RISC-V, SPARC e centenas de arquiteturas de microcontroladores embarcados.
- Análise colaborativa multiusuário: anotação, nomenclatura de função e controle de versão simultâneos no mesmo arquivo binário com a infraestrutura do servidor Ghidra.
- Automação e análise Headless: Verificação automática de milhares de malware no servidor a partir da linha de comando, sem entrar na interface gráfica.
- Extensibilidade com Java e Python: personalize a análise com scripts, plug-ins e bibliotecas de tipos de dados personalizados.

## Requisitos de instalação e sistema
**Instalação do JDK 21 e Ghidra**

```
# macOS Homebrew ile kurulum:
brew install --cask ghidra

# Linux / Windows (Manuel arşivden başlatma):
# JDK 21 64-bit kurulu olmalıdır.
./ghidraRun          # Linux / macOS
ghidraRun.bat        # Windows
```


## Execução e análise de linha de comando sem cabeça
**Iniciando a interface gráfica**

```
./ghidraRun
```

**Executando análise automática sem cabeça**

```
analyzeHeadless /proje/dizini ProjeAdi -import hedef_dosya.bin -postScript GuvenlikAnalizi.py
```


## Arquitetura técnica: mecanismo de trenó e descompilador
- Linguagem de modelagem de processador Sleigh: Linguagem de descrição declarativa usada para introduzir um novo processador ou arquitetura de conjunto de instruções (ISA) no Ghidra.
- Camada de representação intermediária (IR) de código P: Executa fluxo de dados independente da arquitetura e análise de fluxo de controle, traduzindo todas as instruções do processador em uma linguagem intermediária comum (código P).
- Mecanismo de descompilador baseado em C++: mecanismo nativo de alto desempenho que simplifica gráficos de fluxo de controle, extrai tipos de variáveis ​​e reduz loops complexos para código C.

## Fluxos de trabalho de engenharia reversa e análise de vulnerabilidades
- Análise de malware (triagem de malware): Abrindo executáveis ​​suspeitos isoladamente e revelando chamadas de API ocultas, domínios C2 e chaves de criptografia.
- Comparação de arquivos binários (Program Diff): Detectando a vulnerabilidade fechada visualizando as diferenças entre dois arquivos antes e depois do patch de segurança.
- Análise de firmware: colocação de despejos de memória flash brutos de dispositivos IoT no mapa de memória e análise de funções do bootloader e do kernel.

## Se você não programa
Quero examinar um arquivo binário suspeito usando Ghidra. Você pode explicar passo a passo como abrir um novo projeto no Ghidra, importar o arquivo, executar a análise automática, examinar funções na janela do descompilador e detectar funções de API suspeitas chamadas?

## Perguntas frequentes
- Quais são as principais diferenças entre Ghidra e IDA Pro? Embora o IDA Pro tenha taxas de licenciamento comerciais e altas, o Ghidra é totalmente gratuito e de código aberto. Ghidra oferece descompiladores integrados para todas as arquiteturas e inclui um servidor de colaboração multiusuário.
- O Ghidra é seguro ao analisar malware? Sim, durante a análise estática o arquivo não é executado, apenas decodificado. Porém, é essencial para a segurança que a análise seja realizada em uma máquina virtual (VM) isolada.
- Como instalar o servidor Ghidra? Com o script svrAdmin no diretório do servidor incluído no pacote Ghidra, um servidor de equipe pode ser aberto na rede local em poucos minutos e privilégios de usuário podem ser atribuídos.
- Os scripts Python 3 podem ser executados no Ghidra? Embora Ghidra venha com Jython (Python 2.7) por padrão, ambientes Python 3 modernos e bibliotecas externas (NumPy, Capstone) podem ser usados ​​diretamente graças ao plugin PyGhidra.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/ghidra/
