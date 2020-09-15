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
    return(total, lista_camion)

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

def venta(camion, precio):
   vent = 0
   for i in camion:
       if i['Nombre'] in precio:
           vent += (i['Cajones'] * precio.get(i['Nombre']))
   return vent

def f_balance(costo, recaudo):
    diferencia = recaudo - costo
    if recaudo > costo:
        print(f'Hubo una ganancia total de: ${diferencia:0.2f}\n')
    elif recaudo < costo:
        print(f'Hubo una perdida total de: ${diferencia:0.2f}\n')
    else:
        print("No hubieron ganancias ni perdidas, se cubrio el total de lo que costo el camion.\n")
                           
costo, camion_lista = leer_camion('C:/Users/elcav/OneDrive/Documentos/Python/Curso Unsam/ejercicios_python/Data/camion.csv') #En costo guardo lo gastado en la compra de los elementos en camion_lista

precio = leer_precios('C:/Users/elcav/OneDrive/Documentos/Python/Curso Unsam/ejercicios_python/Data/precios.csv')

recaudo_venta = venta(camion_lista, precio) #Calculo lo recaudado en la venta

print(f'El costo total es de: ${costo}\n')

print(f'El total recaudado es de: ${recaudo_venta}\n')

balance = f_balance(costo, recaudo_venta)






