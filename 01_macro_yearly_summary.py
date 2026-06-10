import pandas as pd

df = pd.read_csv('stock_market_regimes_2000_2026.csv')
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year

# One row per year — use S&P 500 only for macro (avoid duplication)
sp500 = df[df['ticker'] == '^GSPC'].copy()

macro_yearly = sp500.groupby('year').agg(
    fed_funds_rate=('fed_funds_rate', 'mean'),
    unemployment_rate=('unemployment_rate', 'mean'),
    cpi=('cpi', 'mean'),
    vix=('vix', 'mean'),
    treasury_10y=('10y_treasury', 'mean'),
    treasury_2y=('2y_treasury', 'mean')
).round(2).reset_index()

macro_yearly.to_csv('macro_yearly.csv', index=False)
print("Done:", macro_yearly.shape)