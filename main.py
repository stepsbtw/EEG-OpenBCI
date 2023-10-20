import pandas
import matplotlib

database = pandas.read_csv('DATABASES/data.csv')

print(database.dtypes)
print(database)