# 📈 Moving Average Crossover Trading Strategy  
**A Quantitative Finance Backtesting Project using Python**

This project implements a **Moving Average Crossover Trading Algorithm** and runs a full **historical backtest** using real stock market data.  
It is a practical introduction to **algorithmic trading, quantitative finance, and data analysis**.

---

## 🚀 Project Overview

The Moving Average Crossover is one of the most widely used trading strategies.  
It works by comparing:

- **Fast Moving Average (short period)**  
- **Slow Moving Average (long period)**  

When the fast MA goes **above** the slow MA → **BUY**  
When the fast MA goes **below** the slow MA → **SELL**

This project:

- Downloads historical stock data using `yfinance`  
- Computes fast/slow moving averages  
- Generates long/flat trading signals  
- Simulates portfolio performance over time  
- Plots the strategy and saves results to files  

---

## 🧠 Technologies Used

| Component | Technology |
|----------|------------|
| Programming Language | Python |
| Market Data | yfinance |
| Data Manipulation | pandas |
| Math / Arrays | numpy |
| Visualization | matplotlib |
| Environment | virtualenv |
| Version Control | Git & GitHub |

---

## 📊 Features

### 🔹 1. Data Downloading  
Automatically fetches daily historical stock data (default: **AAPL**) between 2020-01-01 and 2024-01-01.

### 🔹 2. Technical Indicators  
- Fast Moving Average (20-day)  
- Slow Moving Average (50-day)  

### 🔹 3. Trading Logic  
- Go **long** when fast MA crosses above slow MA  
- Go **flat** when fast MA crosses below slow MA  

### 🔹 4. Backtesting Engine  
Simulates:

- Daily position (in or out of the market)  
- Strategy returns  
- Portfolio equity (account value) over time  

### 🔹 5. Performance Metrics  
The script calculates and saves:

- **Total Return**  
- **Annualized Return**  
- **Annualized Volatility**  
- **Sharpe Ratio**  
- **Max Drawdown**

Results are stored in: `results/metrics.csv`.

### 🔹 6. Visualization  
Generates and saves a chart showing:

- Price  
- Fast & Slow Moving Averages  
- Equity curve  

Chart location: `results/chart.png`

---

## 📁 Project Structure

```text
quant-ma-crossover/
│── main.py
│── requirements.txt
│── results/
│   ├── chart.png
│   ├── equity_curve.csv
│   ├── metrics.csv
│   └── full_backtest_data.csv


