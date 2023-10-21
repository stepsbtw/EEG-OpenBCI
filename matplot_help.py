import pandas
import matplotlib.pyplot as plt

database = pandas.read_csv('DATABASES/data.csv')

print(database.dtypes)
print(database)

list_time = database[' Timestamp (Formatted)'].tolist()
list_data = database[' EXG Channel 0'].tolist()

plt.subplots(nrows = 1, ncols = 1)
plt.subplot(1, 1, 1)
plt.step(list_time, list_data)
plt.title('Channel 0 by Time')
plt.ylabel('EXG Channel 0')
plt.grid()

plt.show()