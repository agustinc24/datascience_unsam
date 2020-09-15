from fileparse import parse_csv

def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    precios = leer_precios(nombre_archivo_precios)
    camion = leer_camion(nombre_archivo_camion)
    informe = Informe(camion, precios)
    titulos = d_titulos()
    p_titulos(titulos)
    p_lineas()
    imprimir_informe(informe)
            
def leer_camion(nombre_archivo):
        camion = parse_csv(nombre_archivo, types = [str, int, float])
        return camion
    
def leer_precios(nombre_archivo):
        precio = parse_csv(nombre_archivo, types = [str, float], has_headers = False)
        return precio

def Informe(camion, precios):
        camion_ = []
        for fila in camion:
            for i, j in enumerate(precios):
                if fila['nombre'] in precios[i]:
                    tupla_cajones = (fila['nombre'], fila['cajones'], fila['precio'], abs((fila['precio'] - precios[i][1])))
                    camion_.append(tupla_cajones)
        return camion_
    
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
    

informe_camion('C:/Users/elcav/OneDrive/Documentos/Python/Curso Unsam/ejercicios_python/Data/camion.csv', 'C:/Users/elcav/OneDrive/Documentos/Python/Curso Unsam/ejercicios_python/Data/precios.csv') 