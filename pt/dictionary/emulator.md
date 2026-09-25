# O que é um Emulador (Emulator)?

> Inglês: Emulator · Etimologia: latim aemulari (imitar, rivalizar)

**Categoria:** Dev  
**Última atualização:** 2026-09-19

Um emulador (emulator) é um software que reproduz virtualmente a arquitetura de hardware, barramentos, registradorez e conjunto de instruções de uma máquina específica, permitindo rodar seus softwares originais em outro computador.

## Conceito, etimologia e diferença para simulador
A palavra deriva do latim aemulari, que traduz o ato de imitar com perfeição. Enquanto um simulador reproduz o comportamento externo de um sistema (como um simulador de vôo imitando a física do avião), o emulador recria a mecânica eletrônica interna: ciclo de registradores, chips de áudio e memória de vídeo.

## Arquitetura do emulador e o ciclo Fetch-Decode-Execute
A espinha dorsal do emulador é uma CPU virtual que traduz instruções :
- **Emulação por Interpretador:** Lê cada instrução convidada, decodifica seu significado e a executa no processador hospedeiro. Fiel, porém consome muita CPU.- **Tradução Binária Dinâmica (JIT):** Recompila blocos inteiros de código estrangeiro em instruções nativas do computador atual, armazenando-as em cache para ganho de velocidade.- **Emulação com Precisão de Ciclo:** Sincroniza cada componente eletrônico ciclo a ciclo para preservar efeitos de hardware originais.

## Aplicações em desenvolvimento e segurança
Usos fundamentais da emulação na tecnologia :
- **Testes Mobile:** Emuladores de Android no computador para verificar layouts e funcionalidades em dezenas de aparelhos.- **Pesquisa de Malware:** Executar códigos maliciosos dentro de máquinas QEMU isoladas para estudar suas táticas sem contaminar o sistema real.- **Preservação Digital:** Manter softwares históricos de bancos ou consoles antigos acessíveis em servidores modernos.

## Legislação e direitos autorais
A jurisprudência internacional (como no processo histórico Sony vs. Connectix) consagrou que desenvolver emuladores via engenharia reversa limpa é perfeitamente legal. A ilegalidade reside apenas na pirataria de BIOS protegidas e cópias não autorizadas de jogos (ROMs).

## Por analogia
Para ler um livro em idioma estrangeiro: o simulador é um guia que resume a história; o emulador interpretador traduz palavra por palavra com dicionário; o recompilador JIT traduz capítulos inteiros para o seu idioma antes da leitura, permitindo ler com máxima velocidade.

## Perguntas frequentes

**Qual a diferença entre emulador e máquina virtual?**  
A máquina virtual executa código nativo na mesma arquitetura de processador; o emulador traduz comandos de uma arquitetura de CPU totalmente diferente através de software.

**Desenvolver emuladores é uma prática legal perante a lei?**  
Sim; recriar o funcionamento de um hardware por engenharia reversa é permitido, desde que o código de BIOS original da fabricante não seja redistribuído.

**Por que emular consoles antigos às vezes exige computadores potentes?**  
Porque emuladores com precisão de ciclo exigem milhões de ciclos da CPU moderna para reproduzir com exatidão matemática cada microssegundo do hardware clássico.

**O que é o QEMU?**  
Uma ferramenta clássica de código aberto capaz de emular sistemas inteiros para arquiteturas como ARM, MIPS, RISC-V e x86.

## Termos relacionados
- [ROM](/pt/dictionary/rom/)
- [Virtual Machines](/pt/dictionary/virtual-machines/)
- [Apple Silicon](/pt/dictionary/apple-silicon/)

---
Fonte: Dicionário Técnico TreScout · https://trescout.com/pt/dictionary/emulator/
