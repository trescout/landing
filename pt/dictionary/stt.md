# O que é STT?

*Glossário · AI · Última atualização: 19 de setembro de 2026*

> Speech-to-Text

STT (Speech-to-Text) é uma tecnologia de inteligência artificial e processamento de sinais que analisa a fala humana em ondas sonoras analógicas ou digitais e a converte em texto escrito com alta precisão.

## Origem conceitual, etimologia e desenvolvimento histórico

STT consiste nas iniciais da expressão inglesa Speech-to-Text. Em turco, é usado como "Fala para Texto", "Reconhecimento de Voz" ou "Transcrição de Voz".

A história da pesquisa sobre reconhecimento de fala é um dos problemas mais desafiadores da ciência da computação:

- 1952 (Sistema Audrey): O primeiro sistema desenvolvido nos Laboratórios Bell só conseguia reconhecer os números de 0 a 9 pronunciados por um único locutor.
- Décadas de 1970 a 1990 (Modelos Estatísticos e HMM): As ondas sonoras começaram a ser analisadas dividindo-as em fonemas (as menores unidades sonoras) com Modelos Ocultos de Markov (HMM) e modelos de linguagem n-gram. No entanto, a taxa de precisão foi bastante baixa em ambientes barulhentos e com diferentes sotaques.
- Década de 2010 (Deep Learning & Hybrid Models): Redes neurais profundas (DNN, CNN, RNN) foram combinadas com HMM, dando origem a assistentes de voz (Siri, Google Assistant) em smartphones.
- Década de 2020 (Revolução do transformador ponta a ponta): Arquiteturas ponta a ponta (OpenAI Whisper, Google Chirp, Conformer) que convertem ondas sonoras brutas diretamente em espectrograma e depois em texto entraram em cena. Treinados em centenas de milhares de horas de dados multilíngues, esses modelos podem transcrever com precisão sussurros, sotaques pesados ​​e ambientes barulhentos.

***Analogia:** STT é a pessoa que se senta ao seu lado enquanto você fala em uma sala de conferências, registrando cada palavra, pausa e entonação com precisão com uma máquina de escrever taquigráfica extremamente rápida; Além disso, ele é como um digitador-chefe perfeito que reconhece instantaneamente o idioma que você fala e aplica automaticamente as regras ortográficas.*

## Modelagem acústica e estudo de arquitetura

Um mecanismo STT moderno passa pelas seguintes camadas ao converter ondas sonoras analógicas em texto digital:

1. Pré-processamento de áudio e transformação de espectrograma: O sinal de áudio bruto (em formato PCM) é analisado com transformada de Fourier de curta duração (STFT · Transformada de Fourier de curta duração). É convertido em espectrogramas Log-Mel adequados para a percepção de frequência do ouvido humano. Este processo converte o som em um mapa visual de frequência.
2. Codificador Acústico: O espectrograma é alimentado na rede neural profunda baseada no Transformer. Ao filtrar o ruído nas ondas sonoras, o modelo extrai a qual fonema ou representação acústica corresponde cada fatia sonora de 20-30 milissegundos (no espaço latente).
3. Codificador de linguagem e previsão de contexto (decodificador autorregressivo): Os sinais do modelo acústico são combinados com o modelo de linguagem treinado. Em línguas ricas em pronúncia, como o turco, os homófonos (homófonos; por exemplo, o número "cem" e o verbo "cem") são detectados corretamente de acordo com o contexto da frase.
4. Pontuação e formatação: letras maiúsculas, vírgulas, pontos, pontos de interrogação são adicionados ao texto bruto e expressões numéricas ("quinze" → "15") são convertidas para o formato de texto.

**Medição de desempenho (WER · Taxa de erro de palavras):** A precisão de um modelo STT é medida pela métrica Word Error Rate (WER). Sua fórmula é WER = (S + D + I) / N (S: substituição, D: exclusão, I: inserção, N: total de palavras). Nos modelos modernos, a taxa WER em inglês diminuiu para 3-5%, e em línguas aglutinantes como o turco, diminuiu para 7-10%.

## Áreas de uso e ecossistema de código aberto

- Assistentes de reuniões e anotações: transcrição e resumo em tempo real de conversas do Zoom, Google Meet ou Teams (Otter.ai, Fireflies).
- Legendas e Tradução: Geração automática de legendas para conteúdo de vídeo e podcast nos formatos timestamp .srt e .vtt.
- Saúde e Direito: Médicos ditando notas de exames clínicos ou ouvindo atas sem usar as mãos.
- Líder de código aberto (Whisper & Whisper.cpp): o modelo Whisper de código aberto da OpenAI e a biblioteca Whisper.cpp de Georgi Gerganov, totalmente otimizada em C/C++, oferecem a capacidade de executar STT com total privacidade em hardware nativo (Mac série M, Raspberry Pi, GPUs de consumo) sem depender do servidor.

## Perguntas frequentes

**O que significa STT e o que significa?**

STT é uma abreviatura de 'Fala para Texto'. É uma tecnologia de inteligência artificial que analisa sinais sonoros, decodifica palavras e as converte em formato de texto.

**Qual é a diferença entre STT e reconhecimento de voz?**

O reconhecimento de voz (identificação do locutor) concentra-se na detecção de quem é o locutor (identidade biométrica). O STT, por outro lado, transcreve o conteúdo das palavras faladas independentemente da identidade do locutor.

**Os modelos STT entendem os sons turcos corretamente?**

Modelos de última geração baseados em Whisper e Conformer são treinados em grandes conjuntos de dados de voz turca; Ele pode realizar transcrição e pontuação com alta precisão em turco foneticamente rico.

**É possível executar o STT local?**

Sim; Graças a mecanismos otimizados como o Whisper.cpp ou o Fast-Whisper, você pode executar seus dados de voz off-line e com total privacidade em seu próprio computador, sem enviá-los para qualquer servidor em nuvem.

## Termos relacionados

- [Speech-to-Text](https://trescout.com/pt/dictionary/speech-to-text/)
- [Speech-to-Speech](https://trescout.com/pt/dictionary/speech-to-speech/)
- [Voice Cloning](https://trescout.com/pt/dictionary/voice-cloning/)
- [Whisper](https://trescout.com/pt/dictionary/whisper/)
- [Tokenizer](https://trescout.com/pt/dictionary/tokenizer/)
- [Apple Silicon](https://trescout.com/pt/dictionary/apple-silicon/)

## Ferramentas relacionadas

- [Agents](https://trescout.com/pt/discover/agents/)
- [Speech to Speech](https://trescout.com/pt/discover/speech-to-speech/)
- [Transcribe.cpp](https://trescout.com/pt/discover/transcribe-cpp/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/stt/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/stt/
