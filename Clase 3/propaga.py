def propagar(vector):
    tamaño = len(vector)
    for i, e in enumerate(vector):
        if e == 1: #Pregunta por cada posicion si es 1
             for j in range(i, -1, -1): #Recorre hacia atras
                 if vector[j] == -1: #Si es -1 sale del for
                     break
                 elif vector[j] == 0: #Si es 0 lo convierte en 1
                     vector[j] = 1
             for k in range(i, tamaño, 1): #Recorre hacia adelante
                if vector[k] == -1: #Si es -1 sale del for
                    break
                elif vector[k] == 0: #Si es 0 lo convierte en 1
                    vector[k] = 1
    return vector