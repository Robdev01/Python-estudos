import pandas as pd

dados = pd.read_csv("C:/Users/robso/Desktop/panda_database/planilha de dados.csv", sep=";", encoding="latin1")

# Use df.head() sem argumentos para visualizar as primeiras linhas do DataFrame
print(dados.head(10))

print(dados.shape)
print(dados['Cidade'].value_counts())