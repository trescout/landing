# O que é On-device STT?

> Reconhecimento de Voz no Próprio Dispositivo

**Categoria:** AI  
**Última atualização:** 2026-09-22

On-device STT (Speech-to-Text no dispositivo) refere-se ao reconhecimento de fala que processa e converte áudio em texto diretamente no hardware do usuário, sem trafegar gravações sonoras para servidores em nuvem.

## Definição e etimologia
Motivado pela proteção de dados e pela necessidade de digitação sem atrasos, o STT local processa ondas sonoras diretamente em NPUs e aceleradores neurais locais. O áudio do microfone nunca é transmitido pela internet.

## Contexto cotidiano e uso prático
- **Dispositivos Móveis:** Ditado contínuo em mensageiros mesmo em viagens ou locais sem sinal de celular.
- **Consultórios e Escritórios:** Degravação sigilosa de depoimentos jurídicos e prontuários médicos.
- **Assistentes Residenciais:** Caixas de som inteligentes que entendem comandos sem monitorar a rotina da casa.

## Profundidade técnica e arquitetura
Mecanismos Arquiteturais:- **Modelos Quantizados:** Redes neurais compactas (Whisper.cpp, Vosk) convertidas para 4 ou 8 bits sem perda perceptível de acurácia.
- **Processamento em NPU:** Execução nativa em silício especializado (Apple Neural Engine, Qualcomm AI Engine) poupando a bateria.
- **Detecção Ativa de Voz (VAD):** Algoritmos leves que descartam silêncio antes do acionamento dos módulos de linguagem.

## Costuma ser confundido com
Frequentemente confundido com APIs de voz baseadas em nuvem. A nuvem depende de conexão e servidores de terceiros; o STT no dispositivo trabalha com total autonomia e privacidade inviolável.

## Perspectivas interdisciplinares
- **Tradução:** Ter um intérprete ao seu lado na sala de reuniões vs fazer chamada telefônica para um serviço internacional.
- **Taquigrafia:** Um escrivão registrando a sessão presencialmente vs enviar fitas para transcrição externa.
- **Revelação:** Ter um laboratório fotográfico próprio em casa vs enviar o rolo de filme pelo correio.

## Por analogia
É comparável a ter um tradutor presencial no mesmo ambiente: suas palavras viram texto imediatamente sem ninguém escutando pela linha telefônica.

## Perguntas frequentes

**A precisão do reconhecimento local é comparável à da nuvem?**  
Sim, arquiteturas destiladas modernas do Whisper alcançam precisão quase idêntica em fala cotidiana.

**O sistema funciona 100% desconectado?**  
Sim, todo o vocabulário e a rede neural ficam armazenados na memória interna do aparelho.

**Qual o consumo de armazenamento no celular ou PC?**  
Os modelos otimizados ocupam entre 40 MB e 350 MB de espaço.

**Quais são as ferramentas open source mais populares?**  
Whisper.cpp, Sherpa-ONNX, Vosk e WhisperX.

## Termos relacionados
- [Speech-to-Text](/pt/dictionary/speech-to-text/)
- [SLM](/pt/dictionary/slm/)
- [Privacidade Digital](/pt/dictionary/digital-privacy/)

---
Fonte: Dicionário Técnico TreScout · https://trescout.com/pt/dictionary/on-device-stt/
