import numpy as np

a = np.arange(1, 20, 2) #Por defecto son int
#print (a)

b = np.linspace(1, 19, num=10) #Por defecto son float
#print(b)


arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
#print(np.sort(arr)) #Con np.sort() lo ordeno
#%%
import numpy as np

d = np.array([1,2,3,4])
e = np.array([5,6,7,8])
print(np.concatenate((e,d))) #Concatena ambos, primero el que ponga en 1 lugar
#%%
import numpy as np

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
print(np.concatenate((x, y), axis=0)) #Concatena tambien

np.ndim(x) #Te dice la dimension de un array
#%%
import numpy as np

f = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(np.shape(f)) #Devuelve una tupla de ints que indican la cantidad de elementos en cada eje. Una matriz de 2 filas y 3 columnas va a dar (2,3)
print(np.size(f)) #Devuelve la cantidad de elementos (numeros) de mi array
#%%
import numpy as np

array_ejemplo = np.array([[[0, 1, 2, 3],
                            [4, 5, 6, 7]],

                           [[0, 1, 2, 3],
                            [4, 5, 6, 7]],

                           [[0 ,1 ,2, 3],
                            [4, 5, 6, 7]]])

print(array_ejemplo.ndim)
print(array_ejemplo.shape)
print(array_ejemplo.size)
#%%
import numpy as np

a = np.arange(6)
print(a)

b = a.reshape(3,2)
print(b)
#%%
import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
print('\na = ', a) 
print('\na shape = ', a.shape) #Devuelve la cantidad de elementos por eje

print("\n---------------")
vec_fila = a[np.newaxis, :] #Lo transforma en vector fila
print('\na [np.newaxis, :] = ', a[np.newaxis, :])
print('\nvec_fila = ', vec_fila.shape)

print("\n-------------------")
vec_col = a[:, np.newaxis]
print('\na [:,np.newaxis] = ', a[:, np.newaxis])
print('\nvec_col = ', vec_col.shape)

#%%
import numpy as np

data = np.array([1,2,3])
print('\nPosicion 1 = ',data[0]) #Se puede acceder a cada posicion como una lista
print('\nDesde pos -2 hasta el final = ', data[-2:]) #Se puede hacer slices como en las listas

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print('\nLos menores de 5 = ', a[a<5]) #Printea con una condicion

five_up = (a >= 5)
print('\nMayores iguales a 5 con una variable = ', a[five_up])

pares = a[a%2==0]
print('\nPares = ', pares)

c = a[(a > 2) & (a < 11)] #El '&' es "and" y '|' es "or"
print('\nCon una doble condicion usando un "and" = ', c)

five_up = (a > 5) | (a == 5) 
print('\nDefine variable valores bool que cumplen una condicion = ', five_up) #Define una nueva variable booleana

b = np.nonzero(a<5)
print('\nImprime los indices de los elementos que cumplen una condicion', b)
'''En este ejemplo, la respuesta es una tupla de arreglos: uno por cada dimensión. 
El primer arreglo representa las filas de los elementos que satisfacen la condición y el segundo sus columnas.'''

'''Si querés generar la lista de coordenadas donde se encuentran estos elementos, podés zipear los arreglos,
 convertir el resultado en una lista e imprimirla:'''

lista_de_coordenadas = list(zip(b[0], b[1]))
print('\nLista de coordenadas de lo anterior: \n',lista_de_coordenadas,'\n')
'''O puedo hacer lo mismo con un for y obtengo tuplas'''
for coord in lista_de_coordenadas:
    print(f'Lo mismo que antes pero con un for = {coord}')

print('\nO puedo (imprimir o seleccionar) los elementos que cumplen con lo que puse en la condicion de a = ',a[b])


no_hay = np.nonzero(a == 42)
print('\nSi la condicion que pongo no la satisface ningun elemento devuelve un arreglo vacio = ',no_hay)


#%%
import numpy as np

a = np.array([1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
arr1 = a[3:8]
print('Nuevo arreglo = ',arr1) #Nuevo arreglo de una seccion del anterior 
'''Es como un puntero (aca le dicen vistas), si lo modifico, modifico al original'''

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

b1 = a[0, :] #Creo a b1 apartir de un slice de a
b1[0] = 99 #Modifico la posicion 0 de b1

print(f'b1 = {b1} y a = {a}') #Modifico a ambos

'''Si uso el metodo copy, si se realiza una copia real y no modifica al que copia (xd)'''

#%% OPERACIONES BASICAS CON ARRAYS
import numpy as np

data = np.array([1, 2])
ones = np.ones(2, dtype=int)

print('\n data + ones = ', data + ones) #Suma
print('\n data - ones = ', data - ones) #Resta
print('\n data * data = ', data * data) #Multiplicacion
print('\n data / data = ', data / data) #Division

a = np.array([1, 2, 3, 4])
print('\n Suma de a con metodo sum', a.sum()) #Hace la suma de todo el array con el metodo sum

print('---------------')

b = np.array([[1, 1], [2, 2]])
b_col = b.sum(axis=0) #Suma los datos de cada COLUMNA
b_fil = b.sum(axis=1) #Suma los datos de cada FILA
print(f'\n b = \n{b}')
print(f'\n La suma de los elementos de cada columna de b es = {b_col}')
print(f'\n La suma de los elementos de cada fila de b es = {b_fil}')

data = np.array([1.0, 2.0])
escalar = (data * 1.6) #Multiplica a cada elemento por el escalar
print(f'Multiplico a {data} por un escalar y queda {escalar}')
'''Puedo hacer operaciones de este tipo en arreglos de diferentes tamaños, pero deben ser de tamaño compatibles ambos'''

#%% OPERACIONES INTERMEDIAS xd
'''En numpy puedo usar el metodo min(), max() y sum() entre otros
   Tambien puedo usar el metodo mean() #para obetener el promedio, prod() #para calcular el producto, std() #para obtener el desvio estandar de los datos, y mas.'''
import numpy as np

a = np.array([[0.45053314, 0.17296777, 0.34376245, 0.5510652],
              [0.54627315, 0.05093587, 0.40067661, 0.55645993],
              [0.12697628, 0.82485143, 0.26590556, 0.56917101]])

print(f'sum de a {a.sum()}')
print(f'\n min de a {a.min()}')
print(f'\n min de cada columna de a {a.min(axis = 0)}')


#%% MATRICES puedo usar una lista de listas para crear arreglos bidimensionales, osea matrices
import numpy as np

data = np.array([[1,2], [3,4]]) #Creo una matriz

data = np.array([[1, 2], [3, 4], [5, 6]]) #Creo una matriz xd
print('Matriz = \n', data)
print('\n Elemento [0, 1] mediante indexacion de la Matriz anterior = ', data[0, 1]) #Indezacion

print('\n Slice [1:3] de la matriz anterior\n', data[1:3])

'''Puedo usar los metodos max, min, sum'''

'''Puedo usar por fila o columna usando axis'''

print('\n Max de data = ',data.max())
print('\n Max elemento de cada columna = ', data.max(axis=0))
print('\n Max elemento de cada fila = ', data.max(axis=1))

#%% OPERACIONES CON MATRICES
import numpy as np

data = np.array([[1, 2], [3, 4]])
ones = np.array([[1, 1], [1, 1]])

print('M1 = \n', data)
print('M2 = \n', ones)
print('M1 + M2 = \n', data + ones)

'''Tambien se puede hacer como con los escalares, solo si tienen 1 fila O 1 columna'''

print('--------------------')

data = np.array([[1, 2], [3, 4], [5, 6]])
ones_row = np.array([[1, 1]])
print('M1 = \n', data)
print('M2 = \n', ones_row)
print('M1 + M2 = \n', data + ones_row)

print('--------------------')

a = np.ones(3) #Creo un arreglo con solo unos, le tengo que decir cuantos elementos quiero
print('\n Array solo uno con .ones', a)
a = np.zeros(3) #Creo un arreglo con solo ceros, le tengo que decir cuantos elementos quiero
print('\n Array solo ceros con .zeros', a)
a = np.random.default_rng(0) #Creo un generador de nums aleatorios
a.random(3) #Lo uso y le digo cuantos numeros aleatorios quiero
print('\n Array de numeros aleatorios', a.random(3))

print('--------------------')

'''Puedo usar lo anterior para usar matrices si le especifico la forma usando una tupla'''

print('\n Matriz usando .ones \n', np.ones((3,2)))
print('\n Matriz usando .zeros \n', np.zeros((3,2)))
print('\n Matriz usando random \n', a.random((3,2)))

#%% GUARDAR UNA MATRIZ EN UN ARCHIVO
import numpy as np

a = np.array([1,2,3,4,5,6])
np.save('array', a) #Guarda el archivo en binario .npy
b = np.load('array.npy') #Lo cargo y uso
print(b)

'''Lo puedo guardar en .csv o en .txt'''

csv_arr = np.array([1,2,3,4,5,6,7,8,9])
np.savetxt('new_file.csv', csv_arr) #Lo aguardo en .csv
csv = np.loadtxt('new_file.csv') #Lo cargo y uso
print(csv)