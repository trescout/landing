# Sistema de radar phased array de código aberto

O PLFM RADAR é um sistema de radar phased array de código aberto operando na frequência de 10.5 GHz (banda X), com direcionamento eletrônico de feixe (electronic beam steering) e processamento digital de sinais em FPGA. Ele detecta e rastreia alvos aéreos e terrestres com alta precisão sem peças móveis.

- ★ 24.168
- C++
- GitHub Trending · 2026-08-18

## Atualizações
- 18 de agosto de 2026: Estrelas 24.168, versão estável v2.0.2-p0-audit (filtragem de sinal em FPGA e calibração de alcance).

## O que você ganha
- Direcionamento eletrônico de feixe: Varre um setor de 90 graus em milissegundos por meio de defasadores digitais sem desgaste mecânico.
- Operação em dois modos de alcance: Modo tático de 3 km para detecção de drones e modo de longo alcance de 20 km para vigilância perimetral.
- Processamento DSP em tempo real no FPGA: Execução acelerada por hardware de FFT bidimensional e detecção de alvos CFAR no próprio silício.
- Hardware acessível de baixo custo: Reduz o custo de centenas de milhares de dólares dos radares comerciais para menos de mil dólares.
- Integração com Python e SDR: Visualize trajetórias de alvos em tempo real com hardware SDR e uma tela de radar PPI em Python.

## Componentes de hardware e arquitetura do radar

O PLFM RADAR é estruturado em front-end de radiofrequência, matriz de antenas e camada de processamento digital:
- Matriz de antenas patch microstrip em 10.5 GHz: Elementos de antena de alta frequência projetados sobre substrato Rogers/FR4 de baixas perdas.
- Defasadores controlados digitalmente: Atrasam a fase de cada antena em passos de 5.6 graus para apontar o feixe de RF no espaço.
- Sintetizador de frequência FMCW: Oscilador local (VCO/PLL) de alta estabilidade gerando ondas contínuas moduladas em frequência.

## Processamento de sinais e software de controle

Os ecos do radar são filtrados em nível de hardware para extrair distância, velocidade radial e ângulo dos alvos:
- 2D FFT Distância-Doppler: Aplica transformadas de Fourier bidimensionais para resolver distância e velocidade simultaneamente.
- Detector CFAR (Taxa Constante de Falso Alarme): Adapta dinamicamente o limiar de decisão para separar alvos reais de ruídos e ecos do solo.
- Interface Python e monitor PPI: Projeta os vetores de rastreamento em uma tela de radar circular tradicional (PPI) sobre mapas.

## Princípio técnico de operação: FMCW e phased array

O PLFM RADAR utiliza a técnica de onda contínua modulada em frequência (FMCW) em vez de pulsos convencionais de alta potência:
- Medição de distância por frequência de batimento: Mistura o sinal chirp emitido com o eco recebido para produzir uma frequência proporcional à distância.
- Conformação de feixe por interferência construtiva: Controlar a fase relativa de cada antena força a onda a se somar construtivamente na direção desejada.

## Casos de uso e cenários de campo

A tecnologia de radar phased array de código aberto abre portas para variadas aplicações:
- Defesa antidrone em baixa altitude: Localiza pequenos drones sob neblina ou escuridão quando câmeras ópticas falham.
- Vigilância perimetral de instalações críticas: Monitora aproximação não autorizada de veículos ou pedestres em raios de 3 km de aeroportos e data centers.
- Pesquisas meteorológicas e atmosféricas: Mede correntes de vento locais e densidade de chuva por análise micro-Doppler.

## Se você não programa
🤖 Se você não programa
Quero entender os circuitos de 10.5 GHz e o processamento de sinal em FPGA do projeto PLFM RADAR. Você pode criar um script de simulação em Python que gere uma onda chirp FMCW, calcule a 2D FFT Distância-Doppler e extraia a distância e velocidade de um drone simulado?

- **Para quem:** Pesquisadores de radar, engenheiros de defesa, desenvolvedores de sistemas antidrone e entusiastas de RF/SDR.
- **Licença:** Licença de hardware e software de código aberto
- **Faixa de Frequência:** 10.5 GHz (Banda X) FMCW
- **Alcance Operacional:** 3 km (tático antidrone) a 20 km (vigilância ampla)

## Perguntas frequentes
- É possível fabricar este sistema em laboratório? Sim. Todos os esquemáticos, arquivos Gerber e códigos Verilog/VHDL para o FPGA estão abertos no GitHub. As placas podem ser produzidas em fabricantes de PCB convencionais.
- Qual a vantagem do phased array sobre antenas giratórias? O feixe eletrônico muda de direção em microssegundos em vez de segundos mecânicos, eliminando peças sujeitas a desgaste e permitindo rastrear múltiplos alvos ao mesmo tempo.
- É necessária autorização governamental para transmitir? A faixa de 10.5 GHz conta com alocações para radioamadores ou ISM em muitos países. Testes em bancada com baixa potência são comuns, mas transmissões externas de longo alcance exigem conformidade regulatória.
- Quais placas FPGA são suportadas? Placas baseadas em Xilinx Zynq-7000 e AMD UltraScale+ RFSoC são suportadas nativamente por meio de conectores FMC com placas de ADC/DAC rápidas.

## Links
- [GitHub →](https://github.com/NawfalMotii79/PLFM_RADAR)

## Termos relacionados do glossário
Edge Computing Open Source Local Offline

---
Source: TreScout Discover · https://trescout.com/pt/discover/plfm-radar/
