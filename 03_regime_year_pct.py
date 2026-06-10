import pandas as pd

df = pd.read_csv('regime_by_year.csv')  # already aggregated

# Add dominant regime column
regime_cols = ['Bear', 'Bull', 'Crisis', 'High-volatility', 'Sideways']
df['dominant_regime'] = df[regime_cols].idxmax(axis=1)

# Add total days column
df['total_days'] = df[regime_cols].sum(axis=1)

# Convert counts to percentages
for col in regime_cols:
    df[col + '_pct'] = (df[col] / df['total_days'] * 100).round(1)

df.to_csv('regime_year_pct.csv', index=False)
print("Done:", df.shape)