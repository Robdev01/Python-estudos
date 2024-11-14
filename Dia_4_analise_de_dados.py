
import pandas as pd
import seaborn as sns
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt

dados_2010_1 = pd.read_csv('7_Days_of_Code_Alura-Python-Pandas-main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20101.csv')
dados_2010_2 = pd.read_csv('7_Days_of_Code_Alura-Python-Pandas-main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20102.csv')
dados_2011_1 = pd.read_csv('7_Days_of_Code_Alura-Python-Pandas-main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20111.csv')
dados_2011_2 = pd.read_csv('7_Days_of_Code_Alura-Python-Pandas-main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20112.csv')
dados_2012_1 = pd.read_csv('7_Days_of_Code_Alura-Python-Pandas-main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20121.csv')
dados_2012_2 = pd.read_csv('7_Days_of_Code_Alura-Python-Pandas-main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20122.csv')
dados_2013_1 = pd.read_csv('7_Days_of_Code_Alura-Python-Pandas-main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20131.csv')
dados_2013_2 = pd.read_csv('7_Days_of_Code_Alura-Python-Pandas-main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20132.csv')
dados_2014_1 = pd.read_csv('7_Days_of_Code_Alura-Python-Pandas-main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20141.csv')
dados_2014_2 = pd.read_csv('7_Days_of_Code_Alura-Python-Pandas-main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20142.csv')
dados_2015_1 = pd.read_csv('7_Days_of_Code_Alura-Python-Pandas-main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20151.csv')
dados_2015_2 = pd.read_csv('7_Days_of_Code_Alura-Python-Pandas-main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20152.csv')
dados_2016_1 = pd.read_csv('7_Days_of_Code_Alura-Python-Pandas-main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20161.csv')
dados_2016_2 = pd.read_csv('7_Days_of_Code_Alura-Python-Pandas-main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20162.csv')
dados_2017_1 = pd.read_csv('7_Days_of_Code_Alura-Python-Pandas-main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20171.csv')
dados_2017_2 = pd.read_csv('7_Days_of_Code_Alura-Python-Pandas-main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20172.csv')
dados_2018_1 = pd.read_csv('7_Days_of_Code_Alura-Python-Pandas-main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20181.csv')
dados_2018_2 = pd.read_csv('7_Days_of_Code_Alura-Python-Pandas-main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20182.csv')
dados_2019_1 = pd.read_csv('7_Days_of_Code_Alura-Python-Pandas-main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20191.csv')
dados_2019_2 = pd.read_csv('7_Days_of_Code_Alura-Python-Pandas-main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20192.csv')
dados_2020_1 = pd.read_csv('7_Days_of_Code_Alura-Python-Pandas-main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20201.csv')



emprestimos_biblioteca = pd.concat([dados_2010_1,dados_2010_2,dados_2011_1,dados_2011_2,dados_2012_1,dados_2012_2,dados_2013_1,dados_2013_2,dados_2014_1, dados_2014_2,dados_2015_1,dados_2015_2,dados_2016_1,dados_2016_2,dados_2017_1,dados_2017_2,dados_2018_1,dados_2018_2,dados_2019_1,dados_2019_2,dados_2020_1],ignore_index=True)


emprestimos_biblioteca.value_counts()
emprestimos_biblioteca = emprestimos_biblioteca.drop_duplicates()
emprestimos_biblioteca = emprestimos_biblioteca.dropna()
dados_exemplares = pd.read_parquet('7_Days_of_Code_Alura-Python-Pandas-main/Dia_1-Importando_dados/Datasets/dados_exemplares.parquet')
emprestimos_completo = emprestimos_biblioteca.merge(dados_exemplares)


emprestimos_completo = emprestimos_completo.dropna()

CDU_lista = []
for CDU in emprestimos_completo['localizacao']:
  if(CDU < 100):
    CDU_lista.append('Generalidades')
  elif(CDU < 200):
    CDU_lista.append('Filosofia e psicologia')
  elif(CDU < 300):
    CDU_lista.append('Religião')
  elif(CDU < 400):
    CDU_lista.append('Ciências sociais')
  elif(CDU < 500):
    CDU_lista.append('Classe vaga')
  elif(CDU < 600):
    CDU_lista.append('Matemática e ciências naturais')
  elif(CDU < 700):
    CDU_lista.append('Ciências aplicadas')
  elif(CDU < 800):
    CDU_lista.append('Belas artes')
  elif(CDU < 900):
    CDU_lista.append('Linguagem')
  else:
    CDU_lista.append('Geografia. Biografia. História.')

emprestimos_completo['CDU_geral'] = CDU_lista

# Verificando valores de variaveis 

print(emprestimos_completo.tipo_vinculo_usuario.unique())
print(emprestimos_completo.colecao.unique())
print(emprestimos_completo.biblioteca.unique())
print(emprestimos_completo.CDU_geral.unique())


# Criando tabela 
def frequencia(variavel):
  

  frame = pd.DataFrame(emprestimos_completo[variavel].value_counts())                      
  frame.columns = ['quantidade']
  frame['percentual'] = round((frame.quantidade / frame.quantidade.sum(numeric_only=True))*100,1)

  return frame

print(frequencia('tipo_vinculo_usuario'))
print(frequencia('colecao'))
print(frequencia('biblioteca'))
print(frequencia('CDU_geral', 'colecao'))