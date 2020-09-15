import numpy as np
import matplotlib.pyplot as plt
import random
from copy import copy

def crear_album(figus_total):
    '''Crea un album vacio'''
    return np.zeros(figus_total)

def album_incompleto(A):
    '''Devuelve False si NO esta vacio, y True SI esta vacio'''
    if A.all():
        return False
    else:
        return True

def comprar_figu(figus_total):
    '''Genera una figurita desde 0 hasta el total'''
    return random.randint(0, figus_total-1)

def cuantas_figus(figus_total):
    '''Genera un album vacio, genera una figurita, llena el album y devuelve la cantidad de figuritas necesitadas'''
    album = crear_album(figus_total)
    total = 0
    while album_incompleto(album) == True:
        compra = comprar_figu(figus_total)
        album[compra] += 1
        total += 1
    return total

def comprar_paquete(figus_total, figus_paquete):
    '''Genera un paquete dado la cantidad de figuritas que tiene el paquete y el total de figuritas'''
    paq = [int(random.randint(0,figus_total-1)) for i in range(figus_paquete)]
    return paq

def cuantos_paquetes(figus_total, figus_paquete):
    '''Genera un album vacio, genera un paquete, llena el album y devuelve la cantidad de paquetes necesitados'''
    album = crear_album(figus_total)
    total = 0
    while album_incompleto(album) == True:
        paquete = comprar_paquete(figus_total, figus_paquete)
        for i in paquete:
            album[i] += 1
        total += 1
    return total

def no_repetidas(paquete):
    '''Devuelve False en caso de que hayan repetidas, sino True'''
    for i in paquete:
       if paquete.count(i) > 1:
           return False
    return True
        
def paquetes_norep(figus_total, figus_paquete):
    '''Genera un album vacio, genera un paquete, llena el album y devuelve la cantidad de paquetes necesitados'''
    album = crear_album(figus_total)
    total = 0
    while album_incompleto(album) == True:
        paquete = comprar_paquete(figus_total, figus_paquete)
        if no_repetidas(paquete):
            for i in paquete:
                album[i] += 1
        total += 1
    return total

def cuantos_paquetes_5amigos(figus_total, figus_paquete):
    '''Calcula los paquetes si son 5 amigos'''
    album1 = crear_album(figus_total)
    album2 = crear_album(figus_total)
    album3 = crear_album(figus_total)
    album4 = crear_album(figus_total)
    album5 = crear_album(figus_total)
    total = 0
    while(album_incompleto(album1) or album_incompleto(album2) or album_incompleto(album3) or album_incompleto(album4) or album_incompleto(album5)):
        paquete = comprar_paquete(figus_total, figus_paquete)
        for i in paquete:
            if album1[i] == 0:
                album1[i] += 1
            elif album2[i] == 0:
                album2[i] += 1
            elif album3[i] == 0:
                album3[i] += 1
            elif album4[i] == 0:
                album4[i] += 1
            elif album5[i] == 0:
                album5[i] += 1
        total += 1        
    return total


n_repeticiones = 1
figus_total = 670
figus_paquete = 5

cuantas_figs = [cuantas_figus(figus_total) for i in range(n_repeticiones)] #Calcula cuantas figuritas sueltas se necesitan para llenar un album
prom_figs = np.mean(cuantas_figs) #Calcula el promedio de figuritas necesitadas
print(f'\nSe necesitan {cuantas_figs} figuritas para llenar el album de {figus_total} figuritas comprandolas sueltas.\n')
print(f'El promedio de figuritas necesitadas para llenar el album de {figus_total} figuritas es {prom_figs}.\n')

cuantos_paqs = [cuantos_paquetes(figus_total, figus_paquete) for i in range(n_repeticiones)] #Calcula cuantos paquetes se necesitan para llenar un album
prom_paqs = np.mean(cuantos_paqs) #Calcula el promedio de paquetes necesitados
print(f'Se necesitan {cuantos_paqs} paquetes para llenar el album de {figus_total} figuritas.\n')
print(f'El promedio de paquetes necesitados para llenar el album de {figus_total} figuritas es {prom_paqs}.\n')

paquetes_hasta_llenar = np.array(cuantos_paqs)
paqs_850 = (paquetes_hasta_llenar <= 850).sum()
prom_paqs_850 = (float(paqs_850) / float(n_repeticiones))
print(f'La probabilidad de llenar un album de {figus_total} con 850 paquetes o menos es de {prom_paqs_850}.\n')

paqs_90 = int((90*np.mean(cuantos_paqs))/100) #Probabilidad del 90%
print(f'Para tener una probabilidad del 90% de llenar un album de {figus_total} se deberian comprar {paqs_90} paquetes.\n')

cuantos_paqs_norep = [paquetes_norep(figus_total, figus_paquete) for i in range(n_repeticiones)] #Calcula cuantos paquetes sin repetidas se necesitan para llenar un album
prom_paqs_norep = np.mean(cuantos_paqs_norep) #Calcula el promedio de paquetes sin repetidas necesitados
print(f'El promedio de paquetes sin figuritas repetidas necesitados para llenar el album de {figus_total} figuritas es {prom_paqs_norep}.\n')

cuantos_paqs_5amigos = [cuantos_paquetes_5amigos(figus_total, figus_paquete) for i in range(n_repeticiones)] #Calcula cuantos paquetes necesitan para llenar un album entre los 5 amigos
print(f'Para que los 5 amigos llenen un album de {figus_total} figuritas deberian comprar {cuantos_paqs_5amigos} paquetes.\n')

plt.hist(cuantos_paqs, bins = 50) #Histograma con la cantidad de paquetes que se compraron



















