# O que é Speaker Diarization?

A diarização de oradores (Speaker Diarization) é uma tecnologia de inteligência artificial que analisa ondas sonoras em uma gravação de áudio com múltiplos participantes para responder à pergunta "quem falou quando?" e rotular os segmentos de fala de acordo com as identidades dos oradores.

## Definição e Origem do Conceito (Definição de Diarização)
Diarization, cuja origem etimológica deriva do verbo francês "diariser" (manter um diário), é o processo na engenharia de áudio que consiste em dividir um fluxo de áudio em segmentos baseados no tempo, associando cada parte a uma identidade de locutor específica (por exemplo, Locutor 1, Locutor 2). Independentemente do conteúdo da fala, a distinção de identidade é feita diretamente através do timbre biométrico e das características de frequência do áudio.

## Como funciona? (Diarização passo a passo)
1. Detecção de Atividade de Voz (VAD - Voice Activity Detection): Música, ruído de fundo e pausas para respiração na gravação são eliminados, e apenas as partes que contêm voz humana são extraídas.

## Onde e em quais áreas é utilizado?
Assistentes de Reunião Inteligentes: Ferramentas de resumo por inteligência artificial (Otter.ai, Meetily) que extraem quem assumiu qual decisão ou tarefa em reuniões no Zoom, Google Meet ou Teams.Centrais de Atendimento: Análise de sentimento e controle de qualidade separando as conversas entre o cliente e o atendente.Transcrição de Podcasts e Entrevistas: Criação automática de legendas profissionais e separação de falantes em conteúdos de áudio e vídeo com múltiplos participantes.Direito e Computação Forense: Documentação de trocas de falantes em registros judiciais e interrogatórios de segurança.

## Costuma ser confundido com
A transcrição (Speech-to-Text ou STT) é frequentemente confundida com a diarização de locutor (Speaker Diarization). Um motor clássico de Speech-to-Text apenas converte "o que foi dito" em texto, mas não consegue distinguir quem falou. A diarização, por sua vez, identifica "quem falou". Por exemplo, enquanto o OpenAI Whisper realiza a transcrição pura, quando combinado com ferramentas como pyannote.audio ou WhisperX, é possível obter tanto o texto quanto as identidades dos locutores de forma completa.

## Perguntas frequentes
**Definição de diarização (o que significa diarização)?**
É um processo de inteligência artificial que, em gravações de áudio com múltiplos participantes, analisa as ondas sonoras para distinguir quem falou e quando, rotulando as transições entre locutores com carimbos de data/hora.

**O sistema consegue encontrar os nomes reais dos locutores por conta própria?**
Não, se uma amostra de voz não tiver sido previamente registrada, o sistema distingue os locutores como Locutor 1, Locutor 2, etc.; os nomes precisam ser associados pelo usuário ou por um sistema de calendário integrado.

**O modelo Whisper consegue realizar a diarização sozinho?**
Não, os modelos oficiais do Whisper realizam apenas a transcrição; para a separação de locutores, eles são utilizados em conjunto com modelos de diarização especializados, como o pyannote.audio.

**Qual é a situação em que os sistemas de diarização têm mais dificuldade?**
É realizar a distinção correta em situações onde várias pessoas falam ao mesmo tempo (fala sobreposta), as palavras se misturam ou em ambientes com eco.


## Termos relacionados
- [Transcription](/pt/dictionary/transcription/)
- [Speech-to-Text](/pt/dictionary/speech-to-text/)
- [NLP](/pt/dictionary/nlp/)

## Ferramentas relacionadas
- [Meetily](/pt/discover/meetily/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/speaker-diarization/
