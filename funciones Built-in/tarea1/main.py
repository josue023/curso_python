# Crea un script que le pida al usuario una lista de países (separados por comas).
# Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set).
# Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.

ingresoPaises = input("Ingrese una lista de paises: ").split(",")

listaPaises = list(set(ingresoPaises))


print(sorted(listaPaises))