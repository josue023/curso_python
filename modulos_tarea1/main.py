
# En este ejercicio tendréis que crear un módulo que contenga las operaciones básicas de una calculadora:
# sumar, restar, multiplicar y dividir.
# Este módulo lo importaréis a un archivo python y llamaréis a las funciones creadas.
# Los resultados tenéis que mostrarlos por consola.

import operaciones as o

def main():
    print(o.sumar(3, 2))
    print(o.restar(3, 2))
    print(o.multiplicar(3, 2))
    print(o.dividir(3, 2))


if __name__ == "__main__":
    main()


