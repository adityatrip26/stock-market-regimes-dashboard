import pandas as pd

df = pd.read_csv('stock_market_regimes_2000_2026.csv')
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year

# Get first and last price per ticker per year
first = df.sort_values('date').groupby(['ticker','year'])['close'].first()
last  = df.sort_values('date').groupby(['ticker','year'])['close'].last()

annual_returns = ((last - first) / first * 100).round(2).reset_index()
annual_returns.columns = ['ticker', 'year', 'annual_return_pct']

annual_returns.to_csv('stock_annual_returns.csv', index=False)
print("Done:", annual_returns.shape)