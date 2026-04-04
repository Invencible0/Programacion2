import random

# Clase base
class Juego:
    def __init__(self, vidas):
        self.numeroDeVidas = vidas
        self.record = 0

    def reiniciaPartida(self):
        # Reinicia las vidas al valor inicial (3)
        self.numeroDeVidas = 3
        print("Partida reiniciada. Vidas:", self.numeroDeVidas)

    def actualizaRecord(self):
        self.record += 1
        print("Record actualizado:", self.record)

    def quitaVida(self):
        self.numeroDeVidas -= 1
        print("Te quedan", self.numeroDeVidas, "vidas")
        return self.numeroDeVidas > 0


# Clase derivada
class JuegoAdivinaNumero(Juego):
    def __init__(self, vidas):
        super().__init__(vidas)
        self.numeroAAdivinar = 0

    def juega(self):
        # 1. Reiniciar partida
        self.reiniciaPartida()

        # 2. Generar numero aleatorio
        self.numeroAAdivinar = random.randint(0, 10)

        # 3. Mensaje inicial
        print("Adivina un numero entre 0 y 10")

        while True:
            # 4. Leer número
            num = int(input("Ingresa un numero: "))

            if num == self.numeroAAdivinar:
                # a) Acertó
                print("Acertaste!")
                self.actualizaRecord()
                break
            else:
                # b) Quita vida
                if self.quitaVida():
                    # c) Indica pista
                    if num < self.numeroAAdivinar:
                        print("El numero es mayor")
                    else:
                        print("El numero es menor")
                else:
                    # d) Sin vidas
                    print("Te quedaste sin vidas")
                    print("El numero era:", self.numeroAAdivinar)
                    break


# Clase Aplicación
class Aplicacion:
    @staticmethod
    def main():
        juego = JuegoAdivinaNumero(3)
        juego.juega()


# Ejecutar programa
if __name__ == "__main__":
    Aplicacion.main()