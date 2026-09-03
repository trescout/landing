# Automated stock selection for the Chinese stock market

Sequoia-X is a Python-based software that performs automated stock selection based on technical analysis formulas using Chinese stock market data. It performs scanning operations after the end-of-day market close and delivers the results via Feishu, a corporate messaging application.

- ★ 6,376
- Python
- GitHub Trending · 2026-09-03

## What you get
- Stores stock data in a local database
- Automatically applies multiple technical analysis strategies
- Delivers end-of-day results via the Feishu messaging app

## Installation
**Installing the required libraries**

```
pip install .
```


## Running it
**Initial loading of historical data**

```
python main.py --backfill
```

**Starting the daily scan**

```
python main.py
```


## If you don't write code
I want to scan stocks in the Chinese market using technical analysis methods with the Sequoia-X tool. After completing the necessary installations in my Python environment, I will use the backfill mode to load historical data first, and then the daily operation mode for automatic scanning and receiving notifications after the daily market close. In this process, I want to ensure that the data is stored in a local SQLite database and the results are sent via Feishu.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/sequoia-x/
