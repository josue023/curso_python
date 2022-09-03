# Escribe una función que pueda decirte si un número (número entero) es primo o no.

def numeroPrimo (numero):
    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True

if numeroPrimo(19) == False:
    print("no es primo")
else:
    print("es primo")
