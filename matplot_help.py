import pandas
import matplotlib.pyplot as plt

database = pandas.read_csv('DATABASES/data.txt', delimiter=', ', engine='python')

print(database.dtypes)
print(database)


list_time = database['Timestamp (Formatted)'].tolist()
newtime = list_time[0].split(' ') # tirando a data do tempo formatado.
newtime = newtime[1]
newtime = newtime.split(':') # transformando o tempo em segundos 
newtime[0] = int(newtime[0]) * 60 * 60
newtime[1] = int(newtime[1]) * 60
newtime[2] = float(newtime[2])
init = newtime[0] + newtime[1] + newtime[2]  # calculando o inicio para obter a variacao depois.

for i, time in enumerate(list_time): # calculo da variacao.
    newtime = time.split(' ')
    newtime = newtime[1]
    newtime = newtime.split(':')
    newtime[0] = int(newtime[0]) * 60 * 60
    newtime[1] = int(newtime[1]) * 60
    newtime[2] = float(newtime[2])
    newnewtime = newtime[0] + newtime[1] + newtime[2]
    list_time[i] = newnewtime - init


k=0
list_data = []
# criando o sistema de plots/graficos
for i in range(2):
    for j in range(4):
        list_data.append(database[f'EXG Channel {k}'].tolist())
        plt.subplot2grid((2,4),(i,j)) # montar uma grade com 2 linhas e 4 colunas
        plt.step(list_time, list_data[k])
        plt.title(f'Channel {k} by Time')
        plt.ylabel(f'EXG Channel {k}')
        k+=1
plt.show()
