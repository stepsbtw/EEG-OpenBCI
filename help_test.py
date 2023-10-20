import pandas
import matplotlib

#1 CRIAR O DATAFRAME
#dataframe = pandas.read_csv('DATABASES/data.csv') # criei um csv sem os espacos

dataframe = pandas.read_csv('DATABASES/data.txt', delimiter=', ', engine='python') 
# posso ler direto do txt, mesmo tendo 'espacos' entre as colunas.

#2 LER O DATAFRAME
print(dataframe.head(10)) # primeiras 10 linhas
print(dataframe.tail(10)) # ultimas 10 linhas

print(dataframe.columns) # todas colunas
print(dataframe['EXG Channel 0']) # coluna especifica
print(dataframe.dtypes) # tipos das colunas

print(dataframe.describe()) # explica / faz um sumario
# mas so funciona em tipos numericos
print(dataframe.describe(include='object'))
# fala um pouco sobre suas especifidades.

print(dataframe[['Sample Index','EXG Channel 0']]) # multiplas colunas
print(dataframe['Sample Index'].unique()) # todos valores unicos.

print(dataframe[dataframe['Sample Index']==255]) # FILTRA a coluna
# MULTIPLOS FILTROS
print(dataframe[(dataframe['Sample Index']==255) & (dataframe['Timestamp (Formatted)'] == '2023-08-28 15:41:48.435')])

print(dataframe.iloc[280]) # INDEXAR COM NUMEROS AS LINHAS
print(dataframe.iloc[280,0]) # LINHA E COLUNA

print(dataframe.iloc[0:256]) # CORTAR UM SEGMENTO DE DADOS.


#3 CHECAR DATAFRAME

print(dataframe.isnull().sum()) # numero de linhas com colunas faltando/ valores nulos

print(dataframe.dropna(inplace=True)) # retirar as linhas com colunas faltando

print(dataframe.drop('Other', axis = 1)) # retirando uma coluna especifica. nao linha

dataframe['Nova Coluna'] = dataframe['EXG Channel 0'] + dataframe['EXG Channel 1']
print(dataframe.head()) # da pra ver a nova coluna criada.

dataframe['Nova Coluna'] /= 2 # TROCA TUDO NA COLUNA.

dataframe.iloc[0,-1] -= dataframe['EXG Channel 1'][0] # troca somente o valor especificado
print(dataframe.head())

# CONDICOES:
# aplicar filtros com ifs
dataframe['ACCEL MODULE'] = dataframe['Accel Channel 0'].apply(lambda x: '+' if x>0 else '-') 
#print(dataframe.head())
#print(dataframe.tail())
#print(dataframe[700:900])

#4 OUTPUT
dataframe.to_csv('DATABASES/test/test_output.csv')
dataframe.to_json('DATABASES/test/test_output.json')
dataframe.to_html('DATABASES/test/test_output.html')



