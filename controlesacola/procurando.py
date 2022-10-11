import pandas as pd


df = pd.read_csv('novosdados.csv')
df.to_excel('novosdados.xlsx', index=False)

print(df.head(60))