import csv

def parse_csv(nombre_archivo, select = None, types = None, has_headers = True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f) 
        if has_headers == True:
            encabezados = next(filas) # Lee los encabezados del archivo
            # Si se indicó un selector de columnas,
            #    buscar los índices de las columnas especificadas.
            # Y en ese caso achicar el conjunto de encabezados para diccionarios
            if select:
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                encabezados = select
            else:
                indices = []
                registros = []
            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
                if indices: # Filtrar la fila si se especificaron columnas
                    fila = [fila[index] for index in indices]
                if types:
                    fila = [func(val) for func, val in zip(types, fila) ]
                registro = dict(zip(encabezados, fila)) # Armar el diccionario
                registros.append(registro)
        else:
            registros=[]
            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
                if types:
                    fila = [func(val) for func, val in zip(types, fila) ]
                    registros.append(tuple(fila))
                    
    return registros

#camion = parse_csv('C:/Users/elcav/OneDrive/Documentos/Python/Curso Unsam/ejercicios_python/Data/camion.csv')
#precio = parse_csv('C:/Users/elcav/OneDrive/Documentos/Python/Curso Unsam/ejercicios_python/Data/precios.csv', types=[str,float], has_headers=False)