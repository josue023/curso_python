# En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt,
# lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.

def escribe(fichero, datos):
    f = open(fichero, "a")

    for linea in datos:

        if not linea.endswith("\n"):
            linea += "\n"

        f.write(linea)


def main():

    lista = [
        "dato1",
        "dato2",
        "dato3"
    ]

    escribe("datos.txt", lista)


if __name__ == "__main__":
    main()