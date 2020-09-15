#%% Ejercicio 3.15 y 3.16
import csv

f = open('C:/Users/elcav/OneDrive/Documentos/Python/Curso Unsam/ejercicios_python/Data/camion.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)
types = [str, int, float]

converted = []
converted = [func(val) for func, val in zip(types, row)]
dict(zip(headers, converted))

diccio = { name: func(val) for name, func, val in zip(headers, types, row) }

#%% Ejercicio 3.17
f = open('C:/Users/elcav/OneDrive/Documentos/Python/Curso Unsam/ejercicios_python/Data/dowstocks.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)

types = [str, float, str, str, float, float, float, float, int]
converted = [func(val) for func, val in zip(types, row)]
record = dict(zip(headers, converted))

print(record)



