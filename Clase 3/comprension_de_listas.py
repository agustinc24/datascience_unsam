import csv

def leer_camion(nombre_archivo):
    '''Lee un archivo y lo almacena en un diccionario,
    tambien calcula el precio y lo devuelve'''
    f = open(nombre_archivo, 'r')
    rows = csv.reader(f)
    next(f)
    total = 0.0
    lista_camion = []
    for row in rows:
        camion = { 
            'Nombre': row[0],
            'Cajones': int(row[1]),
            'Precio': float(row[2])
            }
        lista_camion.append(dict(camion))
        total += camion['Cajones']*camion['Precio']
    f.close()
    return(lista_camion)

def leer_precios(nombre_archivo):
    '''Lee un archivo y lo almacena en un diccionario'''
    dicc_precio = {}
    f = open(nombre_archivo, 'r')
    rows = csv.reader(f)
    try:
        for i, row in enumerate(rows, start=1):
            dicc_precio[row[0]] = float(row[1])
    except IndexError:
        print("La fila", i, "del archivo está vacía.\n")   
    return dicc_precio

camion_lista = leer_camion('C:/Users/elcav/OneDrive/Documentos/Python/Curso Unsam/ejercicios_python/Data/camion.csv')

costo = sum ([s['Cajones'] * s['Precio'] for s in camion_lista])

precio = leer_precios('C:/Users/elcav/OneDrive/Documentos/Python/Curso Unsam/ejercicios_python/Data/precios.csv')

valor = sum([ s['Cajones'] * precio[s['Nombre']] for s in camion_lista])

costo10k = [s for s in camion_lista if s['Cajones'] * s['Precio'] > 10000]

myn = [ s for s in camion_lista if s['Nombre'] in {'Mandarina','Naranja'} ]

print(myn)

print(costo10k) #Las frutas que costaron mas de 10.000

print(valor)

print(costo)








