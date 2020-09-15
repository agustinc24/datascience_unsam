import csv
import sys

def costo_camion(nombre_archivo):
    try:
        f = open(nombre_archivo)
        rows = csv.reader(f)
        acum = 0
        next(f)
        for line in rows:
                acum += float(line[1])*float(line[2])
        f.close()
        return(acum)
    except:
        f = open(nombre_archivo)
        rows = csv.reader(f)
        acum = 0
        next(f)
        for line in rows:
            if line[1]:
                acum += float(line[1])*float(line[2])
        f.close()
        print("Cuidado hubo un error del tipo value, puede que los datos no sean exactos.")
        return(acum)

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = 'C:/Users/elcav/OneDrive/Documentos/Python/Curso Unsam/ejercicios_python/Data/camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)