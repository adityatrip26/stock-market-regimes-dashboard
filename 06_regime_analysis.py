import pandas as pd

df = pd.read_csv('stock_market_regimes_2000_2026.csv')

print("=== REGIME STATS ===")
print(df.groupby('regime_label')[['returns', 'volatility', 'vix']].mean().round(3))

print("\n=== VIX RANGES PER REGIME ===")
print(df.groupby('regime_label')['vix'].describe().round(2))

print("\n=== RETURN RANGES PER REGIME ===")
print(df.groupby('regime_label')['returns'].describe().round(4))