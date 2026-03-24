import math

class AlgebraVectorial:

    # a) Constructor
    def __init__(self, a1, a2, a3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

    # b) Producto escalar
    def producto_escalar(self, v):
        return self.a1*v.a1 + self.a2*v.a2 + self.a3*v.a3

    # c) Magnitud
    def magnitud(self):
        return math.sqrt(self.a1**2 + self.a2**2 + self.a3**2)

    # d) Perpendicular (a · b = 0)
    def perpendicular(self, v):
        return abs(self.producto_escalar(v)) < 1e-9

    # e) Paralela (a = r b)
    def paralela(self, v):
        try:
            r1 = self.a1 / v.a1 if v.a1 != 0 else None
            r2 = self.a2 / v.a2 if v.a2 != 0 else None
            r3 = self.a3 / v.a3 if v.a3 != 0 else None

            ratios = [r for r in [r1, r2, r3] if r is not None]
            return all(abs(r - ratios[0]) < 1e-9 for r in ratios)
        except:
            return False

    # f) Proyección de a sobre b (vector)
    def proyeccion(self, v):
        escalar = self.producto_escalar(v) / (v.magnitud()**2)
        return AlgebraVectorial(
            escalar * v.a1,
            escalar * v.a2,
            escalar * v.a3
        )

    # g) Componente de a en b (escalar)
    def componente(self, v):
        return self.producto_escalar(v) / v.magnitud()

    def __str__(self):
        return f"({self.a1}, {self.a2}, {self.a3})"


# ===== TEST =====
v1 = AlgebraVectorial(1,2,3)
v2 = AlgebraVectorial(4,5,6)

print("Producto escalar =", v1.producto_escalar(v2))
print("Magnitud v1 =", v1.magnitud())
print("¿Perpendiculares?", v1.perpendicular(v2))
print("¿Paralelos?", v1.paralela(v2))
print("Proyección =", v1.proyeccion(v2))
print("Componente =", v1.componente(v2))