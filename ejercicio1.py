#Escriba el codigo necesario para que al ejecutar
#python ejercicio1.py se impriman los enteros del 10 al 1 en cuenta regresiva.

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

a=[10, 25,24,223,23,24,52,5,6,7,8,8,9,9,9,9]
b=[10, 25,24,223,23,24,52,5,6,7,8,8,9,9,9,9]
plt.figure()
plt.scatter(a,b)
plt.savefig("prueba.pdf")