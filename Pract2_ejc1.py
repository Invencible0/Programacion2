import math

class MiPunto:
    
    # a) Constructor con valores por defecto
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    # b) Obtener coordenada X
    def getX(self):
        return self.__x

    # c) Obtener coordenada Y
    def getY(self):
        return self.__y

    # d) Distancia entre dos puntos
    def distancia(self, p):
        dx = self.__x - p.getX()
        dy = self.__y - p.getY()
        return math.sqrt(dx**2 + dy**2)

    # e) Distancia con coordenadas (x, y)
    def distanciaXY(self, x, y):
        dx = self.__x - x
        dy = self.__y - y
        return math.sqrt(dx**2 + dy**2)


# ===== PROGRAMA DE PRUEBA =====

# f) Crear objetos
p1 = MiPunto()
p2 = MiPunto(10, 30.5)

print("Punto 1:", p1.getX(), p1.getY())
print("Punto 2:", p2.getX(), p2.getY())

# g) Calcular distancia
print("Distancia =", p1.distancia(p2))