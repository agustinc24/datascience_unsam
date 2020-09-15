import csv

def leer_arboles(nombre_archivo):
    lista = []
    f = open(nombre_archivo, encoding="utf-8")
    rows = csv.reader(f)
    headers = next(rows)
    types = [float, float, int, int, int, int, int, str, str, str, str, str, str, str, str, float, float]
    for row in rows:
        lista.append({name: func(val) for name, func, val in zip(headers, types, row)})
    f.close()
    return lista
    
arboleda = leer_arboles('C:/Users/elcav/OneDrive/Documentos/Python/Curso Unsam/ejercicios_python/Data/arbolado.csv')

altura=[float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

diametro =[float(arbol['diametro']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

lista_dya = [x for x in zip(altura, diametro)]
 
print(lista_dya)