# O que é Incremental Backup?

É um método de backup que economiza tempo e espaço, salvando apenas os arquivos que foram alterados desde o último backup.

## Definição
O backup incremental detecta apenas alterações recentes e as adiciona, em vez de copiar todos os dados a cada vez. Este método reduz significativamente o tempo de backup e permite usar o espaço de armazenamento de forma eficiente. É uma estratégia indispensável para grandes conjuntos de dados.

## Como funciona
O sistema verifica a data da última modificação dos arquivos. Ele apenas adiciona peças alteradas ou adicionadas recentemente ao arquivo de backup.

## Onde é usado
É usado em bancos de dados corporativos, grandes servidores de arquivos e sistemas de backup profissionais.

## Costuma ser confundido com
Não deve ser confundido com backup completo; um backup completo copia tudo sempre.

## Perguntas frequentes
**É difícil restaurar?**
Sim, é um pouco mais complicado do que um backup completo, pois todas as partes precisam ser combinadas.

**Com que frequência isso deve ser feito?**
Isso pode ser feito diariamente ou de hora em hora, dependendo da taxa de troca de dados.


## Termos relacionados
- [Backup Program](/pt/dictionary/backup-program/)
- [Data Pipeline](/pt/dictionary/data-pipeline/)

## Ferramentas relacionadas
- [Restic](/pt/discover/restic/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/incremental-backup/
