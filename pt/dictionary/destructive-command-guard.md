# O que é Destructive Command Guard?

É um escudo de segurança que o impede antes de executar comandos que correm o risco de excluir dados ou corromper o sistema.

## Definição
É uma camada de segurança projetada para evitar erros irreversíveis no sistema. Quando você digita um comando perigoso, o sistema o detecta e pergunta se você realmente deseja fazê-lo. Este mecanismo é utilizado para reduzir a margem de erro, principalmente em servidores críticos.

## Como funciona
Quando você insere um comando como 'excluir tudo' em uma linha de comando, o sistema não processa esse comando diretamente. Primeiro ele realiza uma verificação de segurança e diz 'Esta ação excluirá todos os seus dados, tem certeza?' Ele exibe uma caixa de seleção ou mensagem de aviso. O comando nunca será executado a menos que você o aprove.

## Onde é usado
É comumente encontrado em aplicativos de terminal, ferramentas avançadas de desenvolvimento de software e painéis de gerenciamento de servidores.

## Costuma ser confundido com
Pode ser confundido com um firewall; Ele bloqueia ataques externos, o que evita erros cometidos internamente.

## Perguntas frequentes
**Essa proteção deve estar sempre ativada?**
Sim, ter esta proteção ativada evita grandes perdas de dados, especialmente ao realizar operações críticas.


## Termos relacionados
- [Security Scanner](/pt/dictionary/security-scanner/)
- [Linux Server Security](/pt/dictionary/linux-server-security/)
- [Terminal Control](/pt/dictionary/terminal-control/)

## Ferramentas relacionadas
- [Destructive Command Guard](/pt/discover/destructive-command-guard/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/destructive-command-guard/
