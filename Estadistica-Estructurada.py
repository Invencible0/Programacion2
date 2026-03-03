import math

def promedio(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    return suma / len(lista)

def Desviacion(lista):
    prom = promedio(lista)
    suma = 0
    for i in range(len(lista)):
        suma += (lista[i] - prom) ** 2
    return math.sqrt(suma / (len(lista) - 1))

n = list(map(float, input("ingrese 10 numeros: ").split()))

print("el promedio es", round(promedio(n), 2))
print("la desviacion estandar es", round(Desviacion(n), 5))