

class Vehiculo:
    color = ""
    ruedas = 0
    puertas = 0

    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas


class Coche(Vehiculo):
    velocidad = 0
    cilindrada = 0

    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada



c = Coche("rojo", 4, 5, 120, 4300)

print(c.color)
print(c.ruedas)
print(c.puertas)
print(c.velocidad)
print(c.cilindrada)
