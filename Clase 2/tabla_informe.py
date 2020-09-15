import csv

def leer_camion(nombre_archivo):
        camion = []
        dicc_costo = {}
        f = open (nombre_archivo)
        fila = csv.reader(f)
        encabezados = next(fila)
        for fi in fila:
            record = dict(zip(encabezados,fi))
            dicc_costo['nombre'] = record['nombre']
            dicc_costo['cajones'] = int(record['cajones'])
            dicc_costo['precio'] = float(record['precio'])
            camion.append(dicc_costo.copy())
        f.close()
        return camion
    
def leer_precios(nombre_archivo):
        dicc_precio = {}
        f = open(nombre_archivo, 'r')
        rows = csv.reader(f)
        try:
            for i, row in enumerate(rows, start=1):
                dicc_precio[row[0]] = float(row[1])
                
        except IndexError:
            print ("La fila", i, "del archivo está vacía.")   
        return dicc_precio
    
def costo_camion(camion):
        costo_cam = 0.0
        for c in camion:
            costo_cam += c['cajones'] * c['precio']
        return costo_cam
    
def recaudacion_venta(precios, camion):
        venta_tot = 0.0
        for c in camion:
            if c['nombre'] in precios:
                venta_tot += (c['cajones'] * precios.get(c['nombre']))
        return venta_tot
    
def diferencia_balance(costo, venta):
        dif = venta - costo 
        if venta > costo:
            print("Hubo una ganancia de $", dif)
        else:
            print("Hubo una pérdida de $", dif)
            
def Informe(camion, precios):
    
        camion_ = []
        for fila in camion:
            if fila['nombre'] in precios:
                tupla_cajones = (fila['nombre'], fila['cajones'], fila['precio'], abs((fila['precio'] - precios[fila['nombre']])))
                camion_.append(tupla_cajones)
        return camion_
                
def p_costo(costo):
        print("El Costo Total es: $", costo)
    
def p_recaudado(venta):
        print("Lo recaudado es: $", venta)
    
def d_titulos():
        return ['Nombre', 'Cajones', 'Precio', 'Cambio']
    
def p_titulos(titulos):
        for t in titulos :
            print(f'{t:>10s}', end=' ')
    
def p_lineas():
        print('\n---------- ---------- ---------- ----------')
    
def imprimir_informe(informe):
        for nombre,cajones,precio,cambio in informe:
            aux_precio = '$' + f'{precio}'
            print(f'{nombre:>10s} {cajones:>10d} {aux_precio:>10s} {cambio:>10.2f}')
        
    
precios = leer_precios('C:/Users/elcav/OneDrive/Documentos/Python/Curso Unsam/ejercicios_python/Data/precios.csv')
    
camion = leer_camion('C:/Users/elcav/OneDrive/Documentos/Python/Curso Unsam/ejercicios_python/Data/camion.csv')        
    
costo = costo_camion(camion)
    
venta = recaudacion_venta(precios, camion)
    
p_costo(costo)
    
p_recaudado(venta)
    
diferencia_balance(costo, venta)
    
informe = Informe(camion, precios)
    
#...............Ejercicio: 2.34................................
    
titulos = d_titulos()
    
p_titulos(titulos)
    
p_lineas()
    
imprimir_informe(informe)
    