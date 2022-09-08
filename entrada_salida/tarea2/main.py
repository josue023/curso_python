# En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo,
# haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.

import pickle

class Vehiculo:
    marca = ""
    color = ""
    anio = 0

    def __init__(self, marca, color, anio):
        self.marca = marca
        self.color = color
        self.anio = anio

    def getMarca(self):
        return self.marca

    def getColor(self):
        return self.color

    def getAnio(self):
        return self.anio

def main():
    v1 = Vehiculo("citroen", "negro", 2019)

    f = open("datos.bin", "wb")
    pickle.dump(v1, f)
    f.close()

    f2 = open("datos.bin", "rb")
    vehiculo = pickle.load(f2)
    f2.close()

    print(vehiculo.getMarca()," ", vehiculo.getColor(), " ", vehiculo.getAnio())

if __name__ == "__main__":
    main()
