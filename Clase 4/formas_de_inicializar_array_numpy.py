import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) #Inicializo un arreglo con tres vectores (un matriz)

b = np.zeros(3) #Inicializo un vector de ceros

c = np.ones(3) #Inicializo un vector de unos

d = np.empty(3) #Inicializo un vector nulo para luego cargarlo

e = np.arange(4) #Inicializo un vector a partir de un rango

f = np.arange(0, 12, 2) #Inicializo un vector desde un inicio, hasta que numero(ese no entra), y de a cuantos aumenta

g = np.linspace(0,10,num=10) #Inicializa un vector especificando el primer numero(incluido), el ultimo numero(incluido) y la cantidad de elementos

h = np.ones(2, dtype = np.int64) #El dtype cambia el tipo de dato, el 64 es la cantidad de bits que usa para representarlo