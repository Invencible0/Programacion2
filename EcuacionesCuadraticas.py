import math

class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getDiscriminante(self):
        return self.b**2 - 4*self.a*self.c

    def getRaiz1(self):
        d = self.getDiscriminante()
        if d >= 0:
            return (-self.b + math.sqrt(d)) / (2*self.a)
        else:
            return 0

    def getRaiz2(self):
        d = self.getDiscriminante()
        if d >= 0:
            return (-self.b - math.sqrt(d)) / (2*self.a)
        else:
            return 0


n = input("ingrese a, b, c: ").split()
a = float(n[0])
b = float(n[1])
c = float(n[2])

ecuacion = EcuacionCuadratica(a, b, c)
discriminante = ecuacion.getDiscriminante()

if discriminante > 0:
    print("la ecuacion tiene 2 raices",
          round(ecuacion.getRaiz1(), 6),
          "y",
          round(ecuacion.getRaiz2(), 6))

elif discriminante == 0:
    print("la ecuacion tiene una raiz",
          round(ecuacion.getRaiz1(), 6))

else:
    print("la ecuacion no tiene raices solucion")