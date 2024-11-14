# analise-de-dados-panda

Olá pessoal,

Recentemente, participei de um desafio de análise de dados como parte de um curso que estou fazendo. Neste desafio, fui solicitado a trabalhar com um conjunto de dados usando Python e a biblioteca Pandas. Gostaria de compartilhar minha abordagem e o código que desenvolvi para resolver o desafio.

Descrição do Desafio
O objetivo do desafio era carregar um conjunto de dados de um arquivo CSV, visualizar as primeiras linhas, entender a forma do DataFrame e contar os valores únicos em uma coluna específica.

Minha Abordagem
Primeiro, utilizei o Pandas para carregar o arquivo CSV usando o método pd.read_csv(). Certifiquei-me de especificar o separador de campo como ponto e vírgula e a codificação como latin1.

Em seguida, utilizei o método head(10) para visualizar as primeiras 10 linhas do DataFrame e shape para entender o número de linhas e colunas.

Finalmente, usei value_counts() para contar os valores únicos na coluna 'Cidade'.
