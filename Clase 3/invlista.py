# Ejercicio 3.8
#Devuelve una lista con sus elementos invertidos

def invertir_lista(lista):
    invertida = []
    tamaño = len(lista)
    for e in range(tamaño, 0, -1):
        invertida.append(lista[e-1])
    return invertida

print(invertir_lista([1, 2, 3, 4, 5]))

print(invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']))