#Ejercicio de errores en el código

#%% Ejercicio 3.1
#El error era que en el while se hacia la comparacion hasta el final de la cadena pero nunca se guarda el resultado total, solo el ultimo caracter
#Lo solucione iniciando la variable t en 'False' y si encontraba una 'a' (utilice el metodo lower por si habian mayusculas), convertia a la variable t en 'True'
#Luego devuelvo el valor de la variable t

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    t = False
    while i<n:
        if expresion[i].lower() == 'a':
            t = True
        i += 1
    return t   

print(tiene_a('UNSAM 2020'))

print(tiene_a('abracadabra'))

print(tiene_a('La novela 1984 de George Orwell'))

#%% Ejercicio 3.2
#Tiene un error de sintaxis invalida, le falta ':' luego de definir la función 'tiene_a', luego del 'while' y del 'if'. También esta mal la comparación en el 'if' ya que utiliza un solo '='
#en vez de dos. Además, retorna la variable 'Falso' que no esta declarada
#Solucione estos errores añadiendo ':' luego de la función, el 'while' y el 'if'. Además agregue el metodo 'lower' en la comparación para que considere el caso de una 'a' mayuscula e hice que
#retorne el estado 'False' en caso de que no encuentre una 'a' 



def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i].lower() == 'a':
            return True
        i += 1
    return False

print(tiene_a('UNSAM 2020'))
print(tiene_a('La novela 1984 de George Orwell'))

#%% Ejercicio 3.3
#Hay un TypeError ya que el tercer caso es un int (todo numeros) y los int no tiene la propiedad len()
#Lo solucione casteando a la variable expresione a una del tipo string

def tiene_uno(expresion):
    n = len(str(expresion))
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if str(expresion)[i] == '1':
            tiene = True
        i += 1
    return tiene


print(tiene_uno('UNSAM 2020'))
print(tiene_uno('La novela 1984 de George Orwell'))
print(tiene_uno(1984))

#%% Ejercicio 3.4
#El error es que se declara y asigna un valor a la variable c pero no es utiliza 
#Lo solucione retornando c

def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#%% Ejrcicio 3.5
#Habia un error en el cual se pisaban los datos, se terminaba guardando el ultimo valor que obtenian las varibles dentro del 'for'
#Para solucionarlo declare el diccionario 'registro' dentro del 'for' y luego agrego el valor a camion

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = {
                encabezado[0] : fila[0],
                encabezado[1] : int(fila[1]),
                encabezado[2] : float(fila[2])
                }
            camion.append(registro)
    return camion

camion = leer_camion("C:/Users/elcav/OneDrive/Documentos/Python/Curso Unsam/ejercicios_python/Data/camion.csv")
pprint(camion)