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

cadastro_usuarios_posgraduacao_json = pd.read_json(cadastro_usuarios_json.registros[1])


#cadastro_usuarios_posgraduacao_json.info()


cadastro_usuarios_posgraduacao_json.matricula_ou_siape = cadastro_usuarios_posgraduacao_json.matricula_ou_siape.astype('float')
cadastro_usuarios_posgraduacao_json.matricula_ou_siape = cadastro_usuarios_posgraduacao_json.matricula_ou_siape.astype('string')
cadastro_usuarios_posgraduacao_json.info()

#Colocando junto Excel e Json
emprestimos_completo['localizacao'] = emprestimos_completo['localizacao'].astype('int')

cadastro_usuarios_cursos = pd.concat([cadastro_usuarios_excel,cadastro_usuarios_posgraduacao_json],ignore_index=True)
print(cadastro_usuarios_cursos)




cadastro_usuarios_cursos_pos_graduacao = cadastro_usuarios_posgraduacao_json.query("tipo_vinculo_usuario == 'ALUNO DE PÓS-GRADUAÇÃO'")
print(cadastro_usuarios_cursos_pos_graduacao)


# Fazendo Filtro para emprestimos desde 2027


matricula_data_de_emprestimo_pos_graduacao = emprestimos_completo.loc[:,['matricula_ou_siape','data_emprestimo']]
matricula_data_de_emprestimo_pos_graduacao['data_emprestimo'] = pd.to_datetime(matricula_data_de_emprestimo_pos_graduacao['data_emprestimo'])
matricula_data_de_emprestimo_pos_graduacao = matricula_data_de_emprestimo_pos_graduacao.query('data_emprestimo > 2017')
matricula_data_de_emprestimo_pos_graduacao = matricula_data_de_emprestimo_pos_graduacao.reset_index(drop=True)
print(matricula_data_de_emprestimo_pos_graduacao)

matricula_data_de_emprestimo_pos_graduacao['matricula_ou_siape'] = matricula_data_de_emprestimo_pos_graduacao['matricula_ou_siape'].astype(str)
cadastro_usuarios_cursos_pos_graduacao['matricula_ou_siape'] = cadastro_usuarios_cursos_pos_graduacao['matricula_ou_siape'].astype(str)
# Unindo os DataFrames 
emprestimos_pos_graduacao_desde_2017 = matricula_data_de_emprestimo_pos_graduacao.merge(cadastro_usuarios_cursos_pos_graduacao, on='matricula_ou_siape')
print(emprestimos_pos_graduacao_desde_2017)


# Modificando estilo de data
emprestimos_pos_graduacao_desde_2017.data_emprestimo = emprestimos_pos_graduacao_desde_2017.data_emprestimo.dt.year

#contagem dos valores emprestado
emprestimos_pos_graduacao_desde_2017 = emprestimos_pos_graduacao_desde_2017.iloc[:,[1,3]].value_counts().reset_index()
emprestimos_pos_graduacao_desde_2017.columns = ['ANO','CURSO','QUANTIDADE_EMPRESTIMOS']
print(emprestimos_pos_graduacao_desde_2017.head())


# Pivotando tabela
emprestimos_pos_graduacao_e_curso_pivot = emprestimos_pos_graduacao_desde_2017.pivot_table(
        index = 'CURSO',
        columns = 'ANO',
        values = 'QUANTIDADE_EMPRESTIMOS'
)
print(emprestimos_pos_graduacao_e_curso_pivot)

#importando previsao de 2022
previsao_2022 = pd.read_table('7_Days_of_Code_Alura-Python-Pandas-main/Dia_7-Apresentando_resultados_em_HTML/Dataset/previsao')

previsao_2022 = previsao_2022['curso previsao_2022'].str.split(' ',expand=True)
print(previsao_2022)

print(emprestimos_pos_graduacao_e_curso_pivot)


# Unindo tabelas
previsao_2022.index = emprestimos_pos_graduacao_e_curso_pivot.index
emprestimos_pos_graduacao_e_curso_pivot['2022'] = previsao_2022.iloc[:,1]
print(emprestimos_pos_graduacao_e_curso_pivot)

#Modificando tabela
emprestimos_pos_graduacao_e_curso_pivot['2022'] = emprestimos_pos_graduacao_e_curso_pivot['2022'].astype('int')
print(emprestimos_pos_graduacao_e_curso_pivot)

# Criando funcoespara diferenca percentual
def diferenca_percentual_ano_anterior(x,y):
  return round(((x / y * 100) - 100),2)


# Calculando percentual
percentual_2018 = diferenca_percentual_ano_anterior(emprestimos_pos_graduacao_e_curso_pivot.iloc[:,1],emprestimos_pos_graduacao_e_curso_pivot.iloc[:,0])
percentual_2019 = diferenca_percentual_ano_anterior(emprestimos_pos_graduacao_e_curso_pivot.iloc[:,2],emprestimos_pos_graduacao_e_curso_pivot.iloc[:,1])
percentual_2022 = diferenca_percentual_ano_anterior(emprestimos_pos_graduacao_e_curso_pivot.iloc[:,3],emprestimos_pos_graduacao_e_curso_pivot.iloc[:,2])


# Criando DataFrame 

percentual = pd.DataFrame({'2018':percentual_2018,
                           '2019':percentual_2019,
                           '2022':percentual_2022})
print(percentual)


percentual.reset_index(inplace=True)
percentual.columns = percentual.columns.str.capitalize()
percentual.Curso = percentual.Curso.str.capitalize()

print(percentual)


th_props = [
  ('font-size', '1.4rem'),
  ('text-align', 'center'),
  ('font-weight', 'bold'),
  ('color', 'whitesmoke'),
  ('background-color', '#001692'),
  ('border-radius', '0.25rem'),
  ('box-shadow','0 0 1rem gray')
  ]

td_props = [
  ('font-size', '1rem'),
  ('padding','0.5rem'),
  ('text-align', 'left'),
  ('font-weight', 'bold'),
  ('border-bottom','0.1rem solid lightgray')
  ]

styles = [
  dict(selector="th", props=th_props),
  dict(selector="td", props=td_props)
  ]

# Exemplo de DataFrame para demonstração
percentual = pd.DataFrame({
    'Ano': ['2018', '2019', '2020', '2021', '2022'],
    'Valor': [0.05, 0.1, 0.15, 0.2, 0.25]
})



# Aplicação de estilos e formatação
html = percentual.style\
    .text_gradient(cmap='RdYlGn', low=1, axis=1, vmax=0.1, vmin=0)\
    .format('{:.2f} %', subset=['Valor'])\
    .hide(axis='index')\
    .set_table_styles(styles)\
    .to_html(doctype_html=True, table_attributes='ALIGN=LEFT WIDTH=50% CELLSPACING=5')
# Salvar o resultado em um arquivo HTML
with open('teste.html', 'w') as f:
    f.write(html)
