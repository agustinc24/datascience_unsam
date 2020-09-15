def busqueda_lineal(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z == e or z > e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
    return pos

def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print('[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos

def buscar_u_elemento(lista, e):
    pos = -1
    for i, z in enumerate(lista):
        if z == e:
            pos = i
            
    if pos != -1:
        return (f'El elemento {e} aparece por ultima vez en la posición {pos} de la lista {lista} \n')
    else:
        return (f'El elemento {e} no aparece en la lista {lista} \n')

def buscar_n_elemento(lista, e):
    cant = 0
    for z in lista:
        if z == e:
            cant += 1
            
    if cant != 0:
        return (f'El elemento {e} aparece {cant} veces en la lista {lista} \n')
    else:
        return (f'El elemento {e} no aparece en la lista {lista} \n')

def maximo(lista):
    '''Una funcion que busca el elemento maximo positivo de una lista, si no lo encuentra devuelve 0'''
    m = 0
    for e in lista:
        if e>0 and e > m:
            m = e
    return m

def minimo(lista):
    '''Busca el elemento minimo de una lista, si la lista esta vacia devuelve False '''
    m = False
    if lista:
        m = lista[0]
    for e in lista:
        if e < m:
            m = e
    return m

def invertir_lista(lista):
    pass

#%%% Ejercicio 3.6

print(buscar_u_elemento([1,2,3,2,3,4],1))
print(buscar_u_elemento([1,2,3,2,3,4],2))
print(buscar_u_elemento([1,2,3,2,3,4],3))
print(buscar_u_elemento([1,2,3,2,3,4],5))

print(buscar_n_elemento([1,2,3,2,3,4],1))
print(buscar_n_elemento([1,2,3,2,3,4],2))
print(buscar_n_elemento([1,2,3,2,3,4],3))
print(buscar_n_elemento([1,2,3,2,3,4],5))

#%% Ejercicio 3.7

print(maximo([1,2,7,2,3,4]))
print(maximo([1,2,3,4]))
print(maximo([-5,4]))
print(maximo([-5,-4]))

print(minimo([1,2,7,2,3,4]))
print(minimo([1,2,3,4]))
print(minimo([-5,4]))
print(minimo([-5,-4]))