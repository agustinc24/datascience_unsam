def costo_camion(nombre_archivo):
    try:
        with open(nombre_archivo,'rt') as f:
            next(f)
            acum = 0
            for line in f:
                row = line.split(',')
                acum += float(row[1])*float(row[2])
            return(round(acum,2))
    except:
        with open(nombre_archivo,'rt') as f:
            next(f)
            acum = 0
            for line in f:
                row = line.split(',')
                if row[1]:
                    acum += float(row[1])*float(row[2])
        print("Cuidado hubo un error del tipo value, puede que los datos no sean exactos.")
        return(round(acum,2))

costo = costo_camion('C:/Users/elcav/OneDrive/Documentos/Python/Curso Unsam/ejercicios_python/Data/missing.csv')
print('Costo total:', costo)