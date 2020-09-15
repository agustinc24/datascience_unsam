import random

def tirar():
    tira = [random.randint(1,6) for i in range(5)]
    return tira

def es_generala(tiro):
    valor = True
    for i, e in enumerate(tiro):
        if tiro[i] != tiro[i-1]:
            valor = False
            break
    return valor

N = 10000
G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')