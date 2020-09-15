import csv

def leer_camion(nombre_archivo):
    '''Lee un archivo y lo almacena en un diccionario,
    tambien calcula el precio y lo devuelve'''
    f = open(nombre_archivo, 'r')
    rows = csv.reader(f)
    next(f)
    lista_camion = []
    for row in rows:
        camion = { 
            'Nombre': row[0],
            'Cajones': int(row[1]),
            'Precio': float(row[2])
            }
        lista_camion.append(dict(camion))
    f.close()
    return(lista_camion)


camion = leer_camion('C:/Users/elcav/OneDrive/Documentos/Python/Curso Unsam/ejercicios_python/Data/camion.csv')

nombre_cajones = [(s['Nombre'], s['Cajones']) for s in camion] #Devuelve una lista de tuplas (nombre, cajon) de la lista camion
#print(nombre_cajones)

nombres = {s['Nombre'] for s in camion} #Devuelve un conjunto de los nombres de la lista camiob
#print("\n",nombres)

stock = {Nombre: 0 for Nombre in nombres} #Creo un diccionario por compresion con pares 'clave:valor' iniciandolos en 0
for s in camion:
        stock[s['Nombre']] += s['Cajones'] #Le agrega la cantidad de cajones al elemento buscado


print("\n", stock)






