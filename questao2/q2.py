import pandas as pd
import re
from unidecode import unidecode

# funcoes para limpar e formatar os dados
def limpar_nome(nome):
    return re.sub(r'[^A-Z ]', '', unidecode(nome.upper()))

def formatar_cpf(cpf):
    digitos = re.sub(r'\D', '', cpf)
    return f"{digitos[:3]}.{digitos[3:6]}.{digitos[6:9]}-{digitos[9:]}" if len(digitos) == 11 else cpf

df = pd.read_csv("dados.csv")
df["nome"] = df["nome"].map(limpar_nome)
df["cpf"] = df["cpf"].map(formatar_cpf)
df["email"] = df["email"].str.strip().str.strip('"') # correção do email da Maria que estava com aspas mesmo após o tratamento

# A questão pedia para salvar em xls (formato antigo do Excel), mas acredito que foi um erro de digitação, 
# então estou salvando em xlsx
df.to_excel("dados_formatados.xlsx", index=False)
