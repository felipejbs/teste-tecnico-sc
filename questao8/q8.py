import pandas as pd

# Leitura do arquivo e correção das aspas curvas na coluna CPF
with open("cpfs.csv", "r", encoding="utf-8") as f:
    linhas = [linha.replace("“", "").replace("”", "").replace('"', '').strip() for linha in f]

df = pd.DataFrame(linhas[1:], columns=["cpf"])

# Limpando os CPFs (utilizando regex para remoção de tudo que não for número)
df['cpf'] = df['cpf'].str.replace(r'\D', '', regex=True)

# Verifica e faz a contagem dos duplicados
duplicados = df['cpf'].value_counts()[lambda x: x > 1].reset_index()
duplicados.columns = ['cpf', 'quantidade']

# Salva saida em xlsx
duplicados.to_excel("duplicados_cpfs.xlsx", index=False)
