import csv

def costo_camion(nombre_archivo):
    f = open(nombre_archivo)
    filas = csv.reader(f)
    encabezados = next(filas)
    costo_total = 0
    records = []
    
    for n_fila, fila in enumerate(filas, start=1):
        record = dict(zip(encabezados, fila))
        records.append(record)
        try:
            ncajones = int(record['cajones'])
            precio = float(record['precio'])
            costo_total += ncajones * precio
            # Esto atrapa errores en los int() y float() de arriba.
        except ValueError:
            print(f'Fila {n_fila}: No pude interpretar: {fila}')
    return costo_total, records

costo, records = costo_camion('C:/Users/elcav/OneDrive/Documentos/Python/Curso Unsam/ejercicios_python/Data/fecha_camion.csv')

print('Costo total:', costo)