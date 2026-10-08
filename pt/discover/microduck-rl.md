# Ambiente de aprendizagem por reforço para o Microduck da Pollen Robotics

Desenvolvido pela Pollen Robotics, o microduck_rl oferece ambientes de treinamento de aprendizagem por reforço e políticas de controle no MuJoCo e mjlab para a plataforma robótica Microduck.

- ★ 2.281
- Python
- GitHub Trending · 2026-08-31

## Atualizações

- **27 de setembro de 2026:** Estrelas 1,001 → 2,281.

## O que você ganha

- Simulação física realista do MuJoCo: Capacidade de simular torques das juntas, atrito e efeitos da gravidade do robô em alta velocidade.
- Tarefas de locomoção e equilíbrio prontas para uso: funções de recompensa predefinidas para cenários de caminhada (walk), manutenção de equilíbrio e superação de obstáculos.
- Compatibilidade com transferência Sim-to-Real: políticas de controle resistentes a ruído facilmente transferíveis para o hardware físico Microduck.
- Algoritmos modernos de aprendizado por reforço: infraestrutura de treinamento com suporte a PPO (Proximal Policy Optimization) e SAC.
- Interface de avaliação visual 3D: Monitoramento em tempo real dos movimentos do agente robótico treinado em um simulador 3D na tela.

## Instalação

**Clonagem do repositório e configuração do ambiente de simulação**

```
git clone https://github.com/pollen-robotics/microduck_rl.git
cd microduck_rl
pip install -e .
```

## Execução

**Execução de treinamento ou avaliação de política**

```
python -m microduck_rl.train --task walk
# Eğitilen politikayı simülatörde izleme:
python -m microduck_rl.enjoy --checkpoint checkpoint.pt
```

## Arquitetura técnica e princípio de funcionamento

- Camada Física MuJoCo e mjlab: arquivos XML/MJCF que definem a cinemática do robô, limites de juntas e modelos de atuadores.
- Espaços de Observação e Ação Compatíveis com Gymnasium: Padronização de ângulos de motor, velocidades, dados de acelerômetro (IMU) e vetores de torque alvo.
- Mecanismo de Randomização de Domínio: Treinar modelos resistentes ao mundo real alterando aleatoriamente os coeficientes de atrito, a distribuição de massa e os ruídos dos sensores.

## Simulação física e políticas de controle robótico

- Prevenção de Danos ao Hardware: Elimine os riscos de queda e quebra das pernas do robô em um ambiente totalmente virtual antes de passar para o robô físico.
- Treinar milhões de passos em tempo acelerado: executar o motor de física 100 vezes mais rápido que o tempo real para concluir em horas um treinamento que levaria dias.
- Design de Missão Especial e Terreno: Teste a adaptação do robô a diferentes terrenos adicionando escadas, pisos inclinados e superfícies escorregadias.

## Se você não programa

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero treinar uma política de caminhada (walking) para o robô Microduck usando a biblioteca microduck_rl da Pollen Robotics. Você poderia explicar como configurar o ambiente MuJoCo, como iniciar o comando de treinamento com o algoritmo PPO e os passos para transferir a política de controle resultante para o robô físico?

## Perguntas frequentes

- É obrigatório possuir o robô físico Microduck para executar o microduck_rl? Não. A base de código pode ser executada inteiramente de forma virtual no simulador MuJoCo; você pode visualizar a simulação 3D do robô no seu computador.
- O suporte a GPU é necessário? O MuJoCo também funciona muito bem na CPU; no entanto, ao realizar treinamento de aprendizado por reforço com ambientes paralelos, uma GPU com suporte a CUDA acelera o processo significativamente.
- Como o modelo treinado é transferido para o robô físico? Quando o treinamento é concluído, o arquivo ONNX ou o checkpoint do PyTorch gerado é carregado no computador de controle integrado do Microduck e conectado diretamente aos torques dos motores.
- Suporta diferentes modelos de robôs? O microduck_rl foi otimizado principalmente para o Microduck; no entanto, graças à sua estrutura modular, pode ser adaptado para modelos MJCF de robôs bípedes ou quadrúpedes semelhantes.

## Termos relacionados do glossário

- [Reinforcement Learning](https://trescout.com/pt/dictionary/reinforcement-learning/)
- [CPU](https://trescout.com/pt/dictionary/cpu/)
- [GPU](https://trescout.com/pt/dictionary/gpu/)
- [API](https://trescout.com/pt/dictionary/api/)
- [Open Source](https://trescout.com/pt/dictionary/open-source/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** Pesquisadores de robótica, engenheiros mecatrônicos, especialistas em aprendizado por reforço e entusiastas.
- **Licença:** Apache-2.0 (Açık kaynak lisansı)
- **Framework:** Python, MuJoCo & Framework Robótico mjlab
- **Plataformas:** Linux, macOS, Windows

## Links

- [Repositório no GitHub →](https://github.com/pollen-robotics/microduck_rl)
- [Ler em turco →](https://trescout.com/discover/microduck-rl/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-08-31: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/microduck-rl/
