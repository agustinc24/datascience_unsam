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

def generala(tiro):
    if es_generala(tiro):
        return True
    numeros = [{'Num':s+1, 'Cant':0} for s in range(6)] #Creo una lista de diccionarios con cada numero y la cantidad de veces que aparece
    for i in numeros: #Recorro la lista de diccionarios
        for k in tiro: 
            if k == i['Num']: #Compara si el valor que salio en el tiro es igual al elemento de mi diccionario
                i['Cant'] +=1 #Si es, suma en 1 la cantidad que aparece (por defecto es 0)
    num = numeros[0] #Guardo la posicion 0 de mi list de dicts para luego compararla
    for i in numeros:
        if i['Cant']>num['Cant']: #Compra si cada posicion de lista tiene mas cantidad que la que puse antes
            num=i #Si tiene mas, la cambia
    for k in range(2): #Hace 2 tiradas mas
        for j,i in enumerate(tiro):
            if i != num['Num']: #Compara si el elemento del tiro es distinto del que mas aparece
                tiro[j] = random.randint(1,6) #Si es otro, lo vuelve a tirar
    valor = es_generala(tiro)
    return valor

N = 10000
G = sum([generala(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala.')
print(f'Podemos estimar la probabilidad de sacar generala en: {prob:.6f}.')