import random

# Clase base
class Juego:
    def __init__(self, vidas):
        self.vidasIniciales = vidas
        self.numeroDeVidas = vidas
        self.record = 0

    def reiniciaPartida(self):
        self.numeroDeVidas = self.vidasIniciales
        print("Partida reiniciada. Vidas:", self.numeroDeVidas)

    def actualizaRecord(self):
        self.record += 1
        print("Record actualizado:", self.record)

    def quitaVida(self):
        self.numeroDeVidas -= 1
        print("Te quedan", self.numeroDeVidas, "vidas")
        return self.numeroDeVidas > 0


# Clase principal
class JuegoAdivinaNumero(Juego):
    def __init__(self, vidas):
        super().__init__(vidas)
        self.numeroAAdivinar = 0

    def validaNumero(self, num):
        return 0 <= num <= 10

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)

        print("Adivina un numero entre 0 y 10")

        while True:
            try:
                num = int(input("Ingresa un numero: "))
            except:
                print("Numero invalido")
                continue

            # Validación
            if not self.validaNumero(num):
                print("Numero fuera de rango")
                continue

            if num == self.numeroAAdivinar:
                print("Acertaste!")
                self.actualizaRecord()
                break
            else:
                if self.quitaVida():
                    if num < self.numeroAAdivinar:
                        print("El numero es mayor")
                    else:
                        print("El numero es menor")
                else:
                    print("Te quedaste sin vidas")
                    print("El numero era:", self.numeroAAdivinar)
                    break


# Clase PAR
class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, num):
        if num % 2 != 0:
            print("Error: debe ser un numero PAR")
            return False
        return 0 <= num <= 10


# Clase IMPAR
class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, num):
        if num % 2 == 0:
            print("Error: debe ser un numero IMPAR")
            return False
        return 0 <= num <= 10


# Clase Aplicación
class Aplicacion:
    @staticmethod
    def main():
        print(" Juego Normal ")
        juego1 = JuegoAdivinaNumero(3)
        juego1.juega()

        print(" Juego PAR ")
        juego2 = JuegoAdivinaPar(3)
        juego2.juega()

        print(" Juego IMPAR ")
        juego3 = JuegoAdivinaImpar(3)
        juego3.juega()


# Ejecutar
if __name__ == "__main__":
    Aplicacion.main()