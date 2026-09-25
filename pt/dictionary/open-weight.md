# O que é Open Weight?

> Pesos de Modelo Publicamente Acessíveis

**Categoria:** AI  
**Última atualização:** 2026-09-22

Open weight refere-se a modelos de IA cujos pesos de parâmetros treinados estão disponíveis para download público, permitindo que desenvolvedores rodem, quantizem e façam fine-tuning em hardware próprio.

## Definição e etimologia
Diferente das plataformas proprietárias fechadas que operam apenas sob cobrança por requisição, os modelos open weight liberam a estrutura neural diretamente para o desenvolvedor. Isso assegura privacidade absoluta e elimina intermediários.

## Contexto cotidiano e uso prático
- **Execução Local em Dispositivos:** Carregamento de modelos quantizados em notebooks de trabalho sem depender de acesso à internet.
- **Privacidade Total de Dados:** Garantia de que segredos comerciais e registros pessoais não serão transmitidos para servidores remotos.
- **Independência de Custos:** Substituição de faturas recorrentes de API por infraestrutura própria amortizada.

## Profundidade técnica e arquitetura
Estrutura Técnica dos Pesos Abertos:- **Formatos de Arquivo:** Pacotes disponibilizados em Safetensors ou contêineres GGUF com precisão em FP16 ou quantização INT4/INT8.
- **Runtimes de Incorrência:** Aceleração em servidores corporativos através de vLLM, Ollama e llama.cpp.
- **Ajuste Fino Eficiente (LoRA):** Treinamento de adaptadores leves para tarefas específicas sem alterar os pesos fundamentais do modelo.

## Costuma ser confundido com
Frequentemente confundido com código aberto completo. O open source estrito inclui o código de treino e a base de dados; o open weight distribui os parâmetros matemáticos consolidados para uso imediato.

## Perspectivas interdisciplinares
- **Padaria:** Ter a massa preparada para assar no próprio forno vs comprar o pão pronto embalado.
- **Computação:** Instalar um programa compilado no disco local vs usar um site de ferramentas online.
- **Música:** Ter acesso aos canais de áudio isolados para remixar vs ouvir uma música compactada em streaming.

## Por analogia
É equivalente a fornecer os ingredientes e instruções de preparo para que cada pessoa possa cozinhar a receita na sua própria casa com total liberdade.

## Perguntas frequentes

**O que é possível fazer com os pesos de um modelo aberto?**  
Você pode hospedar o modelo no seu servidor, convertê-lo para rodar em celulares, aplicar ajustes finos e utilizá-lo sem internet.

**Qual a vantagem frente a serviços como o ChatGPT?**  
Privacidade incondicional, previsibilidade de custos e controle total sobre as versões e respostas do modelo.

**Qual configuração de máquina é necessária para modelos 7B ou 8B?**  
Um computador com 16 GB de RAM ou placa de vídeo de 8 GB roda com tranquilidade modelos comprimidos em 4 bits.

**Posso usar em produtos comerciais?**  
Sim, as licenças dos principais modelos (Llama, Mistral, Qwen) autorizam expressamente o uso comercial na maioria dos cenários.

## Termos relacionados
- [Open Source AI](/pt/dictionary/open-source-ai/)
- [Foundation Model](/pt/dictionary/foundation-model/)
- [SLM](/pt/dictionary/slm/)

---
Fonte: Dicionário Técnico TreScout · https://trescout.com/pt/dictionary/open-weight/
