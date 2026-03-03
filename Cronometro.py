import time
import random

class Cronometro:
    def __init__(self):
        self.__inicia = time.time()
        self.__finaliza = None

    def get_inicia(self):
        return self.__inicia

    def get_finaliza(self):
        return self.__finaliza

    def iniciar(self):
        self.__inicia = time.time()
        self.__finaliza = None

    def detener(self):
        self.__finaliza = time.time()

    def lapsoDeTiempo(self):
        if self.__finaliza is None:
            return (time.time() - self.__inicia) * 1000
        return (self.__finaliza - self.__inicia) * 1000


def ordenacion(lista):
    for i in range(len(lista)):
        menor = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[menor]:
                menor = j
        aux = lista[i]
        lista[i] = lista[menor]
        lista[menor] = aux


# Programa de prueba
numeros = []

for i in range(1000):
    numeros.append(random.randint(1, 10000000))

cronometro = Cronometro()
cronometro.iniciar()
print("Ordenando...")
ordenacion(numeros)
cronometro.detener()

print("Tiempo en milisegundos:", cronometro.lapsoDeTiempo())