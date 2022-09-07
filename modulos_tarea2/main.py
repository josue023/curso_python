# En este segundo ejercicio tendréis que crear un script que nos diga si es la hora de ir a casa.
# Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.
# En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario,
# haréis una operación para calcular el tiempo que queda de trabajo.

from datetime import datetime

def main():

    horaActual = datetime.now()
    hora2 = datetime(2022, 9, 6, 19, 00, 0)
    diferencia = hora2 - horaActual

    if horaActual >= hora2:
        print("Es la hora de ir a casa")
    else:
        print("Faltan: ", diferencia)


if __name__ == "__main__":
    main()