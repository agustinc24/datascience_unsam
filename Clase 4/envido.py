import random

def baraja():
    valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    palos = ['oro', 'copa', 'espada', 'basto']
    naipes = [(valor,palo) for valor in valores for palo in palos]
    return naipes

def envido_31(mano):
    envi = False
    siete = [4,7]
    cinco = [5,6]
    for i in range(3):
        if mano[i][1] == mano[i-1][1] and mano[i][0] in siete and mano[i-1][0] in siete:
            envi = True
        elif mano[i][1] == mano[i-1][1] and mano[i][0] in cinco and mano[i-1][0] in cinco:
            envi = True
    return envi

def envido_32(mano):
    envi = False
    siete = [5,7]
    for i in range(3):
        if mano[i][1] == mano[i-1][1] and mano[i][0] in siete and mano[i-1][0] in siete:
            envi = True
    return envi

def envido_33(mano):
    envi = False
    siete = [6,7]
    for i in range(3):
        if mano[i][1] == mano[i-1][1] and mano[i][0] in siete and mano[i-1][0] in siete:
            envi = True
    return envi

cartas = baraja()

n = 1000000
caso_31 = sum([envido_31(random.sample(cartas,k=3)) for i in range(n)])
prob = caso_31/n

print(f'Tiré {n} veces, de las cuales {caso_31} saqué 31 de envido.')
print(f'Podemos estimar la probabilidad de sacar 31 de envido en: {prob:.6f}.')

caso_32 = sum([envido_32(random.sample(cartas,k=3)) for i in range(n)])
prob = caso_32/n

print(f'Tiré {n} veces, de las cuales {caso_32} saqué 32 de envido.')
print(f'Podemos estimar la probabilidad de sacar 32 de envido en: {prob:.6f}.')

caso_33 = sum([envido_33(random.sample(cartas,k=3)) for i in range(n)])
prob = caso_33/n

print(f'Tiré {n} veces, de las cuales {caso_33} saqué 33 de envido.')
print(f'Podemos estimar la probabilidad de sacar 33 de envido en: {prob:.6f}.')