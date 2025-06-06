import pandas as pd
import re

df = pd.read_csv("dados.csv")

# Padroniza nomes de colunas
df.columns = df.columns.str.replace('[“”"]', '', regex=True).str.strip().str.lower()

for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].astype(str).str.replace('[“”"]', '', regex=True).str.strip()

def corrigir_email_cpf(row):
    if ',' in row['email']:
        partes = row['email'].split(',', 1)
        row['email'] = partes[0].strip()
        row['cpf'] = partes[1].strip()
    return row

df = df.apply(corrigir_email_cpf, axis=1)

# Funções de validação de email e CPF
def checagem_email(email):
    return '@' not in email or ' ' in email

def checagem_cpf(cpf):
    return len(re.sub(r'\D', '', str(cpf))) < 11

# Aplicando validações no dataframe
df['checagem_email'] = df['email'].apply(checagem_email)
df['checagem_cpf'] = df['cpf'].apply(checagem_cpf)

# Filtra e remove colunas auxiliares
df_filtrado = df[df['checagem_email'] | df['checagem_cpf']].drop(columns=['checagem_email', 'checagem_cpf'])
df_filtrado.to_csv("dados_inconsistentes.csv", index=False)
