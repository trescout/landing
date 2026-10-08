# Comercio personal con inteligencia artificial

Vibe-Trading ofrece un agente comercial personal desarrollado para operar en los mercados financieros. El proyecto permite a los usuarios gestionar estrategias comerciales automáticas con su estructura basada en Python.

- ★ 34.287
- Python
- GitHub Trending · 2026-06-04

## Actualizaciones

- **29 de septiembre de 2026:** Estrellas 33,083 → 34,287, última versión v0.1.16 (29 de septiembre de 2026).
- **9 de septiembre de 2026:** Estrellas 32,899 → 33,083, última versión v0.1.15 (9 de septiembre de 2026).
- **7 de septiembre de 2026:** Estrellas 31,295 → 32,899, última versión v0.1.14 (20 de agosto de 2026).
- **20 de agosto de 2026:** Estrellas 30,558 → 31,295, última versión v0.1.14 (20 de agosto de 2026).

## Qué aporta

- Gestión de estrategias automatizada con agente comercial personal.
- Acceso a datos de mercado con soporte de múltiples intermediarios.
- Autorización de transacciones orientada a la seguridad y libro de auditoría.

## Instalación

**Instalación directa**

```
pip install vibe-trading-ai
```

**Configuración del entorno de desarrollador**

```
git clone https://github.com/HKUDS/Vibe-Trading.git
cd Vibe-Trading
python -m venv .venv

# Activate
source .venv/bin/activate          # Linux / macOS
# .venv\Scripts\Activate.ps1       # Windows PowerShell

pip install -e .
cp agent/.env.example agent/.env   # Edit — set your LLM provider API key
vibe-trading                       # Launch interactive TUI
```

## Ejecución

**Investigación con lenguaje natural**

```
vibe-trading run -p "Backtest a BTC-USDT 20/50 moving-average strategy for 2024, summarize return and drawdown, then export the report"
```

**Prueba de estrategia**

```
vibe-trading alpha bench --zoo gtja191 --universe csi300 --period 2018-2025 --top 20
```

## Si no programa

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero operar en los mercados financieros con el agente Vibe-Trading. Ayúdenme a analizar los datos actuales del mercado, realizar pruebas retrospectivas de las estrategias que he identificado y administrar mis conexiones de corretaje de forma segura. Explique paso a paso cómo puedo configurar procesos comerciales automatizados, determinando específicamente mis mandatos comerciales y límites de riesgo.

## Términos relacionados del glosario

- [Trading Agent](https://trescout.com/es/dictionary/trading-agent/)
- [Agent](https://trescout.com/es/dictionary/agent/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Está diseñado para usuarios que desean desarrollar y gestionar estrategias comerciales automáticas en los mercados financieros.
- **Licencia:** MIT

## Enlaces

- [Repositorio en GitHub →](https://github.com/HKUDS/Vibe-Trading)
- [Leer en turco →](https://trescout.com/discover/vibe-trading/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-06-04: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/vibe-trading/
