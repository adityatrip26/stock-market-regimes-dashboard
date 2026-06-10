import pandas as pd

df = pd.read_csv('stock_market_regimes_2000_2026.csv')
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year

# % of days each ticker spent in Bear or Crisis per year
df['is_bad'] = df['regime_label'].isin(['Bear', 'Crisis']).astype(int)

heatmap = df.groupby(['ticker', 'year'])['is_bad'].mean().multiply(100).round(1).reset_index()
heatmap.columns = ['ticker', 'year', 'crisis_pct']

# Pivot: rows = tickers, columns = years
pivot = heatmap.pivot(index='ticker', columns='year', values='crisis_pct').fillna(0)
pivot.to_csv('crisis_heatmap.csv')
print("Done:", pivot.shape)