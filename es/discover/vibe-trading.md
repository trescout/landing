# Comercio personal con inteligencia artificial

Vibe-Trading ofrece un agente comercial personal desarrollado para operar en los mercados financieros. El proyecto permite a los usuarios gestionar estrategias comerciales automáticas con su estructura basada en Python.

- ★ 31.295
- Python
- GitHub Trending · 2026-06-04

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
Quiero operar en los mercados financieros con el agente Vibe-Trading. Ayúdenme a analizar los datos actuales del mercado, realizar pruebas retrospectivas de las estrategias que he identificado y administrar mis conexiones de corretaje de forma segura. Explique paso a paso cómo puedo configurar procesos comerciales automatizados, determinando específicamente mis mandatos comerciales y límites de riesgo.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/vibe-trading/
