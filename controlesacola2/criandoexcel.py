import pandas as pd

df = pd.read_csv('dados_os.csv')

df2 = pd.read_csv('entrada e saida.csv')

df3 = pd.concat([df,df2])

df3.to_excel('dadosatuais.xlsx', index=False)