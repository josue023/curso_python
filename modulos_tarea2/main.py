# En este segundo ejercicio tendréis que crear un script que nos diga si es la hora de ir a casa.
# Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.
# En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario,
# haréis una operación para calcular el tiempo que queda de trabajo.

import time
from datetime import datetime

def main():

    anio = time.localtime().tm_year
    mes = time.localtime().tm_mon
    dia = time.localtime().tm_mday

    #obtenemos la fecha y hora actual y guardamos en la variable "horaActual"
    horaActual = datetime.now()

    #creamos una variable que contenga la fecha actual y la hora que queremos
    hora2 = datetime(anio, mes, dia, 19, 0, 0)

    #calculamos la diferencia que hay entre las dos horas
    diferencia = hora2 - horaActual

    if horaActual >= hora2:
        print("Es la hora de ir a casa")
    else:
        print("Faltan:", diferencia)


if __name__ == "__main__":
    main()