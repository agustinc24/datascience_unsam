import csv
from collections import Counter
import os
import matplotlib.pyplot as plt
import numpy as np

# Ejercicio 2.22: Lectura de los árboles de un parque

def leer_parque(nombre_archivo,nombre_parque):
    parque_esp = []
    with open(nombre_archivo,encoding='utf8') as f:
        rows = csv.reader(f)
        encabezados = next(rows)
        for i, row in enumerate(rows):
            record = dict(zip(encabezados,row))
            try:
                if record['espacio_ve'] == nombre_parque:
                    parque_esp.append(record)
            except ValueError:
                print(f' Fila {i}: No se puede interpretar: {row}')
        
        return parque_esp
    
# Ejercicio 2.23: Determinar las especies en un parque

def especies(lista_arboles):
    especies = set ()
    especies_unicas = set()
    for p in lista_arboles:
        especies.add(p['nombre_com'])
    especies_unicas = set(especies)
    
    return especies_unicas

# Ejercicio 2.24: Contar ejemplares por especie     

def contar_ejemplares(lista_arboles):
    Cant_ejemplares = Counter()
    for arbol in lista_arboles:
        Cant_ejemplares[arbol['nombre_com']] += 1
        
    return Cant_ejemplares

# Ejercicio 2.25: Alturas de una especie en una lista

def obtener_alturas(lista_arboles, especie):
    lista_altura = []
    
    for arbol in lista_arboles:
        if especie in arbol['nombre_com']:
            lista_altura.append(float(arbol['altura_tot']))
    
    return lista_altura


# Ejercicio 2.26: Inclinación promedio por especie de una lista

def obtener_inclinaciones(lista_arboles, especie):
    inclinaciones = []
    for arbol in lista_arboles:
        if especie in arbol['nombre_com']:
            inclinaciones.append(float(arbol['inclinacio']))
            
    return inclinaciones

# Ejercicio 2.27: Especie con el ejemplar más inclinado

def especimen_mas_inclinado(lista_arboles):
    especie = especies(lista_arboles)
    inclinacion=0.0
    for arbol in especie:
        maximo = max(obtener_inclinaciones(lista_arboles, arbol))
        if maximo>inclinacion:
            inc_max = maximo
            espec_max = arbol
            
    return((inc_max,espec_max))
        
# Ejercicio 2.28: Especie con más inclinada en promedio

def especie_promedio_mas_inclinada(lista_arboles):
    especie = especies(lista_arboles)
    incli_prom_max = 0.0
    max_arb = especie
    for arbol in especie:
        lista_incli = obtener_inclinaciones(lista_arboles,arbol)
        incli_prom = sum(lista_incli)/len(lista_incli)

        if incli_prom > incli_prom_max:
            max_arb = arbol
            incli_prom_max = incli_prom
    
    return ((incli_prom_max,max_arb))

# Ejercicio 3.18: Lectura de todos los árboles

def leer_arboles(nombre_archivo):
    arboleda = []
    with open(nombre_archivo,encoding='utf8') as f:
        rows = csv.reader(f)
        encabezados = next(rows)
        for i, row in enumerate(rows):
            record = dict(zip(encabezados,row))
            arboleda.append(record)     
    return arboleda

# Ejercicio 3.21: Diccionario con medidas

def medidas_de_especies(especies,arboleda):
     dic = {especie: 0 for especie in especies}
     for especie in especies:
         dic[especie] = list((float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie)
         
     return dic
                      
#%% Ejercicio 3.18: Lectura de todos los árboles

arboleda = leer_arboles('C:/Users/elcav/OneDrive/Documentos/Python/Curso Unsam/ejercicios_python/Data/arbolado-en-espacios-verdes.csv')


#%% Ejercicio 4.30: Histograma de altos de Jacarandás

os.path.join('Data','C:/Users/elcav/OneDrive/Documentos/Python/Curso Unsam/ejercicios_python/Data/arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles('C:/Users/elcav/OneDrive/Documentos/Python/Curso Unsam/ejercicios_python/Data/arbolado-en-espacios-verdes.csv')
altos = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
plt.hist(altos,bins=10)

#%% Ejercicio 4.31: Scatterplot (diámetro vs alto) de Jacarandás

altydiam_jacaranda = [(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
vector = np.array(altydiam_jacaranda)
print(vector)

h = vector[:,[0]]
d = vector[:,[1]]

plt.scatter(d,h,c='#d62728',alpha=0.04)
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para Jacarandás")
'''
Es parecido a un gráfico lineal, ya que a medida que vas achicando el alpha
se nota como se forma una linea
'''

#%% Ejercicio 4.32: Scatterplot para diferentes especies

os.path.join('Data', 'C:/Users/elcav/OneDrive/Documentos/Python/Curso Unsam/ejercicios_python/Data/arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles('C:/Users/elcav/OneDrive/Documentos/Python/Curso Unsam/ejercicios_python/Data/arbolado-en-espacios-verdes.csv')
Especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
medidas = medidas_de_especies(Especies, arboleda)

for i in medidas:    
    vector=np.array(medidas[i])     
    h=vector[:,[0]]     
    d=vector[:,[1]]  
    colors = np.random.rand(len(h))
    plt.scatter(d,h,c=colors,alpha=0.03)     
    plt.xlabel("diametro (cm)")     
    plt.ylabel("alto (m)")     
    titulo=("Relación diámetro-alto para:"+i)     
    plt.title(titulo)
    plt.xlim(0,100) 
    plt.ylim(0,40) 
    plt.show()
    
# ¿Se mantienen las relaciones que viste en el ejercicio anterior para las tres especies? 
'''Se mantiene la relacion solo para  el jacaranda y el palo borracho'''
#¿Hay diferencias entre las especies? Para un mismo alto
''' Para un mismo alto hay diferencias en el diametro '''
#¿cuál tiene mayor diámetro (tipicamente)?
'''El de mayor diametro es el eucalipto'''