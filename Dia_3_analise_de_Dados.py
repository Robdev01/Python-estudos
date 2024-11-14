
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


dados_2010_1.head()
emprestimos_biblioteca = pd.concat([dados_2010_1,dados_2010_2,dados_2011_1,dados_2011_2,dados_2012_1,dados_2012_2,dados_2013_1,dados_2013_2,dados_2014_1, dados_2014_2,dados_2015_1,dados_2015_2,dados_2016_1,dados_2016_2,dados_2017_1,dados_2017_2,dados_2018_1,dados_2018_2,dados_2019_1,dados_2019_2,dados_2020_1],ignore_index=True)

print(emprestimos_biblioteca)
emprestimos_biblioteca.value_counts()
print('Duplicadas', emprestimos_biblioteca.value_counts())
emprestimos_biblioteca = emprestimos_biblioteca.drop_duplicates()
print(emprestimos_biblioteca.value_counts())
emprestimos_biblioteca = emprestimos_biblioteca.dropna()
print(emprestimos_biblioteca.notnull())
print(emprestimos_biblioteca.head())
dados_exemplares = pd.read_parquet('7_Days_of_Code_Alura-Python-Pandas-main/Dia_1-Importando_dados/Datasets/dados_exemplares.parquet')
emprestimos_completo = emprestimos_biblioteca.merge(dados_exemplares)


emprestimos_completo = emprestimos_completo.dropna()
print(emprestimos_completo)

# Agora vamos organizar a dataFrame por localização

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

# Remove a coluna do DataFrame
emprestimos_completo = emprestimos_completo.drop('registro_sistema', axis=1)
print(emprestimos_completo.columns.tolist())

# Alterando coluna para String
emprestimos_completo['matricula_ou_siape'].to_string()

#mostrando coluna de string
print(emprestimos_completo[['matricula_ou_siape']])


#Filtra o DataFrame para incluir apenas as linhas onde a coluna 'CDU_geral' é igual a 'Geografia. Biografia. História.'
geografia_Lista = emprestimos_completo[emprestimos_completo['CDU_geral'] == 'Geografia. Biografia. História.']

print(geografia_Lista)

#Dia 03

print(emprestimos_completo.head())


# Pedi para lista só o Id_emprestimo
print(emprestimos_completo['id_emprestimo'].value_counts())


#Pedi para apagar as duplicidades e mostra o resultado

emprestimos = len(emprestimos_completo['id_emprestimo'].drop_duplicates())
print(emprestimos)

# Criei uma variavel com nome exemplares para descobrir quantos foram emprestados
exemplares = len(emprestimos_completo)
print(exemplares)


# listaremos quantidade emprestada por ano

emprestimos_data = pd.DataFrame(emprestimos_completo['data_emprestimo'].value_counts()).reset_index()
emprestimos_data.columns = ['data','quantidade']
emprestimos_data['data'] = pd.to_datetime(emprestimos_data['data'])
emprestimos_por_ano = emprestimos_data.groupby(by=emprestimos_data.data.dt.year).sum(numeric_only=True)
emprestimos_por_ano.index.name = 'ano'
print(emprestimos_por_ano)


# Configuramos o tema do Seaborn

sns.set_theme(context='notebook', 
              style='darkgrid', 
              palette='deep', 
              font_scale=1.3, 
              rc={"figure.figsize":(15,8)})

# Criando o gráfico de linha
ax = sns.lineplot(data=emprestimos_por_ano,x='ano',y='quantidade',color='black')
ax.set(xlabel=None,ylabel=None)
ax.tick_params(axis='x', rotation=30)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',').replace(',','.')))  

# Configurando o título do gráfico
ax.set_title('Quantidade de exemplares emprestados por ano'+'\n',size=20,loc='left',weight='bold')


# Mostrando o grafico
plt.show()

# listaremos quantidade emprestada por mes
emprestimos_por_mes = emprestimos_data.groupby(by=emprestimos_data.data.dt.month).sum(numeric_only=True)
emprestimos_por_mes.index.name = 'mes'
dicionario_meses = {1:'Janeiro',2:'Fevereiro',3:'Março',4:'Abril',
                    5:'Maio',6:'Junho',7:'Julho',8:'Agosto',
                    9:'Setembro',10:'Outubro',11:'Novembro',12:'Dezembro'}
emprestimos_por_mes.index = emprestimos_por_mes.index.map(dicionario_meses)
print(emprestimos_por_mes)
# Configuramos o tema do Seaborn
sns.set_theme(context='notebook', 
              style='darkgrid', 
              palette='deep', 
              font_scale=1.3, 
              rc={"figure.figsize":(15,8)})

# Criando o gráfico de linha
ax = sns.lineplot(data=emprestimos_por_mes, x='mes', y='quantidade', color='pink')
ax.set(xlabel=None, ylabel=None)
ax.tick_params(axis='x', rotation=30)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',').replace(',', '.')))

# Configurando o título do gráfico
ax.set_title("Quantidade de exemplares emprestados por mês" + "\n", size=20, loc='left', weight='bold')


# Exibindo o gráfico
plt.show()

# Listaremos emprestimos por hora

emprestimos_por_hora = emprestimos_data.groupby(by=emprestimos_data.data.dt.hour).sum(numeric_only=True)
emprestimos_por_hora.index.name = 'horas'
emprestimos_por_hora = emprestimos_por_hora.reset_index()
print(emprestimos_por_hora)

emprestimos_por_hora = emprestimos_por_hora.sort_values(ascending=True,by='quantidade')

# Configuramos o tema do Seaborn
sns.set_theme(context='notebook', 
              style='darkgrid', 
              palette='deep', 
              font_scale=1.3, 
              rc={"figure.figsize":(15,8)})

# Criando o gráfico de barras
ax = sns.barplot(data=emprestimos_por_hora, y='quantidade', x='horas', 
                 palette='pink', dodge=False)

# Excluindo a legenda do gráfico
plt.legend([],[], frameon=False)

# Configurando os rótulos e o título do gráfico
ax.set(xlabel='Horário', ylabel=None)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',').replace(',', '.')))
ax.set_title("Quantidade de exemplares emprestados do SISBI por faixa horária" + "\n", size=20, loc='left', weight='bold')


# Exibindo o gráfico
plt.show()
