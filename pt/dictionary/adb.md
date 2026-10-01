# O que é ADB?

> Android Debug Bridge

O ADB (Android Debug Bridge, ponte de depuração do Android) é uma ferramenta que permite a comunicação de comandos e depuração entre um computador e um dispositivo Android.

## Definição e origem da palavra
"Debug" significa depuração e "bridge" significa ponte. O ADB comunica o cliente no computador com o adb daemon no dispositivo; é utilizado em operações de instalação de aplicações, recolha de registos, depuração e gestão limitada de dispositivos. Faz parte do pacote Android SDK Platform-Tools.

## Como conhecer e usar no dia a dia?
Desenvolvimento: Instalação e registro de aplicativos.Teste: Testes em vários dispositivos.Personalização: Configuração avançada.

## Profundidade Técnica e Arquitetura
Layout triplo:

## Coisas frequentemente misturadas
Pensa-se que é transferência de arquivos. Ele apenas copia, o ADB interfere no sistema. A diferença de privilégios é grande.

## Use em diferentes disciplinas
Cabo: A linha que transporta o sinal.Intérprete: A linguagem de ambas as partes.Controle: Gerenciamento remoto.

## Perguntas Frequentes
**Todos podem usar?**
Os comandos básicos podem ser aprendidos; no entanto, especialmente o adb shell e as operações de exclusão exigem conhecimento técnico. É preciso verificar o efeito do comando antes de executá-lo.

**Pode ser sem fio?**
Sim. Nas versões do Android compatíveis, é possível estabelecer uma conexão via Wi-Fi após emparelhar com o dispositivo. A estabilidade e a velocidade dependem da qualidade da rede local.

**É seguro?**
Se você estiver com o dispositivo, sim. A autorização não é concedida em um dispositivo conectado a um computador desconhecido.

**Qual é a diferença do Fastboot?**
O ADB se comunica com o sistema operacional enquanto o Android está em execução. O Fastboot, por sua vez, é usado para operações de imagem de partição ou firmware enquanto o dispositivo está no modo bootloader; os comandos suportados e o processo de desbloqueio variam de acordo com o dispositivo.


## Termos relacionados
- [CLI](/pt/dictionary/cli/)
- [SDK](/pt/dictionary/sdk/)
- [Emulator](/pt/dictionary/emulator/)

## Ferramentas relacionadas
- [Universal Android Debloater Next Generation](/pt/discover/universal-android-debloater-next-generation/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/adb/
