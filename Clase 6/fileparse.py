#fileparse clase 6
import csv

def parse_csv(nombre_archivo, select = None, types = None, has_headers = True, silence_errors = False):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    if select and has_headers == False and silence_errors:
        raise RuntimeError("Para seleccionar, necesito encabezados.")
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
            for i, fila in enumerate(filas):
                try:
                    if not fila:    # Saltear filas vacías
                        continue
                    if indices: # Filtrar la fila si se especificaron columnas
                        fila = [fila[index] for index in indices]
                    if types:
                        fila = [func(val) for func, val in zip(types, fila) ]
                    registro = dict(zip(encabezados, fila)) # Armar el diccionario
                    registros.append(registro)
                except ValueError as e:
                    if not silence_errors:
                        print(f'Row {i+1}: No pude convertir {fila} \n')
                        print(f'Row {i+1}: Motivo: {e} \n')
        else:
            registros=[]
            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
                if types:
                    fila = [func(val) for func, val in zip(types, fila) ]
                    registros.append(tuple(fila))
                    
    return registros

#lo de cmd
#python3 -i C:/Users/elcav/OneDrive/Documentos/Python/Curso Unsam/ejercicios_python/Clase 6/informe.py C:/Users/elcav/OneDrive/Documentos/Python/Curso Unsam/ejercicios_python/Data/camion.csv C:/Users/elcav/OneDrive/Documentos/Python/Curso Unsam/ejercicios_python/Data/precios.csv