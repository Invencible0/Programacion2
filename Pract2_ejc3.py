import math

class Vector3D:

    # a) Constructor
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # b) Suma
    def __add__(self, v):
        return Vector3D(
            self.x + v.x,
            self.y + v.y,
            self.z + v.z
        )

    # c) Multiplicación escalar
    def escalar(self, r):
        return Vector3D(
            r*self.x,
            r*self.y,
            r*self.z
        )

    # d) Longitud
    def longitud(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    # e) Normal
    def normal(self):
        m = self.longitud()
        if m == 0:
            raise ValueError("No se puede normalizar el vector cero")
        return Vector3D(
            self.x/m,
            self.y/m,
            self.z/m
        )

    # f) Producto escalar
    def producto_escalar(self, v):
        return self.x*v.x + self.y*v.y + self.z*v.z

    # g) Producto vectorial
    def producto_vectorial(self, v):
        return Vector3D(
            self.y*v.z - self.z*v.y,
            self.z*v.x - self.x*v.z,
            self.x*v.y - self.y*v.x
        )

    # h) Mostrar vector
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"


# ===== TEST =====
v1 = Vector3D(1,2,3)
v2 = Vector3D(4,5,6)

print("Vector 1 =", v1)
print("Vector 2 =", v2)
print("Suma =", v1 + v2)
print("Escalar 2*v1 =", v1.escalar(2))
print("Longitud v1 =", v1.longitud())
print("Producto escalar =", v1.producto_escalar(v2))
print("Producto vectorial =", v1.producto_vectorial(v2))