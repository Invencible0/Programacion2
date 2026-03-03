class EcuacionLineal:

    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def tieneSolucion(self):
        return (self.__a * self.__d - self.__b * self.__c) != 0

    def getX(self):
        return (self.__e * self.__d - self.__b * self.__f) / (self.__a * self.__d - self.__b * self.__c)

    def getY(self):
        return (self.__a * self.__f - self.__e * self.__c) / (self.__a * self.__d - self.__b * self.__c)


# -----------------------
# Programa de prueba
# -----------------------

n = input("Ingrese a, b, c, d, e, f: ").split()

a = float(n[0])
b = float(n[1])
c = float(n[2])
d = float(n[3])
e = float(n[4])
f = float(n[5])

ecuacion = EcuacionLineal(a, b, c, d, e, f)

if ecuacion.tieneSolucion():
    print("X =", ecuacion.getX(), "Y =", ecuacion.getY())
else:
    print("La ecuación no tiene solución")