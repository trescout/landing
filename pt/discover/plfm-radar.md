# Radar phased array de código aberto

O PLFM RADAR é um sistema de radar de matriz de fase de código aberto que opera na frequência de 10,5 GHz (banda X), com capacidades de direcionamento eletrônico de feixe (electronic beam steering) e processamento digital de sinais baseado em FPGA. Ele detecta e rastreia alvos aéreos e terrestres com alta precisão, sem o uso de peças móveis mecânicas.

- ★ 25.440
- C++
- GitHub Trending · 2026-08-18

## O que você ganha
- Direcionamento eletrônico do feixe: varredura de um setor de 90 graus com deslocadores de fase em milissegundos, sem a necessidade de um motor mecânico ou antena rotativa.
- Modo de operação de alcance duplo: Capacidade operacional de 3 km em curto alcance (detecção de VANT/drone) e 20 km em longo alcance (vigilância perimetral e rastreamento de aeronaves).
- Processamento de sinal em tempo real baseado em FPGA: Processamento de hardware de ecos de radar brutos em FPGA com algoritmos FFT e CFAR de alta velocidade.
- Hardware acessível de baixo custo: reduzir o custo de radares comerciais e militares, que chega a centenas de milhares de dólares, para menos de mil dólares com projetos de PCB de código aberto.
- Integração de Python e SDR: Monitoramento em tempo real de dados de radar digital via hardware SDR de código aberto e interface Python.

## Componentes de hardware e arquitetura de radar
- Matriz de antenas de microfita de banda X de 10,5 GHz: Elementos de antena de patch múltiplo projetados em substratos Rogers/FR4 de baixa perda.
- Deslocadores de fase controlados numericamente: ICs de RF que direcionam o feixe no espaço atrasando a fase do sinal de cada elemento da antena com uma precisão de 5,6 graus.
- Sintetizador de frequência FMCW: Oscilador local de alta estabilidade (VCO/PLL) gerando onda contínua com modulação de frequência linear.

## Software de processamento de sinal e controlo
- Range-Doppler FFT (2D FFT): Cálculo simultâneo da distância do alvo e da velocidade radial aplicando primeiro o alcance e depois o Doppler FFT ao sinal de entrada.
- Detector CFAR (Constant False Alarm Rate): Separa alvos reais em movimento do ruído de fundo e ecos de solo (desordem) com limite dinâmico.
- GUI Python e tela PPI: Visualizando trilhas de alvo em um mapa ao vivo em uma tela de radar circular tradicional (PPI).

## Princípio de funcionamento técnico: FMCW e arranjo de fase
- Medição de distância a partir da diferença de frequência: A frequência de batimento é obtida misturando o sinal chirp enviado com o sinal retornando do alvo. Essa frequência é diretamente proporcional à distância.
- Focagem do feixe com interferência construtiva: Ao fornecer um certo atraso de fase a cada elemento da antena do conjunto, o sinal recebe interferência construtiva na direção desejada e interferência destrutiva em outras direções.

## Cenários de uso e testes de campo
- Defesa de UAV e Drones de baixa altitude: Detecção de pequenos veículos aéreos não tripulados em condições de neblina ou noturnas, onde as câmeras ópticas são inadequadas.
- Segurança perimetral de instalações críticas: Monitoramento de abordagens não autorizadas de pessoas ou veículos em um raio de 3 km em aeroportos, data centers e instalações industriais.
- Pesquisa meteorológica e atmosférica: Análise de movimentos de nuvens e intensidade de precipitação em escala local usando métodos micro-Doppler.

## Se você não programa
Gostaria de examinar os esquemas de hardware de matriz de fase de 10,5 GHz e os blocos de processamento de sinal FPGA do projeto PLFM RADAR. Você poderia preparar um script Python de simulação que explique a geração de sinal de chirp FMCW, o cálculo de FFT 2D de Alcance-Doppler e a transferência de dados para uma tela de radar PPI baseada em Python? Você poderia mostrar passo a passo o algoritmo de detecção de distância e velocidade para um alvo artificial?

## Perguntas frequentes
- É possível produzir o sistema em casa ou em laboratório? Sim. Todos os esquemas de PCB, arquivos de produção Gerber e códigos FPGA Verilog/VHDL do projeto estão disponíveis como código aberto no repositório GitHub. As placas podem ser encomendadas de fabricantes de PCB padrão e soldadas em ambiente de laboratório.
- Qual é a vantagem do direcionamento eletrônico do feixe sobre os radares mecânicos? Enquanto os radares mecânicos giram de 1 a 2 rotações por segundo, os radares phased array podem mudar a direção do feixe em microssegundos. Não há peças mecânicas desgastadas e pode travar vários alvos instantaneamente.
- É necessária uma licença especial de radiofrequência para operar? A banda de 10,5 GHz está sujeita a alocações de frequência de rádio amador ou industrial/científica (ISM) em muitos países. Embora testes em laboratório sejam permitidos em baixas potências de saída, as regulamentações locais devem ser observadas para transmissões externas de longo alcance.
- Com quais placas de desenvolvimento FPGA ele é compatível? A série Xilinx Zynq-7000 ou as modernas placas AMD UltraScale+ RFSoC são diretamente suportadas; Interfaces ADC/DAC de alta velocidade são conectadas através do conector FMC.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/plfm-radar/
