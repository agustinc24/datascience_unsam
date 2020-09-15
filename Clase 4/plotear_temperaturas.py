import numpy as np
import matplotlib.pyplot as plt

temperaturas = np.load('C:/Users/elcav/OneDrive/Documentos/Python/Curso Unsam/ejercicios_python/Data/Temperaturas.npy') #Carga del vector con las temperaturas

plt.hist(temperaturas,bins=50) #Histograma de las temperaturas