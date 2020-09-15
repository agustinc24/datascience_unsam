#%% Ejercicio 4.11

import random

n = 99
grados = 37.5 #Mu
desviacion_estandar = 0.2 #Desviacion estandar
mediciones = []
for i in range(n):
    temperatura = random.normalvariate(grados, desviacion_estandar) #Calcula la temperatura con la desviacione estandar
    mediciones.append(temperatura) #La guarda en la lista mediciones

maximo = max(mediciones)
minimo = min(mediciones)
promedio = sum(mediciones)/n
pos_central = round(n/2) #La uso para calcular la mediana
mediana = sorted(mediciones)[pos_central]

print(f'Maximo = {maximo:0.6f}')
print('Minimo = {min:0.6f}')
print('Promedio = {sum:0.6f}')
print('Mediana = {mediana:0.6f}')

#%% Ejercicio 4.13

import numpy as np
import random

n = 99
grados = 37.5 #Mu
desviacion_estandar = 0.2 #Desviacion estandar
mediciones = []
for i in range(n):
    temperatura = random.normalvariate(grados, desviacion_estandar)
    mediciones.append(temperatura)

v_mediciones = np.array(mediciones) #Creo un array de las mediciones y las guardo

np.save('C:/Users/elcav/OneDrive/Documentos/Python/Curso Unsam/ejercicios_python/Data/Temperaturas.npy', v_mediciones) #Guardo el archivo especificandole una ruta











