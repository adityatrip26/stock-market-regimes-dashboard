import pandas as pd

df = pd.read_csv('stock_market_regimes_2000_2026.csv')

portfolio = df.groupby(['regime_label', 'ticker'])['returns'].mean().multiply(100).round(2).reset_index()
portfolio.columns = ['regime', 'ticker', 'avg_daily_return_pct']

best = portfolio.loc[portfolio.groupby('regime')['avg_daily_return_pct'].idxmax()].reset_index(drop=True)
worst = portfolio.loc[portfolio.groupby('regime')['avg_daily_return_pct'].idxmin()].reset_index(drop=True)

best.to_csv('best_stocks_per_regime.csv', index=False)
worst.to_csv('worst_stocks_per_regime.csv', index=False)

print("BEST STOCK PER REGIME:")
print(best.to_string())
print("\nWORST STOCK PER REGIME:")
print(worst.to_string())