"""
Moving Average Crossover Backtest (Enhanced Version)
- Saves results to CSV
- Saves chart as PNG
- Produces professional metrics
"""

import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import os


def run_backtest(
    ticker: str = "AAPL",
    start: str = "2020-01-01",
    end: str = "2024-01-01",
    fast_window: int = 20,
    slow_window: int = 50,
    initial_capital: float = 10_000.0,
) -> None:

    # -------------------------------------------------
    # 1) Create results folder
    # -------------------------------------------------
    if not os.path.exists("results"):
        os.makedirs("results")
        print("📁 Created folder: results/")
    else:
        print("📁 Folder already exists: results/")

    print(f"\n🔁 Running Moving Average Crossover backtest for {ticker}...")
    print(f"Period: {start} to {end}")
    print("-" * 60)

    # -------------------------------------------------
    # 2) Download price data
    # -------------------------------------------------
    data = yf.download(ticker, start=start, end=end, auto_adjust=True)

    if data.empty:
        print("❌ No price data found.")
        return

    data = data[["Close"]].rename(columns={"Close": "price"}).dropna()

    # -------------------------------------------------
    # 3) Compute moving averages
    # -------------------------------------------------
    data["ma_fast"] = data["price"].rolling(fast_window).mean()
    data["ma_slow"] = data["price"].rolling(slow_window).mean()
    data.dropna(inplace=True)

    # -------------------------------------------------
    # 4) Generate trading signals
    # -------------------------------------------------
    data["signal"] = (data["ma_fast"] > data["ma_slow"]).astype(int)
    data["position"] = data["signal"].shift().fillna(0)

    # -------------------------------------------------
    # 5) Compute returns
    # -------------------------------------------------
    data["returns"] = data["price"].pct_change().fillna(0.0)
    data["strategy_returns"] = data["position"] * data["returns"]
    data["equity"] = (1 + data["strategy_returns"]).cumprod() * initial_capital

    # -------------------------------------------------
    # 6) Save results to CSV
    # -------------------------------------------------
    data.to_csv("results/full_backtest_data.csv")
    data[["equity"]].to_csv("results/equity_curve.csv")

    print("💾 Saved: results/full_backtest_data.csv")
    print("💾 Saved: results/equity_curve.csv")

    # -------------------------------------------------
    # 7) Compute metrics
    # -------------------------------------------------
    total_ret = data["equity"].iloc[-1] / initial_capital - 1
    ann_ret = (1 + total_ret) ** (252 / len(data)) - 1
    ann_vol = data["strategy_returns"].std() * np.sqrt(252)
    sharpe = ann_ret / ann_vol if ann_vol > 0 else 0

    running_max = data["equity"].cummax()
    drawdown = (data["equity"] - running_max) / running_max
    max_dd = drawdown.min()

    # -------------------------------------------------
    # 8) Save metrics
    # -------------------------------------------------
    metrics = pd.DataFrame([{
        "Total Return": f"{total_ret:.2%}",
        "Annualized Return": f"{ann_ret:.2%}",
        "Annualized Volatility": f"{ann_vol:.2%}",
        "Sharpe Ratio": f"{sharpe:.2f}",
        "Max Drawdown": f"{max_dd:.2%}"
    }])

    metrics.to_csv("results/metrics.csv", index=False)
    print("💾 Saved: results/metrics.csv")

    # -------------------------------------------------
    # 9) Plot chart and save
    # -------------------------------------------------
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    ax1.plot(data.index, data["price"], label="Price")
    ax1.plot(data.index, data["ma_fast"], label=f"{fast_window}-MA")
    ax1.plot(data.index, data["ma_slow"], label=f"{slow_window}-MA")
    ax1.legend()
    ax1.set_title(f"{ticker} Price with Moving Averages")

    ax2.plot(data.index, data["equity"], label="Equity")
    ax2.legend()
    ax2.set_title("Equity Curve")

    plt.tight_layout()
    plt.savefig("results/chart.png")
    print("📊 Saved: results/chart.png")

    plt.show()

    print("\n🎉 Backtest completed successfully!")


if __name__ == "__main__":
    run_backtest()
