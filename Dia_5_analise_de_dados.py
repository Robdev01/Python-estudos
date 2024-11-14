
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


# Alunos Graduados
alunos_graduacao = emprestimos_completo.query('tipo_vinculo_usuario == "ALUNO DE GRADUAÇÃO"')
#print(alunos_graduacao.colecao.value_counts())

#tabela com quantidade mensal pr ano
alunos_graduacao_acervo_circulante = alunos_graduacao.query('colecao == "Acervo Circulante"')
alunos_graduacao_acervo_circulante = pd.DataFrame(alunos_graduacao_acervo_circulante)
alunos_graduacao_acervo_circulante['data_emprestimo'] = pd.to_datetime(alunos_graduacao_acervo_circulante['data_emprestimo'])
alunos_graduacao_acervo_circulante['ano'] = alunos_graduacao_acervo_circulante['data_emprestimo'].dt.year
alunos_graduacao_acervo_circulante['mes'] = alunos_graduacao_acervo_circulante['data_emprestimo'].dt.month
alunos_graduacao_acervo_circulante = alunos_graduacao_acervo_circulante.loc[:,['ano','mes']]
alunos_graduacao_acervo_circulante = alunos_graduacao_acervo_circulante.value_counts().to_frame('quantidade').reset_index()

#print(alunos_graduacao_acervo_circulante)


def gera_box_plot(dataset,x,y,titulo,subtitulo):
  '''
  Esta função irá gerar um gráfico de boxplot.

  Dataset = conjunto de dados do gráfico
  x = valor do eixo x do gráfico
  y = valor do eixo y do gráfico
  título = título do gráfico
  subtitulo = subtitulo do texto
  '''

  sns.set_theme(style="darkgrid", palette='Blues',font_scale=1.3)                    
  plt.figure(figsize=(16,10))                                                           

  ax = sns.boxplot(y= y, x= x, data= dataset,color='#4171EF')                                           
  ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',').replace(',','.')))                


  plt.ylim(0,max(dataset[y])*1.1)                                               #Definir o limite do eixo y
  plt.xlabel(None)                                                                     
  plt.ylabel(None)                                                                    

  ax.set_title(titulo+"\n",size=20,loc='left',weight='bold')
  ax.text(s=subtitulo,x=-0.5,y=max(dataset[y])*1.11,fontsize=18, ha='left',color='gray')  



#gera_box_plot(alunos_graduacao_acervo_circulante,'ano','quantidade','Distribuição dos empréstimos mensais', 'Realizados pelos alunos de graduação no acervo circulante')

plt.show()

# Aluno de pos-graduação
alunos_pos_graduacao = emprestimos_completo.query('tipo_vinculo_usuario == "ALUNO DE PÓS-GRADUAÇÃO"')
print(alunos_pos_graduacao.colecao.value_counts())
alunos_pos_graduacao_acervo_circulante = alunos_pos_graduacao.query('colecao == "Acervo Circulante"')
alunos_pos_graduacao_acervo_circulante = pd.DataFrame(alunos_pos_graduacao_acervo_circulante)
alunos_pos_graduacao_acervo_circulante['data_emprestimo'] = pd.to_datetime(alunos_pos_graduacao_acervo_circulante['data_emprestimo'])
alunos_pos_graduacao_acervo_circulante['ano'] = alunos_pos_graduacao_acervo_circulante['data_emprestimo'].dt.year
alunos_pos_graduacao_acervo_circulante['mes'] = alunos_pos_graduacao_acervo_circulante['data_emprestimo'].dt.month
alunos_pos_graduacao_acervo_circulante = alunos_pos_graduacao_acervo_circulante.loc[:,['ano','mes']]
alunos_pos_graduacao_acervo_circulante = alunos_pos_graduacao_acervo_circulante.value_counts().to_frame('quantidade').reset_index()

print(alunos_pos_graduacao_acervo_circulante)

gera_box_plot(alunos_pos_graduacao_acervo_circulante,'ano','quantidade','Distribuição dos empréstimos mensais', 'Realizados pelos alunos de pós graduação no acervo circulante')

plt.show()



