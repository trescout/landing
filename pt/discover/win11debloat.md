# Limpe seu sistema Windows de coisas desnecessárias

Win11Debloat é um script do PowerShell que permite remover aplicativos pré-instalados e desabilitar dados de telemetria nos sistemas operacionais Windows 10 e 11. Ele permite que os usuários personalizem seus sistemas e executem a depuração do sistema, removendo componentes desnecessários.

- ★ 56.315
- GitHub Trending · 2026-06-16

**Nota da TreScout:** Ele remove aplicativos indesejados que acompanham o Windows e desativa configurações que coletam dados em segundo plano. Leia o que ele faz antes de executá-lo: não é fácil recuperar algumas peças removidas. Não o use em um computador pessoal, em um dispositivo da empresa ou em um computador que você compartilha com outra pessoa.

## Atualizações

- **27 de agosto de 2026:** Estrelas 54,506 → 56,315, versão mais recente 2026.08.24 (24 de agosto de 2026).
- **2 de agosto de 2026:** Estrelas 48,210 → 54,506, versão mais recente 2026.07.11 (11 de julho de 2026).

*Kaynak: github.com/Raphire/Win11Debloat · MIT*

## O que você ganha

- Remove rapidamente aplicativos pré-instalados desnecessários.
- Desativa telemetria e dados de rastreamento.
- Desativa recursos e anúncios com tecnologia de IA.

## Instalação

**Baixar arquivo do GitHub**

```
Invoke-WebRequest -Uri https://github.com/Raphire/Win11Debloat/archive/refs/heads/master.zip -OutFile Win11Debloat.zip
```

**Abrir arquivo**

```
Expand-Archive -Path .\Win11Debloat.zip -DestinationPath .\Win11Debloat
```

## Execução

**Revisar e executar script**

```
Set-Location .\Win11Debloat\Win11Debloat-master
.\Win11Debloat.ps1
```

## Se você não programa

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Desejo desinstalar aplicativos desnecessários em meu sistema operacional Windows 11, desligar os dados de telemetria e desabilitar recursos como o Copilot com tecnologia de IA. Como posso tornar meu sistema mais leve e focado na privacidade usando a ferramenta Win11Debloat? Explique passo a passo o que preciso prestar atenção para manter a estabilidade do sistema ao usar esta ferramenta e como posso personalizá-la com segurança.

## Termos relacionados do glossário

- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** É para usuários que usam o sistema operacional Windows 10 ou 11 e desejam limpar seu sistema de componentes desnecessários e controlar suas configurações de privacidade.
- **Licença:** MIT

## Links

- [Repositório no GitHub →](https://github.com/Raphire/Win11Debloat)
- [Ler em turco →](https://trescout.com/discover/win11debloat/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-06-16: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/win11debloat/
