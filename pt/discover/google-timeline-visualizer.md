# Transforme seu histórico de localização em vídeo em movimento

O Google Timeline Visualizer visualiza um ano de suas viagens com os dados do Histórico de localização do Google.

- ★ 2.946
- Kotlin
- GitHub Trending · 2026-08-20

## O que você ganha
- Converte dados históricos do Google Maps em vídeo MP4
- Anima rotas de viagem no mapa
- Protege a privacidade processando dados pessoais no dispositivo

## Instalação
**Instale e execute as dependências necessárias**

```
python -m pip install -r requirements.txt
python visualizer.py --input Timeline.json --year 2025 --camera-movement steady \
  --long-trip-compression balanced --output my_trip_2025.mp4
```

**Configurar ferramentas de desenvolvimento**

```
./gradlew test lint assembleGithubDebug assemblePlayDebug
python -m pip install -r requirements-dev.txt
python -m pytest
```


## Se você não programa
Quero criar um vídeo mostrando minhas viagens usando o arquivo Timeline.json que possuo. Depois de instalar as dependências necessárias no ambiente Python, qual comando devo usar para converter meus dados de 2025 em um arquivo chamado 'my_trip_2025.mp4' com movimento de câmera 'estável' e configurações de compactação 'equilibradas'?

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/google-timeline-visualizer/
