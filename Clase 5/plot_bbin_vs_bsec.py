import matplotlib.pyplot as plt
import numpy as np
import random
#%% Ejercicio 5.17: Búsqueda binaria vs. búsqueda secuencial
def generar_lista(n, m):
    l = random.sample(range(m), k = n)
    l.sort()
    return l

def generar_elemento(m):
    return random.randint(0, m-1)

def busqueda_secuencial_(lista, x):
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps

def busqueda_binaria(lista, x):
    izq = 0
    der = len(lista) - 1
    comps = 0
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == x:
            comps += 1
            return comps
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
            comps += 1
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
            comps += 1
    return comps

def experimento_secuencial_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom

def experimento_binario_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria(lista,x)
    
    return comps_tot / k    

m = 10000
k = 1000

largos = np.arange(256) + 1 # estos son los largos de listas que voy a usar
comps_promedio = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.
comps_prom_binario = np.zeros(256)
for i, n in enumerate(largos):
    lista = generar_lista(n, m) # genero lista de largo n
    comps_promedio[i] = experimento_secuencial_promedio(lista, m, k)
    comps_prom_binario[i] = experimento_binario_promedio(lista, m, k)

# ahora grafico largos de listas contra operaciones promedio de búsqueda.
plt.plot(largos,comps_promedio,label = 'Búsqueda Secuencial')
plt.plot(largos,comps_prom_binario,label = 'Búsqueda Binaria')
plt.xlim(0,20)
plt.ylim(0,20)
plt.xlabel("Largo de la lista")
plt.ylabel("Cantidad de comparaiciones")
plt.title("Complejidad de la Búsqueda")
plt.legend()

#%% Conclusión:
    #Observo que la Búsqueda Secuencial tiene una extrema complejidad comparado a la Binaria.
    #Son algoritmos que llegan a un mismo resultado, pero su complejidad es completamente diferente. 