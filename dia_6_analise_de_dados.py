import pandas as pd
from io import StringIO

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

cadastro_usuarios_antes_2010 = pd.read_excel('7_Days_of_Code_Alura-Python-Pandas-main/Dia_6-Novos_dados_novas_analises/Datasets/matricula_alunos.xlsx')

cadastro_usuarios_depois_2010 = pd.read_excel('7_Days_of_Code_Alura-Python-Pandas-main/Dia_6-Novos_dados_novas_analises/Datasets/matricula_alunos.xlsx')

print(cadastro_usuarios_antes_2010)

cadastro_usuarios_antes_2010.columns = ['matricula_ou_siape','tipo_vinculo_usuario','curso']

print(cadastro_usuarios_depois_2010)

cadastro_usuarios_depois_2010.columns = ['matricula_ou_siape', 'tipo_vinculo_usuario', 'curso']


cadastro_usuarios_excel = pd.concat([cadastro_usuarios_antes_2010,cadastro_usuarios_depois_2010],ignore_index=True)
cadastro_usuarios_excel.matricula_ou_siape = cadastro_usuarios_excel.matricula_ou_siape.astype('string')
print(cadastro_usuarios_excel)


cadastro_usuarios_json = pd.read_json('7_Days_of_Code_Alura-Python-Pandas-main/Dia_6-Novos_dados_novas_analises/Datasets/cadastro_alunos.json')

print(cadastro_usuarios_json)

cadastro_usuarios_json_string = cadastro_usuarios_json.registros[0]
cadastro_usuarios_json_buffer = StringIO(cadastro_usuarios_json_string)

cadastro_usuarios_graduacao_json = pd.read_json(cadastro_usuarios_json_buffer)

print(cadastro_usuarios_graduacao_json)

cadastro_usuarios_graduacao_json.matricula_ou_siape = cadastro_usuarios_graduacao_json.matricula_ou_siape.astype('float')
cadastro_usuarios_graduacao_json.matricula_ou_siape = cadastro_usuarios_graduacao_json.matricula_ou_siape.astype('string')

cadastro_usuarios_graduacao_json.info()

#Colocando junto Excel e Json
emprestimos_completo['localizacao'] = emprestimos_completo['localizacao'].astype('int')

cadastro_usuarios_cursos = pd.concat([cadastro_usuarios_excel,cadastro_usuarios_graduacao_json],ignore_index=True)
print(cadastro_usuarios_cursos)


data_limite = pd.to_datetime('2015-01-01')

matricula_data_de_emprestimo = emprestimos_completo.query("tipo_vinculo_usuario == 'ALUNO DE GRADUAÇÃO'")
matricula_data_de_emprestimo['data_emprestimo'] = pd.to_datetime(matricula_data_de_emprestimo['data_emprestimo'])
matricula_data_de_emprestimo = matricula_data_de_emprestimo.loc[:,['matricula_ou_siape','data_emprestimo']]
data_limite = pd.to_datetime('2024-01-01')
matricula_data_de_emprestimo = matricula_data_de_emprestimo.query('data_emprestimo > @data_limite')

matricula_data_de_emprestimo = matricula_data_de_emprestimo.reset_index(drop=True)

matricula_data_de_emprestimo = emprestimos_completo.query("tipo_vinculo_usuario == 'ALUNO DE GRADUAÇÃO'")
matricula_data_de_emprestimo['data_emprestimo'] = pd.to_datetime(matricula_data_de_emprestimo['data_emprestimo'])
matricula_data_de_emprestimo = matricula_data_de_emprestimo.loc[:,['matricula_ou_siape','data_emprestimo']]
matricula_data_de_emprestimo = matricula_data_de_emprestimo.query('data_emprestimo >= 2015')
matricula_data_de_emprestimo = matricula_data_de_emprestimo.reset_index(drop=True)
print(matricula_data_de_emprestimo)

matricula_data_de_emprestimo.isna().sum(numeric_only=True)

matricula_data_de_emprestimo = matricula_data_de_emprestimo.dropna()


cadastro_usuarios_cursos_selecionados = cadastro_usuarios_cursos.query("curso == ['BIBLIOTECONOMIA','CIÊNCIAS SOCIAIS','COMUNICAÇÃO SOCIAL','DIREITO','FILOSOFIA','PEDAGOGIA']")
print(cadastro_usuarios_cursos_selecionados)
print(matricula_data_de_emprestimo['matricula_ou_siape'].dtype)

matricula_data_de_emprestimo['matricula_ou_siape'] = matricula_data_de_emprestimo['matricula_ou_siape'].astype(str)
print(matricula_data_de_emprestimo['matricula_ou_siape'].dtype)



#Unindo os DataFrame
cadastro_usuarios_cursos_selecionados = matricula_data_de_emprestimo.merge(cadastro_usuarios_cursos_selecionados)
cadastro_usuarios_cursos_selecionados['data_emprestimo'] = pd.to_datetime(cadastro_usuarios_cursos_selecionados['data_emprestimo'])
cadastro_usuarios_cursos_selecionados['data_emprestimo'] = cadastro_usuarios_cursos_selecionados['data_emprestimo'].dt.year


emprestimos_cursos_selecionados = cadastro_usuarios_cursos_selecionados.iloc[:,[1,3]].value_counts().reset_index()
emprestimos_cursos_selecionados.columns = ['ANO','CURSO','QUANTIDADE_EMPRESTIMOS']
print(emprestimos_cursos_selecionados)


emprestimos_tipo_usuario_curso_pivot = emprestimos_cursos_selecionados.pivot_table(
        index = 'CURSO',
        columns = 'ANO',
        values = 'QUANTIDADE_EMPRESTIMOS',
        fill_value = '-',
        aggfunc= sum(numeric_only=True),
        margins = True,
        margins_name = 'TOTAL',
)
print(emprestimos_tipo_usuario_curso_pivot)