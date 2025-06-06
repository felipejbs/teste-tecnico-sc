import pandas as pd

df = pd.read_csv('Vendas.csv', sep=';')

# agrupando os dados por loja e calculando o total e a média de vendas
resumo_vendas = df.groupby('Loja')['valor'].agg(total_vendas='sum', media_vendas='mean')

# saida
resumo_vendas.to_excel('resumo_vendas.xlsx')