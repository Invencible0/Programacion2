import math

class Estadistica:
    def __init__(self, n):
        self.n = n

    def promedio(self):
        suma = 0
        for i in range(len(self.n)):
            suma += self.n[i]
        return suma / len(self.n)

    def Desviacion(self):
        prom = self.promedio()
        suma = 0
        for i in range(len(self.n)):
            suma += (self.n[i] - prom) ** 2
        return math.sqrt(suma / (len(self.n) - 1))


n = list(map(float, input("ingrese 10 numeros: ").split()))

estadistica = Estadistica(n)

print("el promedio es", round(estadistica.promedio(), 2))
print("la desviacion estandar es", round(estadistica.Desviacion(), 5))